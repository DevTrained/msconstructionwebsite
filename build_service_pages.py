import os

BASE = "/sessions/eloquent-vibrant-albattani/mnt/outputs/site/services"
os.makedirs(BASE, exist_ok=True)

WA_NUMBER = "923061982828"

HEAD_COMMON = """<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="icon" type="image/png" href="/assets/favicon.png">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="description" content="{og_desc}">
<link rel="canonical" href="{canonical}">
<meta name="geo.region" content="PK-PB">
<meta name="geo.placename" content="Lahore">
<meta name="geo.position" content="31.4243722;74.2439274">
<meta name="ICBM" content="31.4243722, 74.2439274">
<meta property="og:type" content="business.business">
<meta property="og:site_name" content="MS Construction Services">
<meta property="og:locale" content="en_PK">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{og_desc}">
<meta property="og:url" content="{canonical}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{og_title}">
<meta name="twitter:description" content="{og_desc}">
<link rel="stylesheet" href="/assets/styles.css">
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-23JEMZ9Z3N"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', 'G-23JEMZ9Z3N');
</script>
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
}})(window,document,'script','dataLayer','GTM-MRFTVFX9');</script>
<!-- End Google Tag Manager -->"""

HEADER = """<header class="sticky top-0 z-50 bg-navy/90 backdrop-blur-md text-white shadow-lg shadow-black/10">
  <div class="max-w-6xl mx-auto flex items-center justify-between px-5 sm:px-6 py-3.5">
    <a href="/" class="flex items-center gap-2.5 font-heading font-extrabold text-lg">
      <img src="/assets/logo-icon.webp" alt="MS Construction Services logo" width="120" height="120" loading="eager" decoding="async" class="w-9 h-9 object-contain shrink-0 rounded-lg">
      MS <span class="text-goldLight">Construction</span>&nbsp;Services
    </a>
    <nav class="hidden md:flex items-center gap-6 text-sm font-semibold text-slate-200">
      <a href="/" class="hover:text-goldLight transition">Home</a>
      <a href="/services/" class="hover:text-goldLight transition">Services</a>
      <a href="/projects/" class="hover:text-goldLight transition">Projects</a>
      <a href="/#faq" class="hover:text-goldLight transition">FAQs</a>
      <a href="/#lead-form" class="hover:text-goldLight transition">Contact</a>
    </nav>
    <div class="flex gap-2.5 items-center">
      <a class="hidden sm:inline-flex items-center gap-2 border border-white/40 hover:border-white hover:bg-white/10 text-white font-bold text-sm px-5 py-2.5 rounded-lg transition" href="tel:+923061982828">\U0001F4DE 0306-1982828</a>
      <a id="headerWaBtn" class="inline-flex items-center gap-2 bg-whatsapp hover:bg-whatsappDark text-white font-bold text-sm px-5 py-2.5 rounded-lg shadow-lg shadow-whatsapp/30 transition hover:-translate-y-0.5" href="#" target="_blank">\U0001F4AC WhatsApp</a>
    </div>
  </div>
</header>"""

