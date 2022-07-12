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
    entry_points = {
        'console_scripts': ['check-in=southwest_check_in.southwest_check_in:cli']
    },
    install_requires=[
        'async-generator==1.10',
        'attrs==21.4.0',
        'backports.zoneinfo==0.2.1',
        'certifi==2022.6.15',
        'cffi==1.15.1',
        'charset-normalizer==2.1.0',
        'click==8.1.3',
        'cryptography==37.0.4',
        'DateTime==4.5',
        'h11==0.13.0',
        'idna==3.3',
        'outcome==1.2.0',
        'pybrowsers==0.5.1',
        'pycparser==2.21',
        'pyOpenSSL==22.0.0',
        'PySocks==1.7.1',
        'python-dotenv==0.20.0',
        'pytz==2022.1',
        'pytz-deprecation-shim==0.1.0.post0',
        'requests==2.28.1',
        'selenium==4.3.0',
        'sniffio==1.2.0',
        'sortedcontainers==2.4.0',
        'trio==0.21.0',
        'trio-websocket==0.9.2',
        'tzdata==2022.1',
        'tzlocal==4.2',
        'urllib3==1.26.10',
        'webdriver-manager==3.8.0',
        'wsproto==1.1.0',
        'zope.interface==5.4.0'
    ]
)