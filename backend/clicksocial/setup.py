from setuptools import setup

setup(
    name='clicksocial',
    packages=['clicksocial'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-restful',
        'flask-pymongo',
        'flask-cors',
        'gunicorn'
    ],
)
