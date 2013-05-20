from distutils.core import setup


with open("README.rst") as file:
    long_description = file.read()


setup(
    name='django-longer-user-fields',
    version='0.1.3',
    author='Yukilas',
    author_email='yukilas@gmail.com',
    packages=['longeruserfields'],
    url='http://pypi.python.org/pypi/django-longer-user-fields/',
    license='LICENSE',
    description='An app to easily provide longer fields for django User model',
    long_description=long_description,
)
