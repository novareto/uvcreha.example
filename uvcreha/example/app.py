from docmanager.app import browser
from docmanager.request import Request
from horseman.response import Response


class CustomRequest(Request):
    pass


@browser.route('/myview')
def my_view(request: CustomRequest):
    return Response.create(body="HALLO WELT")


@browser.ui.register_slot(request=CustomRequest, name="sitecap")
def render_slot(request, name):
    return Response.create(body="HALLO WELT")
