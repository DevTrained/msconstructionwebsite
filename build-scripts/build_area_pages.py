import os, importlib.util

spec = importlib.util.spec_from_file_location("bsp", "/sessions/eloquent-vibrant-albattani/mnt/outputs/build_service_pages.py")
bsp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bsp)  # re-runs build_service_pages.py, rebuilding those files too (harmless/idempotent)

REVEAL = bsp.REVEAL
SECTION_EYEBROW = bsp.SECTION_EYEBROW
SECTION_H2 = bsp.SECTION_H2

AREAS_BASE = "/sessions/eloquent-vibrant-albattani/mnt/outputs/site/areas"
os.makedirs(AREAS_BASE, exist_ok=True)

LB_ID = "https://msconstruction.services/#localbusiness"


def services_grid():
    def card(icon, title, desc, url):
        return f"""<a href="{url}" class="{REVEAL} block bg-white rounded-2xl overflow-hidden shadow-md shadow-slate-900/5 hover:-translate-y-1.5 hover:shadow-xl transition duration-200">
        <div class="h-28 bg-gradient-to-br from-navy to-navy2 flex items-center justify-center text-white text-3xl">{icon}</div>
        <div class="p-5"><h3 class="font-heading text-navy text-[15.5px] mb-1.5">{title}</h3><p class="text-slate-500 text-sm mb-2">{desc}</p><span class="text-gold font-bold text-sm">Learn More &rarr;</span></div>
      </a>"""
    return f"""<section class="py-16 sm:py-20 bg-white">
  <div class="max-w-6xl mx-auto px-5 sm:px-6">
    <span class="{SECTION_EYEBROW}">What We Build Here</span>
    <h2 class="{SECTION_H2}">Services Available in This Area</h2>
    <div class="grid grid-cols-1 sm:grid-cols-3 gap-6 mt-10">
      {card("&#129521;", "Grey Structure", "The structural skeleton, done right the first time.", "/services/grey-structure/")}
      {card("&#127968;", "House Construction", "Foundation to move-in ready, managed start to finish.", "/services/house-construction/")}
      {card("&#127970;", "Commercial Construction", "Offices, plazas, and commercial spaces.", "/services/commercial-construction/")}
    </div>
  </div>
</section>"""


def area_hero(eyebrow, h1, sub):
    return f"""<section class="relative overflow-hidden bg-gradient-to-br from-navy to-navyDark text-white pt-10 pb-14">
  <div class="max-w-6xl mx-auto px-5 sm:px-6">
    <span class="{REVEAL} block text-gold font-bold text-xs tracking-[2px] uppercase mb-2.5">{eyebrow}</span>
    <h1 class="{REVEAL} font-heading text-3xl sm:text-4xl font-extrabold leading-tight tracking-tight mb-4 max-w-2xl">{h1}</h1>
    <p class="{REVEAL} text-slate-300 max-w-xl mb-7 text-[15px] sm:text-base">{sub}</p>
    <div class="{REVEAL} flex flex-wrap gap-3">
      <a id="serviceWaBtn" href="#" target="_blank" class="inline-flex items-center gap-2 bg-whatsapp hover:bg-whatsappDark text-white font-bold text-sm px-6 py-3.5 rounded-xl shadow-lg shadow-whatsapp/30 transition hover:-translate-y-0.5">&#128172; Get Free Site Visit on WhatsApp</a>
      <a href="tel:+923061982828" class="inline-flex items-center gap-2 border border-white/30 hover:border-white hover:bg-white/10 text-white font-bold text-sm px-6 py-3.5 rounded-xl transition">&#128222; Call 0306-1982828</a>
    </div>
  </div>
</section>"""


def area_intro(heading, paragraphs):
    ps = "".join(f'<p class="{REVEAL} text-slate-600 text-[15px] sm:text-base leading-relaxed mb-4">{p}</p>' for p in paragraphs)
    return f"""<section class="py-16 sm:py-20">
  <div class="max-w-4xl mx-auto px-5 sm:px-6">
    <h2 class="{SECTION_H2} text-left">{heading}</h2>
    <div class="{REVEAL} w-16 h-[3px] bg-gold mb-8 rounded-full"></div>
    {ps}
  </div>
</section>"""


def local_note(heading, text, icon="&#128204;"):
    return f"""<section class="py-10">
  <div class="max-w-4xl mx-auto px-5 sm:px-6">
    <div class="{REVEAL} bg-bg rounded-2xl p-6 sm:p-7 border border-amber-100 flex gap-4 items-start">
      <div class="text-2xl shrink-0">{icon}</div>
      <div>
        <h3 class="font-heading text-navy text-[16px] mb-1.5">{heading}</h3>
        <p class="text-slate-600 text-sm leading-relaxed">{text}</p>
      </div>
    </div>
  </div>
</section>"""