FOOTER = """<footer class="bg-navyDark text-slate-400 py-9 text-[13.5px]">
  <div class="max-w-6xl mx-auto px-5 sm:px-6 flex flex-col sm:flex-row items-center sm:justify-between gap-4 text-center sm:text-left">
    <div>
      <img src="/assets/logo-wordmark.webp" alt="MS Construction Services - From Dream To Reality" width="600" height="248" loading="lazy" decoding="async" class="h-10 sm:h-12 object-contain mb-3 mx-auto sm:mx-0">
      <div><strong class="text-white">MS Construction Services</strong> · Gray Structure, House &amp; Commercial Construction<br>Serving Lahore, Pakistan · Since 1994</div>
    </div>
    <div class="flex flex-col sm:items-end gap-2">
      <div>\U0001F4DE 0306-1982828 &nbsp;|&nbsp; \U0001F4AC WhatsApp available</div>
      <div>\U0001F4E7 <a href="mailto:info@msconstruction.services" class="hover:text-goldLight transition">info@msconstruction.services</a></div>
      <div>\U0001F550 Mon\u2013Sat, 11:00 AM \u2013 7:00 PM</div>
      <div class="flex items-center gap-4 flex-wrap justify-center sm:justify-end">
        <a href="https://www.facebook.com/msconstructionservices.lahore" target="_blank" rel="noopener" class="inline-flex items-center gap-2 text-slate-300 hover:text-goldLight transition">
          <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M22 12.06C22 6.5 17.52 2 12 2S2 6.5 2 12.06c0 5 3.66 9.15 8.44 9.94v-7.03H7.9v-2.91h2.54V9.85c0-2.5 1.49-3.89 3.78-3.89 1.1 0 2.24.2 2.24.2v2.46h-1.26c-1.24 0-1.63.77-1.63 1.56v1.88h2.78l-.44 2.91h-2.34V22c4.78-.79 8.44-4.94 8.44-9.94Z"/></svg>
          Facebook
        </a>
        <a href="https://www.tiktok.com/@ms.construction.s4" target="_blank" rel="noopener" class="inline-flex items-center gap-2 text-slate-300 hover:text-goldLight transition">
          <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M16.5 2c.3 2.4 1.9 4.3 4.5 4.7v3.2c-1.6.1-3.1-.4-4.5-1.4v7.1c0 3.5-2.8 6.4-6.3 6.4S4 19.1 4 15.6c0-3.4 2.7-6.2 6.1-6.4v3.3c-1.5.2-2.8 1.5-2.8 3.1 0 1.7 1.4 3.1 3.1 3.1s3.1-1.4 3.1-3.1V2h3Z"/></svg>
          TikTok
        </a>
        <a href="https://www.instagram.com/msconstructionservice/" target="_blank" rel="noopener" class="inline-flex items-center gap-2 text-slate-300 hover:text-goldLight transition">
          <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2c2.7 0 3.06.01 4.12.06 1.06.05 1.79.22 2.43.47.66.26 1.22.6 1.77 1.15.55.55.9 1.11 1.15 1.77.25.64.42 1.37.47 2.43C21.99 8.94 22 9.3 22 12s-.01 3.06-.06 4.12c-.05 1.06-.22 1.79-.47 2.43a4.9 4.9 0 0 1-1.15 1.77 4.9 4.9 0 0 1-1.77 1.15c-.64.25-1.37.42-2.43.47C15.06 21.99 14.7 22 12 22s-3.06-.01-4.12-.06c-1.06-.05-1.79-.22-2.43-.47a4.9 4.9 0 0 1-1.77-1.15 4.9 4.9 0 0 1-1.15-1.77c-.25-.64-.42-1.37-.47-2.43C2.01 15.06 2 14.7 2 12s.01-3.06.06-4.12c.05-1.06.22-1.79.47-2.43.26-.66.6-1.22 1.15-1.77A4.9 4.9 0 0 1 5.45 2.53c.64-.25 1.37-.42 2.43-.47C8.94 2.01 9.3 2 12 2Zm0 5a5 5 0 1 0 0 10 5 5 0 0 0 0-10Zm0 8.2a3.2 3.2 0 1 1 0-6.4 3.2 3.2 0 0 1 0 6.4Zm5.2-8.4a1.2 1.2 0 1 1-2.4 0 1.2 1.2 0 0 1 2.4 0Z"/></svg>
          Instagram
        </a>
        <a href="https://www.youtube.com/@MsConstructionservicesLahore" target="_blank" rel="noopener" class="inline-flex items-center gap-2 text-slate-300 hover:text-goldLight transition">
          <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M22.5 6.2a2.8 2.8 0 0 0-2-2C18.9 3.8 12 3.8 12 3.8s-6.9 0-8.5.4a2.8 2.8 0 0 0-2 2A29 29 0 0 0 1 12a29 29 0 0 0 .5 5.8 2.8 2.8 0 0 0 2 2c1.6.4 8.5.4 8.5.4s6.9 0 8.5-.4a2.8 2.8 0 0 0 2-2A29 29 0 0 0 23 12a29 29 0 0 0-.5-5.8ZM9.8 15.5v-7l6 3.5-6 3.5Z"/></svg>
          YouTube
        </a>
        <a href="https://maps.app.goo.gl/ud1w2rqY9VFiHBKH7" target="_blank" rel="noopener" class="inline-flex items-center gap-2 text-slate-300 hover:text-goldLight transition">
          <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C7.6 2 4 5.6 4 10c0 5.4 6.8 11.1 7.1 11.4.3.2.5.2.8 0C12.2 21.1 20 15.4 20 10c0-4.4-3.6-8-8-8Zm0 10.8A2.8 2.8 0 1 1 12 7.2a2.8 2.8 0 0 1 0 5.6Z"/></svg>
          Find us on Google Maps
        </a>
      </div>
    </div>
  </div>
  <div class="max-w-6xl mx-auto px-5 sm:px-6 mt-6">
    <div class="rounded-2xl overflow-hidden border border-white/10">
      <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2464.8088555845!2d74.24134710962097!3d31.424372174150676!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3919015ef8a2e45b%3A0x6a5fb9696bd3140a!2sMS%20Construction%20Services%20-%20construction%20company%20in%20Lahore!5e1!3m2!1sen!2s!4v1789067418657!5m2!1sen!2s" width="600" height="300" style="border:0;" class="w-full h-64 sm:h-72" allowfullscreen="" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" title="MS Construction Services location on Google Maps"></iframe>
    </div>
  </div>
</footer>"""

GTM_NOSCRIPT = """<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-MRFTVFX9"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->"""

FLOAT_WA_BTN = """<a id="floatWaBtn" href="#" target="_blank" aria-label="Chat on WhatsApp"
   class="hidden sm:flex fixed bottom-5 right-5 z-50 bg-whatsapp hover:bg-whatsappDark text-white w-[60px] h-[60px] rounded-full items-center justify-center shadow-2xl shadow-black/30 text-2xl animate-floaty">
  \U0001F4AC
</a>"""

SCRIPT_TAIL = """<script>
  const WA_NUMBER = "923061982828";
  function waLink(message){
    return "https://wa.me/" + WA_NUMBER + "?text=" + encodeURIComponent(message);
  }
  const defaultMsg = "Hello, I'd like to discuss my construction project with MS Construction Services.";
  document.getElementById('headerWaBtn').href = waLink(defaultMsg);
  const floatBtn = document.getElementById('floatWaBtn');
  if (floatBtn) floatBtn.href = waLink(defaultMsg);
  const svcBtn = document.getElementById('serviceWaBtn');
  if (svcBtn) svcBtn.href = waLink(SERVICE_MSG || defaultMsg);

  const revealEls = document.querySelectorAll('.reveal');
  const io = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.remove('opacity-0', 'translate-y-6');
        io.unobserve(e.target);
      }
    });
  }, { threshold: 0.1 });
  revealEls.forEach(el => io.observe(el));
</script>"""

