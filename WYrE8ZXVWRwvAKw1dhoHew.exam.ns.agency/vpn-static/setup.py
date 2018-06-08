from setuptools import setup, find_packages

setup(
    name='facegood',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
    ],
    package_data={
        'facegood': [
            'templates/*/*',
            'static/*/*'
        ]
    },
)
