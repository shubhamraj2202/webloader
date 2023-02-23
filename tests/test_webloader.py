""" Test WebLoader"""
from __future__ import annotations

import os
import shutil
from typing import List

from tests.utils import _map, get_dirs, get_files
from webloader.webloader import WebLoader


class TestWebLoader:
    """Test Webloader"""

    def setup(self):
        self.urls = [
            "https://www.google.com/",
            "https://autify.com",
        ]

    def teardown_method(self):
        """Clean Up"""

        # Cleaning Dirs
        web_dirs: List[os.PathLike] = get_dirs(path=".", suffix=".com")
        _map(lambda dir: shutil.rmtree(dir), web_dirs)

        # Cleaning Files
        web_files: List[os.PathLike] = get_files(path=".", suffix=".html")
        _map(lambda file: os.remove(file), web_files)

    def test(self):
        for url in self.urls:
            webloader = WebLoader(url)
            filepath = webloader.save_webpage()
            assert filepath.split("/")[-1].replace(".html", "") in url
