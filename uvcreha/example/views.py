from .app import TEMPLATES
from .models import SomeDocument
from docmanager.app import browser
from docmanager.browser.form import DocFormView, Form
from docmanager.models import Document
from docmanager.workflow import DocumentWorkflow, document_workflow
from horseman.http import Multidict
from reiter.form import trigger
from reiter.view.meta import View
import horseman.response


@browser.routes.register(
    "/users/{username}/files/{az}/docs/{key}", name="index")
class DocumentIndex(View):
    template = TEMPLATES["index.pt"]

    def GET(self):
        document = self.request.database(Document).fetch(self.request.route.params.get("key"))
        if document.state == "Inquiry":
            return horseman.response.Response.create(
                302,
                headers={
                    "Location": self.request.app.routes.url_for(
                        "event_edit", **self.request.route.params
                    )
                },
            )
        return dict(request=self.request, document=document)


@browser.routes.register(
    "/users/{username}/files/{az}/docs/{key}/edit", name="event_edit"
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
            return {
                "form": form,
                "view": self,
                "error": None,
                "path": request.route.path,
            }
        doc_data = data.form.dict()
        form_data = request.route.params
        wf = document_workflow(document, request=request)
        wf.transition_to(DocumentWorkflow.states.sent)
        binding.update(
            item=doc_data, state=DocumentWorkflow.states.sent.name, **form_data
        )
        return horseman.response.Response.create(302, headers={"Location": "/"})
