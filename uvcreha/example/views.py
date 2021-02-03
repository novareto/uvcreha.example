import horseman.response
import pathlib

from horseman.http import Multidict
from reiter.form import trigger
from reiter.application.browser import TemplateLoader
from docmanager.app import browser
from docmanager.models import Document
from docmanager.browser.form import DocFormView, Form
from docmanager.request import Request
from docmanager.workflow import document_workflow, DocumentWorkflow
from .models import SomeDocument


TEMPLATES = TemplateLoader(
    str((pathlib.Path(__file__).parent / "templates").resolve()), ".pt")


@browser.route(
    "/users/{username}/files/{az}/docs/{key}",
    methods=["GET"], name="event_edit"
)
def document_index(request: Request, **kwargs):
    document = request.database(Document).fetch(
        request.route.params.get("key"))
    if document.state == "inquiry":
        view = EventEditForm()
        method = getattr(view, request.method)
        return method(request)
    return request.app.ui.response(
        TEMPLATES["index.pt"],
        request=request,
        document=document
    )


@browser.route(
    "/users/{username}/files/{az}/docs/{key}/edit", name="vent_edit"
)
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
        binding = request.database(Document)
        document = binding.fetch(request.route.params.get("key"))
        form = self.setupForm(formdata=data.form)
        if not form.validate():
            return request.app.ui.response(
                self.template,
                request=request,
                form=form,
                view=self
            )

        doc_data = data.form.dict()
        form_data = request.route.params
        wf = document_workflow(document, request=request)
        wf.set_state(DocumentWorkflow.states.sent)
        binding.update(
            item=doc_data,
            state=DocumentWorkflow.states.sent.name,
            **form_data
        )
        return horseman.response.redirect("/")
