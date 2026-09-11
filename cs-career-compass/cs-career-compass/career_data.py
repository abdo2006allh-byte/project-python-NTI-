# -*- coding: utf-8 -*-
"""CS Career Compass - career field dataset.

ITEM_INFO holds shared metadata (name, short description, free/paid learning
resources) for every skill and tool referenced across the 18 FIELDS entries.
"""

ITEM_INFO = {
  "python": {
    "en": "Python",
    "ar": "بايثون",
    "desc_en": "Readable general-purpose language used across backend, data and AI.",
    "desc_ar": "لغة برمجة عامة سهلة القراءة تُستخدم في الباك اند وتحليل البيانات والذكاء الاصطناعي.",
    "free": [
      "Python docs tutorial (python.org)",
      "freeCodeCamp Python (YouTube)"
    ],
    "paid": [
      "Udemy: 100 Days of Code Python",
      "Coursera: Python for Everybody (Michigan)"
    ]
  },
  "git": {
    "en": "Git",
    "ar": "جيت",
    "desc_en": "Version control system used to track and merge code changes.",
    "desc_ar": "نظام تحكم بالإصدارات لتتبع تعديلات الكود ودمجها.",
    "free": [
      "Git docs (git-scm.com)",
      "freeCodeCamp Git & GitHub (YouTube)"
    ],
    "paid": [
      "Udemy: Git Complete",
      "Pluralsight: Git Fundamentals"
    ]
  },
  "oop": {
    "en": "OOP",
    "ar": "البرمجة الكائنية",
    "desc_en": "Organizing code into classes/objects for reuse and structure.",
    "desc_ar": "تنظيم الكود في كلاسات وكائنات لإعادة الاستخدام والتنظيم.",
    "free": [
      "freeCodeCamp OOP (YouTube)",
      "W3Schools OOP guide"
    ],
    "paid": [
      "Udemy: OOP in Python/Java",
      "Educative: OOP Patterns"
    ]
  },
  "data structures": {
    "en": "Data Structures",
    "ar": "هياكل البيانات",
    "desc_en": "Ways to organize data (arrays, lists, trees, graphs) for efficient use.",
    "desc_ar": "طرق تنظيم البيانات (مصفوفات، قوائم، أشجار، رسوم بيانية) للاستخدام الفعّال.",
    "free": [
      "freeCodeCamp Data Structures (YouTube)",
      "GeeksforGeeks DSA"
    ],
    "paid": [
      "Udemy: Master DSA",
      "Coursera: Data Structures (UCSD)"
    ]
  },
  "algorithms": {
    "en": "Algorithms",
    "ar": "الخوارزميات",
    "desc_en": "Step-by-step methods for solving problems efficiently.",
    "desc_ar": "خطوات منهجية لحل المشكلات بكفاءة.",
    "free": [
      "freeCodeCamp Algorithms (YouTube)",
      "GeeksforGeeks Algorithms"
    ],
    "paid": [
      "Udemy: Algorithms & DS Bootcamp",
      "Coursera: Algorithms (Stanford/Princeton)"
    ]
  },
  "sql": {
    "en": "SQL",
    "ar": "إس كيو إل",
    "desc_en": "Query language for reading and managing relational databases.",
    "desc_ar": "لغة استعلامات لقراءة وإدارة قواعد البيانات العلائقية.",
    "free": [
      "SQLBolt (interactive, free)",
      "freeCodeCamp SQL (YouTube)"
    ],
    "paid": [
      "Udemy: The Complete SQL Bootcamp",
      "DataCamp: SQL Track"
    ]
  },
  "testing": {
    "en": "Testing",
    "ar": "الاختبار",
    "desc_en": "Verifying that code behaves correctly via manual and automated tests.",
    "desc_ar": "التحقق من صحة عمل الكود يدويًا وبشكل آلي.",
    "free": [
      "freeCodeCamp Testing (YouTube)",
      "Pytest docs"
    ],
    "paid": [
      "Udemy: Software Testing Bootcamp",
      "Test Automation University (paid tracks)"
    ]
  },
  "apis": {
    "en": "APIs",
    "ar": "واجهات برمجة التطبيقات",
    "desc_en": "Interfaces that let programs exchange data with each other.",
    "desc_ar": "واجهات تتيح للبرامج تبادل البيانات مع بعضها.",
    "free": [
      "freeCodeCamp REST APIs (YouTube)",
      "MDN: Working with APIs"
    ],
    "paid": [
      "Udemy: REST API Masterclass",
      "Postman Academy (paid tracks)"
    ]
  },
  "debugging": {
    "en": "Debugging",
    "ar": "تصحيح الأخطاء",
    "desc_en": "Finding and fixing defects in code using tools and logic.",
    "desc_ar": "إيجاد الأخطاء في الكود وإصلاحها باستخدام الأدوات والمنطق.",
    "free": [
      "freeCodeCamp Debugging (YouTube)",
      "MDN Debugging guide"
    ],
    "paid": [
      "Udemy: Debugging Techniques",
      "Pluralsight: Effective Debugging"
    ]
  },
  "clean code": {
    "en": "Clean Code",
    "ar": "الكود النظيف",
    "desc_en": "Writing readable, maintainable and well-structured code.",
    "desc_ar": "كتابة كود واضح وسهل الصيانة ومنظم جيدًا.",
    "free": [
      "freeCodeCamp Clean Code (YouTube)",
      "Refactoring.Guru (free articles)"
    ],
    "paid": [
      "Book: Clean Code by Robert Martin (paid)",
      "Udemy: Clean Code Principles"
    ]
  },
  "design patterns": {
    "en": "Design Patterns",
    "ar": "أنماط التصميم",
    "desc_en": "Reusable solutions to common software design problems.",
    "desc_ar": "حلول جاهزة لمشاكل تصميم البرمجيات المتكررة.",
    "free": [
      "Refactoring.Guru Design Patterns (free)",
      "freeCodeCamp Design Patterns (YouTube)"
    ],
    "paid": [
      "Udemy: Design Patterns in Python/Java",
      "Book: Head First Design Patterns"
    ]
  },
  "linux": {
    "en": "Linux",
    "ar": "لينكس",
    "desc_en": "Open-source operating system widely used on servers.",
    "desc_ar": "نظام تشغيل مفتوح المصدر يُستخدم بكثرة في السيرفرات.",
    "free": [
      "Linux Journey (free, interactive)",
      "freeCodeCamp Linux (YouTube)"
    ],
    "paid": [
      "Udemy: Linux Mastery",
      "Linux Foundation: Intro to Linux (paid cert track)"
    ]
  },
  "problem solving": {
    "en": "Problem Solving",
    "ar": "حل المشكلات",
    "desc_en": "Breaking down problems and reasoning toward solutions.",
    "desc_ar": "تفكيك المشكلات والوصول لحلول منطقية.",
    "free": [
      "LeetCode free tier",
      "HackerRank practice"
    ],
    "paid": [
      "AlgoExpert (paid)",
      "Udemy: Coding Interview Prep"
    ]
  },
  "version control": {
    "en": "Version Control",
    "ar": "إدارة الإصدارات",
    "desc_en": "Tracking history of code changes across a team.",
    "desc_ar": "تتبع تاريخ تعديلات الكود بين أعضاء الفريق.",
    "free": [
      "Git docs (git-scm.com)",
      "Atlassian Git tutorials (free)"
    ],
    "paid": [
      "Udemy: Git & GitHub Masterclass",
      "Pluralsight: Version Control"
    ]
  },
  "html": {
    "en": "HTML",
    "ar": "إتش تي إم إل",
    "desc_en": "Markup language that structures content on web pages.",
    "desc_ar": "لغة توصيف تُستخدم لبناء هيكل صفحات الويب.",
    "free": [
      "MDN HTML docs",
      "freeCodeCamp Responsive Web Design"
    ],
    "paid": [
      "Udemy: The Complete Web Developer",
      "Codecademy Pro: HTML"
    ]
  },
  "css": {
    "en": "CSS",
    "ar": "سي إس إس",
    "desc_en": "Styling language that controls layout and appearance of web pages.",
    "desc_ar": "لغة تنسيق تتحكم في شكل وتخطيط صفحات الويب.",
    "free": [
      "MDN CSS docs",
      "freeCodeCamp CSS (YouTube)"
    ],
    "paid": [
      "Udemy: CSS Complete Course",
      "CSS-Tricks Pro guides"
    ]
  },
  "javascript": {
    "en": "JavaScript",
    "ar": "جافاسكريبت",
    "desc_en": "Scripting language that adds interactivity to web pages.",
    "desc_ar": "لغة برمجة تُضيف التفاعل لصفحات الويب.",
    "free": [
      "javascript.info (free)",
      "freeCodeCamp JavaScript Algorithms"
    ],
    "paid": [
      "Udemy: The Complete JavaScript Course",
      "Frontend Masters JS track"
    ]
  },
  "rest": {
    "en": "REST",
    "ar": "ريست",
    "desc_en": "Architectural style for designing networked web APIs.",
    "desc_ar": "أسلوب معماري لتصميم واجهات الويب البرمجية.",
    "free": [
      "freeCodeCamp REST APIs (YouTube)",
      "restfulapi.net (free)"
    ],
    "paid": [
      "Udemy: REST API Design",
      "Educative: REST API Design Course"
    ]
  },
  "http": {
    "en": "HTTP",
    "ar": "إتش تي تي بي",
    "desc_en": "Protocol that governs communication between browsers and servers.",
    "desc_ar": "البروتوكول الذي يحكم الاتصال بين المتصفح والسيرفر.",
    "free": [
      "MDN HTTP overview",
      "freeCodeCamp HTTP explained (YouTube)"
    ],
    "paid": [
      "Udemy: HTTP/Networking for Developers",
      "Pluralsight: HTTP Fundamentals"
    ]
  },
  "responsive design": {
    "en": "Responsive Design",
    "ar": "التصميم المتجاوب",
    "desc_en": "Building layouts that adapt to different screen sizes.",
    "desc_ar": "بناء تصاميم تتكيف مع أحجام الشاشات المختلفة.",
    "free": [
      "freeCodeCamp Responsive Web Design",
      "web.dev Responsive guide"
    ],
    "paid": [
      "Udemy: Responsive Web Design",
      "Frontend Masters: CSS Layout"
    ]
  },
  "deployment": {
    "en": "Deployment",
    "ar": "النشر",
    "desc_en": "Publishing an application so users can access it live.",
    "desc_ar": "نشر التطبيق ليصبح متاحًا للمستخدمين فعليًا.",
    "free": [
      "Netlify/Vercel docs (free)",
      "freeCodeCamp Deployment (YouTube)"
    ],
    "paid": [
      "Udemy: DevOps & Deployment Bootcamp",
      "Pluralsight: CI/CD & Deployment"
    ]
  },
  "typescript": {
    "en": "TypeScript",
    "ar": "تايب سكريبت",
    "desc_en": "Typed superset of JavaScript that catches errors earlier.",
    "desc_ar": "امتداد لجافاسكريبت يضيف أنواع بيانات تكتشف الأخطاء مبكرًا.",
    "free": [
      "TypeScript official docs (free)",
      "freeCodeCamp TypeScript (YouTube)"
    ],
    "paid": [
      "Udemy: Understanding TypeScript",
      "Frontend Masters: TypeScript"
    ]
  },
  "react": {
    "en": "React",
    "ar": "رياكت",
    "desc_en": "JavaScript library for building interactive user interfaces.",
    "desc_ar": "مكتبة جافاسكريبت لبناء واجهات مستخدم تفاعلية.",
    "free": [
      "React official docs (free)",
      "freeCodeCamp React (YouTube)"
    ],
    "paid": [
      "Udemy: React – The Complete Guide",
      "Frontend Masters: React track"
    ]
  },
  "accessibility": {
    "en": "Accessibility",
    "ar": "إمكانية الوصول",
    "desc_en": "Designing products usable by people with disabilities.",
    "desc_ar": "تصميم منتجات يسهل استخدامها لذوي الإعاقة.",
    "free": [
      "web.dev Accessibility (free)",
      "freeCodeCamp Accessibility (YouTube)"
    ],
    "paid": [
      "Udemy: Web Accessibility",
      "Deque University (paid)"
    ]
  },
  "state management": {
    "en": "State Management",
    "ar": "إدارة الحالة",
    "desc_en": "Managing data/state shared across an application's UI.",
    "desc_ar": "إدارة البيانات/الحالة المشتركة عبر واجهة التطبيق.",
    "free": [
      "React docs on State (free)",
      "freeCodeCamp Redux (YouTube)"
    ],
    "paid": [
      "Udemy: Redux & Context API",
      "Frontend Masters: State Management"
    ]
  },
  "performance": {
    "en": "Performance Optimization",
    "ar": "تحسين الأداء",
    "desc_en": "Making applications faster and more efficient.",
    "desc_ar": "جعل التطبيقات أسرع وأكثر كفاءة.",
    "free": [
      "web.dev Performance (free)",
      "freeCodeCamp Web Performance (YouTube)"
    ],
    "paid": [
      "Udemy: Web Performance Optimization",
      "Frontend Masters: Performance"
    ]
  },
  "node.js": {
    "en": "Node.js",
    "ar": "نود جي اس",
    "desc_en": "JavaScript runtime for building server-side applications.",
    "desc_ar": "بيئة تشغيل جافاسكريبت لبناء تطبيقات السيرفر.",
    "free": [
      "Node.js official docs (free)",
      "freeCodeCamp Node.js (YouTube)"
    ],
    "paid": [
      "Udemy: The Complete Node.js Course",
      "Frontend Masters: Node track"
    ]
  },
  "authentication": {
    "en": "Authentication",
    "ar": "المصادقة",
    "desc_en": "Verifying user identity before granting access.",
    "desc_ar": "التحقق من هوية المستخدم قبل السماح له بالدخول.",
    "free": [
      "freeCodeCamp Auth (YouTube)",
      "Auth0 docs (free tier)"
    ],
    "paid": [
      "Udemy: Web Authentication & Security",
      "Pluralsight: Auth Fundamentals"
    ]
  },
  "caching": {
    "en": "Caching",
    "ar": "التخزين المؤقت",
    "desc_en": "Storing data temporarily to speed up repeated access.",
    "desc_ar": "تخزين البيانات مؤقتًا لتسريع الوصول المتكرر لها.",
    "free": [
      "Redis docs (free)",
      "freeCodeCamp Caching (YouTube)"
    ],
    "paid": [
      "Udemy: Caching Strategies",
      "Pluralsight: Redis Fundamentals"
    ]
  },
  "security fundamentals": {
    "en": "Security Fundamentals",
    "ar": "أساسيات الأمن السيبراني",
    "desc_en": "Core practices for protecting systems and data.",
    "desc_ar": "الممارسات الأساسية لحماية الأنظمة والبيانات.",
    "free": [
      "OWASP Top 10 (free)",
      "freeCodeCamp Security (YouTube)"
    ],
    "paid": [
      "Udemy: Cybersecurity Fundamentals",
      "Cybrary paid tracks"
    ]
  },
  "system design": {
    "en": "System Design",
    "ar": "تصميم الأنظمة",
    "desc_en": "Planning the architecture of large-scale software systems.",
    "desc_ar": "تخطيط بنية الأنظمة البرمجية واسعة النطاق.",
    "free": [
      "freeCodeCamp System Design (YouTube)",
      "GitHub: system-design-primer (free)"
    ],
    "paid": [
      "Udemy: System Design Interview",
      "Educative: Grokking System Design"
    ]
  },
  "dart": {
    "en": "Dart",
    "ar": "دارت",
    "desc_en": "Programming language used with the Flutter framework.",
    "desc_ar": "لغة برمجة تُستخدم مع إطار عمل فلاتر.",
    "free": [
      "Dart official docs (free)",
      "freeCodeCamp Flutter/Dart (YouTube)"
    ],
    "paid": [
      "Udemy: Dart & Flutter Complete Guide",
      "Udacity Flutter track"
    ]
  },
  "kotlin": {
    "en": "Kotlin",
    "ar": "كوتلن",
    "desc_en": "Modern language used for native Android development.",
    "desc_ar": "لغة حديثة تُستخدم في تطوير تطبيقات أندرويد الأصلية.",
    "free": [
      "Kotlin official docs (free)",
      "freeCodeCamp Kotlin (YouTube)"
    ],
    "paid": [
      "Udemy: Android Kotlin Developer",
      "Google Android Basics (paid cert)"
    ]
  },
  "swift": {
    "en": "Swift",
    "ar": "سويفت",
    "desc_en": "Apple's language for building iOS applications.",
    "desc_ar": "لغة أبل لبناء تطبيقات آي أو إس.",
    "free": [
      "Swift official docs (free)",
      "Hacking with Swift (free)"
    ],
    "paid": [
      "Udemy: iOS & Swift Bootcamp",
      "Kodeco (raywenderlich) paid tracks"
    ]
  },
  "ui design basics": {
    "en": "UI Design Basics",
    "ar": "أساسيات تصميم الواجهات",
    "desc_en": "Fundamentals of laying out clear, usable interfaces.",
    "desc_ar": "أساسيات بناء واجهات واضحة وسهلة الاستخدام.",
    "free": [
      "freeCodeCamp UI Design (YouTube)",
      "Figma Community files (free)"
    ],
    "paid": [
      "Udemy: UI Design Fundamentals",
      "Interaction Design Foundation (paid)"
    ]
  },
  "local storage": {
    "en": "Local Storage",
    "ar": "التخزين المحلي",
    "desc_en": "Saving app data directly on the user's device.",
    "desc_ar": "حفظ بيانات التطبيق على جهاز المستخدم مباشرة.",
    "free": [
      "MDN Web Storage (free)",
      "freeCodeCamp Local Storage (YouTube)"
    ],
    "paid": [
      "Udemy: Mobile Data Persistence",
      "Pluralsight: Local Storage patterns"
    ]
  },
  "push notifications": {
    "en": "Push Notifications",
    "ar": "الإشعارات الفورية",
    "desc_en": "Sending real-time alerts to users' devices.",
    "desc_ar": "إرسال تنبيهات فورية لأجهزة المستخدمين.",
    "free": [
      "Firebase Cloud Messaging docs (free)",
      "freeCodeCamp Push Notifications (YouTube)"
    ],
    "paid": [
      "Udemy: Firebase Push Notifications",
      "Pluralsight: Mobile Notifications"
    ]
  },
  "excel": {
    "en": "Excel",
    "ar": "إكسل",
    "desc_en": "Spreadsheet tool for organizing and analyzing data.",
    "desc_ar": "أداة جداول بيانات لتنظيم البيانات وتحليلها.",
    "free": [
      "Microsoft Excel free tutorials",
      "ExcelJet (free)"
    ],
    "paid": [
      "Udemy: Excel Bootcamp",
      "LinkedIn Learning: Excel Essential Training"
    ]
  },
  "statistics": {
    "en": "Statistics",
    "ar": "الإحصاء",
    "desc_en": "Mathematical methods for analyzing and interpreting data.",
    "desc_ar": "أساليب رياضية لتحليل البيانات وتفسيرها.",
    "free": [
      "Khan Academy Statistics (free)",
      "StatQuest (YouTube, free)"
    ],
    "paid": [
      "Coursera: Statistics with Python (Duke)",
      "Udemy: Statistics for Data Science"
    ]
  },
  "data cleaning": {
    "en": "Data Cleaning",
    "ar": "تنظيف البيانات",
    "desc_en": "Fixing missing or inconsistent data before analysis.",
    "desc_ar": "إصلاح البيانات الناقصة أو غير المتسقة قبل التحليل.",
    "free": [
      "Kaggle Data Cleaning course (free)",
      "freeCodeCamp Data Cleaning (YouTube)"
    ],
    "paid": [
      "DataCamp: Data Cleaning in Python",
      "Udemy: Data Cleaning Masterclass"
    ]
  },
  "visualization": {
    "en": "Data Visualization",
    "ar": "تصور البيانات",
    "desc_en": "Turning data into clear charts and graphics.",
    "desc_ar": "تحويل البيانات إلى رسوم ومخططات واضحة.",
    "free": [
      "Kaggle Data Visualization (free)",
      "freeCodeCamp Data Viz (YouTube)"
    ],
    "paid": [
      "DataCamp: Data Visualization Track",
      "Udemy: Tableau/Power BI Masterclass"
    ]
  },
  "critical thinking": {
    "en": "Critical Thinking",
    "ar": "التفكير النقدي",
    "desc_en": "Evaluating information logically before drawing conclusions.",
    "desc_ar": "تقييم المعلومات بمنطق قبل الوصول لاستنتاجات.",
    "free": [
      "Coursera: Intro to Logic (free audit)",
      "edX Critical Thinking (free audit)"
    ],
    "paid": [
      "Coursera: Critical Thinking Specialization (paid cert)",
      "Udemy: Critical Thinking Skills"
    ]
  },
  "reporting": {
    "en": "Reporting",
    "ar": "إعداد التقارير",
    "desc_en": "Summarizing findings clearly for decision makers.",
    "desc_ar": "تلخيص النتائج بوضوح لمتخذي القرار.",
    "free": [
      "Google Data Analytics free modules",
      "freeCodeCamp Reporting (YouTube)"
    ],
    "paid": [
      "Coursera: Google Data Analytics Certificate",
      "Udemy: Business Reporting"
    ]
  },
  "data storytelling": {
    "en": "Data Storytelling",
    "ar": "سرد البيانات",
    "desc_en": "Communicating insights from data through narrative.",
    "desc_ar": "توصيل النتائج المستخلصة من البيانات بأسلوب سردي.",
    "free": [
      "Storytelling with Data blog (free)",
      "Kaggle micro-courses"
    ],
    "paid": [
      "Book: Storytelling with Data (paid)",
      "Udemy: Data Storytelling"
    ]
  },
  "machine learning": {
    "en": "Machine Learning",
    "ar": "تعلم الآلة",
    "desc_en": "Building models that learn patterns from data.",
    "desc_ar": "بناء نماذج تتعلم الأنماط من البيانات.",
    "free": [
      "Google Machine Learning Crash Course (free)",
      "StatQuest ML (YouTube)"
    ],
    "paid": [
      "Coursera: Machine Learning by Andrew Ng",
      "Udemy: ML A-Z"
    ]
  },
  "model evaluation": {
    "en": "Model Evaluation",
    "ar": "تقييم النماذج",
    "desc_en": "Measuring how well a machine learning model performs.",
    "desc_ar": "قياس مدى جودة أداء نموذج تعلم الآلة.",
    "free": [
      "scikit-learn docs (free)",
      "StatQuest Model Evaluation (YouTube)"
    ],
    "paid": [
      "Coursera: ML Specialization (Andrew Ng)",
      "Udemy: Model Evaluation Deep Dive"
    ]
  },
  "pandas": {
    "en": "Pandas",
    "ar": "باندا",
    "desc_en": "Python library for working with tabular data.",
    "desc_ar": "مكتبة بايثون للتعامل مع البيانات الجدولية.",
    "free": [
      "Pandas official docs (free)",
      "Kaggle Pandas course (free)"
    ],
    "paid": [
      "DataCamp: Pandas Foundations",
      "Udemy: Python for Data Analysis"
    ]
  },
  "numpy": {
    "en": "NumPy",
    "ar": "نمباي",
    "desc_en": "Python library for fast numerical computing.",
    "desc_ar": "مكتبة بايثون للحوسبة العددية السريعة.",
    "free": [
      "NumPy official docs (free)",
      "Kaggle Python course (free)"
    ],
    "paid": [
      "DataCamp: Intro to NumPy",
      "Udemy: NumPy Masterclass"
    ]
  },
  "communication": {
    "en": "Communication",
    "ar": "مهارات التواصل",
    "desc_en": "Explaining technical ideas clearly to different audiences.",
    "desc_ar": "شرح الأفكار التقنية بوضوح لجمهور مختلف.",
    "free": [
      "Coursera: Effective Communication (free audit)",
      "YouTube: Technical communication talks"
    ],
    "paid": [
      "Coursera: Communication Skills Specialization",
      "Udemy: Technical Communication"
    ]
  },
  "experiment design": {
    "en": "Experiment Design",
    "ar": "تصميم التجارب",
    "desc_en": "Planning valid tests such as A/B experiments.",
    "desc_ar": "تخطيط اختبارات صحيحة مثل اختبارات A/B.",
    "free": [
      "Khan Academy: Study design (free)",
      "Kaggle: A/B testing course (free)"
    ],
    "paid": [
      "Udacity: A/B Testing course",
      "Udemy: Experiment Design for Data Science"
    ]
  },
  "deep learning": {
    "en": "Deep Learning",
    "ar": "التعلم العميق",
    "desc_en": "Neural-network based ML for complex pattern recognition.",
    "desc_ar": "تعلم آلة قائم على الشبكات العصبية للأنماط المعقدة.",
    "free": [
      "fast.ai free course",
      "3Blue1Brown Neural Networks (YouTube)"
    ],
    "paid": [
      "Coursera: Deep Learning Specialization (Andrew Ng)",
      "Udemy: PyTorch/TensorFlow Deep Learning"
    ]
  },
  "linear algebra": {
    "en": "Linear Algebra",
    "ar": "الجبر الخطي",
    "desc_en": "Math of vectors and matrices underlying ML models.",
    "desc_ar": "رياضيات المتجهات والمصفوفات التي تُبنى عليها نماذج تعلم الآلة.",
    "free": [
      "Khan Academy Linear Algebra (free)",
      "3Blue1Brown Essence of Linear Algebra (YouTube)"
    ],
    "paid": [
      "MIT OpenCourseWare (paid cert option)",
      "Udemy: Linear Algebra for ML"
    ]
  },
  "neural networks": {
    "en": "Neural Networks",
    "ar": "الشبكات العصبية",
    "desc_en": "Layered models inspired by the brain used in deep learning.",
    "desc_ar": "نماذج متعددة الطبقات مستوحاة من الدماغ تُستخدم في التعلم العميق.",
    "free": [
      "3Blue1Brown Neural Networks (YouTube)",
      "fast.ai free course"
    ],
    "paid": [
      "Coursera: Neural Networks & Deep Learning",
      "Udemy: Neural Networks from Scratch"
    ]
  },
  "nlp basics": {
    "en": "NLP Basics",
    "ar": "أساسيات معالجة اللغة",
    "desc_en": "Teaching computers to understand human language.",
    "desc_ar": "تعليم الحاسوب فهم اللغة البشرية.",
    "free": [
      "Hugging Face NLP course (free)",
      "freeCodeCamp NLP (YouTube)"
    ],
    "paid": [
      "Coursera: NLP Specialization (DeepLearning.AI)",
      "Udemy: NLP with Python"
    ]
  },
  "computer vision basics": {
    "en": "Computer Vision Basics",
    "ar": "أساسيات رؤية الحاسوب",
    "desc_en": "Teaching computers to interpret images and video.",
    "desc_ar": "تعليم الحاسوب تفسير الصور والفيديو.",
    "free": [
      "OpenCV free docs/tutorials",
      "freeCodeCamp Computer Vision (YouTube)"
    ],
    "paid": [
      "Coursera: Computer Vision Specialization",
      "Udemy: CV with OpenCV & Python"
    ]
  },
  "networking": {
    "en": "Networking",
    "ar": "الشبكات",
    "desc_en": "Fundamentals of how computers communicate over networks.",
    "desc_ar": "أساسيات كيفية تواصل الأجهزة عبر الشبكات.",
    "free": [
      "Cisco Networking Basics (free)",
      "freeCodeCamp Networking (YouTube)"
    ],
    "paid": [
      "Udemy: Networking Fundamentals",
      "CompTIA Network+ (paid cert)"
    ]
  },
  "web security": {
    "en": "Web Security",
    "ar": "أمن الويب",
    "desc_en": "Protecting websites and web apps from attacks.",
    "desc_ar": "حماية المواقع والتطبيقات من الهجمات.",
    "free": [
      "OWASP free resources",
      "freeCodeCamp Web Security (YouTube)"
    ],
    "paid": [
      "Udemy: Web Security Bootcamp",
      "PortSwigger Web Security Academy (free+paid labs)"
    ]
  },
  "incident response": {
    "en": "Incident Response",
    "ar": "الاستجابة للحوادث",
    "desc_en": "Detecting, containing and recovering from security breaches.",
    "desc_ar": "اكتشاف الاختراقات الأمنية واحتوائها والتعافي منها.",
    "free": [
      "SANS free resources",
      "CISA free training"
    ],
    "paid": [
      "Udemy: Incident Response & Forensics",
      "Cybrary Incident Response (paid tracks)"
    ]
  },
  "cryptography basics": {
    "en": "Cryptography Basics",
    "ar": "أساسيات التشفير",
    "desc_en": "Techniques for securing data through encryption.",
    "desc_ar": "تقنيات تأمين البيانات عن طريق التشفير.",
    "free": [
      "Khan Academy Cryptography (free)",
      "Cryptography I (Coursera free audit)"
    ],
    "paid": [
      "Coursera: Cryptography I (Stanford, paid cert)",
      "Udemy: Applied Cryptography"
    ]
  },
  "risk assessment": {
    "en": "Risk Assessment",
    "ar": "تقييم المخاطر",
    "desc_en": "Identifying and prioritizing security or business risks.",
    "desc_ar": "تحديد المخاطر الأمنية أو التشغيلية وترتيب أولوياتها.",
    "free": [
      "NIST free frameworks",
      "CISA free resources"
    ],
    "paid": [
      "Udemy: Risk Management Fundamentals",
      "(ISC)² paid training"
    ]
  },
  "scripting": {
    "en": "Scripting",
    "ar": "البرمجة النصية",
    "desc_en": "Writing small scripts to automate repetitive tasks.",
    "desc_ar": "كتابة سكربتات صغيرة لأتمتة المهام المتكررة.",
    "free": [
      "freeCodeCamp Bash/Python Scripting (YouTube)",
      "Python docs (free)"
    ],
    "paid": [
      "Udemy: Automation with Python",
      "Pluralsight: Shell Scripting"
    ]
  },
  "cloud services": {
    "en": "Cloud Services",
    "ar": "الخدمات السحابية",
    "desc_en": "Using cloud providers to host and scale applications.",
    "desc_ar": "استخدام مزودي الخدمة السحابية لاستضافة التطبيقات وتوسيعها.",
    "free": [
      "AWS Free Tier + docs",
      "Microsoft Learn Azure (free)"
    ],
    "paid": [
      "AWS/Azure/GCP paid certifications",
      "Udemy: Cloud Practitioner Bootcamp"
    ]
  },
  "iam": {
    "en": "IAM (Identity & Access)",
    "ar": "إدارة الهوية والصلاحيات",
    "desc_en": "Controlling who can access which cloud resources.",
    "desc_ar": "التحكم في من يمكنه الوصول لأي موارد سحابية.",
    "free": [
      "AWS IAM docs (free)",
      "Microsoft Learn IAM (free)"
    ],
    "paid": [
      "Udemy: AWS IAM Deep Dive",
      "A Cloud Guru IAM courses"
    ]
  },
  "automation": {
    "en": "Automation",
    "ar": "الأتمتة",
    "desc_en": "Using tools/scripts to perform tasks without manual effort.",
    "desc_ar": "استخدام أدوات/سكربتات لتنفيذ المهام دون تدخل يدوي.",
    "free": [
      "Ansible free docs",
      "freeCodeCamp Automation (YouTube)"
    ],
    "paid": [
      "Udemy: DevOps Automation",
      "Pluralsight: Automation with Ansible"
    ]
  },
  "containers": {
    "en": "Containers",
    "ar": "الحاويات",
    "desc_en": "Packaging apps with dependencies using tools like Docker.",
    "desc_ar": "تغليف التطبيقات مع متطلباتها باستخدام أدوات مثل دوكر.",
    "free": [
      "Docker official docs (free)",
      "freeCodeCamp Docker (YouTube)"
    ],
    "paid": [
      "Udemy: Docker & Kubernetes Bootcamp",
      "KodeKloud paid labs"
    ]
  },
  "monitoring": {
    "en": "Monitoring",
    "ar": "المراقبة",
    "desc_en": "Tracking system health and performance over time.",
    "desc_ar": "متابعة صحة النظام وأدائه بمرور الوقت.",
    "free": [
      "Prometheus/Grafana free docs",
      "freeCodeCamp Monitoring (YouTube)"
    ],
    "paid": [
      "Udemy: Monitoring with Prometheus & Grafana",
      "Pluralsight: Observability"
    ]
  },
  "cost optimization": {
    "en": "Cost Optimization",
    "ar": "تحسين التكلفة",
    "desc_en": "Reducing cloud/infrastructure spend without hurting performance.",
    "desc_ar": "تقليل تكلفة السحابة/البنية التحتية دون الإضرار بالأداء.",
    "free": [
      "AWS Cost free whitepapers",
      "Google Cloud cost docs (free)"
    ],
    "paid": [
      "A Cloud Guru cost courses (paid)",
      "Udemy: Cloud Cost Optimization"
    ]
  },
  "ci/cd": {
    "en": "CI/CD",
    "ar": "التكامل والنشر المستمر",
    "desc_en": "Automatically testing and deploying code changes.",
    "desc_ar": "اختبار ونشر تعديلات الكود تلقائيًا.",
    "free": [
      "GitHub Actions free docs",
      "freeCodeCamp CI/CD (YouTube)"
    ],
    "paid": [
      "Udemy: CI/CD with Jenkins & GitHub Actions",
      "Pluralsight: CI/CD Pipelines"
    ]
  },
  "infrastructure as code": {
    "en": "Infrastructure as Code",
    "ar": "البنية التحتية ككود",
    "desc_en": "Managing infrastructure through versioned config files.",
    "desc_ar": "إدارة البنية التحتية عبر ملفات إعداد قابلة للتتبع.",
    "free": [
      "Terraform free docs",
      "freeCodeCamp Terraform (YouTube)"
    ],
    "paid": [
      "Udemy: Terraform Complete Guide",
      "HashiCorp paid certification"
    ]
  },
  "data modeling": {
    "en": "Data Modeling",
    "ar": "نمذجة البيانات",
    "desc_en": "Designing how data is structured and related in a database.",
    "desc_ar": "تصميم كيفية تنظيم البيانات وعلاقاتها داخل قاعدة البيانات.",
    "free": [
      "freeCodeCamp Data Modeling (YouTube)",
      "PostgreSQL docs (free)"
    ],
    "paid": [
      "Udemy: Database Design Bootcamp",
      "DataCamp: Data Modeling"
    ]
  },
  "normalization": {
    "en": "Normalization",
    "ar": "التسوية (Normalization)",
    "desc_en": "Structuring database tables to reduce redundancy.",
    "desc_ar": "تنظيم جداول قاعدة البيانات لتقليل التكرار.",
    "free": [
      "Studytonight Normalization (free)",
      "freeCodeCamp Normalization (YouTube)"
    ],
    "paid": [
      "Udemy: Database Design & Normalization",
      "Pluralsight: DB Normalization"
    ]
  },
  "indexing": {
    "en": "Indexing",
    "ar": "الفهرسة",
    "desc_en": "Speeding up database queries using indexes.",
    "desc_ar": "تسريع استعلامات قاعدة البيانات باستخدام الفهارس.",
    "free": [
      "PostgreSQL Indexing docs (free)",
      "Use The Index, Luke (free)"
    ],
    "paid": [
      "Udemy: SQL Performance Tuning",
      "Pluralsight: Database Indexing"
    ]
  },
  "query optimization": {
    "en": "Query Optimization",
    "ar": "تحسين الاستعلامات",
    "desc_en": "Making database queries run faster and more efficiently.",
    "desc_ar": "جعل استعلامات قاعدة البيانات أسرع وأكثر كفاءة.",
    "free": [
      "Use The Index, Luke (free)",
      "PostgreSQL performance docs (free)"
    ],
    "paid": [
      "Udemy: SQL Performance Tuning",
      "Pluralsight: Query Optimization"
    ]
  },
  "backup and recovery": {
    "en": "Backup & Recovery",
    "ar": "النسخ الاحتياطي والاسترجاع",
    "desc_en": "Protecting data by backing it up and restoring it when needed.",
    "desc_ar": "حماية البيانات عبر نسخها احتياطيًا واستعادتها عند الحاجة.",
    "free": [
      "PostgreSQL Backup docs (free)",
      "freeCodeCamp DB Backup (YouTube)"
    ],
    "paid": [
      "Udemy: Database Administration",
      "Pluralsight: Backup & Recovery"
    ]
  },
  "nosql basics": {
    "en": "NoSQL Basics",
    "ar": "أساسيات قواعد بيانات NoSQL",
    "desc_en": "Non-relational databases for flexible or large-scale data.",
    "desc_ar": "قواعد بيانات غير علائقية للبيانات المرنة أو واسعة النطاق.",
    "free": [
      "MongoDB University (free)",
      "freeCodeCamp NoSQL (YouTube)"
    ],
    "paid": [
      "Udemy: MongoDB Complete Guide",
      "MongoDB Certified DBA (paid)"
    ]
  },
  "test design": {
    "en": "Test Design",
    "ar": "تصميم حالات الاختبار",
    "desc_en": "Planning test cases that cover key application scenarios.",
    "desc_ar": "تخطيط حالات اختبار تغطي أهم سيناريوهات التطبيق.",
    "free": [
      "Ministry of Testing free resources",
      "freeCodeCamp QA (YouTube)"
    ],
    "paid": [
      "Udemy: Software Testing Bootcamp",
      "ISTQB paid certification"
    ]
  },
  "bug reporting": {
    "en": "Bug Reporting",
    "ar": "توثيق الأخطاء",
    "desc_en": "Writing clear, reproducible bug reports for developers.",
    "desc_ar": "كتابة تقارير أخطاء واضحة وقابلة لإعادة التنفيذ للمطورين.",
    "free": [
      "Ministry of Testing free resources",
      "Atlassian Jira guides (free)"
    ],
    "paid": [
      "Udemy: QA Bug Tracking with Jira",
      "ISTQB paid certification"
    ]
  },
  "automation testing": {
    "en": "Test Automation",
    "ar": "أتمتة الاختبار",
    "desc_en": "Writing scripts that test software automatically.",
    "desc_ar": "كتابة سكربتات تختبر البرنامج تلقائيًا.",
    "free": [
      "Selenium official docs (free)",
      "freeCodeCamp Selenium (YouTube)"
    ],
    "paid": [
      "Udemy: Selenium WebDriver Bootcamp",
      "Test Automation University (paid tracks)"
    ]
  },
  "api testing": {
    "en": "API Testing",
    "ar": "اختبار واجهات البرمجة",
    "desc_en": "Verifying that APIs return correct responses.",
    "desc_ar": "التحقق من أن واجهات البرمجة تعيد استجابات صحيحة.",
    "free": [
      "Postman free docs/academy",
      "freeCodeCamp API Testing (YouTube)"
    ],
    "paid": [
      "Udemy: API Testing with Postman",
      "Postman Academy paid tracks"
    ]
  },
  "regression testing": {
    "en": "Regression Testing",
    "ar": "اختبار الانحدار",
    "desc_en": "Re-testing features to ensure new changes didn't break them.",
    "desc_ar": "إعادة اختبار الميزات للتأكد أن التعديلات الجديدة لم تُفسدها.",
    "free": [
      "Ministry of Testing free resources",
      "freeCodeCamp QA (YouTube)"
    ],
    "paid": [
      "Udemy: Regression Testing Strategies",
      "ISTQB paid certification"
    ]
  },
  "exploratory testing": {
    "en": "Exploratory Testing",
    "ar": "الاختبار الاستكشافي",
    "desc_en": "Testing software creatively without predefined scripts.",
    "desc_ar": "اختبار البرنامج بأسلوب استكشافي دون سكربتات محددة مسبقًا.",
    "free": [
      "Ministry of Testing free resources",
      "James Bach free articles"
    ],
    "paid": [
      "Udemy: Exploratory Testing Techniques",
      "BBST paid courses"
    ]
  },
  "user research": {
    "en": "User Research",
    "ar": "بحث المستخدم",
    "desc_en": "Understanding user needs through interviews and studies.",
    "desc_ar": "فهم احتياجات المستخدم عبر المقابلات والدراسات.",
    "free": [
      "Nielsen Norman Group free articles",
      "Google UX Design free modules"
    ],
    "paid": [
      "Coursera: Google UX Design Certificate",
      "Interaction Design Foundation (paid)"
    ]
  },
  "wireframing": {
    "en": "Wireframing",
    "ar": "التصميم الأولي (Wireframes)",
    "desc_en": "Sketching low-fidelity layouts of a product's screens.",
    "desc_ar": "رسم تخطيطي مبسط لشاشات المنتج.",
    "free": [
      "Figma free tutorials",
      "Balsamiq free guides"
    ],
    "paid": [
      "Udemy: UX Wireframing & Prototyping",
      "Interaction Design Foundation (paid)"
    ]
  },
  "prototyping": {
    "en": "Prototyping",
    "ar": "النماذج الأولية",
    "desc_en": "Building interactive mockups to test ideas before development.",
    "desc_ar": "بناء نماذج تفاعلية لاختبار الأفكار قبل التطوير.",
    "free": [
      "Figma free tutorials",
      "Adobe XD free tutorials"
    ],
    "paid": [
      "Udemy: Figma Prototyping Masterclass",
      "Interaction Design Foundation (paid)"
    ]
  },
  "visual design": {
    "en": "Visual Design",
    "ar": "التصميم البصري",
    "desc_en": "Applying color, typography and layout to create appealing UI.",
    "desc_ar": "تطبيق الألوان والخطوط والتخطيط لإنشاء واجهة جذابة.",
    "free": [
      "Figma Community free files",
      "Canva Design School (free)"
    ],
    "paid": [
      "Udemy: UI Visual Design Masterclass",
      "Interaction Design Foundation (paid)"
    ]
  },
  "usability testing": {
    "en": "Usability Testing",
    "ar": "اختبار قابلية الاستخدام",
    "desc_en": "Observing real users to evaluate how easy a product is to use.",
    "desc_ar": "ملاحظة مستخدمين حقيقيين لتقييم سهولة استخدام المنتج.",
    "free": [
      "Nielsen Norman Group free articles",
      "Google UX Design free modules"
    ],
    "paid": [
      "Coursera: Google UX Design Certificate",
      "UserTesting Academy (paid)"
    ]
  },
  "information architecture": {
    "en": "Information Architecture",
    "ar": "هندسة المعلومات",
    "desc_en": "Organizing and structuring content so users find it easily.",
    "desc_ar": "تنظيم المحتوى وهيكلته ليسهل على المستخدم إيجاده.",
    "free": [
      "Nielsen Norman Group free articles",
      "Google UX Design free modules"
    ],
    "paid": [
      "Interaction Design Foundation (paid)",
      "Udemy: Information Architecture for UX"
    ]
  },
  "interaction design": {
    "en": "Interaction Design",
    "ar": "تصميم التفاعل",
    "desc_en": "Designing how users interact with a product's elements.",
    "desc_ar": "تصميم طريقة تفاعل المستخدم مع عناصر المنتج.",
    "free": [
      "Interaction Design Foundation free articles",
      "Google UX Design free modules"
    ],
    "paid": [
      "Interaction Design Foundation (paid membership)",
      "Udemy: Interaction Design Specialization"
    ]
  },
  "dns": {
    "en": "DNS",
    "ar": "نظام أسماء النطاقات",
    "desc_en": "System that translates domain names into IP addresses.",
    "desc_ar": "نظام يترجم أسماء النطاقات إلى عناوين IP.",
    "free": [
      "Cloudflare Learning Center (free)",
      "freeCodeCamp DNS (YouTube)"
    ],
    "paid": [
      "Udemy: Networking Fundamentals",
      "CompTIA Network+ (paid cert)"
    ]
  },
  "routing": {
    "en": "Routing",
    "ar": "التوجيه (Routing)",
    "desc_en": "Directing data packets between networks efficiently.",
    "desc_ar": "توجيه حزم البيانات بين الشبكات بكفاءة.",
    "free": [
      "Cisco Networking Academy free intro",
      "freeCodeCamp Networking (YouTube)"
    ],
    "paid": [
      "Udemy: CCNA Routing & Switching",
      "Cisco CCNA paid certification"
    ]
  },
  "switching": {
    "en": "Switching",
    "ar": "التحويل (Switching)",
    "desc_en": "Connecting devices within the same local network.",
    "desc_ar": "ربط الأجهزة داخل نفس الشبكة المحلية.",
    "free": [
      "Cisco Networking Academy free intro",
      "freeCodeCamp Networking (YouTube)"
    ],
    "paid": [
      "Udemy: CCNA Routing & Switching",
      "Cisco CCNA paid certification"
    ]
  },
  "protocols": {
    "en": "Network Protocols",
    "ar": "بروتوكولات الشبكات",
    "desc_en": "Rules that govern how devices communicate (TCP/IP, etc).",
    "desc_ar": "القواعد التي تحكم تواصل الأجهزة (مثل TCP/IP).",
    "free": [
      "freeCodeCamp Networking (YouTube)",
      "Cisco Networking Academy free intro"
    ],
    "paid": [
      "Udemy: Networking Fundamentals",
      "CompTIA Network+ (paid cert)"
    ]
  },
  "troubleshooting": {
    "en": "Troubleshooting",
    "ar": "استكشاف الأخطاء وإصلاحها",
    "desc_en": "Diagnosing and resolving network or system problems.",
    "desc_ar": "تشخيص مشكلات الشبكة أو النظام وحلها.",
    "free": [
      "Cisco free resources",
      "freeCodeCamp Troubleshooting (YouTube)"
    ],
    "paid": [
      "Udemy: Network Troubleshooting",
      "CompTIA Network+ (paid cert)"
    ]
  },
  "network security": {
    "en": "Network Security",
    "ar": "أمن الشبكات",
    "desc_en": "Protecting network infrastructure from unauthorized access.",
    "desc_ar": "حماية البنية التحتية للشبكة من الوصول غير المصرح به.",
    "free": [
      "Cisco free security intro",
      "OWASP free resources"
    ],
    "paid": [
      "Udemy: Network Security Fundamentals",
      "CompTIA Security+ (paid cert)"
    ]
  },
  "c/c++": {
    "en": "C / C++",
    "ar": "سي / سي بلس بلس",
    "desc_en": "Low-level languages used for performance-critical systems.",
    "desc_ar": "لغات منخفضة المستوى تُستخدم في الأنظمة عالية الأداء.",
    "free": [
      "learncpp.com (free)",
      "freeCodeCamp C++ (YouTube)"
    ],
    "paid": [
      "Udemy: C++ Complete Bootcamp",
      "Coursera: C++ Specialization"
    ]
  },
  "microcontrollers": {
    "en": "Microcontrollers",
    "ar": "المتحكمات الدقيقة",
    "desc_en": "Small computers embedded in devices to control hardware.",
    "desc_ar": "حواسيب صغيرة مدمجة داخل الأجهزة للتحكم في العتاد.",
    "free": [
      "Arduino official docs (free)",
      "freeCodeCamp Embedded (YouTube)"
    ],
    "paid": [
      "Udemy: Embedded Systems with Arduino/STM32",
      "Coursera: Embedded Systems"
    ]
  },
  "electronics basics": {
    "en": "Electronics Basics",
    "ar": "أساسيات الإلكترونيات",
    "desc_en": "Fundamentals of circuits, voltage and components.",
    "desc_ar": "أساسيات الدوائر الكهربائية والفولت والمكونات.",
    "free": [
      "All About Circuits (free)",
      "freeCodeCamp Electronics (YouTube)"
    ],
    "paid": [
      "Udemy: Electronics for Beginners",
      "Coursera: Intro to Electronics"
    ]
  },
  "rtos": {
    "en": "RTOS",
    "ar": "نظام التشغيل الفوري",
    "desc_en": "Real-time operating systems for predictable embedded timing.",
    "desc_ar": "أنظمة تشغيل فورية توفر توقيتًا يمكن التنبؤ به للأنظمة المدمجة.",
    "free": [
      "FreeRTOS official docs (free)",
      "freeCodeCamp RTOS (YouTube)"
    ],
    "paid": [
      "Udemy: FreeRTOS from Ground Up",
      "Coursera: Real-Time Systems"
    ]
  },
  "c#": {
    "en": "C#",
    "ar": "سي شارب",
    "desc_en": "Object-oriented language widely used with Unity and .NET.",
    "desc_ar": "لغة كائنية التوجه تُستخدم بكثرة مع يونيتي ودوت نت.",
    "free": [
      "Microsoft Learn C# (free)",
      "freeCodeCamp C# (YouTube)"
    ],
    "paid": [
      "Udemy: Complete C# Masterclass",
      "Pluralsight: C# Fundamentals"
    ]
  },
  "game engine concepts": {
    "en": "Game Engine Concepts",
    "ar": "مفاهيم محركات الألعاب",
    "desc_en": "Core concepts behind how game engines render and run games.",
    "desc_ar": "المفاهيم الأساسية لكيفية عمل محركات الألعاب وعرضها.",
    "free": [
      "Unity Learn (free)",
      "freeCodeCamp Game Dev (YouTube)"
    ],
    "paid": [
      "Udemy: Unity Game Development",
      "Unreal Engine paid courses"
    ]
  },
  "3d math": {
    "en": "3D Math",
    "ar": "الرياضيات ثلاثية الأبعاد",
    "desc_en": "Vector and matrix math used to position objects in 3D space.",
    "desc_ar": "رياضيات المتجهات والمصفوفات لتحديد مواضع الأجسام في الفضاء ثلاثي الأبعاد.",
    "free": [
      "3Blue1Brown Linear Algebra (free)",
      "Khan Academy (free)"
    ],
    "paid": [
      "Udemy: Math for Game Developers",
      "Coursera: Computer Graphics"
    ]
  },
  "game design basics": {
    "en": "Game Design Basics",
    "ar": "أساسيات تصميم الألعاب",
    "desc_en": "Principles of designing fun and balanced gameplay.",
    "desc_ar": "مبادئ تصميم لعب ممتع ومتوازن.",
    "free": [
      "Game Maker's Toolkit (YouTube, free)",
      "Extra Credits (YouTube, free)"
    ],
    "paid": [
      "Udemy: Game Design Masterclass",
      "Coursera: Game Design"
    ]
  },
  "physics basics": {
    "en": "Physics Basics",
    "ar": "أساسيات الفيزياء",
    "desc_en": "Applying real-world physics rules to game movement/collisions.",
    "desc_ar": "تطبيق قواعد الفيزياء الواقعية على الحركة والتصادمات في الألعاب.",
    "free": [
      "Unity Physics docs (free)",
      "Khan Academy Physics (free)"
    ],
    "paid": [
      "Udemy: Game Physics Programming",
      "Coursera: Intro to Physics"
    ]
  },
  "solidity": {
    "en": "Solidity",
    "ar": "سوليديتي",
    "desc_en": "Programming language for writing Ethereum smart contracts.",
    "desc_ar": "لغة برمجة لكتابة العقود الذكية على إيثريوم.",
    "free": [
      "Solidity official docs (free)",
      "CryptoZombies (free interactive)"
    ],
    "paid": [
      "Udemy: Ethereum & Solidity Bootcamp",
      "ConsenSys Academy (paid)"
    ]
  },
  "smart contract development": {
    "en": "Smart Contract Development",
    "ar": "تطوير العقود الذكية",
    "desc_en": "Building self-executing contracts that run on a blockchain.",
    "desc_ar": "بناء عقود ذاتية التنفيذ تعمل على البلوك تشين.",
    "free": [
      "Solidity official docs (free)",
      "CryptoZombies (free interactive)"
    ],
    "paid": [
      "Udemy: Solidity, Blockchain & Smart Contracts",
      "ConsenSys Academy (paid)"
    ]
  },
  "web3 basics": {
    "en": "Web3 Basics",
    "ar": "أساسيات ويب 3",
    "desc_en": "Fundamentals of decentralized apps and blockchain interaction.",
    "desc_ar": "أساسيات التطبيقات اللامركزية والتعامل مع البلوك تشين.",
    "free": [
      "Ethereum.org free docs",
      "Alchemy University (free)"
    ],
    "paid": [
      "Udemy: Web3 & Blockchain Developer Bootcamp",
      "Moralis Web3 paid courses"
    ]
  },
  "vscode": {
    "en": "VS Code",
    "ar": "في اس كود",
    "desc_en": "Popular free code editor with rich extensions.",
    "desc_ar": "محرر أكواد مجاني وشهير بإضافات غنية.",
    "free": [
      "VS Code official docs (free)",
      "freeCodeCamp VS Code tips (YouTube)"
    ],
    "paid": [
      "Udemy: VS Code Productivity",
      "Pluralsight: VS Code Tips"
    ]
  },
  "postgresql": {
    "en": "PostgreSQL",
    "ar": "بوستجريسكيوال",
    "desc_en": "Powerful open-source relational database system.",
    "desc_ar": "نظام قاعدة بيانات علائقية مفتوح المصدر وقوي.",
    "free": [
      "PostgreSQL official docs (free)",
      "freeCodeCamp PostgreSQL (YouTube)"
    ],
    "paid": [
      "Udemy: PostgreSQL Bootcamp",
      "DataCamp: PostgreSQL Track"
    ]
  },
  "pytest": {
    "en": "Pytest",
    "ar": "باي تست",
    "desc_en": "Popular Python testing framework.",
    "desc_ar": "إطار عمل شهير لاختبار كود بايثون.",
    "free": [
      "Pytest official docs (free)",
      "freeCodeCamp Pytest (YouTube)"
    ],
    "paid": [
      "Udemy: Testing with Pytest",
      "Test Automation University (paid tracks)"
    ]
  },
  "github": {
    "en": "GitHub",
    "ar": "جيت هاب",
    "desc_en": "Platform for hosting Git repositories and collaboration.",
    "desc_ar": "منصة لاستضافة مستودعات Git والتعاون البرمجي.",
    "free": [
      "GitHub docs (free)",
      "freeCodeCamp GitHub (YouTube)"
    ],
    "paid": [
      "Udemy: GitHub Actions & Collaboration",
      "Pluralsight: GitHub Fundamentals"
    ]
  },
  "docker": {
    "en": "Docker",
    "ar": "دوكر",
    "desc_en": "Tool for packaging applications into portable containers.",
    "desc_ar": "أداة لتغليف التطبيقات في حاويات قابلة للنقل.",
    "free": [
      "Docker official docs (free)",
      "freeCodeCamp Docker (YouTube)"
    ],
    "paid": [
      "Udemy: Docker & Kubernetes Bootcamp",
      "KodeKloud paid labs"
    ]
  },
  "postman": {
    "en": "Postman",
    "ar": "بوستمان",
    "desc_en": "Tool for testing and documenting APIs.",
    "desc_ar": "أداة لاختبار وتوثيق واجهات البرمجة.",
    "free": [
      "Postman free docs/academy",
      "freeCodeCamp Postman (YouTube)"
    ],
    "paid": [
      "Postman Academy paid tracks",
      "Udemy: API Testing with Postman"
    ]
  },
  "jira": {
    "en": "Jira",
    "ar": "جيرا",
    "desc_en": "Project/issue tracking tool used by software teams.",
    "desc_ar": "أداة لتتبع المهام والمشاريع تستخدمها فرق البرمجة.",
    "free": [
      "Atlassian Jira free guides",
      "freeCodeCamp Jira (YouTube)"
    ],
    "paid": [
      "Udemy: Jira Project Management",
      "Atlassian University (paid certs)"
    ]
  },
  "linux terminal": {
    "en": "Linux Terminal",
    "ar": "الطرفية (Terminal)",
    "desc_en": "Command-line interface for controlling Linux systems.",
    "desc_ar": "واجهة سطر أوامر للتحكم في أنظمة لينكس.",
    "free": [
      "Linux Journey (free)",
      "freeCodeCamp Linux (YouTube)"
    ],
    "paid": [
      "Udemy: Linux Command Line Bootcamp",
      "Linux Foundation (paid cert)"
    ]
  },
  "chrome devtools": {
    "en": "Chrome DevTools",
    "ar": "أدوات مطوري كروم",
    "desc_en": "Built-in browser tools for debugging web pages.",
    "desc_ar": "أدوات مدمجة بالمتصفح لتصحيح صفحات الويب.",
    "free": [
      "Chrome DevTools docs (free)",
      "freeCodeCamp DevTools (YouTube)"
    ],
    "paid": [
      "Udemy: Chrome DevTools Mastery",
      "Frontend Masters: Debugging"
    ]
  },
  "npm": {
    "en": "npm",
    "ar": "إن بي إم",
    "desc_en": "Package manager for JavaScript/Node.js projects.",
    "desc_ar": "مدير حزم لمشاريع جافاسكريبت/نود.",
    "free": [
      "npm official docs (free)",
      "freeCodeCamp npm (YouTube)"
    ],
    "paid": [
      "Udemy: npm & Node Package Management",
      "Frontend Masters: Node track"
    ]
  },
  "netlify": {
    "en": "Netlify / Vercel",
    "ar": "نتليفاي / فيرسل",
    "desc_en": "Platforms for deploying and hosting web apps easily.",
    "desc_ar": "منصات لنشر واستضافة تطبيقات الويب بسهولة.",
    "free": [
      "Netlify docs (free)",
      "Vercel docs (free)"
    ],
    "paid": [
      "Udemy: Deploying Web Apps",
      "Frontend Masters: Deployment"
    ]
  },
  "figma": {
    "en": "Figma",
    "ar": "فيجما",
    "desc_en": "Collaborative interface design and prototyping tool.",
    "desc_ar": "أداة تصميم واجهات ونماذج تفاعلية تعاونية.",
    "free": [
      "Figma official tutorials (free)",
      "freeCodeCamp Figma (YouTube)"
    ],
    "paid": [
      "Udemy: Figma UI/UX Masterclass",
      "Interaction Design Foundation (paid)"
    ]
  },
  "react devtools": {
    "en": "React DevTools",
    "ar": "أدوات رياكت للمطورين",
    "desc_en": "Browser extension for inspecting React component trees.",
    "desc_ar": "إضافة متصفح لفحص شجرة مكونات رياكت.",
    "free": [
      "React DevTools docs (free)",
      "freeCodeCamp React DevTools (YouTube)"
    ],
    "paid": [
      "Frontend Masters: React track (paid)",
      "Udemy: React Debugging"
    ]
  },
  "webpack/vite": {
    "en": "Webpack / Vite",
    "ar": "ويب باك / فايت",
    "desc_en": "Build tools that bundle frontend code for production.",
    "desc_ar": "أدوات بناء تجمع كود الواجهة الأمامية للإنتاج.",
    "free": [
      "Vite official docs (free)",
      "Webpack official docs (free)"
    ],
    "paid": [
      "Udemy: Modern Frontend Tooling",
      "Frontend Masters: Build Tools"
    ]
  },
  "jest": {
    "en": "Jest",
    "ar": "جيست",
    "desc_en": "JavaScript testing framework commonly used with React.",
    "desc_ar": "إطار عمل لاختبار جافاسكريبت يُستخدم كثيرًا مع رياكت.",
    "free": [
      "Jest official docs (free)",
      "freeCodeCamp Jest (YouTube)"
    ],
    "paid": [
      "Udemy: Testing React with Jest",
      "Frontend Masters: Testing"
    ]
  },
  "redis": {
    "en": "Redis",
    "ar": "ريديس",
    "desc_en": "In-memory data store used for caching and fast lookups.",
    "desc_ar": "قاعدة بيانات في الذاكرة تُستخدم للتخزين المؤقت والبحث السريع.",
    "free": [
      "Redis official docs (free)",
      "freeCodeCamp Redis (YouTube)"
    ],
    "paid": [
      "Udemy: Redis Crash Course",
      "Pluralsight: Redis Fundamentals"
    ]
  },
  "android studio": {
    "en": "Android Studio",
    "ar": "أندرويد ستوديو",
    "desc_en": "Official IDE for building native Android apps.",
    "desc_ar": "بيئة التطوير الرسمية لبناء تطبيقات أندرويد الأصلية.",
    "free": [
      "Android Developers docs (free)",
      "freeCodeCamp Android (YouTube)"
    ],
    "paid": [
      "Udemy: Android Development Bootcamp",
      "Google Associate Android Developer (paid)"
    ]
  },
  "xcode": {
    "en": "Xcode",
    "ar": "إكس كود",
    "desc_en": "Apple's IDE for building iOS/macOS applications.",
    "desc_ar": "بيئة تطوير أبل لبناء تطبيقات iOS/macOS.",
    "free": [
      "Apple Developer docs (free)",
      "Hacking with Swift (free)"
    ],
    "paid": [
      "Udemy: iOS Development Bootcamp",
      "Kodeco paid tracks"
    ]
  },
  "flutter": {
    "en": "Flutter",
    "ar": "فلاتر",
    "desc_en": "Google's UI toolkit for building cross-platform apps.",
    "desc_ar": "إطار عمل جوجل لبناء تطبيقات متعددة المنصات.",
    "free": [
      "Flutter official docs (free)",
      "freeCodeCamp Flutter (YouTube)"
    ],
    "paid": [
      "Udemy: Flutter & Dart Complete Guide",
      "Udacity Flutter track (paid)"
    ]
  },
  "firebase": {
    "en": "Firebase",
    "ar": "فايربيز",
    "desc_en": "Google's backend platform for auth, database and hosting.",
    "desc_ar": "منصة جوجل الخلفية للمصادقة وقاعدة البيانات والاستضافة.",
    "free": [
      "Firebase official docs (free)",
      "freeCodeCamp Firebase (YouTube)"
    ],
    "paid": [
      "Udemy: Firebase Complete Guide",
      "Google Firebase paid workshops"
    ]
  },
  "power bi": {
    "en": "Power BI",
    "ar": "باور بي آي",
    "desc_en": "Microsoft's business intelligence and dashboard tool.",
    "desc_ar": "أداة مايكروسوفت لذكاء الأعمال ولوحات المؤشرات.",
    "free": [
      "Microsoft Learn Power BI (free)",
      "freeCodeCamp Power BI (YouTube)"
    ],
    "paid": [
      "Udemy: Power BI Masterclass",
      "Microsoft PL-300 certification (paid)"
    ]
  },
  "tableau": {
    "en": "Tableau",
    "ar": "تابلوه",
    "desc_en": "Popular data visualization and dashboard software.",
    "desc_ar": "برنامج شهير لتصور البيانات ولوحات المؤشرات.",
    "free": [
      "Tableau free training videos",
      "freeCodeCamp Tableau (YouTube)"
    ],
    "paid": [
      "Udemy: Tableau Masterclass",
      "Tableau Desktop certification (paid)"
    ]
  },
  "jupyter": {
    "en": "Jupyter Notebook",
    "ar": "جوبيتر",
    "desc_en": "Interactive coding environment popular in data science.",
    "desc_ar": "بيئة برمجة تفاعلية شائعة في علم البيانات.",
    "free": [
      "Jupyter official docs (free)",
      "freeCodeCamp Jupyter (YouTube)"
    ],
    "paid": [
      "DataCamp: Jupyter Notebook Track",
      "Udemy: Jupyter for Data Science"
    ]
  },
  "google sheets": {
    "en": "Google Sheets",
    "ar": "جوجل شيتس",
    "desc_en": "Free cloud-based spreadsheet tool.",
    "desc_ar": "أداة جداول بيانات مجانية تعمل على السحابة.",
    "free": [
      "Google Sheets free help center",
      "freeCodeCamp Google Sheets (YouTube)"
    ],
    "paid": [
      "Udemy: Google Sheets Masterclass",
      "LinkedIn Learning: Sheets Essentials"
    ]
  },
  "scikit-learn": {
    "en": "scikit-learn",
    "ar": "ساي كيت ليرن",
    "desc_en": "Python library for classic machine learning algorithms.",
    "desc_ar": "مكتبة بايثون لخوارزميات تعلم الآلة الكلاسيكية.",
    "free": [
      "scikit-learn official docs (free)",
      "freeCodeCamp scikit-learn (YouTube)"
    ],
    "paid": [
      "Udemy: ML with scikit-learn",
      "DataCamp: Supervised Learning Track"
    ]
  },
  "tensorflow": {
    "en": "TensorFlow",
    "ar": "تنسورفلو",
    "desc_en": "Google's open-source deep learning framework.",
    "desc_ar": "إطار عمل جوجل مفتوح المصدر للتعلم العميق.",
    "free": [
      "TensorFlow official docs (free)",
      "freeCodeCamp TensorFlow (YouTube)"
    ],
    "paid": [
      "Coursera: DeepLearning.AI TensorFlow",
      "Udemy: TensorFlow Developer Bootcamp"
    ]
  },
  "pytorch": {
    "en": "PyTorch",
    "ar": "باي تورش",
    "desc_en": "Popular deep learning framework from Meta.",
    "desc_ar": "إطار عمل شهير للتعلم العميق من ميتا.",
    "free": [
      "PyTorch official docs (free)",
      "freeCodeCamp PyTorch (YouTube)"
    ],
    "paid": [
      "Udemy: PyTorch for Deep Learning",
      "fast.ai paid-adjacent course"
    ]
  },
  "google colab": {
    "en": "Google Colab",
    "ar": "جوجل كولاب",
    "desc_en": "Free cloud notebooks with GPU access for ML experiments.",
    "desc_ar": "دفاتر سحابية مجانية بإمكانية استخدام GPU لتجارب تعلم الآلة.",
    "free": [
      "Google Colab official docs (free)",
      "freeCodeCamp Colab (YouTube)"
    ],
    "paid": [
      "Coursera: ML courses using Colab",
      "Udemy: Deep Learning with Colab"
    ]
  },
  "wireshark": {
    "en": "Wireshark",
    "ar": "واير شارك",
    "desc_en": "Tool for capturing and analyzing network traffic.",
    "desc_ar": "أداة لالتقاط وتحليل حركة مرور الشبكة.",
    "free": [
      "Wireshark official docs (free)",
      "freeCodeCamp Wireshark (YouTube)"
    ],
    "paid": [
      "Udemy: Wireshark Masterclass",
      "INE Security paid labs"
    ]
  },
  "nmap": {
    "en": "Nmap",
    "ar": "إنماب",
    "desc_en": "Network scanning tool used for security assessments.",
    "desc_ar": "أداة فحص شبكات تُستخدم في التقييم الأمني.",
    "free": [
      "Nmap official docs (free)",
      "freeCodeCamp Nmap (YouTube)"
    ],
    "paid": [
      "Udemy: Nmap for Ethical Hacking",
      "INE Security paid labs"
    ]
  },
  "kali linux": {
    "en": "Kali Linux",
    "ar": "كالي لينكس",
    "desc_en": "Linux distribution preloaded with security testing tools.",
    "desc_ar": "توزيعة لينكس محمّلة بأدوات اختبار الاختراق.",
    "free": [
      "Kali Linux official docs (free)",
      "freeCodeCamp Kali Linux (YouTube)"
    ],
    "paid": [
      "Udemy: Ethical Hacking with Kali",
      "Offensive Security PEN-200 (paid)"
    ]
  },
  "burp suite": {
    "en": "Burp Suite",
    "ar": "بيرب سويت",
    "desc_en": "Tool for testing the security of web applications.",
    "desc_ar": "أداة لاختبار أمان تطبيقات الويب.",
    "free": [
      "PortSwigger free Web Security Academy",
      "Burp Suite official docs (free)"
    ],
    "paid": [
      "Udemy: Burp Suite Bootcamp",
      "PortSwigger paid labs"
    ]
  },
  "metasploit": {
    "en": "Metasploit",
    "ar": "ميتاسبلويت",
    "desc_en": "Penetration testing framework for exploiting vulnerabilities.",
    "desc_ar": "إطار عمل لاختبار الاختراق واستغلال الثغرات.",
    "free": [
      "Metasploit official docs (free)",
      "freeCodeCamp Metasploit (YouTube)"
    ],
    "paid": [
      "Udemy: Metasploit Bootcamp",
      "Offensive Security paid training"
    ]
  },
  "siem": {
    "en": "SIEM Basics",
    "ar": "أساسيات SIEM",
    "desc_en": "Tools that collect and analyze security logs centrally.",
    "desc_ar": "أدوات تجمع سجلات الأمان وتحللها مركزيًا.",
    "free": [
      "Splunk free training",
      "freeCodeCamp SIEM (YouTube)"
    ],
    "paid": [
      "Udemy: SIEM with Splunk/ELK",
      "Splunk paid certification"
    ]
  },
  "aws": {
    "en": "AWS",
    "ar": "أمازون ويب سيرفيسز",
    "desc_en": "Amazon's cloud computing platform.",
    "desc_ar": "منصة أمازون للحوسبة السحابية.",
    "free": [
      "AWS Free Tier + docs",
      "AWS Skill Builder (free tier)"
    ],
    "paid": [
      "AWS Certified Cloud Practitioner (paid)",
      "Udemy: AWS Certified Solutions Architect"
    ]
  },
  "azure": {
    "en": "Azure",
    "ar": "أزور",
    "desc_en": "Microsoft's cloud computing platform.",
    "desc_ar": "منصة مايكروسوفت للحوسبة السحابية.",
    "free": [
      "Microsoft Learn Azure (free)",
      "Azure free account docs"
    ],
    "paid": [
      "Microsoft Azure Fundamentals AZ-900 (paid)",
      "Udemy: Azure Administrator"
    ]
  },
  "gcp": {
    "en": "GCP",
    "ar": "جوجل كلاود",
    "desc_en": "Google's cloud computing platform.",
    "desc_ar": "منصة جوجل للحوسبة السحابية.",
    "free": [
      "Google Cloud Skills Boost (free tier)",
      "GCP free tier docs"
    ],
    "paid": [
      "Google Cloud Associate Engineer (paid)",
      "Udemy: GCP Associate Cloud Engineer"
    ]
  },
  "kubernetes": {
    "en": "Kubernetes",
    "ar": "كوبرنيتيس",
    "desc_en": "System for automating deployment and scaling of containers.",
    "desc_ar": "نظام لأتمتة نشر وتوسيع الحاويات.",
    "free": [
      "Kubernetes official docs (free)",
      "freeCodeCamp Kubernetes (YouTube)"
    ],
    "paid": [
      "Udemy: Kubernetes Bootcamp",
      "KodeKloud paid labs"
    ]
  },
  "terraform": {
    "en": "Terraform",
    "ar": "تيرافورم",
    "desc_en": "Tool for defining cloud infrastructure as code.",
    "desc_ar": "أداة لتعريف البنية التحتية السحابية ككود.",
    "free": [
      "Terraform official docs (free)",
      "freeCodeCamp Terraform (YouTube)"
    ],
    "paid": [
      "Udemy: Terraform Complete Guide",
      "HashiCorp paid certification"
    ]
  },
  "jenkins": {
    "en": "Jenkins",
    "ar": "جينكنز",
    "desc_en": "Open-source automation server for CI/CD pipelines.",
    "desc_ar": "سيرفر أتمتة مفتوح المصدر لخطوط CI/CD.",
    "free": [
      "Jenkins official docs (free)",
      "freeCodeCamp Jenkins (YouTube)"
    ],
    "paid": [
      "Udemy: Jenkins Complete Guide",
      "CloudBees paid training"
    ]
  },
  "github actions": {
    "en": "GitHub Actions",
    "ar": "جيت هاب أكشنز",
    "desc_en": "Built-in CI/CD automation for GitHub repositories.",
    "desc_ar": "أتمتة CI/CD مدمجة في مستودعات جيت هاب.",
    "free": [
      "GitHub Actions official docs (free)",
      "freeCodeCamp GitHub Actions (YouTube)"
    ],
    "paid": [
      "Udemy: GitHub Actions Masterclass",
      "Pluralsight: GitHub Actions"
    ]
  },
  "prometheus": {
    "en": "Prometheus / Grafana",
    "ar": "بروميثيوس / جرافانا",
    "desc_en": "Tools for collecting metrics and visualizing system health.",
    "desc_ar": "أدوات لجمع المقاييس وعرض صحة النظام بصريًا.",
    "free": [
      "Prometheus official docs (free)",
      "Grafana official docs (free)"
    ],
    "paid": [
      "Udemy: Prometheus & Grafana Monitoring",
      "Pluralsight: Observability"
    ]
  },
  "ansible": {
    "en": "Ansible",
    "ar": "أنسيبل",
    "desc_en": "Automation tool for configuring servers and deployments.",
    "desc_ar": "أداة أتمتة لإعداد السيرفرات وعمليات النشر.",
    "free": [
      "Ansible official docs (free)",
      "freeCodeCamp Ansible (YouTube)"
    ],
    "paid": [
      "Udemy: Ansible for DevOps",
      "Red Hat paid certification"
    ]
  },
  "mysql": {
    "en": "MySQL",
    "ar": "ماي إس كيو إل",
    "desc_en": "Widely used open-source relational database.",
    "desc_ar": "قاعدة بيانات علائقية مفتوحة المصدر منتشرة بكثرة.",
    "free": [
      "MySQL official docs (free)",
      "freeCodeCamp MySQL (YouTube)"
    ],
    "paid": [
      "Udemy: MySQL Bootcamp",
      "Oracle MySQL certification (paid)"
    ]
  },
  "mongodb": {
    "en": "MongoDB",
    "ar": "مونجو دي بي",
    "desc_en": "Popular document-based NoSQL database.",
    "desc_ar": "قاعدة بيانات NoSQL شهيرة قائمة على المستندات.",
    "free": [
      "MongoDB University (free)",
      "freeCodeCamp MongoDB (YouTube)"
    ],
    "paid": [
      "Udemy: MongoDB Complete Guide",
      "MongoDB Certified DBA (paid)"
    ]
  },
  "pgadmin": {
    "en": "pgAdmin / MySQL Workbench",
    "ar": "بي جي أدمن / ماي إس كيو إل ووركبنش",
    "desc_en": "GUI tools for managing relational databases visually.",
    "desc_ar": "أدوات رسومية لإدارة قواعد البيانات العلائقية بصريًا.",
    "free": [
      "pgAdmin official docs (free)",
      "MySQL Workbench docs (free)"
    ],
    "paid": [
      "Udemy: Database Administration Bootcamp",
      "Pluralsight: DB Management Tools"
    ]
  },
  "selenium": {
    "en": "Selenium",
    "ar": "سيلينيوم",
    "desc_en": "Framework for automating web browser testing.",
    "desc_ar": "إطار عمل لأتمتة اختبار متصفحات الويب.",
    "free": [
      "Selenium official docs (free)",
      "freeCodeCamp Selenium (YouTube)"
    ],
    "paid": [
      "Udemy: Selenium WebDriver Bootcamp",
      "Test Automation University (paid tracks)"
    ]
  },
  "testrail": {
    "en": "TestRail",
    "ar": "تست رايل",
    "desc_en": "Test case management tool for QA teams.",
    "desc_ar": "أداة لإدارة حالات الاختبار لفرق ضمان الجودة.",
    "free": [
      "TestRail free docs",
      "Ministry of Testing free resources"
    ],
    "paid": [
      "TestRail paid training",
      "Udemy: Test Case Management"
    ]
  },
  "cypress": {
    "en": "Cypress",
    "ar": "سايبرس",
    "desc_en": "Modern JavaScript end-to-end testing framework.",
    "desc_ar": "إطار عمل حديث لاختبار الواجهات من طرف إلى طرف بجافاسكريبت.",
    "free": [
      "Cypress official docs (free)",
      "freeCodeCamp Cypress (YouTube)"
    ],
    "paid": [
      "Udemy: Cypress End-to-End Testing",
      "Test Automation University (paid tracks)"
    ]
  },
  "adobe xd": {
    "en": "Adobe XD",
    "ar": "أدوبي إكس دي",
    "desc_en": "Design and prototyping tool for UI/UX (Figma alternative).",
    "desc_ar": "أداة تصميم ونماذج أولية لواجهات المستخدم (بديل لفيجما).",
    "free": [
      "Adobe XD free tutorials",
      "YouTube Adobe XD basics"
    ],
    "paid": [
      "Udemy: Adobe XD UI/UX Design",
      "Adobe paid courses"
    ]
  },
  "miro": {
    "en": "Miro",
    "ar": "ميرو",
    "desc_en": "Online collaborative whiteboard for research and planning.",
    "desc_ar": "سبورة تعاونية أونلاين للبحث والتخطيط.",
    "free": [
      "Miro free templates/guides",
      "YouTube Miro basics"
    ],
    "paid": [
      "Udemy: Miro for UX Teams",
      "Miroverse paid workshops"
    ]
  },
  "notion": {
    "en": "Notion",
    "ar": "نوشن",
    "desc_en": "Workspace tool for notes, docs and light project tracking.",
    "desc_ar": "أداة لتنظيم الملاحظات والمستندات ومتابعة المهام.",
    "free": [
      "Notion official guides (free)",
      "YouTube Notion basics"
    ],
    "paid": [
      "Udemy: Notion Mastery",
      "Notion paid templates/courses"
    ]
  },
  "maze": {
    "en": "Maze / UserTesting",
    "ar": "مايز / يوزر تستنج",
    "desc_en": "Platforms for running remote usability tests.",
    "desc_ar": "منصات لإجراء اختبارات قابلية الاستخدام عن بعد.",
    "free": [
      "Maze free guides",
      "UserTesting free blog"
    ],
    "paid": [
      "Maze paid plans",
      "UserTesting Academy (paid)"
    ]
  },
  "cisco packet tracer": {
    "en": "Cisco Packet Tracer",
    "ar": "سيسكو باكيت تريسر",
    "desc_en": "Free network simulation tool for practicing networking.",
    "desc_ar": "أداة محاكاة شبكات مجانية للتدرب على الشبكات.",
    "free": [
      "Cisco Networking Academy (free)",
      "YouTube Packet Tracer tutorials"
    ],
    "paid": [
      "Udemy: CCNA with Packet Tracer",
      "Cisco CCNA paid certification"
    ]
  },
  "putty": {
    "en": "PuTTY",
    "ar": "بوتي",
    "desc_en": "Lightweight tool for remote terminal/SSH connections.",
    "desc_ar": "أداة خفيفة للاتصال البعيد عبر SSH بالطرفية.",
    "free": [
      "PuTTY official docs (free)",
      "YouTube PuTTY basics"
    ],
    "paid": [
      "Udemy: SSH & Remote Access",
      "Pluralsight: Remote Administration"
    ]
  },
  "arduino ide": {
    "en": "Arduino IDE",
    "ar": "أردوينو IDE",
    "desc_en": "Beginner-friendly environment for programming microcontrollers.",
    "desc_ar": "بيئة سهلة للمبتدئين لبرمجة المتحكمات الدقيقة.",
    "free": [
      "Arduino official docs (free)",
      "freeCodeCamp Arduino (YouTube)"
    ],
    "paid": [
      "Udemy: Arduino Bootcamp",
      "Coursera: Embedded Systems"
    ]
  },
  "keil": {
    "en": "Keil / STM32CubeIDE",
    "ar": "كيل / STM32CubeIDE",
    "desc_en": "Professional IDEs for programming ARM microcontrollers.",
    "desc_ar": "بيئات تطوير احترافية لبرمجة متحكمات ARM.",
    "free": [
      "STMicroelectronics free docs",
      "YouTube STM32 tutorials"
    ],
    "paid": [
      "Udemy: STM32 Embedded Bootcamp",
      "Coursera: Embedded Systems"
    ]
  },
  "unity": {
    "en": "Unity",
    "ar": "يونيتي",
    "desc_en": "Popular cross-platform game engine.",
    "desc_ar": "محرك ألعاب شهير يعمل على منصات متعددة.",
    "free": [
      "Unity Learn (free)",
      "freeCodeCamp Unity (YouTube)"
    ],
    "paid": [
      "Udemy: Unity Game Development Bootcamp",
      "Unity Certified Developer (paid)"
    ]
  },
  "unreal engine": {
    "en": "Unreal Engine",
    "ar": "أنريل إنجن",
    "desc_en": "High-fidelity game engine widely used for AAA games.",
    "desc_ar": "محرك ألعاب عالي الجودة يُستخدم في ألعاب AAA.",
    "free": [
      "Unreal Engine official docs (free)",
      "freeCodeCamp Unreal (YouTube)"
    ],
    "paid": [
      "Udemy: Unreal Engine Bootcamp",
      "Unreal Authorized Training (paid)"
    ]
  },
  "blender": {
    "en": "Blender",
    "ar": "بلندر",
    "desc_en": "Free 3D modeling and animation software.",
    "desc_ar": "برنامج مجاني للنمذجة والرسوم المتحركة ثلاثية الأبعاد.",
    "free": [
      "Blender official docs (free)",
      "Blender Guru (YouTube, free)"
    ],
    "paid": [
      "Udemy: Blender Masterclass",
      "CG Cookie paid courses"
    ]
  },
  "visual studio": {
    "en": "Visual Studio",
    "ar": "فيجوال ستوديو",
    "desc_en": "Full-featured IDE commonly used with C#/.NET and Unity.",
    "desc_ar": "بيئة تطوير متكاملة تُستخدم كثيرًا مع سي شارب ودوت نت ويونيتي.",
    "free": [
      "Microsoft Learn Visual Studio (free)",
      "YouTube Visual Studio basics"
    ],
    "paid": [
      "Udemy: Visual Studio Productivity",
      "Pluralsight: Visual Studio"
    ]
  },
  "remix ide": {
    "en": "Remix IDE",
    "ar": "ريمكس IDE",
    "desc_en": "Browser-based IDE for writing and testing Solidity contracts.",
    "desc_ar": "بيئة تطوير في المتصفح لكتابة واختبار عقود سوليديتي.",
    "free": [
      "Remix official docs (free)",
      "CryptoZombies (free interactive)"
    ],
    "paid": [
      "Udemy: Solidity & Remix Bootcamp",
      "ConsenSys Academy (paid)"
    ]
  },
  "hardhat": {
    "en": "Hardhat / Truffle",
    "ar": "هاردهات / ترافل",
    "desc_en": "Development frameworks for building and testing smart contracts.",
    "desc_ar": "أطر عمل لبناء واختبار العقود الذكية.",
    "free": [
      "Hardhat official docs (free)",
      "Truffle official docs (free)"
    ],
    "paid": [
      "Udemy: Hardhat Smart Contract Bootcamp",
      "ConsenSys Academy (paid)"
    ]
  },
  "metamask": {
    "en": "MetaMask",
    "ar": "ميتاماسك",
    "desc_en": "Browser wallet for interacting with Ethereum-based apps.",
    "desc_ar": "محفظة متصفح للتعامل مع تطبيقات إيثريوم.",
    "free": [
      "MetaMask official docs (free)",
      "Ethereum.org free guides"
    ],
    "paid": [
      "Udemy: Web3 Wallet Integration",
      "Moralis Web3 paid courses"
    ]
  }
}

