def generate_schema(intent: dict, system: dict):

    domain = intent["domain"]
    features = sorted(list(set(intent.get("features", []))))
    roles = sorted(list(set(system.get("roles", ["user"]))))
    entities = sorted(list(set(system.get("entities", []))))

    if "users" not in entities:
        entities.append("users")

    entities = sorted(list(set(entities)))

    # =====================================
    # DATABASE
    # =====================================

    database = []

    for entity in entities:

        fields = ["id", "created_at"]

        if entity == "users":
            fields.extend([
                "name",
                "email",
                "password",
                "role"
            ])

        elif entity == "missing_child_reports":
            fields.extend([
                "child_name",
                "age",
                "last_seen_location",
                "case_status"
            ])

        elif entity == "match_candidates":
            fields.extend([
                "report_id",
                "match_score",
                "review_status"
            ])

        elif entity == "notifications":
            fields.extend([
                "message",
                "recipient",
                "status"
            ])

        elif entity == "analytics":
            fields.extend([
                "metric_name",
                "metric_value"
            ])

        elif entity == "payments":
            fields.extend([
                "amount",
                "payment_status"
            ])

        elif entity == "subscriptions":
            fields.extend([
                "plan",
                "status"
            ])

        else:
            fields.append("name")


        database.append({

            "table_name": entity,

            "fields": sorted(
                list(
                    set(fields)
                )
            )

        })


    database = sorted(

        database,

        key=lambda x:
        x["table_name"]

    )



    # =====================================
    # API GENERATION
    # =====================================

    api=[]


    for table in database:


        table_name=table["table_name"]


        api.append({

            "route":

            f"/api/{table_name}",

            "method":"GET"

        })


        api.append({

            "route":

            f"/api/{table_name}",

            "method":"POST"

        })



    if (

        "login" in features

        or

        "authentication" in features

        or

        domain!="unknown"

    ):

        api.append({

            "route":

            "/api/login",

            "method":"POST"

        })



    api=sorted(

        api,

        key=lambda x:

        (

            x["route"],
            x["method"]

        )

    )



    # =====================================
    # UI GENERATED FROM SYSTEM DESIGN
    # =====================================

    ui=[]


    generated_pages=system.get(

        "pages",

        ["Home"]

    )



    for page in generated_pages:


        components=["Default"]



        if page=="Home":

            components=[

                "Hero",
                "Overview"

            ]


        elif page=="Login":

            components=[

                "LoginForm"

            ]


        elif page=="Dashboard":

            components=[

                "MetricCards",
                "Charts",
                "Reports"

            ]


        elif page=="Cart":

            components=[

                "CartItems",
                "Checkout"

            ]


        elif page=="Products":

            components=[

                "ProductGrid",
                "Filters"

            ]


        elif page=="Notifications":

            components=[

                "NotificationPanel"

            ]


        elif page=="Matching":

            components=[

                "MatchResults",
                "ReviewPanel"

            ]


        elif page=="Alerts":

            components=[

                "AlertCards"

            ]


        ui.append({

            "page":page,

            "components":components

        })



    ui=sorted(

        ui,

        key=lambda x:

        x["page"]

    )



    # =====================================
    # AUTH
    # =====================================

    auth={

        "enabled":True,

        "roles":roles,

        "permissions":[]

    }



    for role in roles:


        access=[

            "Home",
            "Login"

        ]


        if role=="admin":

            access.extend([

                "Dashboard",
                "Matching",
                "Alerts"

            ])


        elif role=="authority":

            access.extend([

                "Dashboard",
                "Matching",
                "Alerts"

            ])


        elif role=="ngo_worker":

            access.extend([

                "Dashboard",
                "Matching"

            ])


        elif role=="guardian":

            access.extend([

                "Dashboard",
                "Alerts"

            ])



        auth["permissions"].append({

            "role":role,

            "access":sorted(

                list(

                    set(access)

                )

            )

        })



    auth["permissions"]=sorted(

        auth["permissions"],

        key=lambda x:
        x["role"]

    )



    # =====================================
    # BUSINESS RULES
    # =====================================

    business_rules=[]



    if domain=="child_rescue":

        business_rules.extend([

            {

                "rule":

                "Sensitive child data must not be public"

            },

            {

                "rule":

                "Authority review is required before rescue escalation"

            },

            {

                "rule":

                "Human review required before facial match approval"

            }

        ])



    if (

        "payments"

        in features

        or

        domain=="fintech"

    ):

        business_rules.append({

            "rule":

            "Payment verification required"

        })



    if len(

        business_rules

    )==0:


        business_rules.append({

            "rule":

            "Role based access required"

        })



    business_rules=sorted(

        business_rules,

        key=lambda x:

        x["rule"]

    )



    # =====================================
    # FINAL OUTPUT
    # =====================================

    return{

        "app":{

            "name":domain,

            "risk":

            intent["risk_level"],

            "unsafe_requests":

            intent.get(

                "unsafe_requests",

                []

            )

        },


        "database":database,

        "api":api,

        "ui":ui,

        "auth":auth,

        "business_rules":

        business_rules

    }