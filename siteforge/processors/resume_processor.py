import os
import json
from siteforge.processors.base_processor import BaseProcessor

class ResumeProcessor(BaseProcessor):
    def process(self):
        self.generate_resume()

    def generate_resume(self):
        resume_data = self.load_resume_data()
        context = {
            'resume': resume_data,
            'config': self.config
        }
        output = self.render_template('resume.html', context)
        self.write_output(os.path.join(self.config['output_dir'], 'resume.html'), output)

    def load_resume_data(self):
        resume_path = os.path.join(self.config['content_dir'], 'resume.json')
        with open(resume_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    class ResumeProcessor(BaseProcessor):
        def get_current_depth(self):
            return 1  # Resume is one level deep