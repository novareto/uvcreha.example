from docmanager import models
#from docmanager.db import Document
from typing import Literal
from pydantic import BaseModel, Field


class SomeDocument(BaseModel):

    content_type: Literal['account_info']
    name: str = Field(title="Name", description="Please Provide the Name!")
    surname: str = Field(title="Surname", description="Please provide your Surname")
    iban: int = Field(title="IBAN", description="Please Provide your IBAN")
