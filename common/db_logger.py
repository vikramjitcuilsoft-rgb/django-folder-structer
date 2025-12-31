from django.conf import settings

def log_database_info():
    db = settings.DATABASES["default"]

    engine = db.get("ENGINE")
    name = db.get("NAME")

    print(
        f"🟢 CONNECTED DATABASE → ENGINE={engine}"
    )
