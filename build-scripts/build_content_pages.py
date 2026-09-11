import os, importlib.util

spec = importlib.util.spec_from_file_location("bsp", "/sessions/eloquent-vibrant-albattani/mnt/outputs/build_service_pages.py")
bsp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bsp)  # re-runs build_service_pages.py, rebuilding those files too (harmless/idempotent)

REVEAL = bsp.REVEAL
SECTION_EYEBROW = bsp.SECTION_EYEBROW
SECTION_H2 = bsp.SECTION_H2
LB_ID = "https://msconstruction.services/#localbusiness"

SITE_BASE = "/sessions/eloquent-vibrant-albattani/mnt/outputs/site"
PROJECTS_BASE = f"{SITE_BASE}/projects"
GUIDES_BASE = f"{SITE_BASE}/guides"
os.makedirs(PROJECTS_BASE, exist_ok=True)
os.makedirs(GUIDES_BASE, exist_ok=True)


def breadcrumb_nav(items):
    # items: list of (name, url_or_None). Last item has no link.
    parts = []
    for name, url in items:
        if url:
            parts.append(f'<a href="{url}" class="hover:text-gold transition">{name}</a>')
        else:
            parts.append(f'<span class="text-slate-500">{name}</span>')
    return f"""<nav class="max-w-4xl mx-auto px-5 sm:px-6 pt-4 text-xs text-slate-400" aria-label="Breadcrumb">
  {' / '.join(parts)}
</nav>"""


def simple_hero(eyebrow, h1, sub, wide=False):
    width = "max-w-4xl" if not wide else "max-w-6xl"
    return f"""<section class="relative overflow-hidden bg-gradient-to-br from-navy to-navyDark text-white pt-10 pb-14">
  <div class="{width} mx-auto px-5 sm:px-6">
    <span class="{REVEAL} block text-gold font-bold text-xs tracking-[2px] uppercase mb-2.5">{eyebrow}</span>
    <h1 class="{REVEAL} font-heading text-3xl sm:text-4xl font-extrabold leading-tight tracking-tight mb-4 max-w-2xl">{h1}</h1>
    <p class="{REVEAL} text-slate-300 max-w-2xl mb-2 text-[15px] sm:text-base">{sub}</p>
  </div>
</section>"""


def project_facts_bar(facts):
    # facts: list of (label, value)
    items = "".join(f"""<div class="bg-bg rounded-2xl p-5 border border-amber-100 text-center">
          <div class="text-slate-400 text-[11px] uppercase tracking-wider mb-1">{label}</div>
          <div class="font-heading text-navy text-[15px] sm:text-base">{value}</div>
        </div>""" for label, value in facts)
    return f"""<section class="pt-10">
  <div class="max-w-4xl mx-auto px-5 sm:px-6">
    <div class="{REVEAL} grid grid-cols-2 sm:grid-cols-4 gap-4">
      {items}
    </div>
  </div>
</section>"""


def prose_section(heading, paragraphs, width="max-w-4xl"):
    ps = "".join(f'<p class="{REVEAL} text-slate-600 text-[15px] sm:text-base leading-relaxed mb-4">{p}</p>' for p in paragraphs)
    return f"""<section class="py-10 sm:py-12">
  <div class="{width} mx-auto px-5 sm:px-6">
    <h2 class="{SECTION_H2} text-left">{heading}</h2>
    <div class="{REVEAL} w-16 h-[3px] bg-gold mb-8 rounded-full"></div>
    {ps}
  </div>
</section>"""


def reviews_section(heading, sub, reviews):
    # reviews: list of (name, text, context)
    cards = "".join(bsp.review_card(name, text, context) for name, text, context in reviews)
    return f"""<section class="py-10 sm:py-12 bg-white">
  <div class="max-w-4xl mx-auto px-5 sm:px-6">
    <h2 class="{SECTION_H2} text-left">{heading}</h2>
    <p class="{REVEAL} text-slate-500 text-[15px] mb-8">{sub}</p>
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-5">
      {cards}
    </div>
  </div>
</section>"""


def photos_pending_note(text):
    return f"""<section class="py-6">
  <div class="max-w-4xl mx-auto px-5 sm:px-6">
    <div class="{REVEAL} bg-bg rounded-2xl p-6 border border-amber-100 flex gap-4 items-start">
      <div class="text-2xl shrink-0">&#128247;</div>
      <p class="text-slate-600 text-sm leading-relaxed">{text}</p>
    </div>
  </div>
</section>"""


