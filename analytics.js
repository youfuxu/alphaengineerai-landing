(function () {
  "use strict";

  // GA4 measures aggregate page visits only. No message text, form input,
  // passwords, codes, or other user-supplied content is sent to Analytics.
  var measurementId = "G-E50HX5K6LP";
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
  window.gtag("config", measurementId, { anonymize_ip: true });

  // Track only intentional, labeled outbound actions. Never send message text,
  // form input, passwords, codes, payment details, or other user-supplied data.
  document.addEventListener("click", function (event) {
    var link = event.target.closest && event.target.closest("a[data-analytics-event]");
    if (!link || typeof window.gtag !== "function") return;
    var params = {
      page_path: window.location.pathname,
      link_target: link.dataset.analyticsTarget || "external"
    };
    if (link.dataset.analyticsCountry) params.country = link.dataset.analyticsCountry;
    window.gtag("event", link.dataset.analyticsEvent, params);
  });
})();
