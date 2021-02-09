from pydantic import BaseModel
import horseman

from reiter.form.wizard import Wizard, WizardForm
from docmanager.app import browser
from docmanager.browser.form import Form
from docmanager.browser.layout import TEMPLATES as DOCTEMPLATES


class Step1(BaseModel):
    field1: str
    field2: str


class Step2(BaseModel):
    field3: int


class Wizard(Wizard):

    session_key = 'registration_wizard'
    steps = (
        Step1,
        Step2
    )

    def conclude(self):
        print(f'I save the data: {self.data}')
        return horseman.response.redirect("/")


@browser.route("/register")
class Registration(WizardForm):
    template = DOCTEMPLATES["base_form.pt"]
    wizard = Wizard
    formclass = Form

    def GET(self):
        wizard = self.wizard(self.request)
        step = wizard.current_step
        form = self.setupForm(step)
        return dict(reqeust=self.request, form=form, wizard=wizard, error=None)

    def POST(self):
        self.request.extract()
        return self.process_action(self.request)