def area_breadcrumb_nav(area_name):
    return f"""<nav class="max-w-6xl mx-auto px-5 sm:px-6 pt-4 text-xs text-slate-400" aria-label="Breadcrumb">
  <a href="/" class="hover:text-gold transition">Home</a> / <a href="/#areas" class="hover:text-gold transition">Areas We Serve</a> / <span class="text-slate-500">{area_name}</span>
</nav>"""


def area_faq_and_json(items):
    return bsp.faq_section(items)


def area_breadcrumb_json(area_name, url):
    return bsp.breadcrumb([
        ("Home", "https://msconstruction.services/"),
        ("Areas We Serve", "https://msconstruction.services/#areas"),
        (area_name, url),
    ])


def area_localbusiness_json(area_name):
    return f'''{{
  "@context": "https://schema.org",
  "@type": ["LocalBusiness", "GeneralContractor", "HomeAndConstructionBusiness"],
  "@id": "{LB_ID}",
  "name": "MS Construction Services",
  "areaServed": {{ "@type": "Place", "name": "{area_name}" }}
}}'''


def area_service_json(area_name, url, desc):
    return f'''{{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "Construction Services in {area_name}",
  "description": "{desc}",
  "url": "{url}",
  "provider": {{ "@id": "{LB_ID}" }},
  "areaServed": {{ "@type": "Place", "name": "{area_name}" }},
  "serviceType": ["Gray Structure Construction", "House Construction", "Commercial Construction"]
}}'''


def review_json_block(reviews):
    # reviews: list of (author, text, rating)
    items = []
    for author, text, rating in reviews:
        items.append('''    {
      "@type": "Review",
      "itemReviewed": { "@id": "%s" },
      "author": { "@type": "Person", "name": "%s" },
      "reviewRating": { "@type": "Rating", "ratingValue": "%s", "bestRating": "5" },
      "reviewBody": "%s"
    }''' % (LB_ID, author, rating, text))
    return '[\n' + ',\n'.join(items) + '\n]'


def project_json_block(projects):
    # projects: list of (name, description, area)
    items = []
    for name, desc, area in projects:
        items.append('''    {
      "@type": "CreativeWork",
      "name": "%s",
      "description": "%s",
      "locationCreated": { "@type": "Place", "name": "%s" },
      "creator": { "@id": "%s" }
    }''' % (name, desc, area, LB_ID))
    return '[\n' + ',\n'.join(items) + '\n]'


def build_area_page(slug, title, og_title, og_desc, service_msg, breadcrumb_area_name,
                     hero_eyebrow, h1, hero_sub, intro_heading, intro_paragraphs,
                     local_note_heading, local_note_text, local_note_icon,
                     trust_block, faq_items, cta_heading, cta_sub,
                     extra_json_blocks):
    os.makedirs(f"{AREAS_BASE}/{slug}", exist_ok=True)
    canonical = f"https://msconstruction.services/areas/{slug}/"

    bc_nav = area_breadcrumb_nav(breadcrumb_area_name)
    hero = area_hero(hero_eyebrow, h1, hero_sub)
    intro = area_intro(intro_heading, intro_paragraphs)
    note = local_note(local_note_heading, local_note_text, local_note_icon)
    services = services_grid()
    faq_html, faq_json = area_faq_and_json(faq_items)
    cta = bsp.cta_footer_block(cta_heading, cta_sub)

    body = bc_nav + "\n" + hero + "\n" + intro + "\n" + note + "\n" + (trust_block or "") + "\n" + services + "\n" + faq_html + "\n" + cta

    json_blocks = [
        area_breadcrumb_json(breadcrumb_area_name, canonical),
        area_localbusiness_json(breadcrumb_area_name),
        area_service_json(breadcrumb_area_name, canonical, og_desc),
        faq_json,
    ] + extra_json_blocks

    page = bsp.area_page_shell(
        title=title, og_title=og_title, og_desc=og_desc, canonical=canonical,
        service_msg=service_msg, json_ld_blocks=json_blocks, body_content=body,
    )
    with open(f"{AREAS_BASE}/{slug}/index.html", "w", encoding="utf-8") as f:
        f.write(page)
    print(f"area page '{slug}' written", len(page), "bytes")
    return canonical


