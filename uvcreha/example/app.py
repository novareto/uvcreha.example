from docmanager.app import browser as application
from docmanager.app import api
from docmanager.request import Request
from horseman.response import Response


class CustomRequest(Request):
    pass


@application.routes.register('/myview')
def my_view(request: CustomRequest):
    return Response.create(body="HALLO WELT")


#@application.ui.register_slot(request=CustomRequest, name="sitecap")
#def render_slot(request, name):
#    return Response.create(body="HALLO WELT")
#

@api.subscribe('document_created')
def handleit(*args, **kwargs):
    print('I CAN SEND A MAIL FROM HERE')
