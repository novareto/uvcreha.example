from docmanager.models import Document
from typing import Literal
from pydantic import BaseModel, Field
from reiter.arango.model import Factory, arango_model


@arango_model('docs')
@Document.alternatives.component('account_info')
class SomeDocument(BaseModel):

    content_type: Literal['account_info']

    name: str = Field(
        title="Name",
        description="Please provide your name"
    )

    surname: str = Field(
        title="Surname",
        description="Please provide your surname"
    )

    iban: int = Field(
        title="IBAN",
        description="Please provide your IBAN"
    )
