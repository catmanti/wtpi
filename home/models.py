from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

class HomePage(Page):
    body = models.CharField(max_length=200)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]