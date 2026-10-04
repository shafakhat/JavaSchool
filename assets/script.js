/* JavaSchool - client-side behaviour: theme, sidebar, search, copy, highlight, quiz. */
(function () {
  "use strict";

  /* ------------------------------------------------------------ theme -- */
  var root = document.documentElement;
  var themeBtn = document.getElementById("themeToggle");
  function applyThemeLabel() {
    if (themeBtn) {
      themeBtn.innerHTML = root.getAttribute("data-theme") === "dark" ? "&#9728;" : "&#9680;";
    }
  }
  applyThemeLabel();
  if (themeBtn) {
    themeBtn.addEventListener("click", function () {
      var dark = root.getAttribute("data-theme") === "dark";
      if (dark) root.removeAttribute("data-theme");
      else root.setAttribute("data-theme", "dark");
      try { localStorage.setItem("jschool-theme", dark ? "light" : "dark"); } catch (e) {}
      applyThemeLabel();
    });
  }

  /* ---------------------------------------------------------- sidebar -- */
  var navToggle = document.getElementById("navToggle");
  if (navToggle) {
    navToggle.addEventListener("click", function (e) {
      e.stopPropagation();
      document.body.classList.toggle("sidebar-open");
    });
  }
  document.addEventListener("click", function (e) {
    if (document.body.classList.contains("sidebar-open")) {
      var sidebar = document.getElementById("sidebar");
      if (sidebar && !sidebar.contains(e.target) && e.target !== navToggle) {
        document.body.classList.remove("sidebar-open");
      }
    }
  });
  document.querySelectorAll(".sidebar .side-link").forEach(function (a) {
    a.addEventListener("click", function () {
      document.body.classList.remove("sidebar-open");
    });
  });

  // collapsible sections (persisted)
  var collapsed = {};
  try { collapsed = JSON.parse(localStorage.getItem("jschool-collapsed") || "{}") || {}; } catch (e) {}
  function persistCollapsed() {
    try { localStorage.setItem("jschool-collapsed", JSON.stringify(collapsed)); } catch (e) {}
  }
  document.querySelectorAll(".side-head").forEach(function (btn) {
    var id = btn.getAttribute("data-target");
    if (collapsed[id]) {
      btn.closest(".side-section").classList.add("collapsed");
      btn.setAttribute("aria-expanded", "false");
    }
    btn.addEventListener("click", function () {
      var sec = btn.closest(".side-section");
      sec.classList.toggle("collapsed");
      var isCollapsed = sec.classList.contains("collapsed");
      btn.setAttribute("aria-expanded", isCollapsed ? "false" : "true");
      collapsed[id] = isCollapsed;
      persistCollapsed();
    });
  });

  /* ------------------------------------------------------- copy buttons -- */
  function attachCopy(btn) {
    btn.addEventListener("click", function () {
      var pre = btn.closest(".code-box").querySelector("pre");
      var text = pre ? pre.innerText : "";
      function done() {
        var old = btn.textContent;
        btn.textContent = "Copied!";
        btn.classList.add("copied");
        setTimeout(function () {
          btn.textContent = old;
          btn.classList.remove("copied");
        }, 1400);
      }
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(done, function () { fallbackCopy(text, done); });
      } else {
        fallbackCopy(text, done);
      }
    });
  }
  function fallbackCopy(text, cb) {
    var ta = document.createElement("textarea");
    ta.value = text;
    ta.style.position = "fixed";
    ta.style.opacity = "0";
    document.body.appendChild(ta);
    ta.select();
    try { document.execCommand("copy"); cb(); } catch (e) {}
    document.body.removeChild(ta);
  }
  document.querySelectorAll(".copy-btn").forEach(attachCopy);

  /* --------------------------------------------------------- highlight -- */
  var JAVA_KEYWORDS = new Set(
    ("abstract assert boolean break byte case catch char class const continue default do double else enum " +
     "extends final finally float for goto if implements import instanceof int interface long native new " +
     "package private protected public return short static strictfp super switch synchronized this throw " +
     "throws transient try void volatile while var record yield sealed permits true false null")
      .split(" ")
  );
  var JAVA_TYPES = new Set(
    ("String System Integer Double Float Long Boolean Character Object Math StringBuilder StringBuffer " +
     "List ArrayList LinkedList HashMap HashSet TreeMap Arrays Collections Scanner Thread Runnable Exception " +
     "IOException RuntimeException Override Deprecated SafeVarargs Comparable Comparator Optional Stream " +
     "LocalDate LocalDateTime Instant Pattern Matcher File Paths Path BigDecimal ThreadLocal")
      .split(" ")
  );
  var SQL_KEYWORDS = new Set(
    ("select from where insert into values update set delete create table drop alter add primary key foreign " +
     "references not null unique index join left right inner outer on as and or in like between order by " +
     "group having count avg sum min max limit offset distinct returning using with serial integer varchar " +
     "text timestamp boolean default begin commit rollback transaction execute prepared statement")
      .split(" ")
  );

  var JAVA_RE =
    /(\/\*[\s\S]*?\*\/|\/\/[^\n]*)|("(?:\\.|[^"\\\n])*"|'(?:\\.|[^'\\\n])*')|(@[A-Za-z_][\w.]*)|(0[xX][0-9a-fA-F_]+|\d[\d_]*(?:\.\d+)?[fFdDlL]?)|([A-Za-z_]\w*)/g;
  var SQL_RE =
    /(--[^\n]*|\/\*[\s\S]*?\*\/)|('(?:''|[^'])*'|"[^"]*")|(@[A-Za-z_]\w*)|(\d+)|([A-Za-z_]\w*)/g;

  function esc(s) {
    return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  }

  function highlight(text, lang) {
    var re = lang === "sql" ? SQL_RE : JAVA_RE;
    var kw = lang === "sql" ? SQL_KEYWORDS : JAVA_KEYWORDS;
    var out = "";
    var last = 0;
    var m;
    re.lastIndex = 0;
    while ((m = re.exec(text)) !== null) {
      out += esc(text.slice(last, m.index));
      var full = m[0];
      if (m[1]) out += '<span class="tok-com">' + esc(full) + "</span>";
      else if (m[2]) out += '<span class="tok-str">' + esc(full) + "</span>";
      else if (m[3]) out += '<span class="tok-anno">' + esc(full) + "</span>";
      else if (m[4]) out += '<span class="tok-num">' + esc(full) + "</span>";
      else if (m[5]) {
        if (kw.has(full)) out += '<span class="tok-kw">' + esc(full) + "</span>";
        else if (lang !== "sql" && JAVA_TYPES.has(full) && /^[A-Z]/.test(full))
          out += '<span class="tok-type">' + esc(full) + "</span>";
        else out += esc(full);
      } else out += esc(full);
      last = m.index + full.length;
      if (m[0] === "") re.lastIndex++;
    }
    out += esc(text.slice(last));
    return out;
  }

  document.querySelectorAll("code[data-lang]").forEach(function (el) {
    var lang = el.getAttribute("data-lang");
    if (lang !== "java" && lang !== "sql") return;
    try {
      el.innerHTML = highlight(el.textContent, lang);
    } catch (e) {}
  });

  /* ------------------------------------------------------------ search -- */
  var input = document.getElementById("searchInput");
  var results = document.getElementById("searchResults");
  var index = window.JSCHOOL_INDEX || [];
  var selIdx = -1;

  function scoreItem(item, tokens) {
    var hay = (item.t + " " + item.s + " " + (item.d || "")).toLowerCase();
    var title = item.t.toLowerCase();
    var s = 0;
    for (var i = 0; i < tokens.length; i++) {
      var tok = tokens[i];
      if (title.indexOf(tok) === 0) s += 6;
      else if (title.indexOf(tok) >= 0) s += 4;
      else if (title.indexOf(tok.replace("-", "")) >= 0) s += 3;
      else if (hay.indexOf(tok) >= 0) s += 1;
      else return -1; // every token must match somewhere
    }
    return s;
  }

  function renderResults(q) {
    if (!results) return;
    var tokens = q.toLowerCase().split(/\s+/).filter(Boolean);
    if (!tokens.length) { results.hidden = true; results.innerHTML = ""; return; }
    var scored = [];
    for (var i = 0; i < index.length; i++) {
      var sc = scoreItem(index[i], tokens);
      if (sc > 0) scored.push([sc, index[i]]);
    }
    scored.sort(function (a, b) { return b[0] - a[0]; });
    scored = scored.slice(0, 8);
    if (!scored.length) {
      results.innerHTML = '<div class="search-empty">No results for "' + esc(q) + '"</div>';
      results.hidden = false;
      return;
    }
    var html = "";
    for (var j = 0; j < scored.length; j++) {
      var it = scored[j][1];
      var t = esc(it.t);
      var firstTok = tokens[0];
      var pos = it.t.toLowerCase().indexOf(firstTok);
      if (pos >= 0) {
        t =
          esc(it.t.slice(0, pos)) +
          "<b>" + esc(it.t.slice(pos, pos + firstTok.length)) + "</b>" +
          esc(it.t.slice(pos + firstTok.length));
      }
      html +=
        '<a class="search-item" href="' + esc(it.u) + '">' +
        '<div class="s-sec">' + esc(it.s) + "</div>" +
        '<div class="s-title">' + t + "</div>" +
        (it.d ? '<div class="s-desc">' + esc(it.d) + "</div>" : "") +
        "</a>";
    }
    results.innerHTML = html;
    results.hidden = false;
    selIdx = -1;
  }

  if (input) {
    input.addEventListener("input", function () { renderResults(input.value); });
    input.addEventListener("keydown", function (e) {
      var items = results ? results.querySelectorAll(".search-item") : [];
      if (e.key === "Escape") { results.hidden = true; input.blur(); return; }
      if (!items.length) return;
      if (e.key === "ArrowDown" || e.key === "ArrowUp") {
        e.preventDefault();
        selIdx += e.key === "ArrowDown" ? 1 : -1;
        if (selIdx < 0) selIdx = items.length - 1;
        if (selIdx >= items.length) selIdx = 0;
        items.forEach(function (el, i) { el.classList.toggle("sel", i === selIdx); });
        items[selIdx].scrollIntoView({ block: "nearest" });
      } else if (e.key === "Enter") {
        e.preventDefault();
        var target = selIdx >= 0 ? items[selIdx] : items[0];
        if (target) window.location.href = target.getAttribute("href");
      }
    });
    document.addEventListener("click", function (e) {
      if (results && !results.contains(e.target) && e.target !== input) results.hidden = true;
    });
  }

  /* ----------------------------------------------------------- top btn -- */
  var topBtn = document.getElementById("topBtn");
  if (topBtn) {
    window.addEventListener("scroll", function () {
      topBtn.classList.toggle("show", window.scrollY > 320);
    }, { passive: true });
    topBtn.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  /* -------------------------------------------------------------- quiz -- */
  var quizRoot = document.getElementById("quiz-root");
  if (quizRoot) {
    var dataEl = document.getElementById("quiz-data");
    var questions = [];
    try { questions = JSON.parse(dataEl.textContent); } catch (e) {}
    var submitted = false;

    function renderQuiz() {
      var html = "";
      questions.forEach(function (q, qi) {
        html += '<div class="quiz-q" data-qi="' + qi + '">';
        html += '<div class="q-title"><span class="q-num">Q' + (qi + 1) + ".</span>" + esc(q.q) + "</div>";
        q.o.forEach(function (opt, oi) {
          html += '<label class="quiz-opt"><input type="radio" name="q' + qi + '" value="' + oi + '"><span>' + esc(opt) + "</span></label>";
        });
        html += '<div class="quiz-expl"><strong>Answer: ' + esc(q.o[q.a]) +
          ".</strong> " + esc(q.e || "") + "</div>";
        html += "</div>";
      });
      html +=
        '<div class="quiz-actions">' +
        '<button type="button" class="btn btn-green" id="quizSubmit">Submit Answers</button>' +
        '<button type="button" class="btn btn-outline" id="quizRetry" style="display:none">Try Again</button>' +
        '<span class="quiz-score" id="quizScore"></span></div>';
      quizRoot.innerHTML = html;

      document.getElementById("quizSubmit").addEventListener("click", submitQuiz);
      document.getElementById("quizRetry").addEventListener("click", function () {
        submitted = false;
        renderQuiz();
      });
    }

    function submitQuiz() {
      if (submitted) return;
      submitted = true;
      var score = 0;
      questions.forEach(function (q, qi) {
        var box = quizRoot.querySelector('.quiz-q[data-qi="' + qi + '"]');
        var checked = quizRoot.querySelector('input[name="q' + qi + '"]:checked');
        var chosen = checked ? parseInt(checked.value, 10) : -1;
        if (chosen === q.a) score++;
        box.classList.add("answered");
        box.querySelectorAll(".quiz-opt").forEach(function (lab, oi) {
          var inp = lab.querySelector("input");
          if (oi === q.a) lab.classList.add("correct");
          if (inp.checked && oi !== q.a) lab.classList.add("wrong");
          inp.disabled = true;
        });
      });
      var pct = Math.round((score / questions.length) * 100);
      document.getElementById("quizScore").textContent =
        "Score: " + score + " / " + questions.length + " (" + pct + "%)";
      document.getElementById("quizSubmit").style.display = "none";
      document.getElementById("quizRetry").style.display = "";
      quizRoot.scrollIntoView({ behavior: "smooth", block: "end" });
    }

    renderQuiz();
  }
})();
