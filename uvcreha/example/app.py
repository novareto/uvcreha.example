from horseman.response import Response
from docmanager.app import api
from docmanager.app import browser
from docmanager.models import User
from docmanager.request import Request


class CustomRequest(Request):
    pass


@browser.route("/myview")
def my_view(request: CustomRequest):
    return Response.create(body="HALLO WELT")


@api.subscribe("document_created")
def handleit(request, username, document):
    if (user := request.database(User).fetch(username)) is not None:
        if (user.preferences is not None and
                user.preferences.webpush_activated and
                    user.preferences.webpush_subscription):
            request.app.plugins['webpush'].send(
                user.preferences.webpush_subscription, 'My Message')
