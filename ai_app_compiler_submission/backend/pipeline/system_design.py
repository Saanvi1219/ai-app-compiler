def design_system(intent:dict):

    text=intent["raw_prompt"].lower()

    domain=intent["domain"]

    roles=["user"]

    pages=["Home"]

    entities=[]

    flows=[]


    # ==================================
    # ROLE EXTRACTION
    # ==================================

    role_keywords={

        "admin":[
            "admin"
        ],

        "authority":[
            "authority"
        ],

        "ngo_worker":[
            "ngo",
            "ngo worker",
            "ngo workers"
        ],

        "guardian":[
            "guardian",
            "guardians"
        ],

        "doctor":[
            "doctor",
            "doctors"
        ],

        "patient":[
            "patient",
            "patients"
        ]

    }


    for role,words in role_keywords.items():

        for word in words:

            if word in text:

                roles.append(role)
                break


    # dashboard always gets admin

    if "dashboard" in text:

        roles.append("admin")


    roles=sorted(
        list(
            set(
                roles
            )
        )
    )


    # ==================================
    # PAGE GENERATION
    # ==================================

    pages.append("Login")


    if "dashboard" in text:

        pages.append(
            "Dashboard"
        )


    if (

        "cart" in text

        or

        "shopping" in text

    ):

        pages.append(
            "Cart"
        )


    if "product" in text:

        pages.append(
            "Products"
        )


    if "notification" in text:

        pages.append(
            "Notifications"
        )


    if (

        "facial" in text

        or

        "matching" in text

    ):

        pages.append(
            "Matching"
        )


    if "alert" in text:

        pages.append(
            "Alerts"
        )


    pages=sorted(
        list(
            set(
                pages
            )
        )
    )


    # ==================================
    # ENTITY GENERATION
    # ==================================

    entities=["users"]


    entity_words={

        "products":"product",
        "cart":"cart",
        "payments":"payment",
        "notifications":"notification",
        "analytics":"analytics",
        "missing_child_reports":"child",
        "match_candidates":"match"

    }


    for entity,keyword in entity_words.items():

        if keyword in text:

            entities.append(
                entity
            )


    entities=sorted(
        list(
            set(
                entities
            )
        )
    )


    # ==================================
    # FLOWS
    # ==================================

    flows.append(
        "authentication_flow"
    )


    if "dashboard" in text:

        flows.append(
            "dashboard_flow"
        )


    if "payment" in text:

        flows.append(
            "payment_flow"
        )


    if "matching" in text:

        flows.append(
            "matching_flow"
        )


    flows=sorted(
        list(
            set(
                flows
            )
        )
    )


    return{

        "architecture":"modular",

        "roles":roles,

        "pages":pages,

        "entities":entities,

        "flows":flows

    }