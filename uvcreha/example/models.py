from docmanager import models
#from docmanager.db import Document
from typing import Literal


class SomeDocument(models.Document):

    content_type: Literal['account_info']
    name: str = ''
    surname: str = ''
    iban: int = 0
