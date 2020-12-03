import horseman.response

from docmanager.app import browser as application
from docmanager.db import Document
from docmanager.browser.form import DocFormView, Form

from horseman.http import Multidict
from .models import SomeDocument
from reiter.form import trigger


@application.routes.register("/users/{username}/files/{az}/docs/{key}/edit", methods=("GET", "POST"))
class EventEditForm(DocFormView):

    title = "Form"
    description = "Bitte füllen Sie alle Details"
    action = "edit"
    model = SomeDocument

    def setupForm(self, data={}, formdata=Multidict()):
        form = Form.from_model(self.model, only=("name", "surname", "iban"))
        form.process(data=data, formdata=formdata)
        return form

    @trigger("speichern", "Speichern", css="btn btn-primary")
    def speichern(self, request, data):
        form = self.setupForm(formdata=data.form)
        if not form.validate():
            return form
        document = Document(request.db_session)
        form_data = data.form.dict()
        form_data.update(request.route.params)
        document.update(**form_data)
        return horseman.response.Response.create(302, headers={"Location": "/"})
