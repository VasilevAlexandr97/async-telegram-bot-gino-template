import os

API_TOKEN = os.environ["API_TOKEN"]

DATABASE = {
    "NAME": os.environ["DATABASE_NAME"],
    "USER": os.environ["DATABASE_USER"],
    "PASSWORD": os.environ["DATABASE_PASSWORD"],
    "HOST": os.environ["DATABASE_HOST"],
}

# База данных/тип postgresql, mysql
DATABASE_TYPE = "postgresql"

DATABASE_STR = ""

if DATABASE_TYPE == "postgresql":
    DATABASE_STR = f"postgresql://{DATABASE['USER']}:{DATABASE['PASSWORD']}@{DATABASE['HOST']}/{DATABASE['NAME']}"