def project_card(title, location, plot, desc, url):
    return f"""<a href="{url}" class="{REVEAL} block bg-white rounded-2xl overflow-hidden shadow-md shadow-slate-900/5 border border-amber-100 hover:-translate-y-1.5 hover:shadow-xl transition duration-200">
      <div class="h-32 bg-gradient-to-br from-navy to-navy2 flex items-center justify-center text-white text-4xl">&#127959;&#65039;</div>
      <div class="p-6">
        <div class="text-gold text-xs font-bold tracking-wider uppercase mb-1.5">{location} &middot; {plot}</div>
        <h3 class="font-heading text-navy text-[17px] mb-2">{title}</h3>
        <p class="text-slate-500 text-sm mb-3">{desc}</p>
        <span class="text-gold font-bold text-sm">View Project &rarr;</span>
      </div>
    </a>"""


# ==================== PROJECT: 10 MARLA HOUSE, LAKE CITY ====================
p1_canonical = "https://msconstruction.services/projects/10-marla-house-lake-city-lahore/"
p1_reviews = [
    ("Huaweicell 200", "We recently had our 10 Marla house constructed in Lake City Lahore by MS Construction Services, and the entire experience was smooth and professional from start to finish. Site supervision was consistent, communication was excellent, and the final result exceeded our expectations.", "Google &middot; Local Guide"),
    ("Minha Muneeb", "We hired them for a 10 Marla house construction in Lake City Lahore and they're honestly the best construction company in Lahore with affordable rates. The quality of work, on-time delivery, and budget-friendly pricing made the whole process stress-free.", "Google review"),
]

p1_body = (
    breadcrumb_nav([("Home", "/"), ("Projects", "/projects/"), ("10 Marla House, Lake City", None)])
    + "\n" + simple_hero("Completed Project", "10 Marla House Construction in Lake City, Lahore",
                          "Full house construction from grey structure through finishing, for a client in Lake City Lahore.")
    + "\n" + project_facts_bar([
        ("Location", "Lake City, Lahore"),
        ("Plot Size", "10 Marla"),
        ("Scope", "Grey Structure &amp; Finishing"),
        ("Service", "House Construction"),
    ])
    + "\n" + prose_section("About This Project", [
        "This 10 Marla house in Lake City Lahore was a full house construction project, grey structure through finishing, built under our standard process: a free site visit, a fixed, itemized quote within 24 hours, and consistent site supervision through to handover.",
        "Like all our house construction projects, material specifications followed our standard A+ grade lineup, Maple Leaf Cement, Mughal Supreme Steel 60 Grade, and the other specs listed on our House Construction page, confirmed in writing before work began.",
    ])
    + "\n" + reviews_section("What the Client Said", "Both reviews below are from this project, left independently on Google.", p1_reviews)
    + "\n" + photos_pending_note("We're adding photos for this project as the client shares them with us. In the meantime, you're welcome to ask about it, or similar 10 Marla Lake City projects, at your own free site visit.")
    + "\n" + bsp.cta_footer_block("Planning a Similar Project in Lake City?", "Book a free site visit and get a fixed, itemized quote within 24 hours, locked for 30 days.")
)

p1_breadcrumb_json = bsp.breadcrumb([
    ("Home", "https://msconstruction.services/"),
    ("Projects", "https://msconstruction.services/projects/"),
    ("10 Marla House, Lake City", p1_canonical),
])

p1_project_json = f'''{{
  "@context": "https://schema.org",
  "@type": "CreativeWork",
  "name": "10 Marla House Construction, Lake City",
  "description": "Full house construction from grey structure through finishing, as described in the client's Google reviews.",
  "url": "{p1_canonical}",
  "locationCreated": {{ "@type": "Place", "name": "Lake City, Lahore" }},
  "creator": {{ "@id": "{LB_ID}" }}
}}'''

p1_reviews_json = '[\n' + ',\n'.join('''    {
      "@type": "Review",
      "itemReviewed": {"@id": "%s"},
      "author": {"@type": "Person", "name": "%s"},
      "reviewRating": {"@type": "Rating", "ratingValue": "5", "bestRating": "5"},
      "reviewBody": "%s"
    }''' % (LB_ID, name, text) for name, text, ctx in p1_reviews) + '\n]'

