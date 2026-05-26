def regenerate_auth(roles):

    permissions=[]

    for role in roles:

        access=["Home"]

        if role=="admin":
            access.extend([
                "Dashboard",
                "Alerts",
                "Matching"
            ])

        permissions.append({

            "role":role,
            "access":access

        })

    return{

        "enabled":True,
        "roles":roles,
        "permissions":permissions

    }



def regenerate_api(database):

    routes=[]

    for table in database:

        name=table["table_name"]

        routes.extend([

            {
                "route":f"/api/{name}",
                "method":"GET"
            },

            {
                "route":f"/api/{name}",
                "method":"POST"
            }

        ])

    return routes



def regenerate_ui(api):

    pages=[

        {
            "page":"Home",
            "components":["Hero"]
        }

    ]


    route_names=[

        x["route"]

        for x in api

    ]


    if "/api/login" in route_names:

        pages.append({

            "page":"Login",
            "components":[
                "LoginForm"
            ]

        })

    return pages