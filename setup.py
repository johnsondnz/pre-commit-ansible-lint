"""
Sets up pre-commit
"""
from datetime import datetime
from setuptools import setup, find_packages

PACKAGES = find_packages(exclude=["test*", "tests*", "testing*"])

PROJECT_NAME = "pre-commit-ansible-lint"
PROJECT_PACKAGE_NAME = "pre-commit-ansible-lint"
PROJECT_LICENSE = "MIT"
PROJECT_AUTHOR = "@johnsondnz"
PROJECT_COPYRIGHT = f"2018-{datetime.now().year}"
PROJECT_URL = "git@github.com:johnsondnz/pre-commit-ansible-lint.git"
PROJECT_EMAIL = "donaldjohnson.nz@gmail.com"
PROJECT_VERSION = "1.0.1"

REQUIRES = [
    "flake8==3.9.2",
    "six",
    "typing",
    "ansible",
    "ansible-lint",
    "netaddr",
    "jinja2",
    "logzero",
    "black==21.9b0",
]

setup(
    name=PROJECT_PACKAGE_NAME,
    version=PROJECT_VERSION,
    url=PROJECT_URL,
    author=PROJECT_AUTHOR,
    author_email=PROJECT_EMAIL,
    packages=PACKAGES,
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIRES,
    python_requires=">=3.5",
    entry_points={
        "console_scripts": [
            "ansible-lint = hooks.ansible_lint:main",
            "jinja2-lint = hooks.jinja2_lint:main",
        ]
    },
)
