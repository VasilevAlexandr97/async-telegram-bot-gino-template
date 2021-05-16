import os
from dotenv import load_dotenv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
load_dotenv(dotenv_path=BASE_DIR)

API_TOKEN = os.getenv("API_TOKEN")

DATABASE = {
    "NAME": os.getenv("DATABASE_NAME"),
    "USER": os.getenv("DATABASE_USER"),
    "PASSWORD": os.getenv("DATABASE_PASSWORD"),
    "HOST": os.getenv("DATABASE_HOST"),
}

# База данных/тип postgresql, mysql
DATABASE_TYPE = "postgresql"
DATABASE_STR = ""

if DATABASE_TYPE == "postgresql":
    DATABASE_STR = (
        f"postgresql://{DATABASE['USER']}:{DATABASE['PASSWORD']}"
        f"@{DATABASE['HOST']}/{DATABASE['NAME']}"
    )



