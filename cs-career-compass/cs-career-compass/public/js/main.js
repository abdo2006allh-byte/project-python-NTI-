/* CS Career Compass — shared frontend logic (plain JavaScript, no build step). */

const CC = (() => {
  const LANG_KEY = "cc_lang";

  function getLang() {
    return localStorage.getItem(LANG_KEY) === "en" ? "en" : "ar";
  }

  function setLang(lang) {
    localStorage.setItem(LANG_KEY, lang === "en" ? "en" : "ar");
    location.reload();
  }

  function t(en, ar) {
    return getLang() === "ar" ? ar : en;
  }

  // Swap the text of every element that carries data-en / data-ar attributes,
  // and set the page direction/lang, based on the stored language preference.
  function applyStaticTranslations() {
    const lang = getLang();
    document.documentElement.lang = lang;
    document.documentElement.dir = lang === "ar" ? "rtl" : "ltr";
    document.querySelectorAll("[data-en]").forEach((el) => {
      const val = lang === "ar" ? el.getAttribute("data-ar") : el.getAttribute("data-en");
      if (val !== null) el.textContent = val;
    });
    document.querySelectorAll("[data-placeholder-en]").forEach((el) => {
      const val = lang === "ar"
        ? el.getAttribute("data-placeholder-ar")
        : el.getAttribute("data-placeholder-en");
      if (val !== null) el.setAttribute("placeholder", val);
    });
  }

  function initHeader() {
    applyStaticTranslations();
    const toggle = document.querySelector("[data-lang-toggle]");
    if (toggle) {
      const lang = getLang();
      toggle.textContent = lang === "ar" ? "English" : "العربية";
      toggle.addEventListener("click", (e) => {
        e.preventDefault();
        setLang(lang === "ar" ? "en" : "ar");
      });
    }
    // highlight active nav link
    const here = location.pathname.replace(/\/index\.html$/, "/");
    document.querySelectorAll("[data-nav-link]").forEach((a) => {
      const href = a.getAttribute("data-nav-link");
      if (href === here || (href !== "/" && here.startsWith(href))) {
        a.classList.add("active");
      }
    });
  }

  async function fetchData() {
    const res = await fetch("/api/data");
    if (!res.ok) throw new Error("Failed to load /api/data");
    return res.json();
  }

  async function postMatch(skills, job, limit = 10) {
    const res = await fetch("/api/match", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ skills, job, limit }),
    });
    const data = await res.json();
    if (!res.ok) return { error: data.error || "Request failed" };
    return data;
  }

  function escapeHtml(str) {
    const div = document.createElement("div");
    div.textContent = String(str ?? "");
    return div.innerHTML;
  }

  function fieldName(f) {
    return t(f.name, f.ar);
  }
  function fieldDesc(f) {
    return t(f.desc, f.ar_desc);
  }
  function itemLabel(items, key) {
    const info = items[key];
    if (!info) return key;
    return t(info.en, info.ar);
  }
  function itemDesc(items, key) {
    const info = items[key];
    if (!info) return "";
    return t(info.desc_en, info.desc_ar);
  }

  return {
    getLang, setLang, t, applyStaticTranslations, initHeader,
    fetchData, postMatch, escapeHtml, fieldName, fieldDesc, itemLabel, itemDesc,
  };
})();
