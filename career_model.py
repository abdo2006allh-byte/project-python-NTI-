
"""Local, explainable AI career-matching engine for CS Career Compass.

No network, API, database, or third-party package is required.
The model uses:
- canonical skill normalization / aliases
- weighted skill coverage
- weighted cosine similarity
- conservative fuzzy job-title similarity
- role-family requirements
- gap prioritization
- confidence / evidence indicators
"""
from __future__ import annotations
from difflib import SequenceMatcher
from math import sqrt
import re
from career_data import FIELDS

ALIASES = {
    "js":"javascript","javascript":"javascript","javascript es6":"javascript",
    "ts":"typescript","typescript":"typescript","reactjs":"react","react.js":"react",
    "node":"node.js","nodejs":"node.js","node.js":"node.js",
    "py":"python","python3":"python","postgres":"postgresql","postgresql":"postgresql",
    "ml":"machine learning","machine learning":"machine learning",
    "ai":"artificial intelligence","artificial intelligence":"artificial intelligence",
    "dl":"deep learning","deep learning":"deep learning",
    "dsa":"data structures","data structures":"data structures",
    "oop":"oop","object oriented programming":"oop",
    "api":"apis","apis":"apis","rest api":"rest","rest apis":"rest","rest":"rest",
    "powerbi":"power bi","power bi":"power bi","sklearn":"scikit-learn","scikit learn":"scikit-learn",
    "scikit-learn":"scikit-learn","tensorflow":"tensorflow","pytorch":"pytorch",
    "k8s":"kubernetes","kubernetes":"kubernetes","aws":"aws","azure":"azure","gcp":"gcp",
    "google cloud":"gcp","amazon web services":"aws","microsoft azure":"azure",
    "csharp":"c#","c#":"c#","cpp":"c++","c++":"c++",".net":".net",
    "dotnet":".net","asp.net":".net","html5":"html","html":"html","css3":"css","css":"css",
    "tcp/ip":"networking","tcp ip":"networking","computer networking":"networking",
    "statistics":"statistics","excel":"excel","figma":"figma","unity":"unity","unreal":"unreal",
    "solidity":"solidity","smart contracts":"smart contract development",
    "smart contract":"smart contract development","ci/cd":"ci/cd","continuous integration":"ci/cd",
    "infrastructure as code":"infrastructure as code","terraform":"terraform",
    "data modeling":"data modeling","data cleaning":"data cleaning","visualization":"visualization",
    "model evaluation":"model evaluation","security fundamentals":"security fundamentals",
    "web security":"web security","incident response":"incident response",
    "user research":"user research","wireframing":"wireframing","prototyping":"prototyping",
    "visual design":"visual design","usability testing":"usability testing",
    "game engine":"game engine","3d math":"3d math","c/c++":"c/c++",
    "microcontrollers":"microcontrollers","electronics basics":"electronics basics",
    "rtos":"rtos","debugging":"debugging","protocols":"protocols",
    "network security":"network security","dns":"dns","routing":"routing","switching":"switching",
    "cloud services":"cloud services","iam":"iam","automation":"automation","containers":"containers",
    "monitoring":"monitoring","test design":"test design","bug reporting":"bug reporting",
    "api testing":"api testing","test automation":"automation","automation testing":"automation",
    "accessibility":"accessibility","responsive design":"responsive design","http":"http",
    "authentication":"authentication","caching":"caching","testing":"testing","sql":"sql","git":"git",
    "linux":"linux","python":"python","java":"java","kotlin":"kotlin","swift":"swift","dart":"dart",
    "go":"go","php":"php","ruby":"ruby","bash":"bash",
}

WEIGHTS = {
    "python":1.30,"javascript":1.20,"typescript":1.20,"java":1.15,"c#":1.15,"c++":1.15,
    "c/c++":1.15,"sql":1.25,"git":1.05,"oop":1.10,"data structures":1.15,"algorithms":1.15,
    "testing":1.10,"apis":1.10,"rest":1.10,"networking":1.25,"linux":1.15,
    "security fundamentals":1.25,"web security":1.20,"machine learning":1.30,
    "deep learning":1.25,"statistics":1.15,"model evaluation":1.15,"docker":1.10,
    "kubernetes":1.10,"cloud services":1.10,"ci/cd":1.10,"infrastructure as code":1.10,
    "react":1.15,"html":1.05,"css":1.05,"accessibility":1.05,"solidity":1.20,
    "smart contract development":1.20,"user research":1.10,"usability testing":1.05,
    "microcontrollers":1.15,"debugging":1.05,"data modeling":1.10,
}

