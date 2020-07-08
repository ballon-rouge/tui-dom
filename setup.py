#!/usr/bin/env python3
import sys
from setuptools import setup


requirements = [
    'colorama',
    "asciimatics",
]
if sys.version_info < (3, 7):
    requirements.append("dataclasses")

setup(
    name="rbs_tui_dom",
    version="1.0.0",
    description="The RBS Terminal User Interface(TUI) framework",
    packages=[
        "rbs_tui_dom",
        "rbs_tui_dom.dom",
        "rbs_tui_dom.extra",
    ],
    ext_modules=[],
    install_requires=requirements,
    extras_require={}
)
