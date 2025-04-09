import yaml
import os

def load_config():
    with open(os.path.join('configs', 'config.yaml'), 'r') as f:
        return yaml.safe_load(f)
