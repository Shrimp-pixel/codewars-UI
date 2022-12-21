import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class User:
    email: str = os.getenv('CODEWARS_EMAIL')
    username: str = os.getenv('CODEWARS_LOGIN')
    password: str = os.getenv('CODEWARS_PASSWORD')


newUser = User()
