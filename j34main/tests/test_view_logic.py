import pytest
from .. view_logic import markdown_to_html

def test_markdown_to_html():
    md_text = "# Header\n## Subhead\nparagraph text\n"
    html = markdown_to_html(md_text)
    header = "<h1>Header<"
    assert header in html
    subhead = "<h2>Subhead<"
    assert subhead in html
    parag = "<p>paragraph text<"
    assert parag in html