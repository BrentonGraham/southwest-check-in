import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='southwest-check-in',
    version='0.0.1',
    author='Brenton Graham',
    author_email='bmgraham54@gmail.com',
    description='Southwest check-in automation tool',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/BrentonGraham/southwest-check-in',
    project_urls = {
        "Bug Tracker": "https://github.com/BrentonGraham/southwest-check-in/issues"
    },
    license='MIT',
    packages=['southwest_check_in'],
    install_requires=['requests'],
)