from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

setup(
    name='openbankingapi',
    version='0.1.5post1',
    description='Simple wrapper for openbanking',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Funding Options',
    author_email='techsupport@fundingoptions.com',
    url='https://github.com/FundingOptions/openbanking-api',
    license='GPLv3',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['requests']
)
