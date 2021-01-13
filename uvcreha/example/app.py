from horseman.response import Response
from docmanager.app import api
from docmanager.models import User
from docmanager.request import Request
from reiter.application.app import Blueprint
from fanstatic import Resource, Library
from docmanager.browser.layout import template
from .views import TEMPLATES
from docmanager.app import api, browser
from docmanager.models import User


event_bp = Blueprint(name="event_blueprint")


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


library = Library('uvcreha.example', 'static')

wc = Resource(library, 'wc.js', bottom=True)


@browser.route('/wc')
@template(TEMPLATES["wc.pt"], layout_name="default", raw=False)
def wd_view(request: CustomRequest):
    wc.need()
    return dict(request=request)
