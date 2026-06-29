"""
Module registry — all 20 AI passive-income stream configs.
Only core models are imported; no UI dependencies.
"""
from core.models import ModuleConfig, Tool

MODULES: list[ModuleConfig] = [
    # ── 1 ──────────────────────────────────────────────────────────────────
    ModuleConfig(
        id=1, emoji="📚",
        title="AI-Generated Ebooks",
        subtitle="Research → Outline → Draft → Edit → Publish",
        category="Content Creation",
        description=(
            "Use AI to rapidly research profitable niches, generate detailed outlines, "
            "write full draft chapters, and polish them to publication-ready quality. "
            "Publish on Kindle Direct Publishing and sell bundled series for recurring income."
        ),
        workflow_steps=[
            "1. Research high-demand, low-competition niches using AI + keyword tools",
            "2. Generate a detailed chapter-by-chapter outline with ChatGPT or Claude",
            "3. Write each chapter with AI assistance (target 30–60 min per chapter)",
            "4. Edit and polish with Grammarly; add human voice and examples",
            "5. Design a professional cover with Canva (use Kindle-size templates)",
            "6. Format for KDP: proper margins, fonts, TOC, and metadata",
            "7. Publish on Amazon KDP; set price at $2.99–$9.99 for best royalties",
            "8. Bundle 3–5 ebooks into a series for higher perceived value",
        ],
        tools=[
            Tool("ChatGPT",                "https://chat.openai.com",         "AI writing & research",      True),
            Tool("Claude",                 "https://claude.ai",               "AI assistant",               True),
            Tool("Canva",                  "https://canva.com",               "Cover design",               True),
            Tool("Grammarly",              "https://grammarly.com",           "Grammar & style checker",    True),
            Tool("Kindle Direct Publishing","https://kdp.amazon.com",         "Self-publishing platform",   True),
        ],
        revenue_range="$200 – $5,000/month",
        difficulty="Beginner",
        time_to_profit="2–4 weeks",
        color="#4ade80",
    ),
    # ── 2 ──────────────────────────────────────────────────────────────────
    ModuleConfig(
        id=2, emoji="🎓",
        title="AI-Assisted Online Courses",
        subtitle="Script → Record → Host → Automate → Scale",
        category="Content Creation",
        description=(
            "Use AI to design a full course curriculum, write lesson scripts, and create "
            "quizzes. Record once, sell repeatedly on platforms like Teachable or Gumroad. "
            "Automate enrollment and email follow-ups for hands-off income."
        ),
        workflow_steps=[
            "1. Validate course topic with AI-driven market demand research",
            "2. Use ChatGPT to generate a complete curriculum outline (modules + lessons)",
            "3. Write detailed lesson scripts and speaker notes with AI",
            "4. Record video lessons (screen + webcam); aim for 5–20 min per lesson",
            "5. Build quizzes, assignments, and resources with Notion",
            "6. Design course graphics and slide decks with Canva",
            "7. Host on Teachable or sell direct via Gumroad",
            "8. Set up automated email enrollment sequences with ConvertKit",
        ],
        tools=[
            Tool("ChatGPT",   "https://chat.openai.com", "Curriculum & scripts",      True),
            Tool("Notion",    "https://notion.so",       "Course planning workspace", True),
            Tool("Canva",     "https://canva.com",       "Slide & graphic design",    True),
            Tool("Teachable", "https://teachable.com",   "Course hosting platform",   False),
            Tool("Gumroad",   "https://gumroad.com",     "Digital product sales",     True),
        ],
        revenue_range="$500 – $10,000/month",
        difficulty="Intermediate",
        time_to_profit="1–3 months",
        color="#60a5fa",
    ),
    # ── 3 ──────────────────────────────────────────────────────────────────
    ModuleConfig(
        id=3, emoji="📱",
        title="Automated Social Content Packs",
        subtitle="Generate → Design → Bundle → Sell → Automate",
        category="Digital Products",
        description=(
            "AI creates post variations, captions, hashtag sets, and visual templates "
            "for a target niche. Sell monthly packs to brands and creators on Gumroad "
            "with recurring subscription pricing."
        ),
        workflow_steps=[
            "1. Choose a profitable niche (real estate, fitness, restaurants, etc.)",
            "2. Use AI to generate 30-day content calendars with post ideas",
            "3. Write captions and hashtag sets for each post with ChatGPT",
            "4. Design visual post templates for every format in Canva",
            "5. Bundle into monthly Content Packs (30 posts + captions + hashtags)",
            "6. Sell on Gumroad with recurring monthly subscription pricing",
            "7. Automate delivery with Zapier + email sequences",
            "8. Expand to include Reels scripts, Story templates, and Carousel decks",
        ],
        tools=[
            Tool("ChatGPT",  "https://chat.openai.com", "Caption & content generation", True),
            Tool("Buffer",   "https://buffer.com",      "Social scheduling preview",    True),
            Tool("Hootsuite","https://hootsuite.com",   "Social media management",      False),
            Tool("Canva",    "https://canva.com",       "Visual template design",       True),
            Tool("Airtable", "https://airtable.com",   "Content calendar & CRM",       True),
        ],
        revenue_range="$300 – $3,000/month",
        difficulty="Beginner",
        time_to_profit="1–2 weeks",
        color="#f472b6",
    ),
    # ── 4 ──────────────────────────────────────────────────────────────────
    ModuleConfig(
        id=4, emoji="🤖",
        title="Build & Sell Chatbots",
        subtitle="Build → Train → Deploy → Charge setup + subscription",
        category="Services",
        description=(
            "Deploy support and lead-generation chatbots trained on company FAQs and docs. "
            "Charge a one-time setup fee plus a monthly maintenance retainer. "
            "Templatize builds to serve multiple clients with minimal extra effort."
        ),
        workflow_steps=[
            "1. Identify SMBs spending on live chat support (their biggest pain point)",
            "2. Build chatbot template in Botpress or Voiceflow for target industry",
            "3. Train chatbot on client FAQ docs, product pages, and knowledge base",
            "4. Integrate via embed code into client's website or app",
            "5. Run thorough QA across all conversation flows and edge cases",
            "6. Deploy and provide a short training video for the client's team",
            "7. Charge $500–$2,000 setup + $200–$500/month maintenance retainer",
            "8. Templatize for each niche to cut future build time to under 5 hours",
        ],
        tools=[
            Tool("Botpress",   "https://botpress.com",        "Open-source chatbot builder", True),
            Tool("Voiceflow",  "https://voiceflow.com",       "Visual conversation design",  True),
            Tool("Zapier",     "https://zapier.com",          "Workflow automation",          True),
            Tool("Intercom",   "https://intercom.com",        "Customer messaging platform", False),
            Tool("OpenAI API", "https://platform.openai.com", "GPT-4 API access",            False),
        ],
        revenue_range="$1,000 – $20,000/month",
        difficulty="Intermediate",
        time_to_profit="1–2 months",
        color="#fb923c",
    ),
    # ── 5 ──────────────────────────────────────────────────────────────────
    ModuleConfig(
        id=5, emoji="🎨",
        title="AI Art Downloads",
        subtitle="Prompt → Generate → Package → Sell digital files/licensing",
        category="Digital Products",
        description=(
            "Generate themed art packs with Midjourney or DALL-E. Sell digital files "
            "and licensing on Etsy, Gumroad, and Creative Market. "
            "Build collections for creators and marketers with consistent style."
        ),
        workflow_steps=[
            "1. Research trending art themes on Etsy, Redbubble, and Pinterest",
            "2. Develop 10–20 high-converting Midjourney prompt templates",
            "3. Generate themed collections (100+ images per pack)",
            "4. Upscale top 30% with Topaz AI for commercial print quality",
            "5. Remove backgrounds and prepare files in PNG, SVG, and PDF formats",
            "6. Write keyword-rich titles and descriptions for each listing",
            "7. List on Etsy with bundle pricing ($5 single / $29 full pack)",
            "8. Cross-promote on Pinterest boards and Instagram Reels",
        ],
        tools=[
            Tool("Midjourney",    "https://midjourney.com",       "AI image generation",        False),
            Tool("DALL-E",        "https://labs.openai.com",      "OpenAI image generation",    False),
            Tool("Adobe Firefly", "https://firefly.adobe.com",    "AI creative suite",          True),
            Tool("Canva",         "https://canva.com",            "Design & mockup creation",   True),
            Tool("Etsy",          "https://etsy.com",             "Marketplace for creatives",  False),
        ],
        revenue_range="$100 – $3,000/month",
        difficulty="Beginner",
        time_to_profit="1–2 weeks",
        color="#e879f9",
    ),
    # ── 6 ──────────────────────────────────────────────────────────────────
    ModuleConfig(
        id=6, emoji="🔍",
        title="AI-Powered SEO Blog",
        subtitle="Research keywords → Write → Publish → Monetize with ads & affiliates",
        category="Content Creation",
        description=(
            "Produce keyword-targeted articles with AI-assisted writing and SurferSEO "
            "optimization. Build internal links, add affiliate offers, and monetize with "
            "display ads for compounding passive income over time."
        ),
        workflow_steps=[
            "1. Use Ahrefs or Semrush to find low-competition, high-volume keywords",
            "2. Create a 3–6 month editorial calendar using AI suggestions",
            "3. Generate SEO-optimized articles (1,500–3,000 words) with SurferSEO + ChatGPT",
            "4. Manually add examples, stories, and internal links for E-E-A-T signals",
            "5. Publish on WordPress with Rank Math or Yoast SEO configured",
            "6. Add affiliate links (Amazon, SaaS tools) and display ads (Mediavine/AdSense)",
            "7. Track keyword rankings weekly with Ahrefs; double down on page-2 articles",
            "8. Scale to 20–30 articles/month with freelance editor support",
        ],
        tools=[
            Tool("Ahrefs",    "https://ahrefs.com",    "SEO & keyword research",     False),
            Tool("Semrush",   "https://semrush.com",   "SEO & marketing platform",   False),
            Tool("ChatGPT",   "https://chat.openai.com","AI content generation",      True),
            Tool("WordPress", "https://wordpress.org", "CMS platform",               True),
            Tool("SurferSEO", "https://surferseo.com", "Content SEO optimizer",      False),
        ],
        revenue_range="$500 – $15,000/month",
        difficulty="Intermediate",
        time_to_profit="2–6 months",
        color="#22d3ee",
    ),
    # ── 7 ──────────────────────────────────────────────────────────────────
    ModuleConfig(
        id=7, emoji="📄",
        title="Template Store",
        subtitle="Design → Bundle → Sell docs, slides & resume packs",
        category="Digital Products",
        description=(
            "AI speeds up copy creation and layout variations for templates. "
            "Sell Canva, Notion, and Google Docs templates in packs. "
            "Upsell custom versions for higher ticket revenue."
        ),
        workflow_steps=[
            "1. Identify high-demand template types: resumes, invoices, planners, pitch decks",
            "2. Create 15–30 variations per category using Canva, Notion, and Google Docs",
            "3. Use AI to write all placeholder copy, instructions, and example content",
            "4. Bundle by persona: Freelancer Pack, Job Seeker Bundle, Founder Toolkit",
            "5. Export preview images and create video demos of each template",
            "6. List on Gumroad, Etsy, and Creative Market with SEO-optimised titles",
            "7. Offer a 'done-for-you' customisation upsell at $50–$150",
            "8. Add new template packs monthly to grow catalog and email list",
        ],
        tools=[
            Tool("Canva",       "https://canva.com",          "Visual template design",      True),
            Tool("Notion",      "https://notion.so",          "Notion template builder",     True),
            Tool("Google Docs", "https://docs.google.com",    "Document editor",             True),
            Tool("ChatGPT",     "https://chat.openai.com",    "Copy & content generation",   True),
            Tool("Gumroad",     "https://gumroad.com",        "Digital storefront",          True),
        ],
        revenue_range="$200 – $5,000/month",
        difficulty="Beginner",
        time_to_profit="1–3 weeks",
        color="#fbbf24",
    ),
    # ── 8 ──────────────────────────────────────────────────────────────────
    ModuleConfig(
        id=8, emoji="📸",
        title="AI Stock Images",
        subtitle="Generate → Upscale → Submit → Earn long-tail royalties",
        category="Digital Products",
        description=(
            "Generate commercial-ready AI images in high-demand categories. "
            "Upload consistently to Shutterstock, Adobe Stock, and Getty "
            "for long-tail royalty income that compounds over time."
        ),
        workflow_steps=[
            "1. Research best-selling categories: business, technology, lifestyle, nature",
            "2. Generate high-resolution images with Midjourney and DALL-E in batches of 50",
            "3. Upscale all images to minimum 4 MP with Topaz AI for acceptance",
            "4. Write detailed keyword metadata (50+ tags) for each image",
            "5. Submit to Shutterstock Contributor, Adobe Stock, Alamy, and iStock",
            "6. Monitor rejection reasons and adjust prompts accordingly",
            "7. Identify top-performing styles and produce 200+ similar images",
            "8. Diversify across platforms to maximise royalty income streams",
        ],
        tools=[
            Tool("Midjourney",   "https://midjourney.com",                   "AI image generation",       False),
            Tool("DALL-E",       "https://labs.openai.com",                  "AI image generation",       False),
            Tool("Shutterstock", "https://submit.shutterstock.com",          "Stock image platform",      False),
            Tool("Adobe Stock",  "https://contributor.stock.adobe.com",      "Stock marketplace",         False),
            Tool("Topaz",        "https://www.topazlabs.com",                "AI image upscaling",        False),
        ],
        revenue_range="$100 – $2,000/month",
        difficulty="Beginner",
        time_to_profit="2–4 weeks",
        color="#94a3b8",
    ),
    # ── 9 ──────────────────────────────────────────────────────────────────
    ModuleConfig(
        id=9, emoji="🎵",
        title="AI Music Loops & Background Tracks",
        subtitle="Compose → Bundle by genre/mood → License on marketplaces",
        category="Content Creation",
        description=(
            "Compose music loops and variations quickly with AI tools. "
            "Bundle by genre or mood and license royalty-free on Pond5 "
            "and AudioJungle for passive streaming income."
        ),
        workflow_steps=[
            "1. Research top-selling genres on AudioJungle and Pond5 (corporate, lo-fi, cinematic)",
            "2. Generate base compositions with Suno, Udio, or AIVA",
            "3. Create 4–5 loop variations per track (8-bar, 16-bar, 60s, 90s, full)",
            "4. Clean audio and normalize levels in Audacity (aim for -14 LUFS)",
            "5. Bundle by mood/genre: Corporate Pack, Cinematic Bundle, Lo-Fi Collection",
            "6. Export as WAV (lossless) and MP3 (320kbps) for upload",
            "7. Upload to Pond5, AudioJungle, and Musicbed with keyword metadata",
            "8. Cross-sell complementary SFX packs and stem files for upsell revenue",
        ],
        tools=[
            Tool("Suno",    "https://suno.ai",               "AI music generation",       True),
            Tool("Udio",    "https://udio.com",              "AI music creation",         True),
            Tool("AIVA",    "https://aiva.ai",               "AI music composition",      True),
            Tool("Audacity","https://www.audacityteam.org",  "Free audio editor",         True),
            Tool("Pond5",   "https://pond5.com",             "Stock media marketplace",   False),
        ],
        revenue_range="$200 – $5,000/month",
        difficulty="Beginner",
        time_to_profit="2–4 weeks",
        color="#818cf8",
    ),
    # ── 10 ─────────────────────────────────────────────────────────────────
    ModuleConfig(
        id=10, emoji="🌐",
        title="AI Website Builds",
        subtitle="Sell packages → Deliver in days → Upsell hosting/updates",
        category="Services",
        description=(
            "Use AI site builders for fast, professional small-business websites. "
            "Sell tiered packages and recurring hosting/update subscriptions "
            "for predictable monthly revenue."
        ),
        workflow_steps=[
            "1. Define 3 service tiers: Starter ($500), Pro ($1,500), Premium ($3,000)",
            "2. Build reusable Webflow / Framer templates for 5 common niches",
            "3. Use AI to generate industry-specific copy and content in under 30 min",
            "4. Collect client assets via intake form; begin build within 24 hours",
            "5. Deliver live preview in 3–5 days; offer 2 revision rounds",
            "6. Record a Loom walkthrough and hand off with editing guide",
            "7. Upsell $99–$299/month for hosting, updates, and SEO reporting",
            "8. Collect video testimonials and build a public portfolio for referrals",
        ],
        tools=[
            Tool("Webflow", "https://webflow.com",      "Visual web builder",        True),
            Tool("Framer",  "https://framer.com",       "Design-to-web builder",     True),
            Tool("Wix",     "https://wix.com",          "Website builder",           True),
            Tool("ChatGPT", "https://chat.openai.com",  "Copy & content writing",    True),
            Tool("Zapier",  "https://zapier.com",       "Intake & delivery automation", True),
        ],
        revenue_range="$2,000 – $30,000/month",
        difficulty="Intermediate",
        time_to_profit="1–2 months",
        color="#2dd4bf",
    ),
    # ── 11 ─────────────────────────────────────────────────────────────────
    ModuleConfig(
        id=11, emoji="🎙️",
        title="AI Voiceover Products",
        subtitle="Generate narration → Package → Sell per-script + license voice packs",
        category="Digital Products",
        description=(
            "Generate professional narration for ads, explainers, and audiobooks with "
            "ElevenLabs. Sell per-script and as licensed voice packs. "
            "Build recurring revenue with subscription voice licences."
        ),
        workflow_steps=[
            "1. Create distinct voice profiles for different use cases in ElevenLabs",
            "2. Write sample scripts covering ads, explainers, e-learning, and podcasts",
            "3. Record and generate narration batches (aim for 50+ files)",
            "4. Enhance audio quality with Adobe Podcast AI remove-background tool",
            "5. Master audio in Audacity or Descript (normalize, EQ, compress)",
            "6. Create tiered licensing: Single Use $25 / Extended $99 / Unlimited $299",
            "7. List on Voices.com, Voice123, and Gumroad for multi-channel reach",
            "8. Offer custom voice-over service at $150–$500/project as premium tier",
        ],
        tools=[
            Tool("ElevenLabs",    "https://elevenlabs.io",     "AI voice synthesis",        True),
            Tool("Descript",      "https://descript.com",      "Audio & video editor",      True),
            Tool("Audacity",      "https://www.audacityteam.org","Free audio editor",        True),
            Tool("ChatGPT",       "https://chat.openai.com",   "Script writing assistant",  True),
            Tool("Adobe Podcast", "https://podcast.adobe.com", "AI audio enhancement",      True),
        ],
        revenue_range="$500 – $8,000/month",
        difficulty="Beginner",
        time_to_profit="2–4 weeks",
        color="#38bdf8",
    ),
    # ── 12 ─────────────────────────────────────────────────────────────────
    ModuleConfig(
        id=12, emoji="📈",
        title="AI Marketing Funnel Kits",
        subtitle="Write landing page + email sequences → Sell 'funnel-in-a-box' by niche",
        category="Services",
        description=(
            "AI writes landing page copy, email nurture sequences, and ad creatives. "
            "Package as complete 'funnel-in-a-box' kits sold by niche. "
            "High-ticket productised service with fast delivery."
        ),
        workflow_steps=[
            "1. Pick 2–3 profitable niches: SaaS, coaches, e-commerce, local businesses",
            "2. Research top-performing funnel structures and swipe files in each niche",
            "3. Use Copy.ai and ChatGPT to write full landing page copy + 7-day email sequence",
            "4. Design pages and emails in ConvertKit / Leadpages with your templates",
            "5. Create a complete kit: page designs, email copy, ad headlines, FB ad copy",
            "6. Package as PDF + editable Canva / Notion files with video setup guide",
            "7. Price at $500–$2,000 per kit; offer done-for-you implementation at 3x",
            "8. Use Mailchimp for follow-up and ConvertKit for automated delivery",
        ],
        tools=[
            Tool("Copy.ai",    "https://copy.ai",         "AI copywriting assistant",  True),
            Tool("ChatGPT",    "https://chat.openai.com", "Long-form copy generation", True),
            Tool("Mailchimp",  "https://mailchimp.com",   "Email marketing platform",  True),
            Tool("ConvertKit", "https://convertkit.com",  "Email automation",          False),
            Tool("Leadpages",  "https://leadpages.com",   "Landing page builder",      False),
        ],
        revenue_range="$1,000 – $15,000/month",
        difficulty="Intermediate",
        time_to_profit="1–3 months",
        color="#f87171",
    ),
    # ── 13 ─────────────────────────────────────────────────────────────────
    ModuleConfig(
        id=13, emoji="🎬",
        title="AI Explainer Videos",
        subtitle="Script → Avatar/voice → Captions → Export in batches",
        category="Content Creation",
        description=(
            "Script explainer videos with AI, present with AI avatars, add captions "
            "automatically, and export in batches. Sell to SaaS companies, educators, "
            "and local businesses needing affordable explainers."
        ),
        workflow_steps=[
            "1. Write 60–90 second scripts with ChatGPT optimised for clear, simple language",
            "2. Create AI avatar presenter in Synthesia or HeyGen (pick industry-appropriate avatar)",
            "3. Add AI voiceover with natural pacing and emphasis",
            "4. Incorporate stock footage, product screenshots, and motion graphics",
            "5. Auto-generate captions and edit with Descript's Overdub feature",
            "6. Polish final video in CapCut: colour grade, add intro/outro, music",
            "7. Produce in batches of 5–10 videos for efficiency and client discount packages",
            "8. Sell to SaaS companies ($500–$2,000), educators, and startups needing explainers",
        ],
        tools=[
            Tool("Synthesia", "https://synthesia.io",     "AI avatar video generation", False),
            Tool("HeyGen",    "https://heygen.com",       "AI video with avatars",      False),
            Tool("CapCut",    "https://capcut.com",       "Video editor",               True),
            Tool("ChatGPT",   "https://chat.openai.com",  "Script writing",             True),
            Tool("Descript",  "https://descript.com",     "Captions & editing",         True),
        ],
        revenue_range="$500 – $10,000/month",
        difficulty="Intermediate",
        time_to_profit="1–2 months",
        color="#a78bfa",
    ),
    # ── 14 ─────────────────────────────────────────────────────────────────
    ModuleConfig(
        id=14, emoji="🎮",
        title="AI-Assisted Micro-Games",
        subtitle="Generate art, dialogue & levels → Ship → Monetise via ads/IAP",
        category="Tech & Dev",
        description=(
            "Use AI for game concept, dialogue, level design, and 2D assets. "
            "Build with Unity or Godot and launch on itch.io and mobile stores. "
            "Monetise via in-app purchases, ads, or one-time purchase."
        ),
        workflow_steps=[
            "1. Brainstorm casual game concepts with AI: pick genre + core mechanic",
            "2. Generate 2D sprites, backgrounds, and UI assets with Midjourney",
            "3. Use ChatGPT to write dialogue, level descriptions, and tutorial text",
            "4. Build game mechanics in Unity (C#) or Godot (GDScript) with AI-assisted code",
            "5. Add AI-generated music and SFX for complete atmosphere",
            "6. Implement monetisation: ad network SDK + in-app purchases",
            "7. Beta test with 20+ users; fix critical bugs before hard launch",
            "8. Publish on itch.io (PC), Google Play, and App Store; run Product Hunt launch",
        ],
        tools=[
            Tool("Unity",      "https://unity.com",           "Professional game engine",   True),
            Tool("Godot",      "https://godotengine.org",     "Open-source game engine",    True),
            Tool("ChatGPT",    "https://chat.openai.com",     "Code & dialogue assistance", True),
            Tool("Midjourney", "https://midjourney.com",      "AI game art generation",     False),
            Tool("itch.io",    "https://itch.io",             "Indie game marketplace",     True),
        ],
        revenue_range="$200 – $5,000/month",
        difficulty="Advanced",
        time_to_profit="2–6 months",
        color="#fb923c",
    ),
    # ── 15 ─────────────────────────────────────────────────────────────────
    ModuleConfig(
        id=15, emoji="🎧",
        title="AI-Powered Podcast Engine",
        subtitle="Draft outlines & titles → Record → Clip → Distribute → Monetise",
        category="Content Creation",
        description=(
            "AI drafts episode outlines, hooks, titles, and summaries. Record once, "
            "repurpose into shorts, blogs, and newsletters. Monetise via sponsorships, "
            "memberships, and digital products."
        ),
        workflow_steps=[
            "1. Choose an evergreen niche with consistent audience demand",
            "2. Use ChatGPT to generate a 90-day episode plan with titles and outlines",
            "3. Write episode scripts and SEO-optimised show notes with AI",
            "4. Record high-quality audio with Riverside.fm (local + cloud backup)",
            "5. Edit podcast with Descript: remove filler words, add intro/outro music",
            "6. Create 60-second audiograms and clips with Opus Clip for social media",
            "7. Distribute on Buzzsprout to all major platforms (Spotify, Apple, Google)",
            "8. Monetise: sponsor reads ($25–100 CPM), Patreon tier, and course upsells",
        ],
        tools=[
            Tool("ChatGPT",   "https://chat.openai.com", "Outline & script writing",  True),
            Tool("Descript",  "https://descript.com",    "Podcast editing suite",     True),
            Tool("Riverside",  "https://riverside.fm",   "Remote recording studio",   False),
            Tool("Buzzsprout", "https://buzzsprout.com", "Podcast hosting & distrib.", False),
            Tool("Opus Clip",  "https://opus.pro",       "AI video/audio clipping",   True),
        ],
        revenue_range="$300 – $8,000/month",
        difficulty="Beginner",
        time_to_profit="1–3 months",
        color="#c084fc",
    ),
    # ── 16 ─────────────────────────────────────────────────────────────────
    ModuleConfig(
        id=16, emoji="⚙️",
        title="AI SEO Optimization Service",
        subtitle="Automate audits & briefs → Sell monthly retainers with KPIs",
        category="Services",
        description=(
            "Automate SEO audits, on-page briefs, and monthly reports using AI. "
            "Sell monthly retainers with measurable KPIs. "
            "Scale by hiring VAs for execution while you oversee strategy."
        ),
        workflow_steps=[
            "1. Run full technical audit with Screaming Frog and Ahrefs for prospective clients",
            "2. Use AI to generate a prioritised 90-day action plan from audit data",
            "3. Optimise titles, meta descriptions, H-tags, and content with SurferSEO + AI",
            "4. Fix technical issues: Core Web Vitals, mobile UX, schema markup, broken links",
            "5. Create keyword-optimised content briefs and publish 4+ articles/month",
            "6. Build quality backlinks via digital PR and link exchange outreach",
            "7. Generate AI-powered monthly progress reports with Ahrefs data",
            "8. Lock in 6-month retainers at $1,500–$5,000/month with KPI SLAs",
        ],
        tools=[
            Tool("Screaming Frog",       "https://www.screamingfrog.co.uk", "SEO crawler",        True),
            Tool("Ahrefs",               "https://ahrefs.com",              "SEO analytics",       False),
            Tool("SurferSEO",            "https://surferseo.com",           "Content optimizer",   False),
            Tool("ChatGPT",              "https://chat.openai.com",         "Report generation",   True),
            Tool("Google Search Console","https://search.google.com/search-console","Free search analytics",True),
        ],
        revenue_range="$2,000 – $25,000/month",
        difficulty="Intermediate",
        time_to_profit="1–3 months",
        color="#34d399",
    ),
    # ── 17 ─────────────────────────────────────────────────────────────────
    ModuleConfig(
        id=17, emoji="📖",
        title="AI Study Guides / Workbooks",
        subtitle="Turn complex topics into modules + quizzes → Sell by certification/niche",
        category="Digital Products",
        description=(
            "Turn complex certification or academic topics into structured study guides "
            "and quiz workbooks using AI. Sell downloads; bundle by exam or niche. "
            "Recurring income as exams update."
        ),
        workflow_steps=[
            "1. Research popular certification exams and curricula with high search demand",
            "2. Use AI to generate comprehensive study summaries for each topic area",
            "3. Create 50–100 practice questions with explanations using ChatGPT",
            "4. Build interactive quizzes with Google Forms for free lead magnets",
            "5. Design beautiful workbook layouts in Canva (printable A4 and digital PDF)",
            "6. Add flashcard pages, cheat sheets, and spaced-repetition schedules",
            "7. Bundle by exam: AWS Cert Pack, PMP Guide, CPA Workbook, etc.",
            "8. Sell on Gumroad, Etsy, and niche Facebook groups; update yearly for re-sales",
        ],
        tools=[
            Tool("ChatGPT",      "https://chat.openai.com",    "Content generation",     True),
            Tool("Notion",       "https://notion.so",          "Study guide structure",  True),
            Tool("Canva",        "https://canva.com",          "Workbook design",        True),
            Tool("Google Forms", "https://forms.google.com",   "Quiz builder",           True),
            Tool("Gumroad",      "https://gumroad.com",        "Digital sales platform", True),
        ],
        revenue_range="$200 – $3,000/month",
        difficulty="Beginner",
        time_to_profit="1–3 weeks",
        color="#7dd3fc",
    ),
    # ── 18 ─────────────────────────────────────────────────────────────────
    ModuleConfig(
        id=18, emoji="✉️",
        title="AI-Curated Newsletter",
        subtitle="Summarise industry updates → Publish consistently → Grow & monetise",
        category="Content Creation",
        description=(
            "Use AI to summarise industry news, write editorial commentary, and schedule "
            "consistently. Monetise via paid tiers, sponsorships, and affiliate slots. "
            "Compound growth through referral programs."
        ),
        workflow_steps=[
            "1. Choose a specific industry niche: AI, fintech, e-commerce, Web3, health-tech",
            "2. Set up Feedly to aggregate the top 20 industry sources automatically",
            "3. Use AI to summarise 5–7 key stories each week in 2–3 sentences each",
            "4. Write engaging editorial intro and '1 tip of the week' with your unique angle",
            "5. Design a clean newsletter template in Beehiiv or Substack",
            "6. Grow via Twitter/LinkedIn threads, cross-promotions, and referral incentives",
            "7. Launch paid tier ($9–$19/month) at 1,000+ subscribers",
            "8. Add sponsored slots ($200–$500/issue) and affiliate deals at scale",
        ],
        tools=[
            Tool("Beehiiv",  "https://beehiiv.com",       "Newsletter platform",       True),
            Tool("Substack", "https://substack.com",      "Newsletter & publishing",   True),
            Tool("Feedly",   "https://feedly.com",        "AI content aggregator",     True),
            Tool("ChatGPT",  "https://chat.openai.com",   "Summarisation & writing",   True),
            Tool("Zapier",   "https://zapier.com",        "Content automation",        True),
        ],
        revenue_range="$500 – $20,000/month",
        difficulty="Beginner",
        time_to_profit="1–3 months",
        color="#86efac",
    ),
    # ── 19 ─────────────────────────────────────────────────────────────────
    ModuleConfig(
        id=19, emoji="👕",
        title="AI Print-on-Demand Designs",
        subtitle="Generate design variants → Test fast with small batches → Earn per-sale royalty",
        category="Digital Products",
        description=(
            "Generate design variants quickly with AI and test with small batches. "
            "Automate Etsy listings via Printful/Printify integration. "
            "Earn royalties per sale with zero inventory risk."
        ),
        workflow_steps=[
            "1. Research trending design niches: funny quotes, pet lovers, professions, hobbies",
            "2. Use Midjourney to generate 20–50 design concepts per niche in batches",
            "3. Refine and adapt top designs for different product sizes in Canva",
            "4. Create professional mockups using Printful's built-in mockup generator",
            "5. Connect Printful or Printify to Etsy shop; upload designs with templates",
            "6. Write SEO-optimised titles, tags (13 max), and descriptions with AI",
            "7. Test 20+ designs per niche; identify winners within 30 days",
            "8. Scale winners with 5–10 colour variations and apply to more product types",
        ],
        tools=[
            Tool("Midjourney", "https://midjourney.com",  "AI design generation",     False),
            Tool("Canva",      "https://canva.com",       "Design refinement",        True),
            Tool("Printful",   "https://printful.com",    "Print-on-demand fulfilment",True),
            Tool("Printify",   "https://printify.com",    "POD product catalogue",    True),
            Tool("Etsy",       "https://etsy.com",        "Marketplace storefront",   False),
        ],
        revenue_range="$200 – $5,000/month",
        difficulty="Beginner",
        time_to_profit="1–3 weeks",
        color="#fde68a",
    ),
    # ── 20 ─────────────────────────────────────────────────────────────────
    ModuleConfig(
        id=20, emoji="💻",
        title="AI-Powered Micro-Apps",
        subtitle="Build simple tools with AI-assisted no-code → Monetise via subscriptions",
        category="Tech & Dev",
        description=(
            "Build simple SaaS micro-tools with AI-assisted no-code platforms. "
            "Integrate OpenAI for AI-powered features and Stripe for subscriptions. "
            "Monetise with usage-based and tiered subscription pricing."
        ),
        workflow_steps=[
            "1. Use AI to identify underserved micro-niches needing simple digital tools",
            "2. Define MVP: solve exactly ONE problem extremely well",
            "3. Design UI/UX mockups with AI assistance and user story mapping",
            "4. Build with no-code: Bubble (complex), Glide (mobile), or Replit (code-based)",
            "5. Integrate OpenAI API for AI-powered features (summarise, generate, classify)",
            "6. Set up Stripe Billing for subscription tiers ($9 / $29 / $79 per month)",
            "7. Launch on Product Hunt, relevant subreddits, and Twitter/X Build in Public",
            "8. Iterate weekly based on user feedback; aim for 100 paid users in 90 days",
        ],
        tools=[
            Tool("Bubble",     "https://bubble.io",           "No-code app builder",       True),
            Tool("Glide",      "https://glideapps.com",       "No-code mobile apps",       True),
            Tool("Replit",     "https://replit.com",          "AI-assisted coding IDE",    True),
            Tool("OpenAI API", "https://platform.openai.com", "GPT-4 API integration",     False),
            Tool("Stripe",     "https://stripe.com",          "Payment & subscriptions",   True),
        ],
        revenue_range="$500 – $20,000/month",
        difficulty="Advanced",
        time_to_profit="1–3 months",
        color="#c4b5fd",
    ),
]

# ── convenience helpers ──────────────────────────────────────────────────────

MODULES_BY_ID: dict[int, ModuleConfig] = {m.id: m for m in MODULES}

CATEGORIES: dict[str, list[ModuleConfig]] = {}
for _m in MODULES:
    CATEGORIES.setdefault(_m.category, []).append(_m)
