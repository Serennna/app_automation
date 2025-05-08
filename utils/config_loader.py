import yaml
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def load_config():
    with open(os.path.join(BASE_DIR, 'configs', 'config.yaml'), 'r') as f:
        return yaml.safe_load(f)
