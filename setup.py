from setuptools import setup


with open('README.md') as f:
    readme = f.read()

setup(
    name='openbankingapi',
    version='0.1.1',
    description='Simple wrapper for openbanking',
    long_description=readme,
    author='Funding Options',
    author_email='techsupport@fundingoptions.com',
    url='https://github.com/FundingOptions/openbanking-api',
    license='GPLv3',
    py_modules=['openbankingapi'],
    install_requires=['requests']
)
