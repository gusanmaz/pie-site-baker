import os
import json
from siteforge.processors.base_processor import BaseProcessor


class PageProcessor(BaseProcessor):
    def __init__(self, config):
        super().__init__(config)
        self.template_name = None

    def process(self, blog_posts):
        self.generate_pages(blog_posts)

    def generate_pages(self, blog_posts):
        index_file = os.path.join(self.config['content_dir'], 'index.md')
        if os.path.exists(index_file):
            self.generate_page(index_file, blog_posts)

    def generate_page(self, filename, blog_posts):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        html_content = self.md.convert(content)
        metadata = self.md.Meta

        with open(os.path.join(self.config['content_dir'], 'resume.json'), 'r', encoding='utf-8') as f:
            resume_data = json.load(f)

        # Prepare the latest posts data
        latest_posts = [
            {
                'title': post['metadata']['title'],
                'url': f"blog/{post['metadata']['url']}",  # Add 'blog/' prefix here for landing page
                'date': post['metadata']['date']
            } for post in blog_posts[:3]
        ]

        # Get featured projects (if available)
        featured_projects = resume_data.get('projects', [])[:3]

        context = {
            'content': html_content,
            'config': self.config,
            'resume': resume_data,
            'latest_posts': latest_posts,
            'featured_projects': featured_projects,
            **metadata
        }

        self.template_name = 'landing.html'
        output = self.render_template(self.template_name, context)
        output_path = os.path.join(self.config['output_dir'], 'index.html')
        self.write_output(output_path, output)

    def get_current_depth(self):
        if self.template_name == 'blog_index.html':
            return 1
        elif self.template_name == 'post.html':
            return 2
        else:
            return 0

    def render_template(self, template_name, context):
        self.template_name = template_name
        return super().render_template(template_name, context)