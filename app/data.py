"""
Portfolio data — single source of truth.
"""

PROFILE = {
    "name": "Ammar Jawed",
    "title": "AI/ML Engineer",
    "location": "Karachi, Pakistan",
    "email": "ammarjawed.1111@gmail.com",
    "github": "https://github.com/ammar20112001",
    "linkedin": "https://linkedin.com/in/ammarjawed",
    "twitter": "https://twitter.com/ammar_20112001",
    "bio": (
        "I lead AI product development at Appedology — "
        "setting architecture, owning production deployments, and making the call on what ships and what doesn't. "
        "Three systems running in production. One model I proposed to a client, trained from messy real data, "
        "evaluated rigorously, and got approved to ship. "
        "I write the design doc before I write the code."
    ),
    "hook": "Three AI systems in production. One model I proposed, built, and got approved to ship.",
}

EXPERIENCE = [
    {
        "title": "AI/ML Engineer",
        "company": "Appedology Pvt. Ltd.",
        "location": "Karachi, Pakistan",
        "period": "Dec 2024 – Present",
        "lead": (
            "I lead AI product development across three systems: a document intelligence platform "
            "for California workers' compensation, an agentic analytics workflow used by the sales "
            "team daily, and an AI-powered medical billing system that classifies and posts payments end-to-end. "
            "I set the architecture, review code, coordinate deployments with IT, and communicate directly with clients. "
            "The biggest call I made: scrapping a working Flask/Jinja prototype and leading a full-stack migration "
            "to Vue + FastAPI when the client's scope expanded beyond what the prototype could carry — "
            "under time, budget, and developer-resource pressure, shipped in ~1 month."
        ),
        "bullets": [
            "Led full-stack migration from Flask/Jinja to Vue + FastAPI: made the architectural call when expanding "
            "CRM requirements outgrew the prototype, drove team alignment, handled all client communication and "
            "approval cycles, reviewed every PR, revamped the DB schema, and shipped to production in ~1 month "
            "under developer resource constraints. Every future integration now takes a fraction of the time.",
            "Designed the system architecture for a QME CRM platform — relational schema, layered FastAPI backend, "
            "ELT pipelines, and client-facing analytics dashboards. Led the production deployment: subdomain config, "
            "auth debugging in live environments, DB promotion from dev to staging, and QA sign-off.",
            "Built a LangGraph agentic workflow where the sales team queries complex market data in plain English. "
            "A supervisor LLM routes across SQL generation, sandboxed Python execution, and a verifier — all under "
            "explicit action spaces so the system can't hallucinate its way to an answer.",
            "Proposed an ML-based demand prediction system to the client, gathered and refined real messy data, "
            "trained an OT-based neural network with W&B logging, and evaluated it against the legacy rules engine. "
            "The model outperformed the baseline by a significant margin — approved and planned for production.",
            "Built an event-driven medical billing pipeline: file watcher → RabbitMQ → GPT-4o extraction → "
            "YAML-driven decision graph → posting API. Business rules live in YAML, not code — "
            "rule changes require zero deployments.",
        ],
    },
    {
        "title": "AI Developer (Intern)",
        "company": "Kabal Research",
        "location": "Remote",
        "period": "Feb 2024 – Jul 2024",
        "lead": None,
        "bullets": [
            "Fine-tuned BERT for text classification — 29% accuracy gain, ~4000× inference speedup over the legacy pipeline.",
            "Built NLP pipelines with T5 and Phi-3 for summarization and retrieval.",
            "Cosine-similarity clustering to detect redundant records and reduce downstream API costs.",
        ],
    },
]