def page_shell(title, og_title, og_desc, canonical, service_msg, breadcrumb_json, service_json, body_content):
    head = HEAD_COMMON.format(canonical=canonical, og_title=og_title, og_desc=og_desc)
    return f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
{head}
<title>{title}</title>
<script type="application/ld+json">
{breadcrumb_json}
</script>
<script type="application/ld+json">
{service_json}
</script>
</head>
<body class="font-sans bg-bg text-slate-800 antialiased selection:bg-goldLight selection:text-navyDark">
{GTM_NOSCRIPT}
{HEADER}
{body_content}
{FOOTER}
{FLOAT_WA_BTN}
<script>const SERVICE_MSG = {service_msg!r};</script>
{SCRIPT_TAIL}
</body>
</html>"""

def breadcrumb(items):
    # items: list of (name, url)
    els = []
    for i, (name, url) in enumerate(items, start=1):
        els.append('{"@type":"ListItem","position":%d,"name":"%s","item":"%s"}' % (i, name, url))
    return '{\n  "@context": "https://schema.org",\n  "@type": "BreadcrumbList",\n  "itemListElement": [\n    ' + ',\n    '.join(els) + '\n  ]\n}'

def service_schema(name, desc, url, area_extra=None):
    areas = ['{"@type":"City","name":"Lahore"}', '{"@type":"Place","name":"Bahria Town Lahore"}', '{"@type":"Place","name":"Lake City Lahore"}']
    return ('{\n  "@context": "https://schema.org",\n  "@type": "Service",\n  "serviceType": "%s",\n'
            '  "name": "%s",\n  "description": "%s",\n  "url": "%s",\n'
            '  "provider": {"@id": "https://msconstruction.services/#localbusiness"},\n'
            '  "areaServed": [%s]\n}') % (name, name, desc, url, ", ".join(areas))

SECTION_EYEBROW = 'block text-center text-gold font-bold text-xs tracking-[2px] uppercase mb-2.5'
SECTION_H2 = 'text-center font-heading text-2xl sm:text-3xl font-extrabold text-navy mb-3 tracking-tight'
SECTION_SUB = 'text-center text-slate-500 max-w-xl mx-auto mb-11 text-[15px] sm:text-base'
REVEAL = 'reveal opacity-0 translate-y-6 transition-all duration-700 ease-out'

def breadcrumb_nav(items):
    # items: list of (name, url_or_None)
    parts = []
    for name, url in items:
        if url:
            parts.append(f'<a href="{url}" class="hover:text-goldLight transition">{name}</a>')
        else:
            parts.append(f'<span class="text-goldLight">{name}</span>')
    return f'<nav aria-label="Breadcrumb" class="max-w-6xl mx-auto px-5 sm:px-6 pt-5 text-[13px] text-slate-300 flex gap-2 items-center">' + ' <span class="text-slate-500">/</span> '.join(parts) + '</nav>'

def hero(eyebrow, h1, sub, service_type_for_form=""):
    return f"""<section class="relative overflow-hidden bg-gradient-to-br from-navy to-navyDark text-white pt-10 pb-14">
  <div class="max-w-6xl mx-auto px-5 sm:px-6">
    <span class="{REVEAL} block text-gold font-bold text-xs tracking-[2px] uppercase mb-2.5">{eyebrow}</span>
    <h1 class="{REVEAL} font-heading text-3xl sm:text-4xl font-extrabold leading-tight tracking-tight mb-4 max-w-2xl">{h1}</h1>
    <p class="{REVEAL} text-slate-300 max-w-xl mb-7 text-[15px] sm:text-base">{sub}</p>
    <div class="{REVEAL} flex flex-wrap gap-3">
      <a id="serviceWaBtn" href="#" target="_blank" class="inline-flex items-center gap-2 bg-whatsapp hover:bg-whatsappDark text-white font-bold text-sm px-6 py-3.5 rounded-xl shadow-lg shadow-whatsapp/30 transition hover:-translate-y-0.5">\U0001F4AC Get Free Site Visit on WhatsApp</a>
      <a href="tel:+923061982828" class="inline-flex items-center gap-2 border border-white/30 hover:border-white hover:bg-white/10 text-white font-bold text-sm px-6 py-3.5 rounded-xl transition">\U0001F4DE Call 0306-1982828</a>
    </div>
  </div>
</section>"""

def cta_footer_block(heading, sub):
    return f"""<section class="py-14 bg-gradient-to-br from-navy to-navyDark text-white text-center">
  <div class="max-w-2xl mx-auto px-5 sm:px-6">
    <h2 class="{REVEAL} font-heading text-2xl sm:text-3xl font-extrabold mb-3">{heading}</h2>
    <p class="{REVEAL} text-slate-300 mb-7 text-[15px] sm:text-base">{sub}</p>
    <div class="{REVEAL} flex flex-wrap gap-3 justify-center">
      <a href="#" onclick="this.href=document.getElementById('serviceWaBtn').href" target="_blank" class="inline-flex items-center gap-2 bg-whatsapp hover:bg-whatsappDark text-white font-bold text-sm px-6 py-3.5 rounded-xl shadow-lg shadow-whatsapp/30 transition hover:-translate-y-0.5">\U0001F4AC Get Free Site Visit on WhatsApp</a>
      <a href="/#lead-form" class="inline-flex items-center gap-2 border border-white/30 hover:border-white hover:bg-white/10 text-white font-bold text-sm px-6 py-3.5 rounded-xl transition">Or Fill Out the Quote Form</a>
    </div>
  </div>
</section>"""

def faq_section(items):
    cards = ""
    faq_json_items = []
    for q, a in items:
        cards += f"""<div class="{REVEAL} bg-white rounded-2xl p-6 shadow-md shadow-slate-900/5 border border-amber-100">
        <h3 class="font-heading text-navy text-[15.5px] sm:text-base font-bold mb-2">{q}</h3>
        <p class="text-slate-600 text-sm sm:text-[14.5px]">{a}</p>
      </div>\n      """
        faq_json_items.append('{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}' % (q.replace('"','\\"'), a.replace('"','\\"')))
    faq_json = '{\n  "@context": "https://schema.org",\n  "@type": "FAQPage",\n  "mainEntity": [\n    ' + ',\n    '.join(faq_json_items) + '\n  ]\n}'
    html = f"""<section id="faq" class="py-16 sm:py-20 bg-bg">
  <div class="max-w-4xl mx-auto px-5 sm:px-6">
    <span class="{SECTION_EYEBROW}">FAQs</span>
    <h2 class="{SECTION_H2}">Frequently Asked Questions</h2>
    <div class="{REVEAL} w-16 h-[3px] bg-gold mx-auto mb-10 rounded-full"></div>
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-5">
      {cards}
    </div>
  </div>
