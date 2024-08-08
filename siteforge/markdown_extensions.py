from markdown import Markdown
from markdown.extensions import codehilite, fenced_code, tables, toc

class MarkdownWithMath:
    def __init__(self):
        self.md = Markdown(extensions=[
            'codehilite',
            'fenced_code',
            'tables',
            'toc',
            'mdx_math'
        ], extension_configs={
            'codehilite': {
                'linenums': False,
                'guess_lang': False
            },
            'mdx_math': {
                'enable_dollar_delimiter': True
            }
        })

    def convert(self, content):
        return self.md.convert(content)