import os

def greet():
    app_name = os.getenv("APP_NAME", "Python Demo")
    environment = os.getenv("ENVIRONMENT", "Development")

    print(f"Application : {app_name}")
    print(f"Environment : {environment}")
    print("GitHub Actions is running successfully!")

if __name__ == "__main__":
    greet()