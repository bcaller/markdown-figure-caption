import re

from markdown import Extension
from markdown.preprocessors import Preprocessor


TEMPLATE = '<figure>{image_markdown}<figcaption>{caption}</figcaption></figure>'
CAPTION_RE = re.compile(r"^!\[(.*)\]\(")


class FigureCaptionProcessor(Preprocessor):
    def run(self, lines):
        new_lines = []
        for line in lines:
            stripped = line.strip()
            should_process = (
                stripped.startswith("![") and
                stripped.endswith(")") and
                "](" in stripped and
                "![" not in stripped[2:]
            )
            if should_process:
                caption = CAPTION_RE.match(stripped).group(1)
                new_lines.append(
                    TEMPLATE.format(image_markdown=stripped, caption=caption),
                )
            else:
                new_lines.append(line)
        return new_lines


class FigureCaptionExtension(Extension):
    def extendMarkdown(self, md):
        """ Add an instance of FigcaptionProcessor to BlockParser. """
        md.preprocessors.register(FigureCaptionProcessor(md.parser), 'figure-caption', 19)  # <html_block


def makeExtension(**kwargs):
    return FigureCaptionExtension(**kwargs)
