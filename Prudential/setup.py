from setuptools import setup, find_packages

setup(
    name="insurance_claim",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "openai", "pydantic", "mysql-connector-python"
    ],
)