PROJECTS = [
    {
        "title": "AI-Generated Video Detection — Fused Semantic & Motion Models",
        "tags": ["PyTorch DDP", "8×A100", "AWS EC2/S3", "W&B", "XCLIP", "DeMamba"],
        "summary": (
            "Near-SOTA performance on AI-generated video detection. "
            "Built from scratch on 8 A100s over multiple days."
        ),
        "highlights": [
            "Processed ~1.5 TB of video data: frame sampling, optical flow (RAFT), augmentation, integrity validation.",
            "Trained two independent models (XCLIP/DeMamba + AIGVDet) to convergence using distributed PyTorch (DDP). "
            "Managed multi-day training stability, checkpointing, and scaling on AWS EC2/S3/EBS.",
            "Designed a feature-level fusion architecture — new fusion head, gradual unfreezing, end-to-end fine-tuning.",
            "~90% validation accuracy, ~85% holdout. Comparable to near-SOTA on the benchmark.",
        ],
        "github": None,
    },
    {
        "title": 'Transformer — "Attention Is All You Need" Reproduction',
        "tags": ["PyTorch", "PyTorch Lightning", "W&B", "AWS Lambda", "Flask"],
        "summary": "Full reproduction from scratch, deployed serverlessly on AWS.",
        "highlights": [
            "Reproduced the full Transformer from scratch in vanilla PyTorch — modular, "
            "no black-box abstractions.",
            "Configurable training pipelines with PyTorch Lightning, W&B experiment tracking, "
            "and reproducible sweep scripts.",
            "Deployed inference via AWS Lambda + S3. Flask UI for testing.",
        ],
        "github": "https://github.com/ammar20112001/Attention-Is-All-You-Need--reproduced",
        "stars": 8,
    },
    {
        "title": "Spiking Neural Network + Fully Homomorphic Encryption",
        "tags": ["PyTorch", "FHE", "Privacy-Preserving ML", "LIF Neurons"],
        "summary": "Fraud detection that runs entirely on encrypted data.",
        "highlights": [
            "Rate-coded SNN with custom LIF neurons for fraud detection in financial transactions.",
            "Inference pipeline compatible with FHE — predictions run on encrypted inputs, "
            "decryptable only client-side. The server never sees plaintext.",
        ],
        "github": None,
    },
]

SKILLS = {
    "Languages": ["Python", "C/C++", "SQL"],
    "ML / AI": ["PyTorch", "PyTorch Lightning", "Transformers", "LangChain", "LangGraph", "Weights & Biases"],
    "Backend & Systems": ["FastAPI", "Flask", "RabbitMQ", "Jinja"],
    "Data / Analytics": ["Pandas", "NumPy", "Scikit-learn", "Matplotlib"],
    "Cloud & Infra": ["AWS EC2", "AWS Lambda", "AWS S3"],
}

EDUCATION = [
    {
        "degree": "Bachelor of Computer Science (In Progress)",
        "institution": "Virtual University of Pakistan",
        "period": "Nov 2022 – Nov 2026",
        "certifications": [
            "Machine Learning Specialization — Coursera",
            "Deep Learning Specialization — Coursera",
            "Stanford CS224N: NLP with Deep Learning",
            "Full Stack Deep Learning (FSDL)",
        ],
    }
]

