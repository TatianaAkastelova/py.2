import sys
import this

from random import choice

from django.conf import settings
from django.core.management import execute_from_command_line
from django.http import HttpResponse
from django.urls import path


settings.configure(
    ROOT_URLCONF=__name__,
    DEBUG=True,
    SECRET_KEY='secret'
)

text = ''.join(this.d.get(c, c) for c in this.s)
title, _, *quotes = text.splitlines()


template = """
<!DOCTYPE html>
<html>
<head>
 <title>{title}</title>
</head>
<body style="color:#FAD946; background-color:#90E156">
 <h1><center>{quote}</center></h1>
</body>
</html>
"""


def hello(request):
    return HttpResponse(template.format(title=title, quote=choice(quotes)))


urlpatterns = [
    path('', hello)
]


execute_from_command_line(sys.argv)