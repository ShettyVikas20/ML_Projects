from setuptools import find_packages,setup


setup(
    name='mlproject',
    version=0.0.1,
    author='Vikas R Shetty',
    author_email='shettyvikas03@gmail.com',
    packages= find_packages(),
    install_requires=['pandas','numpy','seaboen']

)