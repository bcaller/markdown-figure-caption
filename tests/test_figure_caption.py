# coding: utf-8
import pytest
from markdown import Markdown
from markdown_figure_caption import FigureCaptionExtension


@pytest.fixture
def simple_markdown(request):
    return Markdown()


@pytest.fixture(params=[FigureCaptionExtension(), 'markdown_figure_caption'], ids=["import", "str"])
def markdown(request):
    return Markdown(extensions=[request.param])


def test_md(markdown, simple_markdown):
    s = "ab **c** d *e* fghi"
    converted = markdown.convert(s)
    assert converted == simple_markdown.convert(s)


def test_image_simple(markdown):
    s = "![The caption](http://example.com/x.png)"
    converted = markdown.convert(s)
    assert converted == '<p><figure><img alt="The caption" src="http://example.com/x.png" /><figcaption>The caption</figcaption></figure></p>'


def test_image_link_in_caption(markdown):
    s = "![The caption from [source](http://example.com)](http://example.com/x.png)"
    converted = markdown.convert(s)
    assert converted == '<p><figure><img alt="The caption from source" src="http://example.com/x.png" /><figcaption>The caption from <a href="http://example.com">source</a></figcaption></figure></p>'
