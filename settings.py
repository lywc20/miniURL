import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('.') / '.env'
load_dotenv(dotenv_path)

class Config:
    MONGO_URI=os.getenv("MONGO_URI")