</section>"""
    return html, faq_json

def included_grid(eyebrow, heading, sub, items):
    # items: list of (label, value)
    cards = ""
    for label, value in items:
        cards += f"""<div class="{REVEAL} bg-navyDark/40 border border-white/10 rounded-xl p-4 flex items-center gap-2">
        <span class="w-6 h-6 rounded-full bg-gold/20 text-gold flex items-center justify-center text-xs shrink-0">✓</span>
        <div><span class="text-[11px] tracking-wider text-slate-400 uppercase block">{label}</span><span class="font-heading font-bold text-white text-[14.5px]">{value}</span></div>
      </div>\n      """
    return f"""<section class="bg-navyDark text-white py-16 sm:py-20 relative overflow-hidden">
  <div class="absolute -top-20 -right-16 w-80 h-80 rounded-full bg-gold/10 blur-3xl pointer-events-none"></div>
  <div class="max-w-6xl mx-auto px-5 sm:px-6 relative z-10">
    <span class="{SECTION_EYEBROW}">{eyebrow}</span>
    <h2 class="text-center font-heading text-2xl sm:text-4xl font-extrabold text-white mb-4 tracking-tight">{heading}</h2>
    <p class="text-center text-slate-400 max-w-2xl mx-auto mb-10 text-[15px] sm:text-lg">{sub}</p>
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
      {cards}
    </div>
  </div>
</section>"""

def process_steps(heading, steps):
    # steps: list of (title, desc)
    cards = ""
    for i, (title, desc) in enumerate(steps, start=1):
        cards += f"""<div class="{REVEAL} bg-white rounded-2xl p-6 shadow-md shadow-slate-900/5 border border-amber-100 relative">
        <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-goldLight to-gold flex items-center justify-center text-navyDark font-heading font-extrabold mb-3">{i}</div>
        <h3 class="font-heading text-navy text-[16px] mb-1.5">{title}</h3>
        <p class="text-slate-500 text-sm">{desc}</p>
      </div>\n      """
    return f"""<section class="py-16 sm:py-20">
  <div class="max-w-6xl mx-auto px-5 sm:px-6">
    <span class="{SECTION_EYEBROW}">How It Works</span>
    <h2 class="{SECTION_H2}">{heading}</h2>
    <div class="{REVEAL} w-16 h-[3px] bg-gold mx-auto mb-10 rounded-full"></div>
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">
      {cards}
    </div>
  </div>
</section>"""

def trust_section(heading, sub, review_name, review_text, review_context):
    return f"""<section class="py-16 sm:py-20 bg-white">
  <div class="max-w-6xl mx-auto px-5 sm:px-6">
    <span class="{SECTION_EYEBROW}">Why Clients Choose Us</span>
    <h2 class="{SECTION_H2}">{heading}</h2>
    <p class="{REVEAL} text-center text-slate-500 max-w-xl mx-auto mb-11 text-[15px] sm:text-base">{sub}</p>
    <div class="grid grid-cols-1 lg:grid-cols-5 gap-6 items-stretch">
      <div class="{REVEAL} lg:col-span-2 grid grid-cols-2 gap-4">
        <div class="bg-bg rounded-2xl p-5 border border-amber-100 text-center">
          <div class="text-2xl mb-1">&#128181;</div>
          <div class="font-heading text-navy text-sm">Fixed Quote,<br>No Surprises</div>
        </div>
        <div class="bg-bg rounded-2xl p-5 border border-amber-100 text-center">
          <div class="text-2xl mb-1">&#128737;&#65039;</div>
          <div class="font-heading text-navy text-sm">30-Day<br>Price Lock</div>
        </div>
        <div class="bg-bg rounded-2xl p-5 border border-amber-100 text-center">
          <div class="text-2xl mb-1">&#128065;&#65039;</div>
          <div class="font-heading text-navy text-sm">24/7 Site<br>Surveillance</div>
        </div>
        <div class="bg-bg rounded-2xl p-5 border border-amber-100 text-center">
          <div class="text-2xl mb-1">&#127942;</div>
          <div class="font-heading text-navy text-sm">Since 1994,<br>5.0 Rating</div>
        </div>
      </div>
      <div class="{REVEAL} lg:col-span-3 bg-navy rounded-2xl p-7 flex flex-col justify-center">
        <div class="text-gold text-sm mb-3 tracking-[2px]">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <p class="text-white text-[15px] sm:text-base mb-4 leading-relaxed">"{review_text}"</p>
        <div class="flex items-center justify-between">
          <span class="font-heading text-goldLight text-sm">{review_name}</span>
          <span class="text-slate-400 text-xs">{review_context}</span>
        </div>
      </div>
    </div>
  </div>
</section>"""

def review_card(name, text, context=""):
    ctx = f'<span class="text-slate-400 text-xs">{context}</span>' if context else ""
    return f"""<div class="{REVEAL} bg-bg rounded-2xl p-6 shadow-md shadow-slate-900/5 border border-amber-100">
        <div class="text-gold text-sm mb-3 tracking-[2px]">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <p class="text-slate-600 text-sm mb-4 leading-relaxed">"{text}"</p>
        <div class="flex items-center justify-between">
          <span class="font-heading text-navy text-sm">{name}</span>
          {ctx}
        </div>
      </div>"""

def area_page_shell(title, og_title, og_desc, canonical, service_msg, json_ld_blocks, body_content):
    head = HEAD_COMMON.format(canonical=canonical, og_title=og_title, og_desc=og_desc)
    scripts = "\n".join(f'<script type="application/ld+json">\n{block}\n</script>' for block in json_ld_blocks)
    return f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
{head}
<title>{title}</title>
{scripts}
</head>
<body class="font-sans bg-bg text-slate-800 antialiased selection:bg-goldLight selection:text-navyDark">
{GTM_NOSCRIPT}
{HEADER}
{body_content}
{FOOTER}
{FLOAT_WA_BTN}
<script>const SERVICE_MSG = {service_msg!r};</script>
{SCRIPT_TAIL}
</body>
</html>"""

