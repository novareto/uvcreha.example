
from pydantic import BaseModel
from docmanager.app import browser
from docmanager.browser.form import FormView
from uvcreha.example.app import TEMPLATES


class ExampleModel(BaseModel):

    name: str
    vorname: str



@browser.route('/example_form')
class ExampleForm(FormView):
    title = "Beispiel Formular"
    description = "Beschreibung"
    action = "Speichern"
    template = TEMPLATES['custom_form.pt']

    model = ExampleModel

