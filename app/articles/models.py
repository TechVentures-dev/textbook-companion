from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

class ArticleIndexPage(Page):
    max_count = 1
    parent_page_types = ['home.HomePage']
    subpage_types = ['Article']

    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
    def get_context(self, request):
        context = super().get_context(request)
        context['articles'] = Article.objects.child_of(self).live().order_by('title')
        return context
    
class Article(Page):
    parent_page_types = ['ArticleIndexPage']
    subpage_types = []

    body = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]