# ==================== 1. BAHRIA TOWN LAHORE ====================
bt_trust = bsp.trust_section(
    "What Bahria Town Clients Say",
    "Three real reviews from homeowners who built with us in Bahria Town.",
    "Shezad Ali",
    "Very good work, I built my 10 Marla house in Bahria Town, really very good work. They've worked in Bahria Town and other societies for almost 17 years.",
    "Bahria Town, 10 Marla House",
)
bt_reviews_json = review_json_block([
    ("Myacademyrtb123", "We have amazing experience with Mian Shahbaz and his team, they are too much professional. We have a 10 Marla plot in Bahria Town BB Block and got our grey structure ready in just 100 days.", "5"),
    ("Shezad Ali", "Very good work, I built my 10 Marla house in Bahria Town, really very good work. They've worked in Bahria Town and other societies for almost 17 years.", "5"),
    ("Moazam Muzafar Ali", "Highly recommended construction company in Lahore. We recently completed our 5 Marla house in Bahria Town Lahore with MS Construction, as an overseas Pakistani, their care and communication meant a lot.", "5"),
])
bt_projects_json = project_json_block([
    ("10 Marla Grey Structure, Bahria Town BB Block", "Grey structure completed in 100 days on a 10 Marla plot, as described by the client in their Google review.", "Bahria Town BB Block, Lahore"),
    ("5 Marla House, Bahria Town Lahore", "Full house construction for an overseas Pakistani client, as described in their Google review.", "Bahria Town, Lahore"),
])

build_area_page(
    slug="bahria-town-lahore",
    title="Construction Company in Bahria Town Lahore | MS Construction Services",
    og_title="Construction Company in Bahria Town Lahore",
    og_desc="Construction company in Bahria Town Lahore, covering Sector A, C, and E. Free site visit, fixed 24-hour quote, 30-day price lock, real client reviews.",
    service_msg="Hello, I'd like a free site visit and quote for a project in Bahria Town Lahore.",
    breadcrumb_area_name="Bahria Town Lahore",
    hero_eyebrow="Bahria Town Lahore",
    h1="Construction Company in Bahria Town Lahore",
    hero_sub="Grey structure, house construction, and commercial work across Bahria Town, Sector A, Sector C, and Sector E. Free site visit, fixed 24-hour quote, 30-day price lock.",
    intro_heading="Building in Bahria Town, Done the Way Bahria Town Expects",
    intro_paragraphs=[
        "Bahria Town Lahore runs on standardized plot sizes and its own society rules, gated access, vehicle timing restrictions for construction material, and approval processes that differ block to block. We've built here long enough to plan around all of it before it becomes a delay on your project.",
        "Our work in Bahria Town spans Sector A, Sector C, and Sector E, from grey structure only to full turnkey house construction, on plot sizes ranging from 5 Marla to 1 Kanal. Every project starts with the same free site visit and fixed, itemized quote we offer anywhere in Lahore, locked for 30 days.",
    ],
    local_note_heading="What's Different About Building in Bahria Town",
    local_note_text="Bahria Town societies typically restrict when heavy vehicles and construction material can enter, and require society-approved building plans before work starts. We handle this coordination as part of your project, so it doesn't become your problem to solve mid-construction.",
    local_note_icon="&#127959;&#65039;",
    trust_block=bt_trust,
    faq_items=[
        ("Do you build in every sector of Bahria Town Lahore?", "We have an active track record in Sector A, Sector C, and Sector E, and take on projects across other Bahria Town sectors as well. Tell us your block and sector at the site visit and we'll confirm access and any society-specific requirements."),
        ("How fast can grey structure be completed in Bahria Town?", "One recent client in Bahria Town BB Block had their 10 Marla grey structure completed in 100 days. Actual timelines depend on plot size and site conditions, confirmed at your free site visit."),
        ("Do you handle Bahria Town's society approval requirements?", "Yes. We coordinate building plan approvals and material delivery timing with Bahria Town's society rules as part of managing your project, so you don't have to chase paperwork yourself."),
        ("What plot sizes do you typically build in Bahria Town?", "Our Bahria Town projects have ranged from 5 Marla to 10 Marla houses, and we take on both grey structure only and full turnkey house construction."),
    ],
    cta_heading="Ready to Build in Bahria Town?",
    cta_sub="Book a free site visit and get a fixed, itemized quote within 24 hours, locked for 30 days.",
    extra_json_blocks=[bt_reviews_json, bt_projects_json],
)

# ==================== 2. LAKE CITY LAHORE ====================
lc_trust = bsp.trust_section(
    "What Lake City Clients Say",
    "Three real reviews from homeowners who built with us in Lake City.",
    "Huaweicell 200",
    "We recently had our 10 Marla house constructed in Lake City Lahore by MS Construction Services, and the entire experience was smooth and professional from start to finish. Site supervision was consistent, communication was excellent, and the final result exceeded our expectations.",
    "Lake City, 10 Marla House",
)
lc_reviews_json = review_json_block([
    ("Huaweicell 200", "We recently had our 10 Marla house constructed in Lake City Lahore by MS Construction Services, and the entire experience was smooth and professional from start to finish. Site supervision was consistent, communication was excellent, and the final result exceeded our expectations.", "5"),
    ("Minha Muneeb", "We hired them for a 10 Marla house construction in Lake City Lahore and they're honestly the best construction company in Lahore with affordable rates. The quality of work, on-time delivery, and budget-friendly pricing made the whole process stress-free.", "5"),
    ("Muhammad Bota", "Really good experience, I built my 5 Marla house in Lake City and it was completed within 6 months.", "5"),
])
lc_projects_json = project_json_block([
    ("10 Marla House Construction, Lake City", "Full house construction from grey structure through finishing, as described in the client's Google review.", "Lake City, Lahore"),
    ("5 Marla House Construction, Lake City", "Full house construction completed within 6 months, as described in the client's Google review.", "Lake City, Lahore"),
])

