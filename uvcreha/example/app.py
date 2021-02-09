from horseman.response import Response
from docmanager.app import api, browser
from docmanager.models import User
from docmanager.workflow import document_workflow
from docmanager.request import Request
from fanstatic import Resource, Library
from reiter.view.meta import View
#from docmanager.browser.layout import template
#from .views import TEMPLATES
import pathlib
from reiter.application.browser import TemplateLoader

TEMPLATES = TemplateLoader(
    str((pathlib.Path(__file__).parent / "templates").resolve()), ".pt")


library = Library("uvcreha.example", "static")
wc = Resource(library, "wc.js", bottom=True)


class CustomRequest(Request):
    pass


@browser.route("/myview")
def my_view(request):
    return Response.create(body="HALLO WELT")


@browser.route("/wc")
class WebComponent(View):
    template = TEMPLATES['wc.pt']

    def GET(self):
        wc.need()
        return dict(request=self.request)
#
#
#
#
## @browser.ui.register_slot(request=CustomRequest, name="sitecap")
## def render_slot(request, name):
###    return Response.create(body="HALLO WELT")
