from docmanager.models import Document
from pydantic import BaseModel, Field


@Document.alternatives.component('account_info')
class SomeDocument(BaseModel):

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
