from setuptools import setup, find_packages

setup(
    name='lighthive',
    version='0.3.3',
    packages=find_packages('.'),
    url='http://github.com/emre/lighthive',
    license='MIT',
    author='emre yilmaz',
    author_email='mail@emreyilmaz.me',
    description='A light python client to interact with the HIVE blockchain',
    install_requires=["requests", "backoff", "ecdsa", "dateutils", "httpx"],
    extras_require={
        'dev': [
            'requests_mock',
        ]
    }
)
