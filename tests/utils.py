from __future__ import annotations

import os
from typing import Any, Callable, List, Optional, Tuple, Union


def _map(func: Callable, data: List[Any]) -> List[Any]:
    """Wrapper over python's map fucntion"""
    return [*map(func, data)]


def get_files(path, suffix: Union[Tuple[str], str] = None) -> List[str]:
    """
    Function to get all files in a directory
    Args:
        path (str): Path to directory
        suffix (Optional[Tuple[str]], optional): Suffix to filter files. Defaults to None.
    Returns:
        List[str]: List of files
    """
    fullpaths = []
    for root, _, files in os.walk(path):
        for _file in files:
            if suffix and _file.endswith(suffix):
                fullpaths.append(os.path.join(root, _file))
    return fullpaths


def get_dirs(path, suffix: Union[Tuple[str], str] = None) -> List[str]:
    return [f for f in os.listdir(path) if not os.path.isfile(f) and f.endswith(suffix)]
