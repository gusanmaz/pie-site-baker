import os
from siteforge.processors.blog_processor import BlogProcessor
from siteforge.processors.page_processor import PageProcessor
from siteforge.processors.resume_processor import ResumeProcessor
from siteforge.utils import copy_assets, ensure_output_dir

def generate_site(config):
    ensure_output_dir(config['output_dir'])
    copy_assets(config['content_dir'], config['output_dir'])

    blog_processor = BlogProcessor(config)
    page_processor = PageProcessor(config)
    resume_processor = ResumeProcessor(config)

    blog_posts = blog_processor.process()
    page_processor.process(blog_posts)
    resume_processor.process()

    print("Site generated successfully!")