build_area_page(
    slug="lake-city-lahore",
    title="Gray Structure Construction Services in Lake City | MS Construction",
    og_title="Gray Structure Construction Services in Lake City",
    og_desc="Gray structure and full house construction services in Lake City Lahore. Free site visit, fixed 24-hour quote, 30-day price lock, real client reviews.",
    service_msg="Hello, I'd like a free site visit and quote for a project in Lake City Lahore.",
    breadcrumb_area_name="Lake City Lahore",
    hero_eyebrow="Lake City Lahore",
    h1="Gray Structure Construction Services in Lake City",
    hero_sub="Grey structure and full house construction in Lake City, from a 5 Marla starter home to a 10 Marla family house. Free site visit, fixed 24-hour quote, 30-day price lock.",
    intro_heading="Lake City Is Where Our House Construction Track Record Runs Deepest",
    intro_paragraphs=[
        "More of our completed houses are in Lake City than any other single society in Lahore. That's not a coincidence, it's where several of our earliest clients built, and word of mouth from those projects is a big part of how we still get work there today.",
        "Whether you need grey structure only or a full turnkey house, our Lake City projects have run from 5 Marla to 10 Marla plots, with one recent 5 Marla house completed start to finish in 6 months. Every project begins with a free site visit and a fixed, itemized quote, locked for 30 days.",
    ],
    local_note_heading="Why Grey Structure Quality Matters Most in Lake City",
    local_note_text="Lake City plots tend to run on consistent soil and drainage conditions across the society, which means getting the grey structure specification right the first time, correct RCC grade, proper DPC, and consistent brickwork, pays off in fewer finishing-stage issues later. It's the stage we get the most repeat referrals on in this specific area.",
    local_note_icon="&#127959;&#65039;",
    trust_block=lc_trust,
    faq_items=[
        ("Do you specialize in grey structure in Lake City?", "Grey structure is one of our most requested services in Lake City, and it's the stage several of our Google reviews specifically mention. We also handle full house construction from grey structure through finishing."),
        ("How long does house construction take in Lake City?", "One recent client's 5 Marla house in Lake City was completed within 6 months. Larger plots take longer, confirmed at your free site visit based on your specific plot and drawings."),
        ("What plot sizes have you built in Lake City?", "Our completed Lake City projects range from 5 Marla to 10 Marla houses, covering both grey structure only and full turnkey construction."),
        ("Can I see examples of your Lake City work?", "We can share project details and photos during your site visit consultation, and we're adding more project photos to this page as clients share them with us."),
    ],
    cta_heading="Ready to Build in Lake City?",
    cta_sub="Book a free site visit and get a fixed, itemized quote within 24 hours, locked for 30 days.",
    extra_json_blocks=[lc_reviews_json, lc_projects_json],
)

# ==================== 3. DHA LAHORE ====================
build_area_page(
    slug="dha-lahore",
    title="Construction Company in DHA Lahore | MS Construction Services",
    og_title="Construction Company in DHA Lahore",
    og_desc="Construction company serving DHA Lahore phases. Free site visit, fixed 24-hour quote, 30-day price lock, A+ grade materials since 1994.",
    service_msg="Hello, I'd like a free site visit and quote for a project in DHA Lahore.",
    breadcrumb_area_name="DHA Lahore",
    hero_eyebrow="DHA Lahore",
    h1="Construction Company in DHA Lahore",
    hero_sub="Grey structure, house construction, and commercial work across DHA Lahore's phases. Free site visit, fixed 24-hour quote, 30-day price lock.",
    intro_heading="Building in DHA, Within DHA's Own Approval Process",
    intro_paragraphs=[
        "DHA Lahore runs its own building control process, structural drawings need to be approved through DHA's system before construction starts, and inspections happen at defined stages. We're actively taking on grey structure and house construction projects across DHA's phases, and we build the paperwork timeline into your project plan from day one rather than treating it as a separate hassle.",
        "We're currently building out this page with specific DHA project photos and details, if you've worked with us in DHA before or are planning a project there now, we'd love to feature it here. In the meantime, every DHA project gets the same free site visit and fixed, itemized quote we offer across Lahore, locked for 30 days.",
    ],
    local_note_heading="What's Different About Building in DHA",
    local_note_text="DHA requires structural drawings to be approved through its own building control process before construction begins, and inspects work at set stages. We factor DHA's approval timeline into your project schedule upfront, so it doesn't come as a delay partway through.",
    local_note_icon="&#128203;",
    trust_block=None,
    faq_items=[
        ("Do you build in DHA Lahore?", "Yes, we're actively taking on grey structure, house construction, and commercial projects across DHA Lahore's phases."),
        ("Do you handle DHA's approval process?", "We factor DHA's building control approval timeline into your project schedule from the start, so drawing approval and inspection stages are planned for rather than causing unexpected delays."),
        ("What materials do you use for DHA projects?", "The same A+ grade materials used across all our projects: Maple Leaf Cement, Mughal Supreme Steel 60 Grade, semi special bricks, and the other specifications listed on our Grey Structure page."),
        ("How do I get a quote for a DHA project?", "Book a free site visit through WhatsApp or by calling 0306-1982828. We'll assess your plot and DHA phase, then send a fixed, itemized quote within 24 hours, locked for 30 days."),
    ],
    cta_heading="Planning a Project in DHA?",
    cta_sub="Book a free site visit and get a fixed, itemized quote within 24 hours, locked for 30 days.",
    extra_json_blocks=[],
)

