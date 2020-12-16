import horseman.response

from docmanager.app import browser as application
from docmanager.models import Document
from docmanager.browser.form import DocFormView, Form
from docmanager.request import Request
from reiter.routing.predicate_route import BranchingView, PredicateError

from horseman.http import Multidict
from .models import SomeDocument
from reiter.form import trigger


@application.routes.register("/users/{username}/files/{az}/docs/{key}", methods=["GET"], name="event_edit")
class DocumentIndex(BranchingView):
    pass


def not_state_inquiry(request):
    document = request.database(Document).fetch(
        request.route.params.get("key")
    )
    if document.state == "inquiry":
        raise PredicateError.create(400, 'Condition must be test')
    return


def state_inquiry(request):
    document = request.database(Document).fetch(
        request.route.params.get("key")
    )
    if document.state != "inquiry":
        raise PredicateError.create(400, 'Condition must be test')
    return


@DocumentIndex.register(["GET"], not_state_inquiry)
def test_branching(request: Request, *args, **kwargs):  #condition, username, az, key):
    return horseman.response.reply(200, "Yeah, i'm a test")


# @application.routes.register(
#    "/users/{username}/files/{az}/docs/{key}/edit", name="event_edit")
@DocumentIndex.register(["GET", "POST"], state_inquiry)
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
        document = request.database(BaseDocument)
        document.fetch(request.route.params.get("key"))
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
        document.update(item=doc_data, **form_data)
        return horseman.response.Response.create(302, headers={"Location": "/"})
