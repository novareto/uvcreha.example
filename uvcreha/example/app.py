from docmanager.app import browser
from docmanager.app import api
from docmanager.request import Request
from horseman.response import Response


class CustomRequest(Request):
    pass


@browser.route("/myview")
def my_view(request: CustomRequest):
    return Response.create(body="HALLO WELT")


@api.subscribe("document_created")
def handleit(*args, **kwargs):
    print("I CAN SEND A MAIL FROM HERE")


# @browser.ui.register_slot(request=CustomRequest, name="sitecap")
# def render_slot(request, name):
#    return Response.create(body="HALLO WELT")
