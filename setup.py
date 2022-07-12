from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
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
    python_requires='>=3.7, <4',
    packages=['southwest_check_in'],
    install_requires=[
        'click==8.1.3',
        'DateTime==4.5',
        'pytz==2022.1',
        'pytz-deprecation-shim==0.1.0.post0',
        'requests==2.28.1',
        'selenium==4.3.0',
        'tzdata==2022.1',
        'tzlocal==4.2',
        'webdriver-manager==3.8.0',
    ]
)