def terms_columns(eyebrow, heading, sub, columns):
    # columns: list of (title, icon, [list of item strings])
    cols_html = ""
    for title, icon, items in columns:
        lis = "".join(f'<li class="flex items-start gap-2.5 text-slate-600 text-sm mb-3"><span class="text-gold shrink-0">&#10003;</span><span>{item}</span></li>' for item in items)
        cols_html += f"""<div class="{REVEAL} bg-bg rounded-2xl p-6 sm:p-7 border border-amber-100">
        <div class="text-2xl mb-3">{icon}</div>
        <h3 class="font-heading text-navy text-[17px] mb-4">{title}</h3>
        <ul>{lis}</ul>
      </div>
      """
    return f"""<section class="py-16 sm:py-20 bg-white">
  <div class="max-w-6xl mx-auto px-5 sm:px-6">
    <span class="{SECTION_EYEBROW}">{eyebrow}</span>
    <h2 class="{SECTION_H2}">{heading}</h2>
    <p class="{REVEAL} text-center text-slate-500 max-w-xl mx-auto mb-11 text-[15px] sm:text-base">{sub}</p>
    <div class="grid grid-cols-1 sm:grid-cols-3 gap-6">
      {cols_html}
    </div>
  </div>
</section>"""

def intro_block(heading, paragraphs):
    ps = "".join(f'<p class="{REVEAL} text-slate-600 text-[15px] sm:text-base leading-relaxed mb-4">{p}</p>\n      ' for p in paragraphs)
    return f"""<section class="py-14 bg-white">
  <div class="max-w-3xl mx-auto px-5 sm:px-6">
    <h2 class="{REVEAL} font-heading text-2xl sm:text-3xl font-extrabold text-navy mb-5 tracking-tight">{heading}</h2>
    {ps}
  </div>
</section>"""

os.makedirs(f"{BASE}/grey-structure", exist_ok=True)
os.makedirs(f"{BASE}/house-construction", exist_ok=True)
os.makedirs(f"{BASE}/commercial-construction", exist_ok=True)

# ---------------- GREY STRUCTURE ----------------
gs_bc_nav = breadcrumb_nav([("Home","/"), ("Services","/services/"), ("Grey Structure", None)])
gs_hero = hero(
    "Grey Structure",
    "Grey Structure Construction in Lahore, Bahria Town &amp; Lake City",
    "Solid, code-compliant grey structure work — the foundation your entire build depends on. Free site visit, a fixed itemized quote within 24 hours, and a 30-day price lock.",
)
gs_intro = intro_block(
    "What Grey Structure Construction Covers",
    [
        "Grey structure is the structural skeleton of your home or commercial building: excavation, foundation, DPC, RCC columns and beams, floor slabs, brickwork, and roof structure. Get this stage right, and everything built on top of it (finishing, electrical, plumbing) goes smoothly. Get it wrong, and problems show up years later as cracks, dampness, or structural issues that are expensive to fix.",
        "MS Construction Services has been building grey structures in Lahore since 1994, with a strong recent track record in Bahria Town (Sector A, Sector C, and Sector E) and Lake City. Several of our Google reviews mention grey structure completed in as little as 100 days.",
    ]
)
gs_included = included_grid(
    "What We Use", "Grey Structure Material Specifications",
    "We use only A+ grade materials for superior quality, durability, and long-lasting results.",
    [
        ("Cement", "Maple Leaf Cement"),
        ("Steel", "Mughal Supreme Steel 60 Grade"),
        ("Bricks", "Semi Special Bricks"),
        ("Sand", "Chenab &amp; Ravi Pure (Not Mixed)"),
        ("Crush", "Sargodha Plant Crush"),
        ("Aggregate", "Bajri (Not Rori)"),
        ("Pipes", "Popular PN20 Pipes"),
        ("Shuttering", "Steel Shuttering"),
        ("Site Surveillance", "24/7 CCTV Camera System"),
    ]
)
gs_process = process_steps(
    "From Site Visit to Roof-Ready Structure",
    [
        ("Free Site Visit", "We assess your plot, soil, and access conditions in person. No obligation, no cost."),
        ("Fixed 24-Hour Quote", "An itemized quote based on your actual plot size and drawings, locked for 30 days."),
        ("Excavation &amp; Foundation", "Foundation depth and DPC set according to your structural drawings and soil conditions."),
        ("Columns, Beams &amp; Slabs", "RCC work using Mughal Supreme Steel 60 Grade and Maple Leaf Cement, built to your approved drawings."),
        ("Brickwork &amp; Roof", "Semi special brick walls and roof structure, with waterproofing and slope for drainage."),
        ("Handover &amp; Next Stage", "Structure handed over ready for finishing, or we continue straight into House Construction if you're going turnkey."),
    ]
)
gs_terms = terms_columns(
    "How We Work Together",
    "Everything You Need to Know Upfront",
    "No surprises, no fine print you find out about later. Here's exactly what to expect.",
    [
        ("What's Included", "&#128230;", [
            "Full grey structure package: excavation, foundation, DPC, RCC columns and beams, floor slabs, brickwork, and roof structure",
            "All structural material sourcing and quality checks, to the specifications listed above",
            "Skilled labor and daily site supervision, with 24/7 CCTV coverage on every site",
            "A written, itemized scope of work provided alongside your fixed quote",
        ]),
        ("Getting Ready to Start", "&#128203;", [
            "We'll ask for your layout plans and structural drawings before excavation, so nothing gets built twice",
            "If your plot needs clearing first, we'll flag it at the site visit so it's no surprise later",
            "We'll confirm water and electricity access with you upfront, since site work depends on both",
            "If your street is narrow, we plan material deliveries around it in advance",
        ]),
        ("Our Commitments to You", "&#129309;", [
            "We build strictly to the drawings and specifications we agree on in writing",
            "If anything doesn't match what we agreed, we fix it at our own cost, no questions asked",
            "Want to change something mid-project? We quote it separately before touching it, so the cost is never a surprise",
            "You pay in stages as construction milestones are hit, never a lump sum upfront",
            "A typical grey structure for a 5-10 Marla plot takes about 6-8 weeks under normal conditions; if weather or approvals slow things down, you'll hear it from us first",
        ]),
    ]
)

