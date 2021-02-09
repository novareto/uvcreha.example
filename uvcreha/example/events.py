from docmanager.models import User
from docmanager.app import api, browser
from docmanager.workflow import document_workflow


@api.subscribe("document_created")
def handleit(request, username, document):
    if (user := request.database(User).fetch(username)) is not None:
        if (
            user.preferences is not None
            and user.preferences.webpush_activated
            and user.preferences.webpush_subscription
        ):
            request.app.plugins["webpush"].send(
                user.preferences.webpush_subscription, "My Message"
            )
        else:
            print(
                f"{username} does not have a webpush " f"activated {user.preferences}."
            )
    else:
        print(f"Unknown user {username}.")


@browser.subscribe("document_created")
def handleit2(*args, **kwargs):
    print("I CAN SEND A MAIL FROM HERE")


@document_workflow.subscribe("Send")
def handle_save(transition, item, request, **ns):
    print("This is AFTER SAVE")