FIELDS = [
  {
    "id": "software-development",
    "name": "Software Development",
    "ar": "تطوير البرمجيات",
    "desc": "Building reliable applications and software systems from requirements to deployment and maintenance.",
    "ar_desc": "بناء التطبيقات والأنظمة البرمجية الموثوقة من فهم المتطلبات حتى النشر والصيانة.",
    "junior_overview": {
      "en": "A junior software developer turns small, well-defined tasks into working code under a senior's guidance. Day to day they implement small features from a written spec, fix reported bugs, write unit tests for the code they add, use Git branches and open pull requests for review, read existing modules to understand how a system fits together, and document the changes they make so teammates can follow their work.",
      "ar": "مطور البرمجيات المبتدئ (جونيور) يحوّل مهام صغيرة وواضحة إلى كود فعلي تحت إشراف مطور أكبر خبرة. في عمله اليومي ينفّذ ميزات صغيرة من مواصفات مكتوبة، ويصلح الأخطاء المُبلّغ عنها، ويكتب اختبارات وحدة للكود الذي يضيفه، ويستخدم فروع Git ويفتح طلبات دمج (Pull Requests) للمراجعة، ويقرأ الكود الموجود ليفهم كيف يترابط النظام، ويوثّق التغييرات التي يجريها حتى يستطيع زملاؤه متابعة عمله."
    },
    "skills": [
      "python",
      "git",
      "oop",
      "data structures",
      "algorithms",
      "sql",
      "testing",
      "apis",
      "debugging",
      "clean code",
      "design patterns",
      "linux",
      "problem solving",
      "version control"
    ],
    "tools": [
      "python",
      "git",
      "vscode",
      "postgresql",
      "pytest",
      "github",
      "docker",
      "postman",
      "jira",
      "linux terminal"
    ],
    "roles": [
      "Fresh Graduate / Trainee Developer",
      "Junior Software Developer",
      "Software Engineer",
      "Senior Software Engineer",
      "Tech Lead",
      "Software Architect"
    ],
    "junior": [
      "Implement small features from specifications",
      "Fix bugs and write unit tests",
      "Use Git branches and pull requests",
      "Read existing code and document changes"
    ],
    "salary": "Egypt market estimate: junior software-engineering compensation varies widely by company, stack and location; recent Cairo estimates commonly fall around EGP 8K–17K/month. Treat this as an indicative market range, not a guaranteed offer.",
    "roadmap": [
      [
        "Foundation (Months 1-2)",
        "Programming fundamentals, Python syntax, functions, modules, debugging basics, using the terminal"
      ],
      [
        "Level 1 (Months 3-4)",
        "OOP concepts, Git & GitHub workflow, core data structures and algorithms"
      ],
      [
        "Level 2 (Months 5-6)",
        "SQL and relational databases, HTTP basics, writing unit tests"
      ],
      [
        "Level 3 (Months 7-8)",
        "REST APIs, clean code and design patterns, code review etiquette"
      ],
      [
        "Level 4 (Months 9-10)",
        "Docker basics, security fundamentals, CI basics, structured debugging"
      ],
      [
        "Level 5 (Months 11-12)",
        "Portfolio projects, mock interviews, system design basics, applying to junior roles"
      ]
    ],
    "companies_eg": [
      "Microsoft ADC Egypt",
      "IBM Egypt",
      "Vodafone Egypt",
      "Orange Egypt",
      "Valeo Egypt",
      "Instabug",
      "Vezeeta",
      "Fawry",
      "Xceed",
      "ITWorx",
      "Raya Corporation",
      "Dell Technologies Egypt",
      "Cisco Egypt",
      "Intel Egypt",
      "Amazon Egypt",
      "Paymob",
      "MaxAB",
      "Bosta",
      "Trella",
      "Nowpay"
    ],
    "companies_intl": [
      "GitLab (remote-first)",
      "Automattic",
      "Shopify",
      "Stripe",
      "Toptal (freelance/remote)",
      "Turing.com (remote)",
      "Andela (Africa remote talent)",
      "Deloitte Digital (remote programs)",
      "GitHub",
      "Atlassian"
    ]
  },
  {
    "id": "web-development",
    "name": "Web Development",
    "ar": "تطوير الويب",
    "desc": "Building websites and web applications that run in the browser and on servers.",
    "ar_desc": "بناء المواقع والتطبيقات التي تعمل داخل المتصفح وعلى السيرفرات.",
    "junior_overview": {
      "en": "A junior web developer builds and maintains pages and features using HTML, CSS and JavaScript, connects simple frontend pages to backend APIs, fixes layout and styling bugs across browsers/devices, follows a design file (e.g. Figma) to implement UI accurately, and deploys small updates with guidance from a senior teammate.",
      "ar": "مطور الويب المبتدئ يبني ويصون صفحات وميزات باستخدام HTML وCSS وجافاسكريبت، ويربط صفحات الواجهة البسيطة بواجهات برمجية خلفية، ويصلح أخطاء التنسيق عبر المتصفحات والأجهزة المختلفة، ويتبع ملف تصميم (مثل Figma) لتنفيذ الواجهة بدقة، وينشر تحديثات صغيرة بتوجيه من زميل أكبر خبرة."
    },
    "skills": [
      "html",
      "css",
      "javascript",
      "git",
      "rest",
      "http",
      "sql",
      "responsive design",
      "apis",
      "debugging",
      "version control",
      "accessibility"
    ],
    "tools": [
      "vscode",
      "chrome devtools",
      "git",
      "github",
      "node.js",
      "npm",
      "postman",
      "netlify",
      "figma"
    ],
    "roles": [
      "Fresh Graduate / Trainee Web Developer",
      "Junior Web Developer",
      "Web Developer",
      "Senior Web Developer",
      "Tech Lead",
      "Web Architect"
    ],
    "junior": [
      "Build static and dynamic pages from a design file",
      "Connect frontend pages to simple APIs",
      "Fix cross-browser and responsive layout bugs",
      "Deploy small updates under review"
    ],
    "salary": "Egypt market estimate: junior web-developer pay commonly ranges around EGP 7K–15K/month in Cairo depending on stack and company size; treat as indicative only.",
    "roadmap": [
      [
        "Foundation (Months 1-2)",
        "HTML structure, CSS styling, basic JavaScript, using the browser DevTools"
      ],
      [
        "Level 1 (Months 3-4)",
        "Responsive design, Git/GitHub, DOM manipulation, fetching data from APIs"
      ],
      [
        "Level 2 (Months 5-6)",
        "A frontend or backend focus, HTTP/REST basics, forms and validation"
      ],
      [
        "Level 3 (Months 7-8)",
        "Accessibility, performance basics, working with a real backend/database"
      ],
      [
        "Level 4 (Months 9-10)",
        "Deployment (Netlify/Vercel or a VPS), basic SEO, testing pages"
      ],
      [
        "Level 5 (Months 11-12)",
        "2-3 portfolio projects, code reviews, applying to junior roles"
      ]
    ],
    "companies_eg": [
      "Vodafone Egypt",
      "Orange Egypt",
      "Raya Corporation",
      "ITWorx",
      "Xceed",
      "Vezeeta",
      "Elmenus",
      "Breadfast",
      "Fawry",
      "Swvl",
      "Instabug",
      "Yodawy",
      "Nowpay",
      "Trella",
      "CIB Digital",
      "Banque Misr Digital Factory"
    ],
    "companies_intl": [
      "Shopify",
      "Automattic (WordPress.com)",
      "Webflow",
      "GitLab",
      "Toptal (freelance/remote)",
      "Turing.com (remote)",
      "Andela",
      "Wix (remote roles)",
      "freeCodeCamp (open-source contributions)"
    ]
  },
  {
    "id": "frontend",
    "name": "Frontend Engineering",
    "ar": "هندسة الواجهات الأمامية",
    "desc": "Specializing in building fast, accessible, interactive user interfaces for the web.",
    "ar_desc": "التخصص في بناء واجهات مستخدم سريعة وسهلة الوصول وتفاعلية للويب.",
    "junior_overview": {
      "en": "A junior frontend engineer implements UI components from Figma designs using HTML/CSS/JavaScript and a framework such as React, wires components to application state and APIs, fixes visual and interaction bugs, writes basic component tests, and works with accessibility and performance checklists under review.",
      "ar": "مهندس الواجهات الأمامية المبتدئ ينفّذ مكونات الواجهة من تصاميم Figma باستخدام HTML/CSS/جافاسكريبت وإطار عمل مثل React، ويربط المكونات بحالة التطبيق وواجهات البرمجة، ويصلح أخطاء العرض والتفاعل، ويكتب اختبارات أساسية للمكونات، ويعمل وفق قوائم فحص لإمكانية الوصول والأداء تحت المراجعة."
    },
    "skills": [
      "html",
      "css",
      "javascript",
      "typescript",
      "react",
      "responsive design",
      "accessibility",
      "state management",
      "testing",
      "performance",
      "git",
      "rest"
    ],
    "tools": [
      "vscode",
      "react devtools",
      "chrome devtools",
      "npm",
      "webpack/vite",
      "git",
      "github",
      "figma",
      "jest"
    ],
    "roles": [
      "Fresh Graduate / Trainee Frontend Dev",
      "Junior Frontend Engineer",
      "Frontend Engineer",
      "Senior Frontend Engineer",
      "Frontend Tech Lead",
      "Frontend Architect"
    ],
    "junior": [
      "Turn Figma designs into working components",
      "Connect components to state and APIs",
      "Fix UI/interaction bugs and cross-browser issues",
      "Write basic tests for components"
    ],
    "salary": "Egypt market estimate: junior frontend engineer pay commonly ranges around EGP 9K–18K/month in Cairo; higher with React/TypeScript experience. Indicative only.",
    "roadmap": [
      [
        "Foundation (Months 1-2)",
        "HTML/CSS mastery, JavaScript fundamentals, DOM, browser DevTools"
      ],
      [
        "Level 1 (Months 3-4)",
        "Modern JS (ES6+), TypeScript basics, npm and build tools"
      ],
      [
        "Level 2 (Months 5-6)",
        "React fundamentals: components, props, hooks, state"
      ],
      [
        "Level 3 (Months 7-8)",
        "State management, routing, consuming REST APIs, forms"
      ],
      [
        "Level 4 (Months 9-10)",
        "Accessibility, performance, component testing with Jest"
      ],
      [
        "Level 5 (Months 11-12)",
        "Portfolio SPA project, code review practice, mock interviews"
      ]
    ],
    "companies_eg": [
      "Vodafone Egypt",
      "Instabug",
      "Vezeeta",
      "Swvl",
      "Breadfast",
      "Elmenus",
      "Fawry",
      "Xceed",
      "ITWorx",
      "Yodawy",
      "MaxAB",
      "Nowpay",
      "CIB Digital"
    ],
    "companies_intl": [
      "Shopify",
      "Vercel",
      "Netlify",
      "GitLab",
      "Toptal (freelance/remote)",
      "Turing.com (remote)",
      "Andela",
      "Webflow"
    ]
  },
  {
    "id": "backend",
    "name": "Backend Engineering",
    "ar": "هندسة البرمجيات الخلفية",
    "desc": "Building the server-side logic, APIs and data layer that power applications.",
    "ar_desc": "بناء منطق السيرفر وواجهات البرمجة وطبقة البيانات التي تشغّل التطبيقات.",
    "junior_overview": {
      "en": "A junior backend engineer implements API endpoints from a spec, writes queries and simple schema changes against a database, adds tests for new endpoints, handles basic authentication/authorization flows, fixes bugs found in staging, and documents endpoints for the frontend team to consume.",
      "ar": "مهندس الباك اند المبتدئ ينفّذ نقاط نهاية (Endpoints) من مواصفات محددة، ويكتب استعلامات وتعديلات بسيطة في قاعدة البيانات، ويضيف اختبارات للـ endpoints الجديدة، ويتعامل مع تدفقات مصادقة/صلاحيات أساسية، ويصلح الأخطاء المكتشفة في بيئة الاختبار، ويوثّق الـ endpoints ليستخدمها فريق الواجهة الأمامية."
    },
    "skills": [
      "python",
      "node.js",
      "sql",
      "rest",
      "apis",
      "authentication",
      "testing",
      "caching",
      "oop",
      "data structures",
      "security fundamentals",
      "system design",
      "git"
    ],
    "tools": [
      "postman",
      "postgresql",
      "docker",
      "git",
      "github",
      "redis",
      "vscode",
      "pytest"
    ],
    "roles": [
      "Fresh Graduate / Trainee Backend Dev",
      "Junior Backend Engineer",
      "Backend Engineer",
      "Senior Backend Engineer",
      "Backend Tech Lead",
      "Backend/Software Architect"
    ],
    "junior": [
      "Implement API endpoints from a written spec",
      "Write and test database queries",
      "Handle basic auth flows and validation",
      "Fix bugs found in staging/QA"
    ],
    "salary": "Egypt market estimate: junior backend engineer pay commonly ranges around EGP 9K–19K/month in Cairo depending on stack (Python/Node/Java) and company; indicative only.",
    "roadmap": [
      [
        "Foundation (Months 1-2)",
        "A backend language (Python/Node.js/Java), OOP, Git"
      ],
      [
        "Level 1 (Months 3-4)",
        "SQL and relational databases, basic data modeling"
      ],
      [
        "Level 2 (Months 5-6)",
        "Building REST APIs, HTTP, request validation"
      ],
      [
        "Level 3 (Months 7-8)",
        "Authentication/authorization, testing endpoints"
      ],
      [
        "Level 4 (Months 9-10)",
        "Caching, security fundamentals, Docker basics"
      ],
      [
        "Level 5 (Months 11-12)",
        "A backend portfolio project (API + DB), system design basics, applying to jobs"
      ]
    ],
    "companies_eg": [
      "Microsoft ADC Egypt",
      "IBM Egypt",
      "Vodafone Egypt",
      "Orange Egypt",
      "Fawry",
      "Paymob",
      "Vezeeta",
      "Instabug",
      "MaxAB",
      "Bosta",
      "Trella",
      "Nowpay",
      "Valeo Egypt",
      "Etisalat Misr",
      "CIB Digital"
    ],
    "companies_intl": [
      "GitLab",
      "Stripe",
      "Shopify",
      "Automattic",
      "Toptal (freelance/remote)",
      "Turing.com (remote)",
      "Andela",
      "Deloitte Digital (remote)"
    ]
  },
  {
    "id": "mobile-development",
    "name": "Mobile Development",
    "ar": "تطوير تطبيقات الهاتف",
    "desc": "Building native or cross-platform applications for iOS and Android.",
    "ar_desc": "بناء تطبيقات أصلية أو متعددة المنصات لأنظمة iOS وأندرويد.",
    "junior_overview": {
      "en": "A junior mobile developer implements screens from a design file using Flutter/Kotlin/Swift, connects the UI to APIs, handles local storage and simple state, fixes crashes and UI bugs reported by QA, and prepares small updates for testing on real devices/emulators.",
      "ar": "مطور تطبيقات الهاتف المبتدئ ينفّذ الشاشات من ملف تصميم باستخدام Flutter/Kotlin/Swift، ويربط الواجهة بواجهات البرمجة، ويتعامل مع التخزين المحلي والحالة البسيطة، ويصلح الأعطال (Crashes) وأخطاء الواجهة التي يبلّغ عنها فريق الجودة، ويجهّز تحديثات صغيرة للاختبار على أجهزة/محاكيات حقيقية."
    },
    "skills": [
      "dart",
      "kotlin",
      "swift",
      "oop",
      "apis",
      "ui design basics",
      "state management",
      "git",
      "testing",
      "local storage",
      "push notifications",
      "debugging"
    ],
    "tools": [
      "android studio",
      "xcode",
      "flutter",
      "git",
      "github",
      "postman",
      "firebase"
    ],
    "roles": [
      "Fresh Graduate / Trainee Mobile Dev",
      "Junior Mobile Developer",
      "Mobile Developer",
      "Senior Mobile Developer",
      "Mobile Tech Lead",
      "Mobile Architect"
    ],
    "junior": [
      "Implement screens from a design file",
      "Connect UI to APIs and handle local storage",
      "Fix crashes and UI bugs from QA reports",
      "Test builds on devices/emulators"
    ],
    "salary": "Egypt market estimate: junior mobile developer pay commonly ranges around EGP 8K–17K/month in Cairo; Flutter/React Native skills widen opportunities. Indicative only.",
    "roadmap": [
      [
        "Foundation (Months 1-2)",
        "Dart or Kotlin/Swift basics, OOP, mobile UI concepts"
      ],
      [
        "Level 1 (Months 3-4)",
        "Flutter or native UI toolkit fundamentals, layouts, navigation"
      ],
      [
        "Level 2 (Months 5-6)",
        "State management, consuming REST APIs, local storage"
      ],
      [
        "Level 3 (Months 7-8)",
        "Firebase (auth, database, push notifications), testing"
      ],
      [
        "Level 4 (Months 9-10)",
        "Performance, debugging crashes, publishing to test tracks"
      ],
      [
        "Level 5 (Months 11-12)",
        "A complete portfolio app, app-store submission basics, applying to jobs"
      ]
    ],
    "companies_eg": [
      "Vodafone Egypt",
      "Vezeeta",
      "Swvl",
      "Breadfast",
      "Elmenus",
      "Fawry",
      "Instabug",
      "MaxAB",
      "Yodawy",
      "Nowpay",
      "Bosta",
      "CIB Digital"
    ],
    "companies_intl": [
      "Toptal (freelance/remote)",
      "Turing.com (remote)",
      "Andela",
      "Shopify (mobile teams)",
      "GitLab",
      "Automattic"
    ]
  },
  {
    "id": "data-analysis",
    "name": "Data Analysis",
    "ar": "تحليل البيانات",
    "desc": "Turning raw business data into clear insights and reports for decision-making.",
    "ar_desc": "تحويل بيانات الأعمال الخام إلى رؤى وتقارير واضحة لدعم اتخاذ القرار.",
    "junior_overview": {
      "en": "A junior data analyst pulls data using SQL or spreadsheets, cleans and organizes it, builds simple dashboards and reports, checks numbers for accuracy, and presents findings to a manager in plain language with supporting charts.",
      "ar": "محلل البيانات المبتدئ يستخرج البيانات باستخدام SQL أو جداول البيانات، وينظفها وينظمها، ويبني لوحات ومؤشرات وتقارير بسيطة، ويراجع الأرقام للتأكد من دقتها، ويعرض النتائج على مديره بلغة واضحة مدعومة بالرسوم البيانية."
    },
    "skills": [
      "sql",
      "excel",
      "statistics",
      "data cleaning",
      "visualization",
      "python",
      "critical thinking",
      "reporting",
      "data storytelling"
    ],
    "tools": [
      "sql",
      "power bi",
      "tableau",
      "python",
      "jupyter",
      "google sheets"
    ],
    "roles": [
      "Fresh Graduate / Trainee Data Analyst",
      "Junior Data Analyst",
      "Data Analyst",
      "Senior Data Analyst",
      "Analytics Lead",
      "Head of Analytics"
    ],
    "junior": [
      "Pull and clean data using SQL/Excel",
      "Build simple dashboards and reports",
      "Check calculations for accuracy",
      "Present findings clearly to stakeholders"
    ],
    "salary": "Egypt market estimate: junior data analyst pay commonly ranges around EGP 7K–15K/month in Cairo; SQL + a BI tool (Power BI/Tableau) improves offers. Indicative only.",
    "roadmap": [
      [
        "Foundation (Months 1-2)",
        "Excel/Google Sheets, basic statistics, critical thinking"
      ],
      [
        "Level 1 (Months 3-4)",
        "SQL fundamentals: SELECT, JOIN, GROUP BY, aggregation"
      ],
      [
        "Level 2 (Months 5-6)",
        "Data cleaning, Python basics (pandas), visualization principles"
      ],
      [
        "Level 3 (Months 7-8)",
        "Power BI or Tableau dashboards, reporting standards"
      ],
      [
        "Level 4 (Months 9-10)",
        "Data storytelling, stakeholder communication, A/B basics"
      ],
      [
        "Level 5 (Months 11-12)",
        "A portfolio of 2-3 analysis projects, applying to junior roles"
      ]
    ],
    "companies_eg": [
      "Vodafone Egypt",
      "Orange Egypt",
      "Etisalat Misr",
      "Fawry",
      "Vezeeta",
      "Talabat Egypt",
      "Careem Egypt",
      "CIB Digital",
      "Banque Misr Digital Factory",
      "Raya Holding",
      "Commercial International Bank (CIB)"
    ],
    "companies_intl": [
      "Deloitte Digital (remote)",
      "Accenture (remote analytics roles)",
      "Toptal (freelance/remote)",
      "Turing.com (remote)",
      "Andela",
      "Coursera-partner internship programs"
    ]
  },
  {
    "id": "data-science",
    "name": "Data Science",
    "ar": "علم البيانات",
    "desc": "Using statistics, programming and machine learning to extract insight and build predictive models.",
    "ar_desc": "استخدام الإحصاء والبرمجة وتعلم الآلة لاستخلاص الرؤى وبناء نماذج تنبؤية.",
    "junior_overview": {
      "en": "A junior data scientist explores and cleans datasets, engineers basic features, trains and evaluates simple models under a senior's guidance, documents experiments and results, and communicates findings with charts and short written summaries.",
      "ar": "عالم البيانات المبتدئ يستكشف وينظف مجموعات البيانات، ويبني ميزات (Features) بسيطة، ويدرّب ويقيّم نماذج بسيطة بتوجيه من زميل أكبر خبرة، ويوثّق التجارب والنتائج، ويوصّل النتائج عبر رسوم بيانية وملخصات مكتوبة قصيرة."
    },
    "skills": [
      "python",
      "statistics",
      "machine learning",
      "sql",
      "data cleaning",
      "visualization",
      "model evaluation",
      "pandas",
      "numpy",
      "communication",
      "experiment design"
    ],
    "tools": [
      "python",
      "jupyter",
      "pandas",
      "numpy",
      "scikit-learn",
      "sql",
      "power bi"
    ],
    "roles": [
      "Fresh Graduate / Trainee Data Scientist",
      "Junior Data Scientist",
      "Data Scientist",
      "Senior Data Scientist",
      "Lead Data Scientist",
      "Head of Data Science"
    ],
    "junior": [
      "Explore and clean datasets under guidance",
      "Engineer basic features and train simple models",
      "Evaluate models and document experiments",
      "Present findings with charts and summaries"
    ],
    "salary": "Egypt market estimate: junior data scientist pay commonly ranges around EGP 9K–20K/month in Cairo; portfolio projects and a strong GitHub matter a lot. Indicative only.",
    "roadmap": [
      [
        "Foundation (Months 1-3)",
        "Python, statistics fundamentals, SQL, pandas/numpy"
      ],
      [
        "Level 1 (Months 4-5)",
        "Data cleaning and exploratory data analysis (EDA)"
      ],
      [
        "Level 2 (Months 6-7)",
        "Classic machine learning with scikit-learn: regression, classification"
      ],
      [
        "Level 3 (Months 8-9)",
        "Model evaluation, cross-validation, feature engineering"
      ],
      [
        "Level 4 (Months 10-11)",
        "Visualization and storytelling, a capstone Kaggle-style project"
      ],
      [
        "Level 5 (Month 12)",
        "Portfolio + GitHub polish, mock case-study interviews, applying to jobs"
      ]
    ],
    "companies_eg": [
      "Vodafone Egypt",
      "Orange Egypt",
      "Fawry",
      "Vezeeta",
      "Talabat Egypt",
      "Careem Egypt",
      "CIB Digital",
      "Instabug",
      "Microsoft ADC Egypt",
      "IBM Egypt"
    ],
    "companies_intl": [
      "DeepMind (competitive, remote-adjacent)",
      "Deloitte Digital (remote)",
      "Toptal (freelance/remote)",
      "Turing.com (remote)",
      "Kaggle (competitions/portfolio)",
      "Andela"
    ]
  },
  {
    "id": "ai-machine-learning",
    "name": "AI & Machine Learning",
    "ar": "الذكاء الاصطناعي وتعلم الآلة",
    "desc": "Designing and training models that let software learn from data and make predictions or decisions.",
    "ar_desc": "تصميم وتدريب نماذج تتيح للبرمجيات التعلم من البيانات واتخاذ قرارات أو تنبؤات.",
    "junior_overview": {
      "en": "A junior AI/ML engineer implements and trains models from an existing pipeline, prepares and preprocesses datasets, runs experiments and tracks results, tunes basic hyperparameters under supervision, and helps package a trained model for use in an application.",
      "ar": "مهندس الذكاء الاصطناعي المبتدئ ينفّذ ويدرّب نماذج ضمن خط أنابيب (Pipeline) موجود مسبقًا، ويجهّز ويعالج مجموعات البيانات، ويجري تجارب ويسجل نتائجها، ويضبط بعض المعاملات الفائقة (Hyperparameters) الأساسية تحت إشراف، ويساعد في تجهيز نموذج مدرّب للاستخدام داخل تطبيق."
    },
    "skills": [
      "python",
      "machine learning",
      "deep learning",
      "statistics",
      "model evaluation",
      "data structures",
      "algorithms",
      "linear algebra",
      "neural networks",
      "nlp basics",
      "computer vision basics"
    ],
    "tools": [
      "python",
      "tensorflow",
      "pytorch",
      "jupyter",
      "scikit-learn",
      "git",
      "google colab"
    ],
    "roles": [
      "Fresh Graduate / Trainee AI Engineer",
      "Junior ML/AI Engineer",
      "ML/AI Engineer",
      "Senior ML/AI Engineer",
      "Lead ML Engineer",
      "AI Research/Architecture Lead"
    ],
    "junior": [
      "Implement and train models from an existing pipeline",
      "Prepare and preprocess datasets",
      "Run experiments and track results",
      "Help package models for use in an app"
    ],
    "salary": "Egypt market estimate: junior AI/ML engineer pay commonly ranges around EGP 10K–22K/month in Cairo; competitive due to global remote demand. Indicative only.",
    "roadmap": [
      [
        "Foundation (Months 1-3)",
        "Python, linear algebra, statistics, data structures/algorithms"
      ],
      [
        "Level 1 (Months 4-5)",
        "Classic ML with scikit-learn: supervised/unsupervised learning"
      ],
      [
        "Level 2 (Months 6-7)",
        "Neural networks fundamentals, TensorFlow or PyTorch basics"
      ],
      [
        "Level 3 (Months 8-9)",
        "Deep learning: CNNs (vision) or basic NLP concepts"
      ],
      [
        "Level 4 (Months 10-11)",
        "Model evaluation, hyperparameter tuning, experiment tracking"
      ],
      [
        "Level 5 (Month 12)",
        "A deployed end-to-end ML project, portfolio, applying to jobs"
      ]
    ],
    "companies_eg": [
      "Microsoft ADC Egypt",
      "IBM Egypt",
      "Vodafone Egypt",
      "Instabug",
      "Vezeeta",
      "Fawry",
      "Valeo Egypt (AI for automotive)",
      "Intel Egypt"
    ],
    "companies_intl": [
      "DeepMind",
      "OpenAI (competitive, remote-adjacent)",
      "Hugging Face (remote-friendly)",
      "Deloitte Digital (remote)",
      "Toptal (freelance/remote)",
      "Turing.com (remote)",
      "Kaggle competitions"
    ]
  },
  {
    "id": "cybersecurity",
    "name": "Cybersecurity",
    "ar": "الأمن السيبراني",
    "desc": "Protecting systems, networks and data from unauthorized access and attacks.",
    "ar_desc": "حماية الأنظمة والشبكات والبيانات من الوصول غير المصرح به والهجمات.",
    "junior_overview": {
      "en": "A junior cybersecurity analyst monitors security alerts and logs, performs basic vulnerability scans, follows an incident-response checklist when something looks suspicious, documents findings clearly, and helps apply security patches and configuration fixes under supervision.",
      "ar": "محلل الأمن السيبراني المبتدئ يراقب التنبيهات الأمنية والسجلات، ويجري فحوصات ثغرات أساسية، ويتبع قائمة إجراءات محددة عند ظهور نشاط مشبوه، ويوثّق النتائج بوضوح، ويساعد في تطبيق التحديثات الأمنية وإصلاحات الإعدادات تحت إشراف."
    },
    "skills": [
      "networking",
      "linux",
      "security fundamentals",
      "web security",
      "incident response",
      "cryptography basics",
      "risk assessment",
      "scripting"
    ],
    "tools": [
      "wireshark",
      "nmap",
      "kali linux",
      "burp suite",
      "metasploit",
      "linux terminal",
      "siem",
      "python"
    ],
    "roles": [
      "Fresh Graduate / Trainee Security Analyst",
      "Junior Security Analyst / SOC Analyst",
      "Security Analyst",
      "Senior Security Analyst",
      "Security Team Lead",
      "Security Architect / CISO track"
    ],
    "junior": [
      "Monitor alerts and logs for suspicious activity",
      "Run basic vulnerability scans",
      "Follow incident-response checklists",
      "Document findings and help apply fixes"
    ],
    "salary": "Egypt market estimate: junior cybersecurity analyst pay commonly ranges around EGP 9K–18K/month in Cairo; certifications (Security+, eJPT) improve offers. Indicative only.",
    "roadmap": [
      [
        "Foundation (Months 1-2)",
        "Networking fundamentals, Linux basics, security concepts"
      ],
      [
        "Level 1 (Months 3-4)",
        "Web security (OWASP Top 10), scripting for automation"
      ],
      [
        "Level 2 (Months 5-6)",
        "Vulnerability scanning with Nmap, traffic analysis with Wireshark"
      ],
      [
        "Level 3 (Months 7-8)",
        "Web app testing with Burp Suite, basic exploitation with Metasploit"
      ],
      [
        "Level 4 (Months 9-10)",
        "Incident response basics, SIEM fundamentals, cryptography basics"
      ],
      [
        "Level 5 (Months 11-12)",
        "Home-lab/CTF practice, a security certification, applying to SOC roles"
      ]
    ],
    "companies_eg": [
      "Vodafone Egypt",
      "Orange Egypt",
      "Etisalat Misr",
      "IBM Egypt (security services)",
      "CIB Digital",
      "Banque Misr Digital Factory",
      "EG Bank",
      "Paymob",
      "Instabug"
    ],
    "companies_intl": [
      "Cloudflare (remote-friendly)",
      "CrowdStrike (remote-friendly)",
      "Deloitte Cyber (remote)",
      "Toptal (freelance/remote)",
      "Turing.com (remote)",
      "HackerOne (bug bounty, remote)"
    ]
  },
  {
    "id": "cloud-computing",
    "name": "Cloud Computing",
    "ar": "الحوسبة السحابية",
    "desc": "Designing, deploying and managing applications and infrastructure on cloud platforms.",
    "ar_desc": "تصميم ونشر وإدارة التطبيقات والبنية التحتية على منصات الحوسبة السحابية.",
    "junior_overview": {
      "en": "A junior cloud engineer provisions basic cloud resources (VMs, storage, networking) from a runbook, monitors usage and costs, applies IAM permissions correctly under review, helps automate small tasks with scripts, and documents environment configurations.",
      "ar": "مهندس السحابة المبتدئ يجهّز موارد سحابية أساسية (خوادم افتراضية، تخزين، شبكات) وفق دليل عمل محدد، ويراقب الاستخدام والتكاليف، ويطبّق صلاحيات IAM بشكل صحيح تحت المراجعة، ويساعد في أتمتة مهام صغيرة بالسكربتات، ويوثّق إعدادات البيئات."
    },
    "skills": [
      "linux",
      "networking",
      "cloud services",
      "iam",
      "automation",
      "containers",
      "monitoring",
      "cost optimization",
      "security fundamentals"
    ],
    "tools": [
      "aws",
      "azure",
      "gcp",
      "docker",
      "kubernetes",
      "terraform",
      "linux terminal",
      "git"
    ],
    "roles": [
      "Fresh Graduate / Trainee Cloud Engineer",
      "Junior Cloud Engineer",
      "Cloud Engineer",
      "Senior Cloud Engineer",
      "Cloud Team Lead",
      "Cloud Architect"
    ],
    "junior": [
      "Provision basic cloud resources from a runbook",
      "Monitor usage and costs",
      "Apply IAM permissions correctly under review",
      "Document environment configurations"
    ],
    "salary": "Egypt market estimate: junior cloud engineer pay commonly ranges around EGP 9K–19K/month in Cairo; an AWS/Azure certification improves offers. Indicative only.",
    "roadmap": [
      [
        "Foundation (Months 1-2)",
        "Linux fundamentals, networking basics, cloud concepts"
      ],
      [
        "Level 1 (Months 3-4)",
        "Core services of one provider (compute, storage, networking)"
      ],
      [
        "Level 2 (Months 5-6)",
        "IAM, security groups, monitoring and logging basics"
      ],
      [
        "Level 3 (Months 7-8)",
        "Containers with Docker, intro to Kubernetes"
      ],
      [
        "Level 4 (Months 9-10)",
        "Infrastructure as Code with Terraform, cost awareness"
      ],
      [
        "Level 5 (Months 11-12)",
        "A cloud certification (e.g. AWS Cloud Practitioner), portfolio project, applying to jobs"
      ]
    ],
    "companies_eg": [
      "Vodafone Egypt",
      "Orange Egypt",
      "IBM Egypt",
      "Microsoft ADC Egypt",
      "Fawry",
      "Vezeeta",
      "CIB Digital",
      "Instabug",
      "Amazon Egypt"
    ],
    "companies_intl": [
      "AWS (remote-friendly teams)",
      "GitLab",
      "DigitalOcean (remote-friendly)",
      "Toptal (freelance/remote)",
      "Turing.com (remote)",
      "A Cloud Guru community/internships"
    ]
  },
  {
    "id": "devops",
    "name": "DevOps",
    "ar": "دي ف أوبس",
    "desc": "Bridging development and operations to automate builds, testing and deployment pipelines.",
    "ar_desc": "الربط بين التطوير والتشغيل لأتمتة عمليات البناء والاختبار والنشر.",
    "junior_overview": {
      "en": "A junior DevOps engineer maintains and tweaks existing CI/CD pipelines, containerizes small services with Docker, monitors deployments and rolls back when something breaks, writes basic automation scripts, and documents runbooks under a senior's supervision.",
      "ar": "مهندس DevOps المبتدئ يصون ويعدّل خطوط CI/CD الموجودة، ويحوّل خدمات صغيرة إلى حاويات باستخدام Docker، ويراقب عمليات النشر ويتراجع عنها عند حدوث مشكلة، ويكتب سكربتات أتمتة أساسية، ويوثّق أدلة التشغيل تحت إشراف زميل أكبر خبرة."
    },
    "skills": [
      "linux",
      "git",
      "ci/cd",
      "containers",
      "infrastructure as code",
      "scripting",
      "monitoring",
      "cloud services",
      "automation",
      "networking"
    ],
    "tools": [
      "docker",
      "kubernetes",
      "jenkins",
      "github actions",
      "terraform",
      "git",
      "linux terminal",
      "prometheus",
      "ansible"
    ],
    "roles": [
      "Fresh Graduate / Trainee DevOps Engineer",
      "Junior DevOps Engineer",
      "DevOps Engineer",
      "Senior DevOps Engineer",
      "DevOps Team Lead",
      "Platform Architect"
    ],
    "junior": [
      "Maintain and tweak existing CI/CD pipelines",
      "Containerize small services with Docker",
      "Monitor deployments and roll back on failure",
      "Write basic automation scripts and runbooks"
    ],
    "salary": "Egypt market estimate: junior DevOps engineer pay commonly ranges around EGP 10K–20K/month in Cairo; cloud + container skills raise offers. Indicative only.",
    "roadmap": [
      [
        "Foundation (Months 1-2)",
        "Linux, Git/GitHub, scripting (Bash/Python)"
      ],
      [
        "Level 1 (Months 3-4)",
        "Docker fundamentals, containerizing an app"
      ],
      [
        "Level 2 (Months 5-6)",
        "CI/CD with GitHub Actions or Jenkins"
      ],
      [
        "Level 3 (Months 7-8)",
        "Kubernetes basics, cloud services of one provider"
      ],
      [
        "Level 4 (Months 9-10)",
        "Infrastructure as Code with Terraform, monitoring with Prometheus/Grafana"
      ],
      [
        "Level 5 (Months 11-12)",
        "A CI/CD portfolio project end-to-end, applying to junior roles"
      ]
    ],
    "companies_eg": [
      "Vodafone Egypt",
      "IBM Egypt",
      "Microsoft ADC Egypt",
      "Fawry",
      "Vezeeta",
      "Instabug",
      "Paymob",
      "CIB Digital",
      "Valeo Egypt"
    ],
    "companies_intl": [
      "GitLab",
      "HashiCorp (remote-friendly)",
      "DigitalOcean (remote-friendly)",
      "Toptal (freelance/remote)",
      "Turing.com (remote)",
      "Andela"
    ]
  },
  {
    "id": "databases",
    "name": "Database Engineering",
    "ar": "هندسة قواعد البيانات",
    "desc": "Designing, building and maintaining the databases that store an application's data.",
    "ar_desc": "تصميم وبناء وصيانة قواعد البيانات التي تخزّن بيانات التطبيق.",
    "junior_overview": {
      "en": "A junior database engineer writes and tunes SQL queries, implements schema changes designed by a senior, sets up basic indexes, helps configure backups, and investigates slow queries or data issues reported by the application team.",
      "ar": "مهندس قواعد البيانات المبتدئ يكتب استعلامات SQL ويحسّنها، وينفّذ تعديلات على هيكل قاعدة البيانات صممها زميل أكبر خبرة، ويضبط فهارس أساسية، ويساعد في إعداد النسخ الاحتياطية، ويحقق في الاستعلامات البطيئة أو مشاكل البيانات التي يبلّغ عنها فريق التطبيق."
    },
    "skills": [
      "sql",
      "data modeling",
      "normalization",
      "indexing",
      "query optimization",
      "backup and recovery",
      "security fundamentals",
      "nosql basics"
    ],
    "tools": [
      "postgresql",
      "mysql",
      "mongodb",
      "pgadmin",
      "redis",
      "git",
      "linux terminal"
    ],
    "roles": [
      "Fresh Graduate / Trainee DB Engineer",
      "Junior Database Engineer / DBA",
      "Database Engineer / DBA",
      "Senior DBA / Database Engineer",
      "Database Team Lead",
      "Database Architect"
    ],
    "junior": [
      "Write and tune SQL queries",
      "Implement schema changes from a senior's design",
      "Set up basic indexes and backups",
      "Investigate slow queries and data issues"
    ],
    "salary": "Egypt market estimate: junior database engineer/DBA pay commonly ranges around EGP 8K–17K/month in Cairo. Indicative only.",
    "roadmap": [
      [
        "Foundation (Months 1-2)",
        "SQL fundamentals, relational theory, ER diagrams"
      ],
      [
        "Level 1 (Months 3-4)",
        "Data modeling, normalization, constraints"
      ],
      [
        "Level 2 (Months 5-6)",
        "Indexing and query optimization"
      ],
      [
        "Level 3 (Months 7-8)",
        "Backup & recovery, basic security and permissions"
      ],
      [
        "Level 4 (Months 9-10)",
        "Intro to NoSQL (MongoDB/Redis), when to use each"
      ],
      [
        "Level 5 (Months 11-12)",
        "A schema-design portfolio project, applying to junior roles"
      ]
    ],
    "companies_eg": [
      "Vodafone Egypt",
      "Orange Egypt",
      "Etisalat Misr",
      "Fawry",
      "Vezeeta",
      "CIB Digital",
      "Banque Misr Digital Factory",
      "Raya Corporation",
      "IBM Egypt"
    ],
    "companies_intl": [
      "MongoDB (remote-friendly)",
      "Percona (remote-friendly)",
      "GitLab",
      "Toptal (freelance/remote)",
      "Turing.com (remote)",
      "Andela"
    ]
  },
  {
    "id": "software-testing",
    "name": "Software Testing & QA",
    "ar": "اختبار البرمجيات وضمان الجودة",
    "desc": "Verifying that software works correctly and meets quality expectations before release.",
    "ar_desc": "التأكد من أن البرمجيات تعمل بشكل صحيح وتلبي معايير الجودة قبل الإصدار.",
    "junior_overview": {
      "en": "A junior QA engineer executes test cases written by a senior, reports bugs with clear reproduction steps, runs regression tests before releases, writes simple automated tests for stable features, and tracks issues in a tool like Jira until they're resolved.",
      "ar": "مهندس ضمان الجودة المبتدئ ينفّذ حالات اختبار كتبها زميل أكبر خبرة، ويُبلّغ عن الأخطاء بخطوات واضحة لإعادة تنفيذها، ويجري اختبارات الانحدار قبل الإصدارات، ويكتب اختبارات آلية بسيطة للميزات المستقرة، ويتابع المشكلات في أداة مثل Jira حتى حلها."
    },
    "skills": [
      "test design",
      "bug reporting",
      "testing",
      "automation testing",
      "api testing",
      "sql",
      "regression testing",
      "exploratory testing",
      "git"
    ],
    "tools": [
      "selenium",
      "postman",
      "jira",
      "git",
      "testrail",
      "cypress",
      "linux terminal"
    ],
    "roles": [
      "Fresh Graduate / Trainee QA Engineer",
      "Junior QA Engineer",
      "QA Engineer",
      "Senior QA Engineer",
      "QA Team Lead",
      "QA/Test Architect"
    ],
    "junior": [
      "Execute test cases written by a senior",
      "Report bugs with clear reproduction steps",
      "Run regression tests before releases",
      "Write simple automated tests for stable features"
    ],
    "salary": "Egypt market estimate: junior QA engineer pay commonly ranges around EGP 6K–14K/month in Cairo; automation skills (Selenium/Cypress) raise offers. Indicative only.",
    "roadmap": [
      [
        "Foundation (Months 1-2)",
        "Manual testing fundamentals, test-case design, bug reporting"
      ],
      [
        "Level 1 (Months 3-4)",
        "SQL basics, exploratory testing, using Jira/TestRail"
      ],
      [
        "Level 2 (Months 5-6)",
        "API testing with Postman"
      ],
      [
        "Level 3 (Months 7-8)",
        "Test automation basics with Selenium or Cypress"
      ],
      [
        "Level 4 (Months 9-10)",
        "Regression suites, CI integration of tests"
      ],
      [
        "Level 5 (Months 11-12)",
        "An automation portfolio project, applying to junior QA roles"
      ]
    ],
    "companies_eg": [
      "Vodafone Egypt",
      "Orange Egypt",
      "Vezeeta",
      "Instabug",
      "Fawry",
      "Xceed",
      "ITWorx",
      "Raya Corporation",
      "Valeo Egypt",
      "CIB Digital"
    ],
    "companies_intl": [
      "GitLab",
      "Toptal (freelance/remote)",
      "Turing.com (remote)",
      "Andela",
      "Test Automation University community",
      "Ministry of Testing community"
    ]
  },
  {
    "id": "ui-ux",
    "name": "UI/UX & Product Design",
    "ar": "تصميم UI/UX",
    "desc": "Researching user needs and designing interfaces that are clear, usable and visually appealing.",
    "ar_desc": "دراسة احتياجات المستخدم وتصميم واجهات واضحة وسهلة الاستخدام وجذابة بصريًا.",
    "junior_overview": {
      "en": "A junior UI/UX designer creates wireframes and mockups from requirements, builds simple interactive prototypes in Figma, joins user interviews/usability sessions and summarizes findings, keeps a design system's components consistent, and iterates on designs based on feedback from a senior designer.",
      "ar": "مصمم UI/UX المبتدئ ينشئ تصميمات أولية (Wireframes) ونماذج من المتطلبات، ويبني نماذج أولية تفاعلية بسيطة في Figma، ويشارك في مقابلات المستخدمين/جلسات اختبار قابلية الاستخدام ويلخّص النتائج، ويحافظ على اتساق مكونات نظام التصميم، ويطوّر التصاميم بناءً على ملاحظات مصمم أكبر خبرة."
    },
    "skills": [
      "user research",
      "wireframing",
      "prototyping",
      "visual design",
      "usability testing",
      "information architecture",
      "interaction design",
      "accessibility"
    ],
    "tools": [
      "figma",
      "adobe xd",
      "miro",
      "notion",
      "maze"
    ],
    "roles": [
      "Fresh Graduate / Trainee UI/UX Designer",
      "Junior UI/UX Designer",
      "UI/UX Designer",
      "Senior UI/UX Designer",
      "Design Team Lead",
      "Head of Product Design"
    ],
    "junior": [
      "Create wireframes and mockups from requirements",
      "Build simple interactive prototypes in Figma",
      "Join user research sessions and summarize findings",
      "Iterate on designs based on senior feedback"
    ],
    "salary": "Egypt market estimate: junior UI/UX designer pay commonly ranges around EGP 7K–15K/month in Cairo; a strong portfolio matters more than a degree here. Indicative only.",
    "roadmap": [
      [
        "Foundation (Months 1-2)",
        "Design principles, typography, color theory, Figma basics"
      ],
      [
        "Level 1 (Months 3-4)",
        "Wireframing and information architecture"
      ],
      [
        "Level 2 (Months 5-6)",
        "Prototyping and interaction design in Figma"
      ],
      [
        "Level 3 (Months 7-8)",
        "User research methods, usability testing basics"
      ],
      [
        "Level 4 (Months 9-10)",
        "Design systems, accessibility, handoff to developers"
      ],
      [
        "Level 5 (Months 11-12)",
        "A polished case-study portfolio (3 projects), applying to junior roles"
      ]
    ],
    "companies_eg": [
      "Vodafone Egypt",
      "Vezeeta",
      "Swvl",
      "Elmenus",
      "Breadfast",
      "Fawry",
      "Instabug",
      "Xceed",
      "ITWorx",
      "MaxAB"
    ],
    "companies_intl": [
      "Figma (remote-friendly)",
      "InVision (remote-friendly)",
      "Toptal (freelance/remote)",
      "Turing.com (remote)",
      "Dribbble (portfolio/freelance)",
      "Andela"
    ]
  },
  {
    "id": "networking",
    "name": "Computer Networking",
    "ar": "شبكات الحاسوب",
    "desc": "Designing, configuring and maintaining the networks that connect devices and systems.",
    "ar_desc": "تصميم وإعداد وصيانة الشبكات التي تربط الأجهزة والأنظمة ببعضها.",
    "junior_overview": {
      "en": "A junior network engineer configures basic switches/routers from a diagram, monitors network health and reports issues, troubleshoots simple connectivity problems, documents network topology, and assists a senior engineer with change requests.",
      "ar": "مهندس الشبكات المبتدئ يعدّ أجهزة التحويل والتوجيه الأساسية وفق مخطط محدد، ويراقب صحة الشبكة ويُبلّغ عن المشكلات، ويستكشف أعطال الاتصال البسيطة ويصلحها، ويوثّق مخطط الشبكة، ويساعد مهندسًا أكبر خبرة في تنفيذ طلبات التغيير."
    },
    "skills": [
      "networking",
      "security fundamentals",
      "dns",
      "routing",
      "switching",
      "protocols",
      "linux",
      "troubleshooting",
      "network security"
    ],
    "tools": [
      "cisco packet tracer",
      "wireshark",
      "linux terminal",
      "putty",
      "nmap"
    ],
    "roles": [
      "Fresh Graduate / Trainee Network Engineer",
      "Junior Network Engineer",
      "Network Engineer",
      "Senior Network Engineer",
      "Network Team Lead",
      "Network Architect"
    ],
    "junior": [
      "Configure basic switches/routers from a diagram",
      "Monitor network health and report issues",
      "Troubleshoot simple connectivity problems",
      "Document network topology"
    ],
    "salary": "Egypt market estimate: junior network engineer pay commonly ranges around EGP 7K–15K/month in Cairo; a CCNA certification often raises offers. Indicative only.",
    "roadmap": [
      [
        "Foundation (Months 1-2)",
        "Networking fundamentals: OSI model, IP addressing"
      ],
      [
        "Level 1 (Months 3-4)",
        "Routing and switching basics with Packet Tracer"
      ],
      [
        "Level 2 (Months 5-6)",
        "DNS, DHCP, common protocols, Linux basics"
      ],
      [
        "Level 3 (Months 7-8)",
        "Troubleshooting methodology, Wireshark traffic analysis"
      ],
      [
        "Level 4 (Months 9-10)",
        "Network security fundamentals, firewalls, VPNs (concepts)"
      ],
      [
        "Level 5 (Months 11-12)",
        "CCNA exam preparation, home-lab practice, applying to jobs"
      ]
    ],
    "companies_eg": [
      "Vodafone Egypt",
      "Orange Egypt",
      "Etisalat Misr",
      "Cisco Egypt",
      "Nokia Egypt",
      "Ericsson Egypt",
      "Juniper Networks Egypt",
      "CIB Digital"
    ],
    "companies_intl": [
      "Cisco (remote-friendly training/partner programs)",
      "Cloudflare (remote-friendly)",
      "Toptal (freelance/remote)",
      "Turing.com (remote)",
      "Andela"
    ]
  },
  {
    "id": "embedded-systems",
    "name": "Embedded Systems",
    "ar": "الأنظمة المدمجة",
    "desc": "Programming the software that runs directly on hardware devices and microcontrollers.",
    "ar_desc": "برمجة البرمجيات التي تعمل مباشرة على الأجهزة والمتحكمات الدقيقة.",
    "junior_overview": {
      "en": "A junior embedded engineer writes and tests small firmware modules for a microcontroller, wires up and tests simple circuits/sensors, debugs using a debugger or basic instruments, follows datasheets to configure peripherals, and documents code and hardware setup.",
      "ar": "مهندس الأنظمة المدمجة المبتدئ يكتب ويختبر وحدات برمجية صغيرة (Firmware) لمتحكم دقيق، ويوصّل ويختبر دوائر/حساسات بسيطة، ويصحّح الأخطاء باستخدام أداة تصحيح أو أدوات قياس أساسية، ويتبع ورقات البيانات (Datasheets) لإعداد الوحدات الطرفية، ويوثّق الكود وإعداد العتاد."
    },
    "skills": [
      "c/c++",
      "microcontrollers",
      "electronics basics",
      "rtos",
      "debugging",
      "protocols",
      "data structures"
    ],
    "tools": [
      "arduino ide",
      "keil",
      "git",
      "linux terminal"
    ],
    "roles": [
      "Fresh Graduate / Trainee Embedded Engineer",
      "Junior Embedded Systems Engineer",
      "Embedded Systems Engineer",
      "Senior Embedded Engineer",
      "Embedded Team Lead",
      "Embedded Systems Architect"
    ],
    "junior": [
      "Write and test small firmware modules",
      "Wire and test simple circuits/sensors",
      "Debug using a debugger or basic instruments",
      "Follow datasheets to configure peripherals"
    ],
    "salary": "Egypt market estimate: junior embedded engineer pay commonly ranges around EGP 8K–17K/month in Cairo, higher in automotive/semiconductor firms. Indicative only.",
    "roadmap": [
      [
        "Foundation (Months 1-2)",
        "C/C++ fundamentals, electronics basics (voltage, current)"
      ],
      [
        "Level 1 (Months 3-4)",
        "Microcontroller basics with Arduino, GPIO, timers"
      ],
      [
        "Level 2 (Months 5-6)",
        "Communication protocols: UART, I2C, SPI"
      ],
      [
        "Level 3 (Months 7-8)",
        "Intro to RTOS concepts, interrupts, debugging tools"
      ],
      [
        "Level 4 (Months 9-10)",
        "Working with a professional toolchain (STM32/Keil)"
      ],
      [
        "Level 5 (Months 11-12)",
        "A hardware+firmware portfolio project, applying to jobs"
      ]
    ],
    "companies_eg": [
      "Valeo Egypt",
      "Mentor Graphics / Siemens EDA Egypt",
      "Intel Egypt",
      "Vodafone Egypt (IoT teams)",
      "Orange Egypt (IoT)",
      "Schneider Electric Egypt",
      "Bosch Egypt"
    ],
    "companies_intl": [
      "Bosch (remote-adjacent R&D partnerships)",
      "Toptal (freelance/remote)",
      "Turing.com (remote)",
      "Andela",
      "Arduino community/open-source projects"
    ]
  },
  {
    "id": "game-development",
    "name": "Game Development",
    "ar": "تطوير الألعاب",
    "desc": "Designing and programming interactive games for PC, console, mobile or web.",
    "ar_desc": "تصميم وبرمجة ألعاب تفاعلية لأجهزة الكمبيوتر والكونسول والهاتف والويب.",
    "junior_overview": {
      "en": "A junior game developer implements small gameplay features and scripts in an engine like Unity, fixes reported gameplay/physics bugs, builds and tests levels or prototypes, integrates simple 3D assets, and iterates based on playtesting feedback.",
      "ar": "مطور الألعاب المبتدئ ينفّذ ميزات وسكربتات لعب صغيرة داخل محرك مثل يونيتي، ويصلح أخطاء اللعب/الفيزياء المُبلّغ عنها، ويبني ويختبر مراحل أو نماذج أولية، ويدمج أصول ثلاثية الأبعاد بسيطة، ويطوّر اللعبة بناءً على ملاحظات اختبار اللعب."
    },
    "skills": [
      "c#",
      "game engine concepts",
      "3d math",
      "oop",
      "debugging",
      "game design basics",
      "physics basics",
      "version control"
    ],
    "tools": [
      "unity",
      "unreal engine",
      "git",
      "blender",
      "visual studio"
    ],
    "roles": [
      "Fresh Graduate / Trainee Game Developer",
      "Junior Game Developer",
      "Game Developer",
      "Senior Game Developer",
      "Lead Game Developer",
      "Technical Director"
    ],
    "junior": [
      "Implement small gameplay features/scripts",
      "Fix reported gameplay and physics bugs",
      "Build and test levels or prototypes",
      "Integrate simple 3D assets"
    ],
    "salary": "Egypt market estimate: junior game developer pay commonly ranges around EGP 6K–14K/month in Cairo; the local market is smaller than global remote studios. Indicative only.",
    "roadmap": [
      [
        "Foundation (Months 1-2)",
        "C# fundamentals, OOP, basic game design concepts"
      ],
      [
        "Level 1 (Months 3-4)",
        "Unity basics: scenes, GameObjects, components, scripting"
      ],
      [
        "Level 2 (Months 5-6)",
        "Physics, collisions, basic 3D math for movement"
      ],
      [
        "Level 3 (Months 7-8)",
        "UI in games, audio, simple AI/behavior scripting"
      ],
      [
        "Level 4 (Months 9-10)",
        "Optimization, build/deploy to a platform, playtesting"
      ],
      [
        "Level 5 (Months 11-12)",
        "A playable portfolio game, applying to studios/freelance"
      ]
    ],
    "companies_eg": [
      "Instant Games / local indie studios (Cairo/Alexandria)",
      "Chillingo/EA-affiliated remote contractors",
      "Ubisoft (remote/outsourcing partners, when active)",
      "Vodafone Egypt (gamified apps)"
    ],
    "companies_intl": [
      "Unity Technologies (remote-friendly)",
      "Epic Games (remote-friendly)",
      "Toptal (freelance/remote)",
      "Turing.com (remote)",
      "itch.io (indie/freelance distribution)"
    ]
  },
  {
    "id": "blockchain",
    "name": "Blockchain Development",
    "ar": "تطوير البلوك تشين",
    "desc": "Building decentralized applications and smart contracts on blockchain platforms.",
    "ar_desc": "بناء تطبيقات لامركزية وعقود ذكية على منصات البلوك تشين.",
    "junior_overview": {
      "en": "A junior blockchain developer writes and tests small smart contracts from a spec, connects a simple frontend to a contract using Web3 libraries, writes unit tests for contract functions, checks for common vulnerabilities using a checklist, and documents deployed contract addresses/ABIs.",
      "ar": "مطور البلوك تشين المبتدئ يكتب ويختبر عقودًا ذكية صغيرة وفق مواصفات محددة، ويربط واجهة أمامية بسيطة بعقد باستخدام مكتبات Web3، ويكتب اختبارات وحدة لدوال العقد، ويتحقق من الثغرات الشائعة باستخدام قائمة فحص، ويوثّق عناوين العقود المنشورة وملفات ABI."
    },
    "skills": [
      "solidity",
      "smart contract development",
      "javascript",
      "typescript",
      "cryptography basics",
      "web3 basics",
      "testing",
      "git"
    ],
    "tools": [
      "remix ide",
      "hardhat",
      "metamask",
      "git",
      "github",
      "node.js"
    ],
    "roles": [
      "Fresh Graduate / Trainee Blockchain Developer",
      "Junior Blockchain Developer",
      "Blockchain Developer",
      "Senior Blockchain Developer",
      "Blockchain Team Lead",
      "Protocol/Blockchain Architect"
    ],
    "junior": [
      "Write and test small smart contracts from a spec",
      "Connect a simple frontend to a contract via Web3",
      "Write unit tests for contract functions",
      "Check for common vulnerabilities using a checklist"
    ],
    "salary": "Egypt market estimate: junior blockchain developer pay is highly variable, often EGP 10K–25K/month locally, with many roles paid in crypto/remote-first. Indicative only.",
    "roadmap": [
      [
        "Foundation (Months 1-2)",
        "JavaScript/TypeScript, blockchain fundamentals"
      ],
      [
        "Level 1 (Months 3-4)",
        "Solidity basics, writing simple smart contracts"
      ],
      [
        "Level 2 (Months 5-6)",
        "Testing contracts with Hardhat/Truffle"
      ],
      [
        "Level 3 (Months 7-8)",
        "Connecting a frontend via Web3/Ethers.js and MetaMask"
      ],
      [
        "Level 4 (Months 9-10)",
        "Common vulnerabilities (reentrancy, overflow) and secure patterns"
      ],
      [
        "Level 5 (Months 11-12)",
        "A deployed testnet dApp portfolio project, applying to jobs"
      ]
    ],
    "companies_eg": [
      "Local Egyptian Web3 startups (Cairo-based, project-dependent)",
      "Paymob (fintech, blockchain-adjacent R&D)",
      "Freelance/remote-first local developers"
    ],
    "companies_intl": [
      "ConsenSys (remote-first)",
      "Chainlink Labs (remote-first)",
      "Toptal (freelance/remote)",
      "Turing.com (remote)",
      "Gitcoin (open-source bounties, remote)",
      "Andela"
    ]
  }
]