gs_trust = trust_section(
    "Real Clients, Real Grey Structures",
    "Don't just take our word for it, here's what a recent client had to say.",
    "Myacademyrtb123",
    "We have amazing experience with Mian Shahbaz and his team, they are too much professional. We have a 10 Marla plot in Bahria Town BB Block and got our grey structure ready in just 100 days.",
    "Bahria Town BB Block, 10 Marla",
)

gs_faq_html, gs_faq_json = faq_section([
    ("What's included in your grey structure package?", "Excavation, foundation, DPC, RCC columns, beams and slabs, brickwork, and roof structure, built using Maple Leaf Cement, Mughal Supreme Steel 60 Grade, semi special bricks, and the other materials listed above. A written scope is provided with your fixed quote."),
    ("How long does grey structure construction take?", "It depends on plot size. For a full house construction timeline including grey structure, see our <a href='/services/house-construction/' class='text-navy underline'>House Construction</a> page. Grey structure alone is typically the first 6-8 weeks of that timeline for a 5-10 Marla plot."),
    ("Do you provide site supervision during grey structure?", "Yes. Every site has 24/7 CCTV camera surveillance, and we personally check structural milestones before moving to the next stage."),
    ("Do you build grey structure in Bahria Town and Lake City?", "Yes. Grey structure is one of our most requested services in Bahria Town (Sector A, C, and E) and Lake City, and we also take on projects across the rest of Lahore."),
])
gs_cta = cta_footer_block("Ready to Start Your Grey Structure?", "Book a free site visit and get a fixed, itemized quote within 24 hours — the price is locked for 30 days, no hidden costs.")

gs_body = gs_bc_nav + "\n" + gs_hero + "\n" + gs_intro + "\n" + gs_included + "\n" + gs_process + "\n" + gs_trust + "\n" + gs_terms + "\n" + gs_faq_html + "\n" + gs_cta

gs_page = page_shell(
    title="Grey Structure Construction in Lahore | MS Construction Services",
    og_title="Grey Structure Construction in Lahore, Bahria Town &amp; Lake City",
    og_desc="Grey structure construction in Lahore using Maple Leaf Cement and Mughal Supreme Steel. Free site visit, fixed 24-hour quote, 30-day price lock.",
    canonical="https://msconstruction.services/services/grey-structure/",
    service_msg="Hello, I'd like a free site visit and quote for Grey Structure construction.",
    breadcrumb_json=breadcrumb([("Home","https://msconstruction.services/"),("Services","https://msconstruction.services/services/"),("Grey Structure","https://msconstruction.services/services/grey-structure/")]),
    service_json=service_schema("Grey Structure Construction", "Grey structure (structural shell) construction in Lahore, Bahria Town, and Lake City using Maple Leaf Cement and Mughal Supreme Steel 60 Grade.", "https://msconstruction.services/services/grey-structure/"),
    body_content=gs_body,
)

with open(f"{BASE}/grey-structure/index.html", "w", encoding="utf-8") as f:
    f.write(gs_page)

print("grey-structure page written", len(gs_page), "bytes")

# ---------------- HOUSE CONSTRUCTION ----------------
hc_bc_nav = breadcrumb_nav([("Home","/"), ("Services","/services/"), ("House Construction", None)])
hc_hero = hero(
    "House Construction",
    "House Construction in Lahore, Bahria Town &amp; Lake City",
    "Full home construction from foundation to finishing, managed start to finish, with a free site visit, a 24-hour fixed quote, and your price locked for 30 days.",
)
hc_intro = intro_block(
    "Turnkey House Construction, Stage by Stage",
    [
        "House construction covers everything from the first shovel of excavation to a finished, move-in-ready home: grey structure, then finishing (plaster, paint, electrical, sanitary, tiles, doors and windows), then furnishing (flooring, kitchen cabinets, wardrobes, lighting). We manage every stage under one fixed quote so you're not coordinating separate contractors for each phase.",
        "We take on only 3 new house construction projects a month so every client gets full attention from site visit to handover, with 24/7 CCTV surveillance on every site.",
    ]
)
hc_timeline = f"""<section class="py-16 sm:py-20 bg-white">
  <div class="max-w-6xl mx-auto px-5 sm:px-6">
    <span class="{SECTION_EYEBROW}">Planning Ahead</span>
    <h2 class="{SECTION_H2}">Construction Timeline by Plot Size</h2>
    <p class="{SECTION_SUB}">Estimated complete construction timelines for residential projects.</p>
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
      <div class="{REVEAL} bg-bg rounded-2xl p-6 text-center border border-amber-100">
        <div class="text-[13px] text-slate-500 mb-1">5 Marla House</div>
        <div class="font-heading text-3xl font-extrabold text-navy mb-1">2&ndash;3</div>
        <div class="text-[13px] text-slate-500">Months</div>
      </div>
      <div class="{REVEAL} bg-bg rounded-2xl p-6 text-center border border-amber-100">
        <div class="text-[13px] text-slate-500 mb-1">10 Marla House</div>
        <div class="font-heading text-3xl font-extrabold text-navy mb-1">3&ndash;4</div>
        <div class="text-[13px] text-slate-500">Months</div>
      </div>
      <div class="{REVEAL} bg-bg rounded-2xl p-6 text-center border border-amber-100">
        <div class="text-[13px] text-slate-500 mb-1">1 Kanal House</div>
        <div class="font-heading text-3xl font-extrabold text-navy mb-1">4&ndash;5</div>
        <div class="text-[13px] text-slate-500">Months</div>
      </div>
      <div class="{REVEAL} bg-bg rounded-2xl p-6 text-center border border-amber-100">
        <div class="text-[13px] text-slate-500 mb-1">2 Kanal House</div>
        <div class="font-heading text-3xl font-extrabold text-navy mb-1">6&ndash;8</div>
        <div class="text-[13px] text-slate-500">Months</div>
      </div>
    </div>
  </div>
</section>"""
hc_included = included_grid(
    "What's Included", "Grey Structure Through Finishing",
    "Every house construction project starts with the same A+ grade grey structure specification, then moves into finishing and furnishing.",
    [
        ("Cement", "Maple Leaf Cement"),
        ("Steel", "Mughal Supreme Steel 60 Grade"),
        ("Bricks", "Semi Special Bricks"),
        ("Plaster &amp; Paint", "Included in finishing stage"),
        ("Electrical &amp; Sanitary", "Included in finishing stage"),
        ("Tiles, Doors &amp; Windows", "Included in finishing stage"),
        ("Kitchen Cabinets &amp; Wardrobes", "Included in furnishing stage"),
        ("Site Surveillance", "24/7 CCTV Camera System"),
        ("Quote", "Fixed, itemized, locked 30 days"),
    ]
)
hc_faq_html, hc_faq_json = faq_section([
    ("How long does it take to build a house in Lahore?", "It depends on plot size: a 5 Marla house typically takes 2-3 months, a 10 Marla house 3-4 months, a 1 Kanal house 4-5 months, and a 2 Kanal house 6-8 months for complete construction."),
    ("How much does house construction cost per marla in Lahore?", "Costs vary based on plot size, material specifications, and site conditions. We provide a free site visit and a fixed, itemized quote within 24 hours, locked for 30 days with no hidden costs."),
    ("Do you build houses in Bahria Town and Lake City?", "Yes. Several of our completed houses are in Bahria Town (Sector A, C, and E) and Lake City, and we build across the rest of Lahore as well."),
    ("Can I hire you just for grey structure, not the full house?", "Yes. See our <a href='/services/grey-structure/' class='text-navy underline'>Grey Structure</a> page: grey structure and full house construction are both available as separate fixed-quote services."),
])
hc_cta = cta_footer_block("Ready to Build Your House?", "A free site visit gets you a fixed, itemized quote within 24 hours, locked for 30 days with no hidden costs.")

