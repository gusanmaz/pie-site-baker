import os
import jinja2
import markdown
from siteforge.utils import get_url

class BaseProcessor:
    def __init__(self, config):
        self.config = config
        self.env = jinja2.Environment(loader=jinja2.FileSystemLoader(config['template_dir']))
        self.md = markdown.Markdown(extensions=['meta', 'fenced_code', 'codehilite'])

    def render_template(self, template_name, context):
        # Add current_depth to the context
        if 'current_depth' not in context:
            context['current_depth'] = self.get_current_depth()
        template = self.env.get_template(template_name)
        return template.render(**context)

    def write_output(self, output_path, content):
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)

    def get_url(self, path):
        return get_url(path)

    def get_current_depth(self):
        # Override this in child classes to return the correct depth
        return 0