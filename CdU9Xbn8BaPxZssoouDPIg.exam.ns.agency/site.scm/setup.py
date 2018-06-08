from setuptools import setup, find_packages

setup(
    name='safespace',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
    ],
    package_data={
        'safespace': [
            'templates/*/*',
            'static/*/*'
        ]
    },
)