ARTIFACTS = {

    "design_docs": [
        {
            "title": "AI Cheque Posting — Automating Medical Billing End-to-End",
            "subtitle": "Event-driven pipeline · YAML-driven decision graph · Zero-deployment rule changes",
            "date": "2025–2026",
            "status": "Production",
            "sections": [
                {
                    "heading": "The Problem",
                    "body": (
                        "Workers' compensation billing is genuinely complex. Each payment needs to be "
                        "classified — Billing, ReBilling, Appeal, Settlement, BoardRep — against a web of "
                        "insurance-specific rules, date windows, CPT code verifications, and provider contracts. "
                        "The team was doing this by hand, reading PDFs, and entering data into MedFlow. "
                        "The goal was to automate from document drop to posted payment, with human review "
                        "only for exceptions."
                    ),
                },
                {
                    "heading": "Architecture",
                    "body": (
                        "File Watcher polls a folder every 2 seconds and publishes a NewPacket event to RabbitMQ. "
                        "Consumer picks it up, routes to OpenAIExtractor, which renders the PDF to images and calls "
                        "GPT-4o with document-type-specific prompts. Extracted JSON flows into the decision graph. "
                        "Two graphs: decision_graph classifies the payment type, cheque_poster_graph executes the "
                        "posting. Both are pure YAML — nodes, edges, guards. "
                        "Every component is a Worker with its own broker client. No shared state. "
                        "All coordination via RabbitMQ events with correlation IDs."
                    ),
                },
                {
                    "heading": "The Key Design Decision",
                    "body": (
                        "Business rules are in YAML, not Python. Insurance rules, provider rules, "
                        "billing window periods, notes terms, close percentage thresholds — all external config. "
                        "When the client's billing team changes a rule, they edit a file, not a codebase. "
                        "No PR, no deployment, no regression risk from a code change. "
                        "The graph executor interprets guard conditions at runtime against the current state context. "
                        "This keeps the code stable while the business logic evolves independently."
                    ),
                },
                {
                    "heading": "What's Hard",
                    "body": (
                        "The decision graph has 15+ nodes and 30+ edges with conditional guards. "
                        "Testing it requires simulating every payment path — and the business rules "
                        "interact in non-obvious ways (e.g., the 90-day SBR window interacts with "
                        "whether a fax note exists and whether a collector is active). "
                        "EOB fallback adds another branch: Exception doesn't always mean failure — "
                        "it means try getting the Explanation of Benefits first. "
                        "The right next step is a golden test set of 100 labeled payments with "
                        "known correct classifications, run on every rules change."
                    ),
                },
            ],
        },
        {
            "title": "LangGraph Agentic Analytics — NL to Validated Answer",
            "subtitle": "Supervisor routing · Explicit action spaces · Verifier before every response",
            "date": "2025–2026",
            "status": "Production",
            "sections": [
                {
                    "heading": "The Problem",
                    "body": (
                        "The sales team needs to query complex QME market data — panel volumes by ZIP, "
                        "specialty, month; doctor office movements; competitor coverage gaps. "
                        "The schema is non-trivial and the questions often require post-processing "
                        "that SQL alone can't express. Standard text-to-SQL fails silently: "
                        "it produces plausible-looking but wrong queries, and users can't tell the difference."
                    ),
                },
                {
                    "heading": "Why a Supervisor Graph",
                    "body": (
                        "A single LLM call can't be trusted to generate correct SQL, verify it, "
                        "post-process it, and compose a response — all without hallucinating. "
                        "The solution is a state machine where a Supervisor LLM gets a compact state "
                        "snapshot and a hardcoded list of allowed next actions. It picks one. "
                        "It cannot route to actions outside that list. It cannot generate SQL itself. "
                        "Specialization forces correctness: the SQL agent knows only how to write "
                        "read-only SQL; the verifier knows only how to check domain invariants."
                    ),
                },
                {
                    "heading": "Pipeline",
                    "body": (
                        "CLARIFY (detect ambiguity, apply defaults) → PLAN (analytical plan from intent + schema) → "
                        "PROBE (derive temporal assumptions deterministically) → GENERATE_SQL → RUN_SQL → "
                        "GENERATE_CODE (deterministic Python post-processing, no IO) → RUN_CODE (sandboxed) → "
                        "VERIFY (domain invariants + LLM semantic check) → COMPOSE (text / table / chart). "
                        "Each node reads from named artifacts in shared state — never raw prior messages. "
                        "This prevents agents from misreading intermediate results."
                    ),
                },
                {
                    "heading": "What Makes It Safe",
                    "body": (
                        "The verifier runs before every response reaches the UI. "
                        "Code runs in a sandbox with no filesystem or network access. "
                        "SQL is read-only, enforced at generation time. "
                        "Cost is controlled by preferring COMPOSE over STOP — no unnecessary re-runs. "
                        "If verification fails, the graph retries with the error in context, not silently degrades."
                    ),
                },
            ],
        },
    ],

    "case_studies": [
        {
            "title": "Scrapping a Working Prototype and Leading a Full-Stack Migration Under Pressure",
            "subtitle": "Flask/Jinja → Vue + FastAPI · Architecture decision · Team lead · Client negotiation · ~1 month",
            "date": "2025–2026",
            "tags": ["Technical Leadership", "System Architecture", "Migration", "Client Communication"],
            "sections": [
                {
                    "heading": "How We Got Here",
                    "body": (
                        "The client came in with unclear requirements. The right move was to ship fast — "
                        "a Flask/Jinja prototype, a few dashboard views, get something in front of them quickly. "
                        "That's what we did. It worked. But scope expanded: CRM features, more analytical views, "
                        "AI integrations, multi-user workflows. The prototype wasn't designed for any of that. "
                        "Flask/Jinja with server-side rendering doesn't scale to a rich, interactive CRM — "
                        "every new feature would be a fight against the architecture."
                    ),
                },
                {
                    "heading": "The Decision",
                    "body": (
                        "I made the call to migrate. Full-stack: Vue on the front end, FastAPI backend, "
                        "clean API boundary between them, DB schema revamped to support the actual data model "
                        "the CRM needed. This wasn't a popular decision — it meant throwing away working code, "
                        "resetting timelines, and going back to the client to ask for more time and budget. "
                        "The alternative was continuing to bolt features onto a prototype and accruing debt "
                        "that would eventually make every future addition a multi-week ordeal."
                    ),
                },
                {
                    "heading": "What Leading It Actually Looked Like",
                    "body": (
                        "Team alignment: got every developer on the same page about the new architecture, "
                        "the rationale, and the delivery plan before a single line was written. "
                        "Client communication: drafted the case for the transition — why the prototype couldn't "
                        "carry the expanded scope, what the migration would cost in time and money, "
                        "and what we'd get on the other side. Got approval. "
                        "Execution: PR reviews on every merge, procedure reviews when patterns drifted, "
                        "DB schema decisions made with the full data model in view, not just the current sprint. "
                        "Resource shortage meant the team was small and the timeline kept shifting — "
                        "managed that reality without letting it collapse into chaos."
                    ),
                },
                {
                    "heading": "The Outcome",
                    "body": (
                        "Shipped to production in ~1 month under genuine pressure: tight timeline, limited developers, "
                        "active client with opinions. The system is now consistent and scalable — "
                        "every future feature, analytics view, or AI integration plugs into an architecture "
                        "that was actually designed for it. The prototype got us in the room; "
                        "the migration is what lets us stay there."
                    ),
                },
            ],
        },
        {
            "title": "I Proposed a Model, Trained It on Messy Real Data, and Got It Approved for Production",
            "subtitle": "On taking an idea from client pitch to evaluated, production-ready ML system",
            "date": "2025–2026",
            "tags": ["ML Evaluation", "Optimal Transport", "W&B", "Engineering Judgment"],
            "sections": [
                {
                    "heading": "The Proposal",
                    "body": (
                        "The client wanted to know which ZIP codes were the best targets for their sales team — "
                        "where panel demand was highest and QME supply was weakest. "
                        "The existing approach: eratio / 12, a simple deterministic heuristic from historical panel counts. "
                        "I proposed to the client that a learned model could do meaningfully better — "
                        "one that captured temporal trends, geographic structure, and supply-demand dynamics jointly. "
                        "They approved the experiment."
                    ),
                },
                {
                    "heading": "The Data Problem",
                    "body": (
                        "The raw data was messy: inconsistent ZIP encodings, partial month records, "
                        "mismatched specialty labels across time, and a non-obvious supply-to-demand ratio of ~2.7× "
                        "(not 3×, because not all panel slots appear in selection data). "
                        "I gathered the data, cleaned it, built the batch pkl pipeline per month-specialty pair, "
                        "and validated structural assumptions before writing a line of model code."
                    ),
                },
                {
                    "heading": "What I Built",
                    "body": (
                        "QMEOtModel: PyTorch neural network with three inputs fused into a learned transport cost matrix. "
                        "Demand (IW) encoder: MLP + ID embeddings. "
                        "Supply (QME ZIP) encoder: MLP + Transformer over 12 months of panel history per ZIP. "
                        "Cost head: combines latent similarity, geographic distance (5 distance-bucket embeddings), "
                        "and temporal signal — summed through Softplus. "
                        "OT solver: unbalanced Sinkhorn (row-constrained) — demand masses fixed, supply learned implicitly. "
                        "Full training tracked on W&B: loss curves, Spearman rank metrics, geographic residual maps."
                    ),
                },
                {
                    "heading": "The Evaluation and the Result",
                    "body": (
                        "Held out month 11. Ran inference at eps=0.03 (matching training end), "
                        "rescaled b_hat to raw panel count, and compared against b_true on "
                        "Pearson and Spearman rank correlation. "
                        "Spearman was the metric that mattered — the sales team needs rank order, not absolute counts. "
                        "Also ran geographically: scatter maps of actual, predicted, and residuals across California "
                        "ZIP codes to check for systematic bias by region. "
                        "The OT model outperformed the deterministic baseline by a significant margin. "
                        "The residual maps showed the model capturing geographic patterns the heuristic missed. "
                        "Decision: ship it. Planned for production deployment."
                    ),
                },
            ],
        },
    ],

    "runbooks": [
        {
            "title": "QME Platform — Production Deployment Runbook",
            "subtitle": "Dev → staging promotion for a live client system",
            "date": "Feb–Mar 2026",
            "sections": [
                {
                    "heading": "Before You Touch Staging",
                    "items": [
                        "Run schema diff between dev and staging. Do not proceed if there's a mismatch — apply migrations first.",
                        "Confirm all env vars are set on staging: DB URL, OAuth client IDs, SESSION_SECRET, ALLOWED_ORIGINS.",
                        "Complete QA report on dev. Document every open issue with severity before promoting.",
                        "Coordinate DB access window with IT — they control staging DB permissions.",
                    ],
                },
                {
                    "heading": "Deployment Sequence",
                    "items": [
                        "Deploy to subdomain. Confirm process starts cleanly, no import errors.",
                        "OAuth smoke test: full login flow, session creation, access to a protected route.",
                        "Validate DB connectivity from the live environment — staging DB must be reachable.",
                        "Run clustering sanity check: verify region assignments match known-correct ZIP outputs.",
                        "Spot-check analytics dashboards against values computed on dev.",
                        "Confirm audit logging is writing. Check the destination, not just that no errors occurred.",
                    ],
                },
                {
                    "heading": "Known Failure Modes",
                    "items": [
                        "Schema mismatch: staging DB lagging behind dev is the most common deployment failure. Always diff first.",
                        "OAuth in live: cookie/session config behaves differently outside localhost. Verify SESSION_SECRET and ALLOWED_ORIGINS match the live domain.",
                        "Analytics dashboard integrity: spot-check all views after every deployment — panel volume trends, ZIP-level demand maps, specialty breakdowns, doctor office movement, and competitor coverage gaps. A silent data bug in any one view will mislead the sales team without raising an error.",
                        "Data integrity gate: every schema migration, upstream data change, or ELT pipeline update must go through a QA review before staging promotion. Compare row counts, key distributions, and known-correct aggregate values against dev baselines.",
                        "Procedure update review: any change to business logic — clustering heuristics, date window calculations, specialty mappings — requires a PR with explicit before/after output comparison on a fixed sample dataset. No logic change merges without a reviewer sign-off on the diff.",
                        "File upload artifact: upstream export includes 3 stale header rows. Strip them before import.",
                    ],
                },
            ],
        },
    ],

    "postmortems": [],

    "evaluation_harnesses": [
        {
            "title": "OT Model vs. Deterministic Baseline — ZIP-Level Panel Prediction",
            "subtitle": "Proposed, trained on real data, evaluated against the legacy system — model wins, going into production",
            "date": "2025–2026",
            "sections": [
                {
                    "heading": "Context",
                    "body": (
                        "The existing system used a deterministic heuristic — eratio / 12 — "
                        "to estimate panel demand by ZIP code. I proposed to the client that a learned model "
                        "could do meaningfully better by capturing temporal trends, geographic structure, "
                        "and supply-demand dynamics that a fixed formula can't represent. "
                        "They approved the experiment. I gathered the data, cleaned it, and built the pipeline."
                    ),
                },
                {
                    "heading": "Evaluation Setup",
                    "body": (
                        "Monthly batch pkl files (one per month-specialty pair). "
                        "Hold-out: month index 11. "
                        "Inference at eps=0.03 (matching training end), b_hat rescaled to raw panel count "
                        "via actual_total / demand_total. "
                        "Baseline: eratio / 12 from the deterministic pczip table. "
                        "All training runs tracked on W&B — loss curves, rank metrics, geographic residual maps."
                    ),
                },
                {
                    "heading": "Metrics",
                    "items": [
                        "Spearman rank correlation — primary metric. Sales team needs rank order, not absolute counts.",
                        "Pearson correlation — linear agreement as secondary signal.",
                        "Residual scatter: actual panels vs. (actual − predicted) to detect systematic geographic bias.",
                        "Geographic maps: turbo colormap scatter of actual, predicted, and difference across California lat/long.",
                    ],
                },
                {
                    "heading": "Result",
                    "body": (
                        "The OT model outperformed the deterministic baseline by a significant margin on Spearman rank correlation. "
                        "Residual maps showed the model capturing geographic demand patterns the heuristic missed — "
                        "particularly in underserved ZIP clusters with high panel volume but low QME density. "
                        "Decision: ship. Planned for production deployment to replace the legacy system."
                    ),
                },
            ],
        },
    ],
}

ROADMAP = {
    "current_quarter": 1,
    "quarters": [
        {"q": 1, "title": "Engineering Baseline", "status": "in_progress"},
        {"q": 2, "title": "Reliability & Distributed Systems", "status": "pending"},
        {"q": 3, "title": "Data Engineering as Truth Engine", "status": "pending"},
        {"q": 4, "title": "Applied AI System v1 — Doc Intelligence", "status": "pending"},
        {"q": 5, "title": "LLM/RAG with Evaluation Discipline", "status": "pending"},
        {"q": 6, "title": "LLMOps/MLOps — Make It Shippable", "status": "pending"},
        {"q": 7, "title": "Security & Privacy by Design", "status": "pending"},
        {"q": 8, "title": "Solutions Architecture", "status": "pending"},
    ],
}