# Extra role-level requirements. They are deliberately conservative: the field's
# own dataset remains the primary source of requirements.
ROLE_RULES = [
    (("frontend", "front end", "ui developer"), ["html","css","javascript","react"]),
    (("backend", "back end"), ["sql","rest","apis","testing"]),
    (("full stack",), ["html","css","javascript","sql","rest"]),
    (("data analyst", "analytics"), ["sql","statistics","visualization"]),
    (("data scientist",), ["python","statistics","machine learning","sql"]),
    (("ml engineer","machine learning engineer","ai engineer"), ["python","machine learning","model evaluation"]),
    (("security analyst","soc analyst"), ["networking","linux","security fundamentals","incident response"]),
    (("network engineer",), ["networking","linux"]),
    (("cloud engineer","cloud architect","cloud support"), ["linux","networking","cloud services","iam"]),
    (("devops","platform engineer"), ["linux","git","ci/cd","containers"]),
    (("database","dba"), ["sql","data modeling"]),
    (("qa","test","testing"), ["test design","bug reporting","testing","automation"]),
    (("ux","product designer","ui designer"), ["user research","wireframing","prototyping","usability testing"]),
    (("embedded",), ["c/c++","microcontrollers","debugging","protocols"]),
    (("game",), ["game engine","debugging"]),
    (("blockchain","smart contract"), ["solidity","smart contract development"]),
]

def normalize_skill(value:str)->str:
    s=str(value or "").strip().lower()
    s=s.replace("–","-").replace("—","-")
    s=re.sub(r"\s+"," ",s)
    s=re.sub(r"^[•*\-]+\s*","",s)
    return ALIASES.get(s,s)

def parse_skills(raw:str|list[str])->list[str]:
    items=raw if isinstance(raw,list) else re.split(r"[,;\n|]+",raw or "")
    seen=set(); result=[]
    for item in items:
        n=normalize_skill(item)
        if n and n not in seen:
            seen.add(n); result.append(n)
    return result

def _expand_skill(skill:str)->set[str]:
    n=normalize_skill(skill)
    out={n}
    # Compound entries in the existing dataset represent alternatives.
    if n in {"python/java/node.js","python/java/node","python/java/node.js"}:
        out.update({"python","java","node.js"})
    if n in {"python/java/node.js"}:
        out.update({"python","java","node.js"})
    if n in {"dart/kotlin/swift"}:
        out.update({"dart","kotlin","swift"})
    if n in {"c# / c++","c#/c++"}:
        out.update({"c#","c++"})
    if n in {"javascript/typescript"}:
        out.update({"javascript","typescript"})
    if n in {"c/c++"}:
        out.update({"c","c++"})
    return out

def expand_user_skills(skills:str|list[str])->set[str]:
    out=set()
    for s in parse_skills(skills):
        out |= _expand_skill(s)
    return out

def role_requirements(role:str, field:dict)->list[str]:
    req=[]
    seen=set()
    for s in field.get("skills",[]):
        n=normalize_skill(s)
        # Keep the compound skill but also expose alternatives where possible.
        for x in _expand_skill(n):
            if x not in seen:
                seen.add(x); req.append(x)
    r=role.lower()
    for phrases, extras in ROLE_RULES:
        if any(p in r for p in phrases):
            for s in extras:
                n=normalize_skill(s)
                if n not in seen:
                    seen.add(n); req.append(n)
    # Seniority requires engineering maturity, but only modestly affects the score.
    if any(x in r for x in ("senior","lead","architect","staff")):
        for s in ("communication","code review","system design"):
            if s not in seen:
                seen.add(s); req.append(s)
    return req

def _w(s): return WEIGHTS.get(s,1.0)

def weighted_coverage(user:set[str], required:set[str])->float:
    if not required:return 0.0
    total=sum(_w(s) for s in required)
    hit=sum(_w(s) for s in user & required)
    return hit/total if total else 0.0

