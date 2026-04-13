/* app.js — Lightweight VLOOK replacement
 * Features: chapter nav, TOC sidebar, sidebar toggle, auto-numbering, SPA navigation
 */

(function () {
  "use strict";

  // ── Math rendering ───────────────────────────────────────────
  // Called on initial load and after each SPA content swap.

  function renderMath(root) {
    root = root || document;
    var mathElements = root.getElementsByClassName("math");
    var macros = [];
    for (var i = 0; i < mathElements.length; i++) {
      var el = mathElements[i];
      if (el.tagName !== "SPAN") continue;
      var texText = el.firstChild;
      if (!texText) continue;
      try {
        katex.render(texText.data, el, {
          displayMode: el.classList.contains("display"),
          throwOnError: false,
          strict: false,
          macros: macros,
          fleqn: false
        });
      } catch (e) {}
    }
  }

  // ── SPA Navigation ───────────────────────────────────────────
  // Fetch a chapter page and swap content without a full reload.
  // Keeps CSS, KaTeX, and app.js loaded — only content changes.

  var tocHighlightObserver = null;

  function navigate(url) {
    fetch(url)
      .then(function (r) {
        if (!r.ok) throw new Error("fetch failed");
        return r.text();
      })
      .then(function (html) {
        var doc = new DOMParser().parseFromString(html, "text/html");

        // Swap main content
        var newContent = doc.getElementById("content");
        var contentEl  = document.getElementById("content");
        if (newContent && contentEl) contentEl.innerHTML = newContent.innerHTML;

        // Update page title and topbar
        document.title = doc.title;
        var newTopbar = doc.getElementById("topbar-title");
        var topbar    = document.getElementById("topbar-title");
        if (newTopbar && topbar) topbar.textContent = newTopbar.textContent;

        // Extract per-chapter variables from the fetched page's inline script
        var newVideoUrl   = "";
        var newChpAutonum = "";
        doc.querySelectorAll("script:not([src])").forEach(function (s) {
          var m;
          m = s.textContent.match(/window\.videoUrl\s*=\s*"([^"]*)"/);
          if (m) newVideoUrl = m[1];
          m = s.textContent.match(/window\.chpAutonum\s*=\s*"([^"]*)"/);
          if (m) newChpAutonum = m[1];
        });
        window.videoUrl   = newVideoUrl;
        window.chpAutonum = newChpAutonum;

        // Reset video panel
        var panel = document.getElementById("video-panel");
        if (panel) panel.style.display = "none";
        var frame = document.getElementById("video-frame");
        if (frame) { frame.src = ""; }
        // Move panel back inside #content (detach from wherever it ended up)
        if (panel && contentEl) contentEl.appendChild(panel);

        // Update URL and scroll to top
        history.pushState({ url: url }, "", url);
        var mainEl = document.getElementById("main");
        if (mainEl) mainEl.scrollTo(0, 0);

        // Update sidebar: clear current state, set new current chapter
        var currentFile = url.split("?")[0].split("/").pop();
        var oldToc = document.querySelector("ul.chapter-toc");
        if (oldToc) oldToc.remove();

        document.querySelectorAll("#doc-nav-list li.nav-chapter").forEach(function (li) {
          var a = li.querySelector("a");
          li.classList.remove("nav-chapter-current", "open");
          a.classList.remove("current");

          var itemFile = a.getAttribute("href").split("?")[0].split("/").pop();
          if (itemFile !== currentFile) return;

          a.classList.add("current");
          li.classList.add("nav-chapter-current");

          // Inline the new chapter's TOC
          var newTocUl = doc.querySelector("#toc-nav ul");
          if (newTocUl) {
            var tocUl = newTocUl.cloneNode(true);
            tocUl.className = "chapter-toc";
            li.appendChild(tocUl);
          }

          // Toggle chapter TOC on click
          a.onclick = function (e) {
            e.preventDefault();
            li.classList.toggle("open");
          };

          setTimeout(function () { a.scrollIntoView({ block: "nearest" }); }, 0);
        });

        // Disconnect previous scroll observer before creating a new one
        if (tocHighlightObserver) {
          tocHighlightObserver.disconnect();
          tocHighlightObserver = null;
        }

        // Re-run per-page init
        applyAutonum();
        initTocAccordion();
        tocHighlightObserver = initTocHighlight();
        buildFigureCaptions();
        initVideo();
        renderMath(contentEl);
      })
      .catch(function () {
        // Fall back to normal navigation on any error
        window.location.href = url;
      });
  }

  // Handle browser back / forward
  window.addEventListener("popstate", function (e) {
    var url = (e.state && e.state.url) || location.href;
    navigate(url);
  });

  // ── Chapter navigation ───────────────────────────────────────

  function buildDocNav() {
    var list = document.getElementById("doc-nav-list");
    if (!list || !window.docLib || !window.docLib.length) return;

    var currentFile = location.pathname.split("/").pop() || "index.html";

    window.docLib.forEach(function (item) {
      var li = document.createElement("li");
      li.className = "nav-chapter";
      var a = document.createElement("a");

      a.href = item.url;
      a.textContent = item.title;
      a.title = item.title;

      var itemFile = item.url.split("?")[0].split("/").pop();
      var isCurrent = (itemFile === currentFile);

      if (isCurrent) {
        a.className = "current";
        li.classList.add("nav-chapter-current");

        // Move the page TOC into this list item as an inline sub-list
        var tocNav = document.getElementById("toc-nav");
        if (tocNav) {
          var tocUl = tocNav.querySelector("ul");
          if (tocUl) {
            tocUl.className = "chapter-toc";
            li.appendChild(tocUl);
          }
          tocNav.style.display = "none";
          var divider = document.querySelector(".nav-divider");
          if (divider) divider.style.display = "none";
        }

        // Toggle chapter TOC on click
        a.addEventListener("click", function (e) {
          e.preventDefault();
          li.classList.toggle("open");
        });

        setTimeout(function () {
          a.scrollIntoView({ block: "nearest" });
        }, 0);
      } else {
        // SPA navigation for other chapters
        a.addEventListener("click", function (e) {
          e.preventDefault();
          navigate(item.url);
        });
      }

      li.insertBefore(a, li.firstChild);
      list.appendChild(li);
    });
  }

  // ── Auto chapter numbering ───────────────────────────────────

  function applyAutonum() {
    document.body.classList.remove("chp-autonum");
    if (!window.chpAutonum || window.chpAutonum === "") return;
    if (window.chpAutonum.indexOf("off") !== -1 &&
        window.chpAutonum.indexOf("h1") !== -1) {
      document.body.classList.add("chp-autonum");
    }
  }

  // ── Sidebar toggle ───────────────────────────────────────────

  function toggleSidebar() {
    var sidebar = document.getElementById("sidebar");
    var overlay = document.getElementById("overlay");
    sidebar.classList.toggle("open");
    overlay.classList.toggle("visible");
  }

  function closeSidebar() {
    var sidebar = document.getElementById("sidebar");
    var overlay = document.getElementById("overlay");
    sidebar.classList.remove("open");
    overlay.classList.remove("visible");
  }

  window.toggleSidebar = toggleSidebar;
  window.closeSidebar  = closeSidebar;

  // ── TOC active section highlighting ─────────────────────────

  function initTocHighlight() {
    var tocLinks = document.querySelectorAll("#doc-nav-list a[href^='#']");
    if (!tocLinks.length) return null;

    var headings = Array.from(
      document.querySelectorAll("#content h1, #content h2, #content h3, #content h4")
    );
    if (!headings.length) return null;

    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          var id = entry.target.id;
          if (!id) return;
          tocLinks.forEach(function (a) {
            a.classList.toggle("toc-active", a.getAttribute("href") === "#" + id);
          });
        });
      },
      { rootMargin: "0px 0px -60% 0px", threshold: 0 }
    );

    headings.forEach(function (h) { if (h.id) observer.observe(h); });
    return observer;
  }

  // ── Image captions ───────────────────────────────────────────

  function buildFigureCaptions() {
    var imgs = document.querySelectorAll("#content img");
    imgs.forEach(function (img) {
      var alt = img.getAttribute("alt");
      if (!alt || alt.match(/^https?:\/\//)) return;
      if (img.parentElement && img.parentElement.tagName === "FIGURE") return;

      var figure = document.createElement("figure");
      figure.className = "img-figure";
      img.parentNode.insertBefore(figure, img);
      figure.appendChild(img);

      var caption = document.createElement("figcaption");
      caption.textContent = alt;
      figure.appendChild(caption);
    });
  }

  // ── TOC accordion ────────────────────────────────────────────

  function initTocAccordion() {
    var chapterToc = document.querySelector("ul.chapter-toc");
    if (!chapterToc) return;

    chapterToc.querySelectorAll("li").forEach(function (li) {
      var childUl = null;
      for (var i = 0; i < li.children.length; i++) {
        if (li.children[i].tagName === "UL") { childUl = li.children[i]; break; }
      }
      if (!childUl) return;

      li.classList.add("has-children");

      var link = null;
      for (var i = 0; i < li.children.length; i++) {
        if (li.children[i].tagName === "A") { link = li.children[i]; break; }
      }
      if (!link) return;

      link.addEventListener("click", function (e) {
        e.preventDefault();
        li.classList.toggle("open");
      });
    });
  }

  // ── Video panel ──────────────────────────────────────────────

  function initVideo() {
    var url = (window.videoUrl || "").trim();
    if (!url) return;

    var panel    = document.getElementById("video-panel");
    var frame    = document.getElementById("video-frame");
    var closeBtn = document.getElementById("video-close-btn");
    var mainEl   = document.getElementById("main");
    if (!panel || !frame) return;

    frame.src = url;
    panel.style.display = "none";

    var activeOwner = null;

    function openAfter(owner) {
      owner.insertAdjacentElement("afterend", panel);
      panel.style.display = "block";
      frame.style.height = Math.round(panel.offsetWidth * 9 / 16) + "px";
      activeOwner = owner;
      var top = panel.getBoundingClientRect().top + mainEl.scrollTop - 56;
      mainEl.scrollTo({ top: top, behavior: "smooth" });
    }

    function closePanel() {
      panel.style.display = "none";
      activeOwner = null;
    }

    if (closeBtn) closeBtn.onclick = closePanel;
    var closeBottom = document.getElementById("video-close-bottom");
    if (closeBottom) closeBottom.onclick = closePanel;

    document.querySelectorAll(".callout.callout-tip").forEach(function (tip) {
      var trigger = document.createElement("button");
      trigger.className = "video-inline-btn";
      trigger.innerHTML = "&#9654; 观看视频";
      trigger.onclick = function () {
        if (activeOwner === trigger) { closePanel(); }
        else { openAfter(trigger); }
      };
      tip.insertAdjacentElement("afterend", trigger);
    });
  }

  // ── Init ─────────────────────────────────────────────────────

  function init() {
    buildDocNav();
    applyAutonum();
    initTocAccordion();
    tocHighlightObserver = initTocHighlight();
    buildFigureCaptions();
    initVideo();
    // Math already rendered by inline <script> in template on first load
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }

  // ── Exercise show/hide ───────────────────────────────────────
  // Handles .ex-solution-toggle and .ex-reveal-btn buttons.
  // Uses event delegation on document so it works after SPA navigation.

  function handleExerciseClick(e) {
    var btn = e.target.closest(".ex-solution-toggle, .ex-reveal-btn");
    if (!btn) return;
    var targetId = btn.getAttribute("data-target");
    if (!targetId) return;
    var panel = document.getElementById(targetId);
    if (!panel) return;
    var hidden = panel.hasAttribute("hidden");
    if (hidden) {
      panel.removeAttribute("hidden");
      // Rotate arrow on solution toggles
      if (btn.classList.contains("ex-solution-toggle")) {
        btn.textContent = btn.textContent.replace("▼", "▲");
      }
      // Re-render any math inside newly revealed content
      if (typeof renderMath === "function") renderMath(panel);
    } else {
      panel.setAttribute("hidden", "");
      if (btn.classList.contains("ex-solution-toggle")) {
        btn.textContent = btn.textContent.replace("▲", "▼");
      }
    }
  }

  document.addEventListener("click", handleExerciseClick);
})();
