from setuptools import setup, find_packages

setup(
    name='peterpy',
    version='1.0.0',
    description='Print Elapsed TimE Running a piece of Python code ',

    # The project's main homepage.
    url='http://ribera.me',

    # Author details
    author='Javier Ribera',
    author_email='javiribera@gmail.com',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Specify the Python versions you support here. In
        # particular, ensure
        # that you indicate whether you support Python 2, Python 3
        # or both.
        'Programming Language :: Python :: 3.6',
    ],

    packages=find_packages(),
    
)


