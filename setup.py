from setuptools import find_packages,setup

def get_requirements():
    pass


setup(
    name="sensor",
    version="0.0.2",
    author="madas venkata siva goud",
    author_email="madasvenkatasiva@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements(),
)