# ==================== 4. BAHRIA ORCHARD LAHORE ====================
build_area_page(
    slug="bahria-orchard-lahore",
    title="Construction Company in Bahria Orchard Lahore | MS Construction",
    og_title="Construction Company in Bahria Orchard Lahore",
    og_desc="Construction company serving Bahria Orchard Lahore. Free site visit, fixed 24-hour quote, 30-day price lock, A+ grade materials since 1994.",
    service_msg="Hello, I'd like a free site visit and quote for a project in Bahria Orchard Lahore.",
    breadcrumb_area_name="Bahria Orchard Lahore",
    hero_eyebrow="Bahria Orchard Lahore",
    h1="Construction Company in Bahria Orchard Lahore",
    hero_sub="Grey structure and house construction across Bahria Orchard's blocks. Free site visit, fixed 24-hour quote, 30-day price lock.",
    intro_heading="Bahria Orchard Projects, Built Around Gated Access Rules",
    intro_paragraphs=[
        "Bahria Orchard shares the same gated-society structure as Bahria Town, controlled entry, defined hours for material delivery, and society-level plan approval, so the coordination work is similar to what we already handle daily in Bahria Town Lahore. We're actively taking on grey structure and house construction projects across Bahria Orchard's blocks.",
        "We're building out this page with specific Bahria Orchard project photos and details as we complete more work there, if you're a past or current client in Bahria Orchard, we'd welcome the chance to feature your project. Every quote starts with the same free site visit and fixed 24-hour turnaround, locked for 30 days.",
    ],
    local_note_heading="What's Different About Building in Bahria Orchard",
    local_note_text="Like Bahria Town Lahore, Bahria Orchard controls when construction vehicles and material can enter, and requires society-approved plans before work begins. We plan material deliveries and paperwork around these rules as part of managing your project.",
    local_note_icon="&#127959;&#65039;",
    trust_block=None,
    faq_items=[
        ("Do you build in Bahria Orchard Lahore?", "Yes, we're actively taking on grey structure and house construction projects across Bahria Orchard's blocks."),
        ("Is building in Bahria Orchard different from Bahria Town?", "The gated-access rules are similar, controlled entry and defined material delivery hours, which is coordination we already handle for our Bahria Town Lahore projects."),
        ("What plot sizes do you build in Bahria Orchard?", "We take on both grey structure only and full turnkey house construction, confirmed for your specific plot size at the free site visit."),
        ("How do I request a quote for Bahria Orchard?", "Message us on WhatsApp or call 0306-1982828 to book a free site visit. You'll get a fixed, itemized quote within 24 hours, locked for 30 days."),
    ],
    cta_heading="Planning a Project in Bahria Orchard?",
    cta_sub="Book a free site visit and get a fixed, itemized quote within 24 hours, locked for 30 days.",
    extra_json_blocks=[],
)