hc_trust = trust_section(
    "Real Clients, Real Homes",
    "Don't just take our word for it, here's what a recent client had to say.",
    "Minha Muneeb",
    "We hired them for a 10 Marla house construction in Lake City Lahore and they're honestly the best construction company in Lahore with affordable rates. The quality of work, on-time delivery, and budget-friendly pricing made the whole process stress-free.",
    "Lake City, 10 Marla",
)

hc_body = hc_bc_nav + "\n" + hc_hero + "\n" + hc_intro + "\n" + hc_timeline + "\n" + hc_included + "\n" + hc_trust + "\n" + hc_faq_html + "\n" + hc_cta

hc_page = page_shell(
    title="House Construction in Lahore | MS Construction Services",
    og_title="House Construction in Lahore, Bahria Town &amp; Lake City",
    og_desc="Full house construction in Lahore from foundation to finishing. Free site visit, fixed 24-hour quote, 30-day price lock. Serving Bahria Town &amp; Lake City.",
    canonical="https://msconstruction.services/services/house-construction/",
    service_msg="Hello, I'd like a free site visit and quote for House Construction.",
    breadcrumb_json=breadcrumb([("Home","https://msconstruction.services/"),("Services","https://msconstruction.services/services/"),("House Construction","https://msconstruction.services/services/house-construction/")]),
    service_json=service_schema("House Construction", "Full turnkey house construction in Lahore, Bahria Town, and Lake City from grey structure through finishing and furnishing.", "https://msconstruction.services/services/house-construction/"),
    body_content=hc_body,
)

with open(f"{BASE}/house-construction/index.html", "w", encoding="utf-8") as f:
    f.write(hc_page)

print("house-construction page written", len(hc_page), "bytes")

# ---------------- COMMERCIAL CONSTRUCTION ----------------
cc_bc_nav = breadcrumb_nav([("Home","/"), ("Services","/services/"), ("Commercial Construction", None)])
cc_hero = hero(
    "Commercial Construction",
    "Commercial Construction in Lahore",
    "Offices, plazas, and commercial spaces built to open on schedule, backed by a free site visit and a fixed 24-hour quote, locked in for 30 days.",
)
cc_intro = intro_block(
    "Commercial Construction That Opens On Time",
    [
        "Commercial projects run on a different clock than residential ones. Every week of delay can mean lost rent or a delayed business opening. We scope commercial jobs around your actual deadline, using the same A+ grade materials and structural standards as our residential work, with a fixed quote agreed before the first brick is laid.",
        "Because every commercial project is different in size and complexity, from a single retail unit to a full plaza, we don't publish a fixed price list. What we do offer is a free site visit and a fixed, itemized quote within 24 hours of seeing your plot and requirements, locked for 30 days.",
    ]
)
cc_included = included_grid(
    "What We Use", "Commercial-Grade Material Specifications",
    "Commercial builds use the same A+ grade structural materials as our residential projects, specified to your project's load and use requirements.",
    [
        ("Cement", "Maple Leaf Cement"),
        ("Steel", "Mughal Supreme Steel 60 Grade"),
        ("Bricks", "Semi Special Bricks"),
        ("Sand", "Chenab &amp; Ravi Pure (Not Mixed)"),
        ("Crush", "Sargodha Plant Crush"),
        ("Shuttering", "Steel Shuttering"),
        ("Site Surveillance", "24/7 CCTV Camera System"),
        ("Quote", "Fixed, itemized, locked 30 days"),
        ("Coverage", "Lahore, Bahria Town, Lake City"),
    ]
)
cc_faq_html, cc_faq_json = faq_section([
    ("Do you build offices and commercial plazas, not just houses?", "Yes. Commercial Construction is one of our three core services alongside Gray Structure and House Construction: offices, plazas, and other commercial spaces."),
    ("How is commercial construction priced differently from a house?", "Commercial projects vary much more in scope than residential plots, so pricing is based on a site visit and your specific drawings rather than a fixed per-marla rate. You still get a fixed, itemized quote within 24 hours, locked for 30 days."),
    ("Can you work around a business's opening deadline?", "Yes, deadline-driven scheduling is discussed at the site visit stage so the build plan is set around your target opening date from day one."),
    ("What areas do you cover for commercial projects?", "Lahore, Pakistan, with particular experience in Bahria Town and Lake City, alongside projects across the rest of the city."),
])
cc_cta = cta_footer_block("Have a Commercial Project in Mind?", "We'll visit your site for free and send a fixed, itemized quote within 24 hours. Price locked for 30 days.")