p1_page = bsp.area_page_shell(
    title="10 Marla House Construction, Lake City Lahore | MS Construction",
    og_title="10 Marla House Construction in Lake City, Lahore",
    og_desc="A completed 10 Marla house construction project in Lake City Lahore, grey structure through finishing, with real client reviews.",
    canonical=p1_canonical,
    service_msg="Hello, I'd like a free site visit and quote for a house construction project in Lake City.",
    json_ld_blocks=[p1_breadcrumb_json, p1_project_json, p1_reviews_json],
    body_content=p1_body,
)
os.makedirs(f"{PROJECTS_BASE}/10-marla-house-lake-city-lahore", exist_ok=True)
with open(f"{PROJECTS_BASE}/10-marla-house-lake-city-lahore/index.html", "w", encoding="utf-8") as f:
    f.write(p1_page)
print("project page '10-marla-house-lake-city-lahore' written", len(p1_page), "bytes")


# ==================== PROJECT: GREY STRUCTURE, BAHRIA TOWN BB BLOCK ====================
p2_canonical = "https://msconstruction.services/projects/grey-structure-bahria-town-bb-block/"
p2_reviews = [
    ("Myacademyrtb123", "We have amazing experience with Mian Shahbaz and his team, they are too much professional. We have a 10 Marla plot in Bahria Town BB Block and got our grey structure ready in just 100 days.", "Google review"),
]

os.makedirs(f"{PROJECTS_BASE}/grey-structure-bahria-town-bb-block", exist_ok=True)

p2_body = (
    breadcrumb_nav([("Home", "/"), ("Projects", "/projects/"), ("Grey Structure, Bahria Town BB Block", None)])
    + "\n" + simple_hero("Completed Project", "Grey Structure Construction, Bahria Town BB Block",
                          "A 10 Marla grey structure completed in 100 days in Bahria Town BB Block, Lahore.")
    + "\n" + project_facts_bar([
        ("Location", "Bahria Town BB Block"),
        ("Plot Size", "10 Marla"),
        ("Scope", "Grey Structure Only"),
        ("Timeline", "100 Days"),
    ])
    + "\n" + prose_section("About This Project", [
        "This 10 Marla plot in Bahria Town BB Block was a grey structure-only project, foundation, structural walls, roof slab, beams, and basic internal conduit work, completed in 100 days.",
        "Grey structure used our standard A+ grade specifications: Maple Leaf Cement, Mughal Supreme Steel 60 Grade, semi special bricks, and steel shuttering, the same lineup listed on our Grey Structure page, confirmed in the client's fixed, itemized quote before work started.",
    ])
    + "\n" + reviews_section("What the Client Said", "Left independently on Google.", p2_reviews)
    + "\n" + photos_pending_note("We're adding photos for this project as the client shares them with us. Ask to see similar Bahria Town grey structure work at your own free site visit.")
    + "\n" + bsp.cta_footer_block("Planning Grey Structure in Bahria Town?", "Book a free site visit and get a fixed, itemized quote within 24 hours, locked for 30 days.")
)

p2_breadcrumb_json = bsp.breadcrumb([
    ("Home", "https://msconstruction.services/"),
    ("Projects", "https://msconstruction.services/projects/"),
    ("Grey Structure, Bahria Town BB Block", p2_canonical),
])

p2_project_json = f'''{{
  "@context": "https://schema.org",
  "@type": "CreativeWork",
  "name": "10 Marla Grey Structure, Bahria Town BB Block",
  "description": "Grey structure completed in 100 days on a 10 Marla plot, as described by the client in their Google review.",
  "url": "{p2_canonical}",
  "locationCreated": {{ "@type": "Place", "name": "Bahria Town BB Block, Lahore" }},
  "creator": {{ "@id": "{LB_ID}" }}
}}'''

p2_reviews_json = '[\n' + ',\n'.join('''    {
      "@type": "Review",
      "itemReviewed": {"@id": "%s"},
      "author": {"@type": "Person", "name": "%s"},
      "reviewRating": {"@type": "Rating", "ratingValue": "5", "bestRating": "5"},
      "reviewBody": "%s"
    }''' % (LB_ID, name, text) for name, text, ctx in p2_reviews) + '\n]'

p2_page = bsp.area_page_shell(
    title="Grey Structure Construction, Bahria Town BB Block | MS Construction",
    og_title="Grey Structure Construction in Bahria Town BB Block",
    og_desc="A completed 10 Marla grey structure project in Bahria Town BB Block, Lahore, finished in 100 days, with a real client review.",
    canonical=p2_canonical,
    service_msg="Hello, I'd like a free site visit and quote for a grey structure project in Bahria Town.",
    json_ld_blocks=[p2_breadcrumb_json, p2_project_json, p2_reviews_json],
    body_content=p2_body,
)
with open(f"{PROJECTS_BASE}/grey-structure-bahria-town-bb-block/index.html", "w", encoding="utf-8") as f:
    f.write(p2_page)
