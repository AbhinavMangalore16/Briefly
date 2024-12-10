import os 
from box.exceptions import BoxValueError
import yaml
from Briefly.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from typing import Any
from pathlib import Path

@ensure_annotations
def create_dirs(path_dirs: list, verbose = True):
    for path in path_dirs:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Creating directory at: {path}")
            
@ensure_annotations
def read_yaml(path: Path) -> ConfigBox:
    try:
        with open(path) as yaml_f:
            content = yaml.safe_load(yaml_f)
            logger.info(f"YaML File: {path} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YaML File is empty")
    except Exception as e:
        raise e

@ensure_annotations
def get_size(path:Path) -> str:
    size = round(os.path.getsize(path)/1024)
    return f"~ {size} KB"