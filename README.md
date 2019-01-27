# Image Captions and Python and Markdown, together!

Your images have `<figcaption>` elements attached.

[![travis](https://travis-ci.org/bcaller/markdown_figure_caption.svg)](https://travis-ci.org/bcaller/markdown_figure_caption)
[![PyPI version](https://badge.fury.io/py/markdown_figure_caption.svg)](https://badge.fury.io/py/markdown_figure_caption)

Very similar to [figureAltCaption](https://github.com/jdittrich/figureAltCaption). This version doesn' handle references or attributes, but does handle links inside the caption.

Behaviour is best displayed via the tests:

```python
def test_image_simple(markdown):
    s = "![The caption](http://example.com/x.png)"
    converted = markdown.convert(s)
    assert converted == '<p><figure><img alt="The caption" src="http://example.com/x.png" /><figcaption>The caption</figcaption></figure></p>'


def test_image_link_in_caption(markdown):
    s = "![The caption from [source](http://example.com)](http://example.com/x.png)"
    converted = markdown.convert(s)
    assert converted == '<p><figure><img alt="The caption from source" src="http://example.com/x.png" /><figcaption>The caption from <a href="http://example.com">source</a></figcaption></figure></p>'

```
