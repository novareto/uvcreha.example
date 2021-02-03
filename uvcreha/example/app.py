from fanstatic import Resource, Library
from horseman.response import Response
from docmanager.app import api, browser
from docmanager.models import User
from docmanager.request import Request
from .views import TEMPLATES


library = Library('uvcreha.example', 'static')
wc = Resource(library, 'wc.js', bottom=True)


class CustomRequest(Request):
    pass


@browser.route("/myview")
def my_view(request):
    return Response.create(body="HALLO WELT")


@api.subscribe("document_created")
def handleit(request, username, document):
    if (user := request.database(User).fetch(username)) is not None:
        if (user.preferences is not None and
                user.preferences.webpush_activated and
                    user.preferences.webpush_subscription):
            request.app.plugins['webpush'].send(
                user.preferences.webpush_subscription, 'My Message')
        else:
            print(f'{username} does not have a webpush '
                  f'activated {user.preferences}.')
    else:
        print(f'Unknown user {username}.')


@browser.route('/wc')
def wd_view(request: CustomRequest):
    wc.need()
    return request.app.ui.response(
        TEMPLATES["wc.pt"],
        request=request
    )
