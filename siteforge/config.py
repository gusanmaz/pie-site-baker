import os
import yaml

def load_config():
    config_path = os.path.join('config', 'config.yaml')
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)

    # Set default values
    config.setdefault('content_dir', 'content')
    config.setdefault('output_dir', 'output')
    config.setdefault('template_dir', 'templates')
    config.setdefault('url_prefix', '/')

    return config