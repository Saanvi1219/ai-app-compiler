APP_CONFIG_SCHEMA = {
    "type": "object",
    "required": ["app", "ui", "api", "database", "auth", "business_logic"],
    "properties": {
        "app": {
            "type": "object",
            "required": ["name", "description", "assumptions"],
            "properties": {
                "name": {"type": "string"},
                "description": {"type": "string"},
                "assumptions": {
                    "type": "array",
                    "items": {"type": "string"}
                }
            }
        },
        "ui": {
            "type": "object",
            "required": ["pages"],
            "properties": {
                "pages": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "required": ["name", "route", "components", "requires_auth"],
                        "properties": {
                            "name": {"type": "string"},
                            "route": {"type": "string"},
                            "requires_auth": {"type": "boolean"},
                            "allowed_roles": {
                                "type": "array",
                                "items": {"type": "string"}
                            },
                            "components": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "required": ["type", "data_source"],
                                    "properties": {
                                        "type": {"type": "string"},
                                        "data_source": {"type": "string"}
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "api": {
            "type": "object",
            "required": ["endpoints"],
            "properties": {
                "endpoints": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "required": ["path", "method", "entity", "auth_required", "request_fields", "response_fields"],
                        "properties": {
                            "path": {"type": "string"},
                            "method": {"type": "string"},
                            "entity": {"type": "string"},
                            "auth_required": {"type": "boolean"},
                            "allowed_roles": {
                                "type": "array",
                                "items": {"type": "string"}
                            },
                            "request_fields": {
                                "type": "array",
                                "items": {"type": "string"}
                            },
                            "response_fields": {
                                "type": "array",
                                "items": {"type": "string"}
                            }
                        }
                    }
                }
            }
        },
        "database": {
            "type": "object",
            "required": ["tables"],
            "properties": {
                "tables": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "required": ["name", "fields"],
                        "properties": {
                            "name": {"type": "string"},
                            "fields": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "required": ["name", "type", "required"],
                                    "properties": {
                                        "name": {"type": "string"},
                                        "type": {"type": "string"},
                                        "required": {"type": "boolean"}
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "auth": {
            "type": "object",
            "required": ["enabled", "roles", "permissions"],
            "properties": {
                "enabled": {"type": "boolean"},
                "roles": {
                    "type": "array",
                    "items": {"type": "string"}
                },
                "permissions": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "required": ["role", "can_access"],
                        "properties": {
                            "role": {"type": "string"},
                            "can_access": {
                                "type": "array",
                                "items": {"type": "string"}
                            }
                        }
                    }
                }
            }
        },
        "business_logic": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["rule", "condition", "action"],
                "properties": {
                    "rule": {"type": "string"},
                    "condition": {"type": "string"},
                    "action": {"type": "string"}
                }
            }
        }
    }
}
