from docmanager.app import application
from docmanager.request import Request
from horseman.response import Response


class CustomRequest(Request):
    pass


@application.routes.register('/myview')
def my_view(request: CustomRequest):
    return Response.create(body="HALLO WELT")


@application.ui.register_slot(request=CustomRequest, name="sitecap")
def render_slot(request, name):
    return Response.create(body="HALLO WELT")
