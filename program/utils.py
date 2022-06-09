import yaml
from pathlib import Path
from typing import Dict, Any

def get_config(config_path: Path = 'config.yml') -> Dict[str, Any]:
    """Reads config file into dictionary.

    Args:
        config_path (Path): Config path.

    Returns:
        Dict[str, Any]: Dictionary with
    """
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.full_load(f.read())


if __name__ == '__main__':
    v = get_config('config.yml')
    print(v['api']['api_url'].format('derek','sasthav'))