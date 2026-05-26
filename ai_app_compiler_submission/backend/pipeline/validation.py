def validate_config(config:dict):

    errors=[]

    # ====================================
    # INVALID JSON
    # ====================================

    if not isinstance(config,dict):

        return{

            "valid":False,

            "errors":[

                {

                    "type":"invalid_json",
                    "message":"Expected JSON object"

                }

            ]

        }



    # ====================================
    # ROOT CONTRACT
    # ====================================

    allowed_root=[

        "app",
        "database",
        "api",
        "ui",
        "auth",
        "business_rules"

    ]


    required_root=[

        "app",
        "database",
        "api",
        "ui",
        "auth",
        "business_rules"

    ]



    # ====================================
    # HALLUCINATED FIELDS
    # ====================================

    for field in config.keys():

        if field not in allowed_root:

            errors.append({

                "type":"hallucinated_field",
                "message":f"{field} unexpected"

            })



    # ====================================
    # MISSING KEYS
    # ====================================

    for field in required_root:

        if field not in config:

            errors.append({

                "type":"missing_key",
                "message":f"{field} missing"

            })



    if errors:

        return{

            "valid":False,
            "errors":errors

        }



    # ====================================
    # ROOT TYPE SAFETY
    # ====================================

    type_contract={

        "app":dict,
        "database":list,
        "api":list,
        "ui":list,
        "auth":dict,
        "business_rules":list

    }


    for key,expected in type_contract.items():

        if not isinstance(

            config[key],
            expected

        ):

            errors.append({

                "type":"type_error",
                "message":f"{key} should be {expected.__name__}"

            })



    # ====================================
    # DATABASE CHECKS
    # ====================================

    database_tables=[]
    database_fields=[]


    for table in config["database"]:


        if "table_name" not in table:

            errors.append({

                "type":"schema_mismatch",
                "message":"table_name missing"

            })

            continue


        if "fields" not in table:

            errors.append({

                "type":"schema_mismatch",
                "message":"fields missing"

            })

            continue


        database_tables.append(

            table["table_name"]

        )


        database_fields.extend(

            table["fields"]

        )



    # ====================================
    # API CHECKS
    # ====================================

    system_routes=[

        "/api/login"

    ]


    for route in config["api"]:


        if "route" not in route:

            errors.append({

                "type":"schema_mismatch",
                "message":"route missing"

            })

            continue


        if "method" not in route:

            errors.append({

                "type":"schema_mismatch",
                "message":"method missing"

            })

            continue


        route_name=route["route"].lower()


        # Ignore internal routes

        if route_name in system_routes:

            continue


        found=False


        for table in database_tables:

            if table.lower() in route_name:

                found=True
                break


        if not found:

            errors.append({

                "type":"logical_inconsistency",

                "message":

                f"{route_name} has no DB mapping"

            })



    # ====================================
    # UI ↔ API
    # ====================================

    pages=[]


    for page in config["ui"]:

        pages.append(

            page["page"]

        )


    if "Login" in pages:


        login_exists=False


        for route in config["api"]:

            if route["route"]=="/api/login":

                login_exists=True


        if not login_exists:

            errors.append({

                "type":"logical_inconsistency",

                "message":

                "Login page without login API"

            })



    # ====================================
    # AUTH ↔ UI
    # ====================================

    roles=config["auth"].get(
        "roles",
        []
    )


    if(

        "Dashboard" in pages

        and

        "admin" not in roles

    ):

        errors.append({

            "type":"permission_error",

            "message":

            "Dashboard requires admin"

        })



    # ====================================
    # SECURITY
    # ====================================

    if(

        "unsafe_requests"

        in config["app"]

        and

        len(

            config["app"]["unsafe_requests"]

        )>0

    ):

        errors.append({

            "type":"security_violation",

            "message":

            "Unsafe behavior requested"

        })



    # ====================================
    # BUSINESS RULES
    # ====================================

    if len(

        config["business_rules"]

    )==0:

        errors.append({

            "type":"missing_rule",

            "message":

            "No business rules found"

        })



    return{

        "valid":

        len(errors)==0,

        "errors":errors

    }