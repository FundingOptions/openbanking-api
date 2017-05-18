from setuptools import setup


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='openbanking',
    version='0.1.0',
    description='Simple wrapper for openbanking',
    long_description=readme,
    author='Jon Staley',
    author_email='jon.staley@fundingoptions.com',
    url='',
    license=license,
    py_modules=['openbanking'],
    install_requires=['requests']
)
