def create_profile(username, **details):
    print(f"Username: {username}")
    for key, value in details.items():
        print(f"{key}: {value}")

create_profile("admin_01", email="admin@co.co", access="High")
