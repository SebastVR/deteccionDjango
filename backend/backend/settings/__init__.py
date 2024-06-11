with open("/run/secrets/CREDS") as f:
    import json

    credentials = json.load(f)

environment = credentials["ENVIRONMENT"]

if environment == "testing":
    from .base import *
elif environment == "local":
    from .local import *
elif environment == "dev":
    from .dev import *
else:
    from .production import *