cc_trust = trust_section(
    "Trusted for Over Three Decades",
    "Our commercial work is backed by the same standards clients rely on for their homes.",
    "Shezad Ali",
    "Very good work, I built my 10 Marla house in Bahria Town, really very good work. They've worked in Bahria Town and other societies for almost 17 years.",
    "Bahria Town, 10 Marla",
)

cc_body = cc_bc_nav + "\n" + cc_hero + "\n" + cc_intro + "\n" + cc_included + "\n" + cc_trust + "\n" + cc_faq_html + "\n" + cc_cta

cc_page = page_shell(
    title="Commercial Construction in Lahore | MS Construction Services",
    og_title="Commercial Construction in Lahore",
    og_desc="Commercial construction in Lahore: offices, plazas, and commercial spaces. Free site visit, fixed 24-hour quote, 30-day price lock.",
    canonical="https://msconstruction.services/services/commercial-construction/",
    service_msg="Hello, I'd like a free site visit and quote for a Commercial Construction project.",
    breadcrumb_json=breadcrumb([("Home","https://msconstruction.services/"),("Services","https://msconstruction.services/services/"),("Commercial Construction","https://msconstruction.services/services/commercial-construction/")]),
    service_json=service_schema("Commercial Construction", "Commercial construction in Lahore including offices, plazas, and commercial spaces.", "https://msconstruction.services/services/commercial-construction/"),
    body_content=cc_body,
)

with open(f"{BASE}/commercial-construction/index.html", "w", encoding="utf-8") as f:
    f.write(cc_page)

print("commercial-construction page written", len(cc_page), "bytes")

# ---------------- SERVICES HUB ----------------
hub_bc_nav = breadcrumb_nav([("Home","/"), ("Services", None)])
hub_hero = hero(
    "What We Build",
    "Our Construction Services in Lahore",
    "Gray Structure, House Construction, and Commercial Construction, serving Lahore, Bahria Town, and Lake City since 1994. Free site visit, fixed 24-hour quote, 30-day price lock.",
)

def hub_card(icon, title, desc, url):
    return f"""<a href="{url}" class="{REVEAL} block bg-white rounded-2xl overflow-hidden shadow-md shadow-slate-900/5 hover:-translate-y-1.5 hover:shadow-xl transition duration-200">
        <div class="h-32 bg-gradient-to-br from-navy to-navy2 flex items-center justify-center text-white text-4xl">{icon}</div>
        <div class="p-6"><h3 class="font-heading text-navy text-[18px] mb-2">{title}</h3><p class="text-slate-500 text-sm mb-3">{desc}</p><span class="text-gold font-bold text-sm">Learn More &rarr;</span></div>
      </a>"""

hub_cards = f"""<section class="py-16 sm:py-20">
  <div class="max-w-6xl mx-auto px-5 sm:px-6">
    <div class="grid grid-cols-1 sm:grid-cols-3 gap-6">
      {hub_card("&#129521;", "Grey Structure", "Solid, code-compliant grey structure work — the foundation your entire build depends on.", "/services/grey-structure/")}
      {hub_card("&#127968;", "House Construction", "Full home construction from foundation to finishing, managed start to finish.", "/services/house-construction/")}
      {hub_card("&#127970;", "Commercial Construction", "Offices, plazas, and commercial spaces built to open on schedule.", "/services/commercial-construction/")}
    </div>
  </div>
</section>"""

hub_faq_html, hub_faq_json = faq_section([
    ("Which service is right for me?", "If you already have a structure and need it built, choose Grey Structure. If you need a complete house from foundation to move-in ready, choose House Construction. For offices, plazas, or other commercial spaces, choose Commercial Construction."),
    ("Do all services include a free site visit?", "Yes. Every service starts with a free site visit and a fixed, itemized quote within 24 hours, locked for 30 days with no hidden costs."),
    ("What areas do you serve?", "Lahore, Pakistan, with a strong track record in Bahria Town (Sector A, C, and E) and Lake City."),
])
hub_cta = cta_footer_block("Not Sure Where to Start?", "Tell us about your project on WhatsApp and we'll point you to the right service.")

hub_body = hub_bc_nav + "\n" + hub_hero + "\n" + hub_cards + "\n" + hub_faq_html + "\n" + hub_cta

hub_page = page_shell(
    title="Construction Services in Lahore | MS Construction Services",
    og_title="Our Construction Services in Lahore",
    og_desc="Gray Structure, House Construction, and Commercial Construction in Lahore, Bahria Town &amp; Lake City. Free site visit, fixed 24-hour quote.",
    canonical="https://msconstruction.services/services/",
    service_msg="Hello, I'd like to discuss my construction project with MS Construction Services.",
    breadcrumb_json=breadcrumb([("Home","https://msconstruction.services/"),("Services","https://msconstruction.services/services/")]),
    service_json=service_schema("Construction Services", "Overview of Gray Structure, House Construction, and Commercial Construction services offered in Lahore, Bahria Town, and Lake City.", "https://msconstruction.services/services/"),
    body_content=hub_body,
)

with open(f"{BASE}/index.html", "w", encoding="utf-8") as f:
    f.write(hub_page)

print("services hub page written", len(hub_page), "bytes")

# save FAQ JSON blocks for reference / sitemap step
with open(f"{BASE}/../_faq_jsons.txt", "w", encoding="utf-8") as f:
    f.write("GS FAQ:\n" + gs_faq_json + "\n\nHC FAQ:\n" + hc_faq_json + "\n\nCC FAQ:\n" + cc_faq_json + "\n\nHUB FAQ:\n" + hub_faq_json)

print("ALL PAGES BUILT")
