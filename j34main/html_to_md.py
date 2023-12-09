from . models import Content
from markdownify import markdownify


def convert_all_to_markdown():
    articles = Content.objects.all()
    for article in articles:
        article.content = markdownify(article.content, heading_style="atx")
        article.teaser = markdownify(article.teaser, heading_style="atx")
        print(f"Converting Content and Teaser for {article.title} to markdown")
        article.save()