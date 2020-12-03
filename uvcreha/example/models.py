from docmanager import models
from docmanager.db import Document
from typing import Literal


@Document.alternatives.component('account_info')
class SomeDocument(models.Document):

    content_type: Literal['account_info']
    name: str = ''
    surname: str = ''
    iban: int = 0
