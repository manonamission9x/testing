/* ============================================
   Trimurti Plant Sciences — Main JS
   Search, modals, enquire, animations
   ============================================ */
(function () {
  'use strict';

  // --- helpers ---
  var qs = function(s, ctx) { return (ctx || document).querySelector(s); };
  var qsa = function(s, ctx) { return (ctx || document).querySelectorAll(s); };
  var on = function(el, ev, fn) { if (el) el.addEventListener(ev, fn); };

  // ========== GLOBAL SEARCH OVERLAY ==========
  // Works on ANY page — searches product data if available
  window.searchOverlay = (function() {
    var overlay = qs('.search-overlay');
    if (!overlay) return null;

    var input = qs('#global-search-input');
    var resultsContainer = qs('#search-results');
    var resultsList = resultsContainer ? qs('.search-results-list', resultsContainer) : null;

    // Load product data if available
    var productLookup = [];
    if (typeof PRODUCT_DATA !== 'undefined') {
      productLookup = PRODUCT_DATA;
    } else {
      // Try to load from products-data.js dynamically
      try {
        var script = document.createElement('script');
        script.src = 'products-data.js';
        script.onload = function() {
          if (typeof PRODUCT_DATA !== 'undefined') {
            productLookup = PRODUCT_DATA;
          }
        };
        document.head.appendChild(script);
      } catch(e) {}
    }

    function open() {
      if (!overlay) return;
      overlay.classList.add('open');
      if (input) setTimeout(function() { input.focus(); }, 100);
      document.body.style.overflow = 'hidden';
    }

    function close() {
      if (!overlay) return;
      overlay.classList.remove('open');
      document.body.style.overflow = '';
      if (resultsContainer) resultsContainer.style.display = 'none';
    }

    function search(val) {
      var q = (val || '').toLowerCase().trim();
      if (!q || productLookup.length === 0) {
        if (resultsContainer) resultsContainer.style.display = 'none';
        return;
      }

      var results = [];
      productLookup.forEach(function(group) {
        if (!group.hybrids) return;
        group.hybrids.forEach(function(h) {
          var name = (h.name || '').toLowerCase();
          var code = (group.code || '').toLowerCase();
          var desc = (h.desc || '').toLowerCase();
          if (name.indexOf(q) !== -1 || desc.indexOf(q) !== -1 || code.indexOf(q) !== -1) {
            results.push({ name: h.name, group: group.name, category: group.category, desc: h.desc, img: h.img, code: group.code });
          }
        });
      });

      if (results.length === 0) {
        if (resultsList) resultsList.innerHTML = '<div class="empty-state"><p>No products found for "' + val + '"</p></div>';
        if (resultsContainer) resultsContainer.style.display = 'block';
        return;
      }

      var html = '<div style="display:flex;flex-direction:column;gap:6px;">';
      results.slice(0, 12).forEach(function(r) {
        var imgHtml = r.img ? '<img src="' + r.img + '" alt="" style="width:36px;height:36px;object-fit:contain;border-radius:4px;background:var(--cream-75);flex-shrink:0;">' : '<div style="width:36px;height:36px;border-radius:4px;background:var(--cream-75);flex-shrink:0;"></div>';
        html += '<a href="crops.html" class="search-result-item" data-product="' + esc(r.name) + '" style="display:flex;align-items:center;gap:10px;padding:8px 12px;border-radius:6px;transition:background 0.2s;text-decoration:none;color:inherit;" onmouseover="this.style.background=\'var(--cream-75)\'" onmouseout="this.style.background=\'transparent\'">'
          + imgHtml
          + '<div><div style="font-size:0.875rem;font-weight:600;color:var(--text);">' + esc(r.name) + '</div><div style="font-size:0.6875rem;color:var(--text-muted);">' + esc(r.group) + ' · ' + esc(r.code) + '</div></div>'
          + '<span style="margin-left:auto;font-size:0.6875rem;color:var(--green-600);font-weight:600;">View <i class="ph ph-arrow-right"></i></span>'
          + '</a>';
      });
      if (results.length > 12) {
        html += '<div style="text-align:center;font-size:0.75rem;color:var(--text-muted);padding:8px;">+' + (results.length - 12) + ' more results</div>';
      }
      html += '</div>';
      if (resultsList) resultsList.innerHTML = html;
      if (resultsContainer) resultsContainer.style.display = 'block';
    }

    if (input) {
      on(input, 'input', function() { search(this.value); });
      on(input, 'keydown', function(e) {
        if (e.key === 'Escape') close();
      });
    }

    // Wire toggle buttons
    var toggle = qs('.search-toggle');
    var closeBtn = qs('.search-close');
    if (toggle) on(toggle, 'click', function(e) { e.preventDefault(); open(); });
    if (closeBtn) on(closeBtn, 'click', close);

    // Keyboard shortcuts
    on(document, 'keydown', function(e) {
      if (e.key === 'Escape' && overlay.classList.contains('open')) close();
      if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        if (!overlay.classList.contains('open')) open(); else close();
      }
    });

    // Click outside to close
    on(overlay, 'click', function(e) {
      if (e.target === overlay) close();
    });

    return { open: open, close: close };
  })();

  // ========== SCROLL-REVEAL ==========
  function initReveal() {
    var els = qsa('.reveal');
    if (!els.length) return;
    var observer = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('revealed');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });
    els.forEach(function(el) { observer.observe(el); });
  }

  // ========== COUNTER ANIMATION ==========
  function initCounters() {
    var counters = qsa('[data-counter]');
    if (!counters.length) return;

    counters.forEach(function(el) {
      // Pre-render the final number so we never show zeros
      var target = parseFloat(el.getAttribute('data-counter'));
      var decimals = parseInt(el.getAttribute('data-decimals')) || 0;
      el.textContent = target.toFixed(decimals);
    });

    var observer = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          var el = entry.target;
          var target = parseFloat(el.getAttribute('data-counter'));
          var decimals = parseInt(el.getAttribute('data-decimals')) || 0;
          var duration = 1800;
          var startTime = performance.now();
          var startVal = target * 0.7; // Start at 70% so there's still animation but no zero-shock

          function update(currentTime) {
            var elapsed = currentTime - startTime;
            var progress = Math.min(elapsed / duration, 1);
            var eased = 1 - (1 - progress) * (1 - progress);
            var currentVal = startVal + (target - startVal) * eased;
            el.textContent = currentVal.toFixed(decimals);
            if (progress < 1) {
              requestAnimationFrame(update);
            } else {
              el.textContent = target.toFixed(decimals);
            }
          }
          requestAnimationFrame(update);
          observer.unobserve(el);
        }
      });
    }, { threshold: 0.5 });

    counters.forEach(function(el) { observer.observe(el); });
  }

  // ========== HEADER SCROLL ==========
  function initHeaderScroll() {
    var header = qs('.site-header');
    if (!header) return;
    var ticking = false;
    on(window, 'scroll', function() {
      if (!ticking) {
        requestAnimationFrame(function() {
          header.classList.toggle('scrolled', window.scrollY > 60);
          ticking = false;
        });
        ticking = true;
      }
    });
    if (window.scrollY > 60) header.classList.add('scrolled');
  }

  // ========== MOBILE NAV ==========
  function initMobileNav() {
    var toggle = qs('.mobile-menu-toggle');
    var close = qs('.mobile-nav-close');
    var nav = qs('.mobile-nav');
    if (!toggle || !nav) return;

    function open() { nav.classList.add('open'); document.body.style.overflow = 'hidden'; }
    function closeNav() { nav.classList.remove('open'); document.body.style.overflow = ''; }

    on(toggle, 'click', open);
    on(close, 'click', closeNav);

    qsa('.mobile-nav-link', nav).forEach(function(link) {
      on(link, 'click', function(e) {
        if (link.getAttribute('data-sub')) return;
        closeNav();
      });
    });

    qsa('[data-sub]', nav).forEach(function(link) {
      on(link, 'click', function(e) {
        e.preventDefault();
        var subId = link.getAttribute('data-sub');
        var sub = document.getElementById(subId);
        if (!sub) return;
        sub.classList.toggle('open');
        var caret = qs('.mobile-caret', link);
        if (caret) caret.style.transform = sub.classList.contains('open') ? 'rotate(180deg)' : 'rotate(0deg)';
      });
    });

    on(document, 'keydown', function(e) {
      if (e.key === 'Escape' && nav.classList.contains('open')) closeNav();
    });
  }

  // ========== DROPDOWN TOUCH + KEYBOARD ==========
  function initTouchDropdown() {
    var items = qsa('.nav-item');
    items.forEach(function(item) {
      var link = qs('.nav-link', item);
      var dropdown = qs('.nav-dropdown', item);
      if (!dropdown) return;

      // Keyboard: open on focus within
      on(item, 'focusin', function() {
        dropdown.style.opacity = '1';
        dropdown.style.visibility = 'visible';
        dropdown.style.pointerEvents = 'auto';
      });
      on(item, 'focusout', function(e) {
        // Only close if focus left the entire item
        if (!item.contains(e.relatedTarget)) {
          dropdown.style.opacity = '';
          dropdown.style.visibility = '';
          dropdown.style.pointerEvents = '';
        }
      });

      // Touch: tap to toggle
      if ('ontouchstart' in window) {
        on(link, 'click', function(e) {
          if (dropdown.style.opacity === '1') return;
          e.preventDefault();
          items.forEach(function(other) {
            if (other !== item) {
              var otherDd = qs('.nav-dropdown', other);
              if (otherDd) {
                otherDd.style.opacity = '0';
                otherDd.style.visibility = 'hidden';
              }
            }
          });
          dropdown.style.opacity = '1';
          dropdown.style.visibility = 'visible';
          dropdown.style.pointerEvents = 'auto';
        });
      }
    });

    // Close all on click outside
    on(document, 'click', function(e) {
      if (!e.target.closest('.nav-item')) {
        items.forEach(function(item) {
          var dd = qs('.nav-dropdown', item);
          if (dd) {
            dd.style.opacity = '';
            dd.style.visibility = '';
            dd.style.pointerEvents = '';
          }
        });
      }
    });
  }

  // ========== ENQUIRE LINKS — pass product to contact page ==========
  function initEnquireLinks() {
    qsa('[data-enquire]').forEach(function(link) {
      on(link, 'click', function(e) {
        e.preventDefault();
        var product = link.getAttribute('data-enquire');
        window.location.href = 'contact.html?product=' + encodeURIComponent(product);
      });
    });
  }

  // ========== PRODUCT DETAIL MODAL ==========
  function initProductModal() {
    var overlay = qs('.modal-overlay');
    if (!overlay) return;

    // Use event delegation on document so dynamically-rendered cards work
    on(document, 'click', function(e) {
      var card = e.target.closest('[data-product-name]');
      if (!card) return;
      // Don't open modal if clicking a link or button inside
      if (e.target.closest('a') || e.target.closest('button')) return;
      openModalFromCard(card);
    });

    function openModalFromCard(card) {
      var name = card.getAttribute('data-product-name');
      var type = card.getAttribute('data-product-type') || '';
      var code = card.getAttribute('data-product-code') || '';
      var desc = card.getAttribute('data-product-desc') || '';
      var img = card.getAttribute('data-product-img') || '';
      var duration = card.getAttribute('data-product-duration') || '';
      var region = card.getAttribute('data-product-region') || '';
      var seasons = card.getAttribute('data-product-season') || '';
      openModal({ name: name, type: type, code: code, desc: desc, img: img, duration: duration, region: region, seasons: seasons });
    }

    function openModal(data) {
      if (!data) return;
      var content = qs('.modal-content', overlay);
      var h = qs('.modal-header h2', content);
      var body = qs('.modal-body', content);
      var footer = qs('.modal-footer', content);
      if (h) h.textContent = data.name || '';
      if (body) {
        var imgHtml = data.img ? '<img class="modal-img" src="' + data.img + '" alt="' + esc(data.name) + '" onerror="this.style.display=\'none\'">' : '';
        var seasonHtml = '';
        if (data.seasons) {
          var seasons = data.seasons.split('/').map(function(s) { return '<span class="prod-tag prod-tag-season">' + s.trim() + '</span>'; });
          seasonHtml = '<div class="modal-spec"><span class="modal-spec-label">Season</span><span class="modal-spec-value">' + seasons.join('') + '</span></div>';
        }
        body.innerHTML = imgHtml
          + '<div class="modal-specs">'
          + '<div class="modal-spec"><span class="modal-spec-label">Type</span><span class="modal-spec-value">' + esc(data.type || '—') + '</span></div>'
          + '<div class="modal-spec"><span class="modal-spec-label">Code</span><span class="modal-spec-value">' + esc(data.code || '—') + '</span></div>'
          + (data.duration ? '<div class="modal-spec"><span class="modal-spec-label">Duration</span><span class="modal-spec-value">' + esc(data.duration) + '</span></div>' : '')
          + (data.region ? '<div class="modal-spec"><span class="modal-spec-label">Region</span><span class="modal-spec-value">' + esc(data.region) + '</span></div>' : '')
          + seasonHtml
          + '</div>'
          + '<div class="modal-desc">' + esc(data.desc || '') + '</div>';
      }
      if (footer) {
        footer.innerHTML = '<a href="contact.html?product=' + encodeURIComponent(data.name || '') + '" class="btn btn-primary">Enquire About This Product <i class="ph ph-arrow-right"></i></a>'
          + '<button class="btn btn-ghost modal-close-btn" onclick="document.querySelector(\'.modal-overlay\').classList.remove(\'open\')">Close</button>';
      }
      overlay.classList.add('open');
      document.body.style.overflow = 'hidden';
    }

    // Close on overlay click
    on(overlay, 'click', function(e) {
      if (e.target === overlay) {
        overlay.classList.remove('open');
        document.body.style.overflow = '';
      }
    });

    // Close on Escape
    on(document, 'keydown', function(e) {
      if (e.key === 'Escape' && overlay.classList.contains('open')) {
        overlay.classList.remove('open');
        document.body.style.overflow = '';
      }
    });

    return overlay;
  }

  // ========== UTILITY ==========
  function esc(s) {
    if (!s) return '';
    var div = document.createElement('div');
    div.textContent = s;
    return div.innerHTML;
  }

  // ========== INIT ==========
  document.addEventListener('DOMContentLoaded', function() {
    initHeaderScroll();
    initMobileNav();
    initReveal();
    initCounters();
    initTouchDropdown();
    initEnquireLinks();
    initProductModal();
  });

})();
