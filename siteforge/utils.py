import os
import shutil
import re

def ensure_output_dir(output_dir):
    os.makedirs(output_dir, exist_ok=True)

def copy_assets(content_dir, output_dir):
    assets_src = os.path.join(content_dir, 'assets')
    assets_dst = os.path.join(output_dir, 'assets')
    if os.path.exists(assets_src):
        if os.path.exists(assets_dst):
            shutil.rmtree(assets_dst)
        shutil.copytree(assets_src, assets_dst)

def slugify(text):
    text = str(text).lower()
    return re.sub(r'[\W_]+', '-', text).strip('-')

def get_url(path):
    return path.lstrip('/')