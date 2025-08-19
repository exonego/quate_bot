# This function init "database"
def init_db():
    return {
        "user_template": {"favorites": set()},
        "users": dict()
    }