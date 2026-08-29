import os
import sys
from django.apps import AppConfig
from django.conf import settings


class PollsConfig(AppConfig):
    name = 'polls'

    def ready(self):
        if not settings.DEBUG:
            return
        if "runserver" not in sys.argv:
            return
        if os.environ.get("RUN_MAIN") != "true":
            return

        from django.core.management import call_command
        call_command("seed")

