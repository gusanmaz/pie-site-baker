import os
from datetime import datetime
from siteforge.processors.base_processor import BaseProcessor
from siteforge.utils import slugify

class BlogProcessor(BaseProcessor):
    def process(self):
        blog_posts = self.get_blog_posts()
        self.generate_blog_index(blog_posts)
        self.generate_blog_posts(blog_posts)
        return blog_posts

    def get_blog_posts(self):
        blog_dir = os.path.join(self.config['content_dir'], 'blog')
        blog_posts = []
        for filename in os.listdir(blog_dir):
            if filename.endswith('.md'):
                with open(os.path.join(blog_dir, filename), 'r', encoding='utf-8') as f:
                    content = f.read()
                    self.md.convert(content)
                    metadata = self.md.Meta
                    metadata['date'] = datetime.strptime(metadata['date'][0], '%Y-%m-%d')
                    metadata['title'] = metadata['title'][0]
                    metadata['author'] = metadata['author'][0]
                    metadata['url'] = f"{slugify(metadata['title'])}.html"  # Remove 'blog/' prefix
                    blog_posts.append({
                        'metadata': metadata,
                        'content': content,
                        'filename': filename
                    })
        return sorted(blog_posts, key=lambda x: x['metadata']['date'], reverse=True)

    def generate_blog_index(self, blog_posts):
        context = {
            'posts': [post['metadata'] for post in blog_posts],
            'config': self.config
        }
        output = self.render_template('blog_index.html', context)
        self.write_output(os.path.join(self.config['output_dir'], 'blog', 'index.html'), output)

    def generate_blog_posts(self, blog_posts):
        for post in blog_posts:
            context = {
                'content': self.md.convert(post['content']),
                'config': self.config,
                **post['metadata']
            }
            output = self.render_template('post.html', context)
            output_path = os.path.join(self.config['output_dir'], 'blog', f"{slugify(post['metadata']['title'])}.html")
            self.write_output(output_path, output)

    def get_current_depth(self):
        return 1  # Blog pages are always one level deep