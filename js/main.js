/* ============================================
   TriMurti Plant Sciences — Main JS
   ============================================ */

(function () {
  'use strict';

  // --- helpers ---
  const qs = (s, ctx) => (ctx || document).querySelector(s);
  const qsa = (s, ctx) => (ctx || document).querySelectorAll(s);
  const on = (el, ev, fn) => el.addEventListener(ev, fn);

  // ========== SCROLL-REVEAL (Intersection Observer) ==========
  function initReveal() {
    const els = qsa('.reveal');
    if (!els.length) return;

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('revealed');
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.1, rootMargin: '0px 0px -40px 0px' }
    );

    els.forEach((el) => observer.observe(el));
  }

  // ========== COUNTER ANIMATION ==========
  function initCounters() {
    const counters = qsa('[data-counter]');
    if (!counters.length) return;

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            const el = entry.target;
            const target = parseFloat(el.getAttribute('data-counter'));
            const decimals = parseInt(el.getAttribute('data-decimals')) || 0;
            const duration = 1800;
            const startTime = performance.now();
            const startVal = 0;

            function update(currentTime) {
              const elapsed = currentTime - startTime;
              const progress = Math.min(elapsed / duration, 1);
              // ease-out quad
              const eased = 1 - (1 - progress) * (1 - progress);
              const currentVal = startVal + (target - startVal) * eased;
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
      },
      { threshold: 0.5 }
    );

    counters.forEach((el) => observer.observe(el));
  }

  // ========== HEADER SCROLL EFFECT ==========
  function initHeaderScroll() {
    const header = qs('.site-header');
    if (!header) return;

    let ticking = false;
    on(window, 'scroll', () => {
      if (!ticking) {
        requestAnimationFrame(() => {
          header.classList.toggle('scrolled', window.scrollY > 60);
          ticking = false;
        });
        ticking = true;
      }
    });
    // initial check
    if (window.scrollY > 60) header.classList.add('scrolled');
  }

  // ========== MOBILE NAV ==========
  function initMobileNav() {
    const toggle = qs('.mobile-menu-toggle');
    const close = qs('.mobile-nav-close');
    const nav = qs('.mobile-nav');
    if (!toggle || !nav) return;

    const open = () => {
      nav.classList.add('open');
      document.body.style.overflow = 'hidden';
    };
    const closeNav = () => {
      nav.classList.remove('open');
      document.body.style.overflow = '';
    };

    on(toggle, 'click', open);
    on(close, 'click', closeNav);

    // close on link click
    qsa('.mobile-nav-link', nav).forEach((link) => {
      on(link, 'click', (e) => {
        // don't close if it's a submenu toggler
        if (link.getAttribute('data-sub')) return;
        closeNav();
      });
    });

    // mobile sub-menu toggle
    qsa('[data-sub]', nav).forEach((link) => {
      on(link, 'click', (e) => {
        e.preventDefault();
        const subId = link.getAttribute('data-sub');
        const sub = document.getElementById(subId);
        if (!sub) return;
        sub.classList.toggle('open');
        const caret = link.querySelector('.mobile-caret');
        if (caret) {
          caret.style.transform = sub.classList.contains('open')
            ? 'rotate(180deg)'
            : 'rotate(0deg)';
        }
      });
    });

    // close on escape key
    on(document, 'keydown', (e) => {
      if (e.key === 'Escape' && nav.classList.contains('open')) {
        closeNav();
      }
    });
  }

  // ========== SEARCH OVERLAY ==========
  function initSearch() {
    const overlay = qs('.search-overlay');
    const toggle = qs('.search-toggle');
    const close = qs('.search-close');
    const input = overlay ? qs('input', overlay) : null;
    if (!overlay) return;

    const open = () => {
      overlay.classList.add('open');
      if (input) setTimeout(() => input.focus(), 100);
      document.body.style.overflow = 'hidden';
    };
    const closeSearch = () => {
      overlay.classList.remove('open');
      document.body.style.overflow = '';
    };

    if (toggle) on(toggle, 'click', open);
    if (close) on(close, 'click', closeSearch);

    on(document, 'keydown', (e) => {
      if (e.key === 'Escape' && overlay.classList.contains('open')) {
        closeSearch();
      }
      // Ctrl+K or Cmd+K to open search
      if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        if (!overlay.classList.contains('open')) open();
      }
    });

    // Click outside search box to close
    on(overlay, 'click', (e) => {
      if (e.target === overlay) closeSearch();
    });
  }

  // ========== DROPDOWN TOUCH SUPPORT ==========
  function initTouchDropdown() {
    if (!('ontouchstart' in window)) return;
    const items = qsa('.nav-item');
    items.forEach((item) => {
      const link = qs('.nav-link', item);
      const dropdown = qs('.nav-dropdown', item);
      if (!dropdown) return;

      on(link, 'click', (e) => {
        // if dropdown is already visible, let the link navigate
        // otherwise show dropdown
        if (dropdown.style.opacity === '1') return;
        e.preventDefault();
        // close all other dropdowns
        items.forEach((other) => {
          if (other !== item) {
            const otherDd = qs('.nav-dropdown', other);
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
    });

    // close on tap outside
    on(document, 'click', (e) => {
      if (!e.target.closest('.nav-item')) {
        items.forEach((item) => {
          const dd = qs('.nav-dropdown', item);
          if (dd) {
            dd.style.opacity = '';
            dd.style.visibility = '';
            dd.style.pointerEvents = '';
          }
        });
      }
    });
  }

  // ========== SMOOTH SCROLL FOR ANCHOR LINKS ==========
  function initSmoothScroll() {
    qsa('a[href^="#"]').forEach((link) => {
      on(link, 'click', (e) => {
        const targetId = link.getAttribute('href').slice(1);
        if (!targetId) return;
        const target = document.getElementById(targetId);
        if (!target) return;
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      });
    });
  }

  // ========== CROP SEARCH FILTER ==========
  function initCropSearch() {
    const searchInput = document.querySelector('[oninput*="filterProducts"]');
    if (!searchInput) return;
    
    const allCards = document.querySelectorAll('.product-card');
    const allSections = document.querySelectorAll('.crop-section-inner');
    
    window.filterProducts = function(val) {
      const q = val.toLowerCase().trim();
      
      // Filter individual cards
      allCards.forEach(card => {
        const text = card.textContent.toLowerCase();
        card.style.display = (!q || text.includes(q)) ? '' : 'none';
      });
      
      // Show/hide entire sections
      allSections.forEach(section => {
        const visibleCards = section.querySelectorAll('.product-card[style*="display: none"]');
        const totalCards = section.querySelectorAll('.product-card');
        const header = section.querySelector('.crop-section-header');
        if (header) {
          header.style.display = (visibleCards.length === totalCards.length && q) ? 'none' : '';
        }
      });
    };
  }

  // ========== INIT ==========
  document.addEventListener('DOMContentLoaded', () => {
    initHeaderScroll();
    initMobileNav();
    initSearch();
    initReveal();
    initCounters();
    initTouchDropdown();
    initSmoothScroll();
    initCropSearch();
  });

})();
