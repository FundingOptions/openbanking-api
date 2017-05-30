from setuptools import setup


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='openbankingapi',
    version='0.1.0',
    description='Simple wrapper for openbanking',
    long_description=readme,
    author='Funding Options',
    author_email='techsupport@fundingoptions.com',
    url='',
    license=license,
    py_modules=['openbankingapi'],
    install_requires=['requests']
)
