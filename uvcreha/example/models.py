from docmanager import models
from docmanager.db import Document
from typing import Literal


@Document.alternatives.component('text/plain')
class SomeDocument(models.Document):

    content_type: Literal['text/plain']
    myfield: str