def cosine(user:set[str], required:set[str])->float:
    if not user or not required:return 0.0
    dot=sum(_w(s)**2 for s in user & required)
    a=sum(_w(s)**2 for s in user); b=sum(_w(s)**2 for s in required)
    return dot/(sqrt(a)*sqrt(b)) if a and b else 0.0

def title_similarity(query:str, role:str)->float:
    if not query:return 0.0
    q=re.sub(r"[^a-z0-9+#. ]+"," ",query.lower()).strip()
    r=re.sub(r"[^a-z0-9+#. ]+"," ",role.lower()).strip()
    if not q:return 0.0
    seq=SequenceMatcher(None,q,r).ratio()
    qt=set(q.split()); rt=set(r.split())
    overlap=len(qt&rt)/max(1,len(qt|rt))
    return .65*seq+.35*overlap

def _gaps(user,required):
    gaps=sorted((s for s in required if s not in user), key=lambda s:(-_w(s),s))
    return gaps

def _label(score):
    if score>=85:return ("Excellent","ممتاز")
    if score>=70:return ("Strong","قوي")
    if score>=55:return ("Promising","واعد")
    if score>=40:return ("Partial","جزئي")
    return ("Low","ضعيف")

def all_roles():
    rows=[]
    for field in FIELDS:
        for role in field.get("roles",[]):
            req=role_requirements(role,field)
            rows.append({"field_id":field["id"],"field_name":field["name"],
                         "field_ar":field["ar"],"role":role,"required":req})
    return rows

ROLE_INDEX=all_roles()

def match_jobs(user_skills:str|list[str], desired_job:str="", limit:int=10)->dict:
    user=expand_user_skills(user_skills)
    query=(desired_job or "").strip()
    scored=[]
    for rec in ROLE_INDEX:
        required=set(rec["required"])
        cov=weighted_coverage(user,required)
        cos=cosine(user,required)
        title=title_similarity(query,rec["role"])
        # Skill evidence is dominant; title similarity is only a modifier.
        score=.62*cov+.28*cos+.10*title
        # Transferable family signal is intentionally small.
        if user and required:
            groups=[
                {"python","java","c#","c++","javascript","typescript","go"},
                {"html","css","javascript","typescript","react","rest","apis"},
                {"sql","excel","pandas","statistics","visualization","data cleaning"},
                {"machine learning","deep learning","pytorch","tensorflow","scikit-learn"},
                {"linux","networking","docker","kubernetes","aws","azure","gcp"},
            ]
            if any(user&g and required&g and not(user&required&g) for g in groups):
                score += .025
        score=max(0,min(1,score))
        matched=sorted(user&required,key=lambda s:(-_w(s),s))
        gaps=_gaps(user,required)
        scored.append({**rec,"score":round(score*100,1),
                       "coverage":round(cov*100,1),"cosine":round(cos*100,1),
                       "title_similarity":round(title*100,1),
                       "matched":matched,"missing":gaps,
                       "label":_label(score*100)})
    scored.sort(key=lambda x:(-x["score"],len(x["missing"]),x["role"]))
    return {"user_skills":sorted(user),"desired_job":query,"results":scored[:max(1,limit)],
            "all_results":scored,"roles_evaluated":len(ROLE_INDEX),"fields_evaluated":len(FIELDS)}

def match_specific_job(job:str,skills:str|list[str])->dict:
    data=match_jobs(skills,job,len(ROLE_INDEX))
    exact=next((r for r in data["all_results"] if r["role"].lower()==job.lower()),None)
    return exact or data["all_results"][0]

def learning_plan(results:list[dict],max_items:int=8)->list[str]:
    counts={}
    for r in results[:5]:
        for s in r["missing"][:8]:
            counts[s]=counts.get(s,0)+_w(s)
    return [s for s,_ in sorted(counts.items(),key=lambda kv:(-kv[1],kv[0]))[:max_items]]

def model_info():
    return {"name":"CS Career Compass Local AI Matching Engine","version":"1.0",
            "algorithm":"weighted skill coverage + weighted cosine similarity + fuzzy title relevance + transferable-skill signal + gap analysis",
            "roles_evaluated":len(ROLE_INDEX),"fields_evaluated":len(FIELDS),
            "dependencies":"Python standard library only","network_required":False}