# ==================== 5. ETIHAD TOWN LAHORE ====================
build_area_page(
    slug="etihad-town-lahore",
    title="Construction Company in Etihad Town Lahore | MS Construction Services",
    og_title="Construction Company in Etihad Town Lahore",
    og_desc="Construction company serving Etihad Town Lahore. Free site visit, fixed 24-hour quote, 30-day price lock, A+ grade materials since 1994.",
    service_msg="Hello, I'd like a free site visit and quote for a project in Etihad Town Lahore.",
    breadcrumb_area_name="Etihad Town Lahore",
    hero_eyebrow="Etihad Town Lahore",
    h1="Construction Company in Etihad Town Lahore",
    hero_sub="Grey structure and house construction in Etihad Town. Free site visit, fixed 24-hour quote, 30-day price lock.",
    intro_heading="Straightforward Construction for Etihad Town's Newer Plots",
    intro_paragraphs=[
        "Etihad Town has grown quickly as one of Lahore's newer residential options, which means a lot of plots there are being built on for the first time, no demolition, no existing structure to work around. That generally makes site access and planning more straightforward than in older, denser parts of the city.",
        "We're actively taking on grey structure and house construction projects in Etihad Town and building out this page with real project details as they're completed. Every project starts with a free site visit and a fixed, itemized quote within 24 hours, locked for 30 days.",
    ],
    local_note_heading="What to Expect Building in Etihad Town",
    local_note_text="Since much of Etihad Town is newer development, site access for construction vehicles is generally more flexible than in established societies with tighter internal roads. We'll confirm your specific block's access and any society requirements at the free site visit.",
    local_note_icon="&#128204;",
    trust_block=None,
    faq_items=[
        ("Do you build in Etihad Town Lahore?", "Yes, we're actively taking on grey structure and house construction projects in Etihad Town."),
        ("Is site access easier in Etihad Town than older societies?", "Generally, yes. Since much of Etihad Town is newer development, construction vehicle access tends to be more straightforward than in older, denser societies."),
        ("What's included in a grey structure quote for Etihad Town?", "The same specifications as our standard Grey Structure service: excavation, foundation, DPC, RCC columns and beams, floor slabs, brickwork, and roof structure, using A+ grade materials."),
        ("How do I get a quote for Etihad Town?", "Book a free site visit through WhatsApp or by calling 0306-1982828. We'll send a fixed, itemized quote within 24 hours, locked for 30 days."),
    ],
    cta_heading="Planning a Project in Etihad Town?",
    cta_sub="Book a free site visit and get a fixed, itemized quote within 24 hours, locked for 30 days.",
    extra_json_blocks=[],
)

# ==================== 6. AL-KABIR TOWN LAHORE ====================
build_area_page(
    slug="al-kabir-town-lahore",
    title="Construction Company in Al-Kabir Town Lahore | MS Construction",
    og_title="Construction Company in Al-Kabir Town Lahore",
    og_desc="Construction company serving Al-Kabir Town Lahore. Free site visit, fixed 24-hour quote, 30-day price lock, A+ grade materials since 1994.",
    service_msg="Hello, I'd like a free site visit and quote for a project in Al-Kabir Town Lahore.",
    breadcrumb_area_name="Al-Kabir Town Lahore",
    hero_eyebrow="Al-Kabir Town Lahore",
    h1="Construction Company in Al-Kabir Town Lahore",
    hero_sub="Grey structure and house construction in Al-Kabir Town. Free site visit, fixed 24-hour quote, 30-day price lock.",
    intro_heading="Fixed-Quote Construction for Al-Kabir Town Homeowners",
    intro_paragraphs=[
        "Al-Kabir Town has become a popular choice for homeowners looking for value plots in Lahore, and we're actively taking on grey structure and house construction projects there. The same fixed-quote, no-hidden-costs approach we use everywhere applies here too, so budget-conscious doesn't mean surprise-prone.",
        "We're building out this page with real Al-Kabir Town project photos and details as they're completed, if you're planning a project here, we'd welcome the chance to be your first documented project in this area. Every quote starts with a free site visit and a fixed, itemized turnaround within 24 hours, locked for 30 days.",
    ],
    local_note_heading="Why a Fixed Quote Matters in Al-Kabir Town",
    local_note_text="Value-focused plot buyers are often working to a tighter budget than in premium societies, which makes an itemized, fixed quote more important, not less. You'll know your full cost before construction starts, with the price locked for 30 days.",
    local_note_icon="&#128181;",
    trust_block=None,
    faq_items=[
        ("Do you build in Al-Kabir Town Lahore?", "Yes, we're actively taking on grey structure and house construction projects in Al-Kabir Town."),
        ("Is construction more affordable in Al-Kabir Town?", "Plot prices in Al-Kabir Town tend to be more accessible than in premium societies, but our construction pricing and material quality (A+ grade) stay the same everywhere we build."),
        ("Do you offer grey structure only in Al-Kabir Town?", "Yes, grey structure only or full turnkey house construction, both available with the same fixed, itemized quote and 30-day price lock."),
        ("How do I request a quote for Al-Kabir Town?", "Message us on WhatsApp or call 0306-1982828 to book a free site visit. You'll receive a fixed, itemized quote within 24 hours."),
    ],
    cta_heading="Planning a Project in Al-Kabir Town?",
    cta_sub="Book a free site visit and get a fixed, itemized quote within 24 hours, locked for 30 days.",
    extra_json_blocks=[],
)

print("ALL AREA PAGES BUILT")

# ==================== LISTICLE GUIDE PAGE ====================
GUIDES_BASE = "/sessions/eloquent-vibrant-albattani/mnt/outputs/site/guides"
os.makedirs(f"{GUIDES_BASE}/find-a-reliable-house-construction-contractor-in-lahore", exist_ok=True)

guide_canonical = "https://msconstruction.services/guides/find-a-reliable-house-construction-contractor-in-lahore/"

