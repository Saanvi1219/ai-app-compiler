from backend.pipeline.regenerator import *


def repair_config(config, validation):

    repair_log=[]

    repaired_layers=set()

    errors=validation["errors"]


    for error in errors:

        error_type=error["type"]
        message=error["message"]


        # ===========================
        # AUTH
        # ===========================

        if (

            error_type=="permission_error"

            and

            "auth" not in repaired_layers

        ):

            roles=config["auth"].get(

                "roles",

                ["user","admin"]

            )


            if "admin" not in roles:

                roles.append(
                    "admin"
                )


            config["auth"]=(
                regenerate_auth(
                    roles
                )
            )


            repair_log.append(

                "Auth regenerated"

            )

            repaired_layers.add(
                "auth"
            )



        # ===========================
        # LOGIN API ONLY
        # ===========================

        elif(

            error_type=="logical_inconsistency"

            and

            "login API"

            in message

            and

            "api" not in repaired_layers

        ):


            login_exists=False


            for route in config["api"]:

                if route["route"]=="/api/login":

                    login_exists=True


            if not login_exists:

                config["api"].append(

                    {

                        "route":"/api/login",

                        "method":"POST"

                    }

                )


            repair_log.append(

                "Login API regenerated"

            )

            repaired_layers.add(
                "api"
            )



        # ===========================
        # BUSINESS RULES
        # ===========================

        elif(

            error_type=="missing_rule"

            and

            "rules"

            not in repaired_layers

        ):


            config["business_rules"]=[

                {

                    "rule":

                    "Default validation"

                },

                {

                    "rule":

                    "Role access required"

                }

            ]


            repair_log.append(

                "Business rules regenerated"

            )

            repaired_layers.add(
                "rules"
            )



    return{

        "config":config,

        "repair_log":repair_log

    }