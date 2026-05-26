
def extract_intent(prompt: str):

    text = prompt.lower()

    ambiguity = []
    unsafe = []
    features = []
    assumptions = []
    conflicts = []

    domain = "unknown"

    # ====================================
    # DOMAIN DETECTION
    # ====================================

    domains = {

        "child_rescue": [
            "child",
            "rescue",
            "missing",
            "ngo",
            "authority",
            "facial"
        ],

        "fintech": [
            "finance",
            "payment",
            "wallet",
            "portfolio",
            "trading"
        ],

        "healthcare": [
            "doctor",
            "patient",
            "hospital",
            "healthcare"
        ],

        "analytics": [
            "analytics",
            "dashboard",
            "report",
            "reports"
        ],

        "crm": [
            "crm",
            "customer",
            "customers",
            "lead",
            "leads"
        ],

        "ecommerce": [
            "ecommerce",
            "cart",
            "product",
            "products",
            "shop",
            "shopping"
        ]

    }

    scores = {}

    for app, keywords in domains.items():

        scores[app] = 0

        for word in keywords:

            if word in text:
                scores[app] += 1


    max_score = max(scores.values())

    if max_score > 0:

        domain = max(
            scores,
            key=scores.get
        )


    # ====================================
    # FEATURES
    # ====================================

    feature_words = [

        "dashboard",
        "login",
        "authentication",
        "alerts",
        "payments",
        "matching",
        "analytics"

    ]

    for feature in feature_words:

        if feature in text:

            features.append(
                feature
            )


    # ====================================
    # CONFLICTS
    # ====================================

    if (

        "login" in text

        and

        "remove authentication" in text

    ):

        conflicts.append(

            "Login requested but authentication removed"

        )


    if (

        "dashboard" in text

        and

        "remove admin" in text

    ):

        conflicts.append(

            "Dashboard requested but admin removed"

        )


    # ====================================
    # VAGUE / REJECTION LOGIC
    # ====================================

    if len(text.strip()) < 5:

        ambiguity.append(
            "Prompt too short"
        )


    if (

        domain == "unknown"

        and

        len(features) == 0

        and

        len(conflicts) == 0

    ):

        ambiguity.append(
            "No recognizable domain"
        )


    # ====================================
    # ASSUMPTIONS
    # ====================================

    assumptions.append(
        "Authentication enabled by default"
    )

    assumptions.append(
        "Default user role added"
    )

    assumptions.append(
        "Dashboard enabled"
    )

    assumptions.append(
        "Basic workflow generated"
    )


    assumptions = sorted(

        list(

            set(
                assumptions
            )

        )

    )


    risk = "standard"

    if domain == "child_rescue":

        risk = "high"


    return {

        "raw_prompt": prompt,

        "domain": domain,

        "features": features,

        "users": ["user"],

        "risk_level": risk,

        "unsafe_requests": unsafe,

        "ambiguity": ambiguity,

        "conflicts": conflicts,

        "assumptions": assumptions

    }