guide_bc_nav = f"""<nav class="max-w-4xl mx-auto px-5 sm:px-6 pt-4 text-xs text-slate-400" aria-label="Breadcrumb">
  <a href="/" class="hover:text-gold transition">Home</a> / <span class="text-slate-500">Find a Reliable Contractor in Lahore</span>
</nav>"""

guide_hero = f"""<section class="relative overflow-hidden bg-gradient-to-br from-navy to-navyDark text-white pt-10 pb-14">
  <div class="max-w-4xl mx-auto px-5 sm:px-6">
    <span class="{REVEAL} block text-gold font-bold text-xs tracking-[2px] uppercase mb-2.5">Buyer's Guide</span>
    <h1 class="{REVEAL} font-heading text-3xl sm:text-4xl font-extrabold leading-tight tracking-tight mb-4">How to Find a Reliable House Construction Contractor in Lahore</h1>
    <p class="{REVEAL} text-slate-300 max-w-2xl mb-2 text-[15px] sm:text-base">Eight things worth checking before you hand over a plot, or a payment, to anyone.</p>
  </div>
</section>"""

guide_intro = f"""<section class="pt-16 pb-8">
  <div class="max-w-4xl mx-auto px-5 sm:px-6">
    <h2 class="{SECTION_H2} text-left">Why This Matters More in Lahore Than You'd Think</h2>
    <div class="{REVEAL} w-16 h-[3px] bg-gold mb-8 rounded-full"></div>
    <p class="{REVEAL} text-slate-600 text-[15px] sm:text-base leading-relaxed mb-4">Construction in Lahore is largely unregulated at the small-contractor level, there's no licensing board most homeowners can check, and verbal agreements are still common. That's exactly the gap where projects go over budget, timelines slip by months, or the person you hired turns out to be a broker subcontracting your job to someone else entirely.</p>
    <p class="{REVEAL} text-slate-600 text-[15px] sm:text-base leading-relaxed mb-4">None of this means you need to be suspicious of everyone, most contractors are honest people trying to run a business. But a few checks before you sign anything will tell you a lot about who you're actually dealing with.</p>
  </div>
</section>"""


def tip(number, title, text):
    return f"""<div class="{REVEAL} bg-white rounded-2xl p-6 sm:p-7 shadow-md shadow-slate-900/5 border border-amber-100 flex gap-5 items-start mb-5">
      <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-goldLight to-gold flex items-center justify-center text-navyDark font-heading font-extrabold shrink-0">{number}</div>
      <div>
        <h3 class="font-heading text-navy text-[16px] sm:text-[17px] mb-1.5">{title}</h3>
        <p class="text-slate-600 text-sm sm:text-[14.5px] leading-relaxed">{text}</p>
      </div>
    </div>"""

guide_tips_section = f"""<section class="py-8 sm:py-10 bg-bg">
  <div class="max-w-4xl mx-auto px-5 sm:px-6">
    <h2 class="{SECTION_H2} text-left">8 Things to Check Before You Hire a Contractor</h2>
    <div class="{REVEAL} w-16 h-[3px] bg-gold mb-8 rounded-full"></div>
    {tip(1, "Ask for a Written, Itemized Quote", "A real quote breaks down materials, labor, and stages, not a single round number. If a contractor won't put pricing in writing before work starts, that's the clearest early warning sign there is.")}
    {tip(2, "Check Real Reviews, Not Just a Portfolio", "Photos can come from anywhere. Google reviews tied to real names, ideally ones that mention specific areas or plot sizes, are harder to fake and easier to verify by searching the reviewer's name.")}
    {tip(3, "Ask What Material Brands and Grades They'll Actually Use", "“Good quality material” means nothing on its own. Ask for the actual cement brand, steel grade, and brick type by name, and get it written into your quote so there's no ambiguity later.")}
    {tip(4, "Find Out How Many Projects They're Running at Once", "A contractor juggling fifteen sites at once can't give any one of them daily attention. Ask directly how many active projects they're managing, and how often they'll actually be on your site.")}
    {tip(5, "Confirm How Site Supervision Works", "Daily supervision is different from a manager stopping by once a week. Ask specifically who checks structural milestones, and whether there's any camera coverage or documentation of progress.")}
    {tip(6, "Get the Payment Schedule in Writing Before You Sign Anything", "Payments should be tied to construction milestones, not a large lump sum upfront. If most of the money is due before most of the work is done, that's backwards.")}
    {tip(7, "Ask How Change Requests Are Priced", "Plans change mid-project more often than people expect. Ask upfront how a mid-project change gets quoted, before you're in a position where you have to accept whatever price you're given.")}
    {tip(8, "Check How Long They've Actually Been in Business", "Anyone can register a business name last month. Ask how long they've been building specifically, and look for a track record that predates their current marketing.")}
  </div>
</section>"""