print("project page 'grey-structure-bahria-town-bb-block' written", len(p2_page), "bytes")


# ==================== PROJECTS HUB ====================
hub_canonical = "https://msconstruction.services/projects/"
os.makedirs(PROJECTS_BASE, exist_ok=True)

more_reviews = [
    ("Shezad Ali", "Very good work, I built my 10 Marla house in Bahria Town, really very good work. They've worked in Bahria Town and other societies for almost 17 years.", "Bahria Town, 10 Marla"),
    ("Muhammad Bota", "Really good experience, I built my 5 Marla house in Lake City and it was completed within 6 months.", "Lake City, 5 Marla"),
    ("Moazam Muzafar Ali", "Highly recommended construction company in Lahore. We recently completed our 5 Marla house in Bahria Town Lahore with MS Construction, as an overseas Pakistani, their care and communication meant a lot.", "Bahria Town, 5 Marla"),
]

hub_body = (
    breadcrumb_nav([("Home", "/"), ("Projects", None)])
    + "\n" + simple_hero("Our Work", "Completed Construction Projects in Lahore",
                          "Two of our projects, told in detail with real client reviews. More are added as clients share photos and details with us.", wide=True)
    + f"""
<section class="py-14 sm:py-16">
  <div class="max-w-6xl mx-auto px-5 sm:px-6">
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
      {project_card("10 Marla House Construction", "Lake City", "10 Marla", "Full house construction, grey structure through finishing.", "/projects/10-marla-house-lake-city-lahore/")}
      {project_card("Grey Structure Construction", "Bahria Town BB Block", "10 Marla", "Grey structure completed in 100 days.", "/projects/grey-structure-bahria-town-bb-block/")}
    </div>
  </div>
</section>"""
    + "\n" + reviews_section("More Client Projects", "Real reviews from three more completed projects, full case studies for these are being built out.", more_reviews)
    + f"""
<section class="pb-10">
  <div class="max-w-4xl mx-auto px-5 sm:px-6 text-center">
    <a href="https://maps.app.goo.gl/ud1w2rqY9VFiHBKH7" target="_blank" rel="noopener" class="{REVEAL} inline-flex items-center gap-2 text-gold font-bold text-sm hover:text-goldLight transition">See All Reviews on Google &rarr;</a>
  </div>
</section>"""
    + "\n" + bsp.cta_footer_block("Want Your Project Featured Here Next?", "Book a free site visit and get a fixed, itemized quote within 24 hours, locked for 30 days.")
)

hub_breadcrumb_json = bsp.breadcrumb([
    ("Home", "https://msconstruction.services/"),
    ("Projects", hub_canonical),
])

hub_itemlist_json = f'''{{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "name": "Completed Construction Projects by MS Construction Services",
  "itemListElement": [
    {{"@type": "ListItem", "position": 1, "name": "10 Marla House Construction, Lake City", "url": "{p1_canonical}"}},
    {{"@type": "ListItem", "position": 2, "name": "10 Marla Grey Structure, Bahria Town BB Block", "url": "{p2_canonical}"}}
  ]
}}'''

hub_page = bsp.area_page_shell(
    title="Completed Construction Projects in Lahore | MS Construction",
    og_title="Completed Construction Projects in Lahore",
    og_desc="Real completed construction projects by MS Construction Services in Lake City and Bahria Town, Lahore, with client reviews.",
    canonical=hub_canonical,
    service_msg="Hello, I'd like a free site visit and quote for my construction project.",
    json_ld_blocks=[hub_breadcrumb_json, hub_itemlist_json],
    body_content=hub_body,
)
with open(f"{PROJECTS_BASE}/index.html", "w", encoding="utf-8") as f:
    f.write(hub_page)
print("projects hub page written", len(hub_page), "bytes")


# ==================== GUIDE: 5 MARLA CONSTRUCTION TIMELINE ====================
g_canonical = "https://msconstruction.services/guides/5-marla-house-construction-timeline-lahore/"
os.makedirs(f"{GUIDES_BASE}/5-marla-house-construction-timeline-lahore", exist_ok=True)

