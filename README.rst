peterpy
====

Add peter's context manager around your code and it will measure how long it takes to run:

.. code:: python

    from peterpy import peter

    with peter('Running some code'):
        fib = lambda n: n if n < 2 else fib(n-1) + fib(n-2)
        fib(30)

``Running some code... DONE (took 0.590127 seconds)``

.. contents:: Table of contents
   :backlinks: top
   :local:


Installation
------------

Latest PyPI stable release
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: sh

    pip install peterpy

Latest development release on GitHub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pull and install in the current directory:

.. code:: sh

    pip install git+https://github.com/javiribera/peterpy.git@master

Usage
------------

.. code:: python

    class peter():
    """
    Context manager that will print 
    the time elapsed while executing the code inside it.
    """

        def __init__(self,
                     msg="Running",
                     erase_stdout=False,
                     erase_stderr=False):

Parameters
~~~~~~~~~~

* msg  : str, optional  
    Message to show on standard output before running.
    Default: "Running..."
* erase_stdout : bool, optional  
    Ignore everything sent to the standard output inside the context.
    Default: False
* erase_stderr : bool, optional  
    Ignore everything sent to the standard error inside the context.
    Default: False