guide_transition = f"""<section class="py-16 sm:py-20">
  <div class="max-w-4xl mx-auto px-5 sm:px-6">
    <h2 class="{SECTION_H2} text-left">Where MS Construction Services Stands on These</h2>
    <div class="{REVEAL} w-16 h-[3px] bg-gold mb-8 rounded-full"></div>
    <p class="{REVEAL} text-slate-600 text-[15px] sm:text-base leading-relaxed mb-4">We wrote this guide from the checks we'd want as a homeowner, not as a sales pitch. For what it's worth, here's how we handle each one: a fixed, itemized quote within 24 hours of your site visit, real Google reviews from named clients, named material brands and grades on every quote, a cap on how many new projects we take per month, 24/7 CCTV site coverage, milestone-based payment, separately quoted change requests, and a track record since 1994.</p>
    <p class="{REVEAL} text-slate-600 text-[15px] sm:text-base leading-relaxed mb-4">Whoever you choose, run them through this list first. It's a quick way to separate a real contractor from someone hoping you won't ask too many questions.</p>
  </div>
</section>"""

guide_faq_html, guide_faq_json = bsp.faq_section([
    ("How do I verify a contractor's Google reviews are real?", "Search the reviewer's name alongside the area they mention, for example a plot size and society name. Real reviews tend to include specific, verifiable details rather than generic praise."),
    ("Should I always choose the cheapest quote?", "Not necessarily. Compare quotes on what's actually included, material brands, grades, and scope, not just the bottom-line number. A lower quote missing key specifications can end up costing more in change orders later."),
    ("What's a reasonable payment schedule for house construction in Lahore?", "Payments tied to construction milestones, excavation, DPC, structure, finishing stages, are standard practice. Be cautious of any contractor asking for the majority of payment before significant work has started."),
    ("How many active projects should a reliable contractor be running?", "There's no fixed number, but ask directly and listen for a specific answer. A contractor who limits new projects to maintain quality, rather than taking on everything available, is generally a positive sign."),
])

guide_cta = bsp.cta_footer_block("Ready to Get a Fixed Quote?", "Book a free site visit and see how we measure up against this checklist yourself.")

guide_body = guide_bc_nav + "\n" + guide_hero + "\n" + guide_intro + "\n" + guide_tips_section + "\n" + guide_transition + "\n" + guide_faq_html + "\n" + guide_cta

guide_breadcrumb_json = bsp.breadcrumb([
    ("Home", "https://msconstruction.services/"),
    ("Find a Reliable Contractor in Lahore", guide_canonical),
])

guide_article_json = f'''{{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "How to Find a Reliable House Construction Contractor in Lahore",
  "description": "Eight practical checks to run before hiring a house construction contractor in Lahore, covering quotes, reviews, materials, supervision, and payment terms.",
  "url": "{guide_canonical}",
  "author": {{ "@type": "Organization", "name": "MS Construction Services", "@id": "{LB_ID}" }},
  "publisher": {{ "@type": "Organization", "name": "MS Construction Services", "@id": "{LB_ID}" }},
  "datePublished": "2026-09-10",
  "dateModified": "2026-09-10",
  "mainEntityOfPage": "{guide_canonical}"
}}'''

guide_itemlist_json = '''{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "name": "8 Things to Check Before You Hire a Contractor in Lahore",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Ask for a Written, Itemized Quote"},
    {"@type": "ListItem", "position": 2, "name": "Check Real Reviews, Not Just a Portfolio"},
    {"@type": "ListItem", "position": 3, "name": "Ask What Material Brands and Grades They'll Actually Use"},
    {"@type": "ListItem", "position": 4, "name": "Find Out How Many Projects They're Running at Once"},
    {"@type": "ListItem", "position": 5, "name": "Confirm How Site Supervision Works"},
    {"@type": "ListItem", "position": 6, "name": "Get the Payment Schedule in Writing Before You Sign Anything"},
    {"@type": "ListItem", "position": 7, "name": "Ask How Change Requests Are Priced"},
    {"@type": "ListItem", "position": 8, "name": "Check How Long They've Actually Been in Business"}
  ]
}'''

guide_page = bsp.area_page_shell(
    title="Find a Reliable House Construction Contractor in Lahore",
    og_title="How to Find a Reliable House Construction Contractor in Lahore",
    og_desc="Eight practical checks to run before hiring a house construction contractor in Lahore: quotes, reviews, materials, supervision, and payment terms.",
    canonical=guide_canonical,
    service_msg="Hello, I'd like a free site visit and quote for my construction project.",
    json_ld_blocks=[guide_breadcrumb_json, guide_article_json, guide_itemlist_json, guide_faq_json],
    body_content=guide_body,
)

with open(f"{GUIDES_BASE}/find-a-reliable-house-construction-contractor-in-lahore/index.html", "w", encoding="utf-8") as f:
    f.write(guide_page)

print("listicle guide page written", len(guide_page), "bytes")
