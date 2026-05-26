def simulate_runtime(config:dict):

    runtime_log=[]

    failures=[]

    execution_graph={

        "pages":[],
        "apis":[],
        "tables":[],
        "roles":[],
        "business_rules":[]

    }


    # ==================================
    # LOAD DATABASE TABLES
    # ==================================

    tables=[]

    for table in config.get("database",[]):

        tables.append(
            table["table_name"]
        )

        execution_graph["tables"].append({

            "table":
            table["table_name"],

            "status":
            "loaded"

        })


    if len(tables)==0:

        failures.append(
            "No database tables available"
        )



    # ==================================
    # LOAD API ROUTES
    # ==================================

    api_routes=[]

    system_routes=[
        "/api/login"
    ]


    for route in config.get("api",[]):

        api_routes.append(
            route["route"]
        )

        route_status="loaded"

        route_name=route["route"].lower()


        if route_name not in system_routes:

            matched_table=False

            for table in tables:

                if table.lower() in route_name:

                    matched_table=True
                    break


            if not matched_table:

                route_status="failed"

                failures.append(

                    f"API route {route['route']} has no backing database table"

                )


        execution_graph["apis"].append({

            "route":
            route["route"],

            "method":
            route["method"],

            "status":
            route_status

        })


    if len(api_routes)==0:

        failures.append(
            "No API routes registered"
        )



    # ==================================
    # LOAD UI PAGES
    # ==================================

    pages=[]


    for page in config.get("ui",[]):

        pages.append(
            page["page"]
        )

        page_status="loaded"


        if page["page"]=="Login":

            if "/api/login" not in api_routes:

                page_status="failed"

                failures.append(

                    "Login page cannot execute because /api/login is missing"

                )


        if page["page"]=="Dashboard":

            has_dashboard_api=False


            for route in api_routes:

                if (

                    "analytics" in route

                    or

                    "reports" in route

                    or

                    "audit_logs" in route

                ):

                    has_dashboard_api=True



            if not has_dashboard_api:

                page_status="warning"

                runtime_log.append(

                    "Dashboard loaded with generic data source"

                )


        execution_graph["pages"].append({

            "page":
            page["page"],

            "components":
            page.get(
                "components",
                []
            ),

            "status":
            page_status

        })



    if len(pages)==0:

        failures.append(
            "No UI pages registered"
        )



    # ==================================
    # LOAD AUTH
    # ==================================

    auth=config.get(
        "auth",
        {}
    )


    roles=auth.get(
        "roles",
        []
    )


    permissions=auth.get(
        "permissions",
        []
    )


    if len(roles)==0:

        failures.append(
            "No auth roles initialized"
        )


    if len(permissions)==0:

        failures.append(
            "No auth permissions initialized"
        )


    permission_roles=[]

    for permission in permissions:

        permission_roles.append(
            permission["role"]
        )


    for role in roles:

        role_status="loaded"

        if role not in permission_roles:

            role_status="failed"

            failures.append(

                f"Role {role} has no permission mapping"

            )


        execution_graph["roles"].append({

            "role":
            role,

            "status":
            role_status

        })



    # ==================================
    # LOAD BUSINESS RULES
    # ==================================

    business_rules=config.get(
        "business_rules",
        []
    )


    if len(business_rules)==0:

        failures.append(
            "No business rules registered"
        )


    for rule in business_rules:

        execution_graph["business_rules"].append({

            "rule":
            rule["rule"],

            "status":
            "loaded"

        })



    # ==================================
    # SMOKE TESTS
    # ==================================

    smoke_tests=[]


    smoke_tests.append({

        "test":
        "database_startup",

        "passed":
        len(tables)>0

    })


    smoke_tests.append({

        "test":
        "api_startup",

        "passed":
        len(api_routes)>0

    })


    smoke_tests.append({

        "test":
        "ui_startup",

        "passed":
        len(pages)>0

    })


    smoke_tests.append({

        "test":
        "auth_startup",

        "passed":
        len(roles)>0 and len(permissions)>0

    })


    smoke_tests.append({

        "test":
        "business_rules_startup",

        "passed":
        len(business_rules)>0

    })


    smoke_tests.append({

        "test":
        "login_flow",

        "passed":
        (
            "Login" not in pages

            or

            "/api/login" in api_routes
        )

    })


    # ==================================
    # FINAL EXECUTION STATUS
    # ==================================

    executable=(
        len(failures)==0
    )


    if executable:

        runtime_log.append(
            "Runtime startup completed successfully"
        )

    else:

        runtime_log.append(
            "Runtime startup failed"
        )



    return{

        "executable":
        executable,

        "runtime_summary":{

            "pages":
            len(pages),

            "apis":
            len(api_routes),

            "tables":
            len(tables),

            "roles":
            len(roles),

            "business_rules":
            len(business_rules)

        },

        "execution_graph":
        execution_graph,

        "smoke_tests":
        smoke_tests,

        "runtime_log":
        runtime_log,

        "failures":
        failures

    }