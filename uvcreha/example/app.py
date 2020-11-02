from docmanager.app import application
from docmanager.request import Request
from horseman.response import reply
from functools import cached_property


class CustomRequest(Request):

    @cached_property
    def database_session(self):
        return self.app.database.new_session()


@application.routes.register('/myview')
def my_view(request: CustomRequest):
    return reply(body=u"HALLO WELT")


@application.ui.register_slot(request=CustomRequest, name="sitecap")
def render_slot(request, name):
    return reply(body=u"HALLO WELT")
