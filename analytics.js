(function () {
  "use strict";

  // GA4 measures aggregate page visits only. No message text, form input,
  // passwords, codes, or other user-supplied content is sent to Analytics.
  var measurementId = "G-E50HX5K6LP";
  var pageLanguage = document.documentElement.lang || "und";
  var script = document.createElement("script");
  script.async = true;
  script.src = "https://www.googletagmanager.com/gtag/js?id=" + measurementId;
  document.head.appendChild(script);

  window.dataLayer = window.dataLayer || [];
  function gtag() {
    window.dataLayer.push(arguments);
  }
  window.gtag = window.gtag || gtag;
  window.gtag("js", new Date());
  window.gtag("config", measurementId, {
    anonymize_ip: true,
    allow_google_signals: false
  });

  // Keep legacy share links usable as X evolves its public Intent endpoint.
  document.querySelectorAll('a[href^="https://twitter.com/intent/tweet"]').forEach(function (link) {
    link.href = link.href.replace(
      "https://twitter.com/intent/tweet",
      "https://x.com/intent/post"
    );
  });

  // Track only intentional, labeled outbound actions. Never send message text,
  // form input, passwords, codes, payment details, or other user-supplied data.
  document.addEventListener("click", function (event) {
    var link = event.target.closest && event.target.closest("a[data-analytics-event]");
    if (!link || typeof window.gtag !== "function") return;
    var params = {
      page_path: window.location.pathname,
      page_language: pageLanguage,
      link_target: link.dataset.analyticsTarget || "external"
    };
    if (link.dataset.analyticsCountry) params.country = link.dataset.analyticsCountry;
    try {
      var destination = new URL(link.href, window.location.href);
      params.link_host = destination.hostname;
      params.link_path = destination.pathname;
    } catch (error) {
      // Keep the event useful even if a malformed link is present.
    }
    window.gtag("event", link.dataset.analyticsEvent, params);
  });
})();