g_faq_html, g_faq_json = bsp.faq_section([
    ("How long does a 5 Marla house take to build in Lahore?", "Typically 2 to 3 months under normal conditions, though actual timelines vary. One of our completed 5 Marla projects in Lake City took 6 months due to normal project variables. Your specific timeline is confirmed at your free site visit."),
    ("Why don't you give one fixed timeline for every 5 Marla house?", "Plot conditions, drawing complexity, and how quickly design decisions get finalized all affect the real timeline. A single fixed number would be accurate for some projects and misleading for others, so we confirm yours specifically after seeing your site and drawings."),
    ("Does grey structure or finishing take longer on a 5 Marla house?", "Grey structure is typically the larger portion of the timeline, since finishing work can often start on completed sections while structural work continues elsewhere on the site."),
    ("What's the fastest a 5 Marla grey structure has been completed?", "Our fastest documented grey structure timeline is 100 days, on a 10 Marla plot in Bahria Town BB Block. Smaller 5 Marla plots can move faster under similarly favorable conditions, confirmed at your site visit."),
])

g_body = (
    breadcrumb_nav([("Home", "/"), ("5 Marla Construction Timeline", None)])
    + "\n" + simple_hero("Buyer's Guide", "5 Marla House Construction Timeline in Lahore",
                          "What actually determines how long a 5 Marla house takes to build, with a realistic range instead of a single made-up number.")
    + "\n" + prose_section("The Short Answer", [
        "A 5 Marla house typically takes 2 to 3 months to build in Lahore, from grey structure through basic finishing, under normal site conditions. That's an estimate, not a guarantee, actual timelines depend on your specific plot, drawings, and how quickly design decisions get finalized.",
        "To be transparent about the range: one of our own completed 5 Marla projects in Lake City took 6 months. Both outcomes are real. The 2-3 month figure is what typically happens when drawings are finalized early and there are no major delays, the 6-month case shows how much things like weather, approvals, or mid-project changes can extend a project.",
    ])
    + "\n" + prose_section("What the Timeline Actually Covers", [
        "Grey structure, foundation, structural walls, roof slab, beams, and basic conduit work, is the largest single chunk of the timeline on most 5 Marla projects. Finishing work, flooring, electrical fittings, paint, kitchen and bathroom fixtures, follows once the structure is sound and typically runs in parallel with later-stage structural work where possible.",
        "Before either stage starts, there's a free site visit and a fixed, itemized quote, usually within 24 hours. That quote is based on your specific drawings and plot conditions, which is why we don't publish one fixed number for every 5 Marla house, actual scope varies enough between projects that a single figure would be misleading either way.",
    ])
    + "\n" + prose_section("What Can Extend the Timeline", [
        "A few things reliably push a project past the typical 2-3 month range: design changes made mid-construction, monsoon-season weather delays, society approval processes (DHA and Bahria Town both have their own review steps before construction starts), and material availability for specific finishes.",
        "None of these are unusual, they're a normal part of construction anywhere. The difference is whether your contractor plans around them upfront or treats them as surprises. We build known approval steps into your project plan from day one, and flag likely weather-sensitive stages before they happen, not after.",
    ])
    + "\n" + g_faq_html
    + "\n" + bsp.cta_footer_block("Get Your Actual Timeline", "Book a free site visit and we'll confirm a realistic timeline alongside your fixed, itemized quote.")
)

g_breadcrumb_json = bsp.breadcrumb([
    ("Home", "https://msconstruction.services/"),
    ("5 Marla Construction Timeline", g_canonical),
])

g_article_json = f'''{{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "5 Marla House Construction Timeline in Lahore",
  "description": "A realistic 2-3 month typical timeline for 5 Marla house construction in Lahore, what the stages cover, and what can extend it.",
  "url": "{g_canonical}",
  "author": {{ "@type": "Organization", "name": "MS Construction Services", "@id": "{LB_ID}" }},
  "publisher": {{ "@type": "Organization", "name": "MS Construction Services", "@id": "{LB_ID}" }},
  "datePublished": "2026-09-11",
  "dateModified": "2026-09-11",
  "mainEntityOfPage": "{g_canonical}"
}}'''

g_page = bsp.area_page_shell(
    title="5 Marla House Construction Timeline in Lahore | MS Construction",
    og_title="5 Marla House Construction Timeline in Lahore",
    og_desc="A realistic 2-3 month typical timeline for 5 Marla house construction in Lahore, what each stage covers, and what can extend it.",
    canonical=g_canonical,
    service_msg="Hello, I'd like a free site visit and quote for a 5 Marla house construction project.",
    json_ld_blocks=[g_breadcrumb_json, g_article_json, g_faq_json],
    body_content=g_body,
)
with open(f"{GUIDES_BASE}/5-marla-house-construction-timeline-lahore/index.html", "w", encoding="utf-8") as f:
    f.write(g_page)
print("guide page '5-marla-house-construction-timeline-lahore' written", len(g_page), "bytes")

print("ALL CONTENT PAGES BUILT")
