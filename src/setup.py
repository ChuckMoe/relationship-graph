from setuptools import setup, find_packages

setup(
    name="relationship_graph",
    install_requires="pluggy>=1.0",
    entry_points={"console_scripts": ["relationship_graph=mein:main"]},
    packages=find_packages(),
)