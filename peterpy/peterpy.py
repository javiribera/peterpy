import time
import sys

class peter:
    """
    Context manager that will print 
    the time elapsed while executing the code inside it.
    """
        
    def __init__(self,
                 msg="Running",
                 erase_stdout=False,
                 erase_stderr=False):
        """
        Create a context manager that will print 
        the time elapsed while executing the code inside it.

        :param msg: Message to show on standard output before running.
                    Default: "Running..."
        :param erase_stdout: If True, ignore everything sent to
                             the standard output inside the context.
                             Default: False.
        :param erase_stdout: If True, ignore everything sent to
                             the standard output inside the context.
                             Default: False.
        """
        self.msg = msg
        self.erase_stdout = erase_stdout
        self.erase_stderr = erase_stderr
        self.stdout = sys.stdout
        self.stderr = sys.stderr

    def __enter__(self):
        self.t = time.clock()
        print('%s... ' % self.msg, flush=True, end='')

        # Ignore standard output inside the context
        if self.erase_stdout:
            sys.stdout = None
        if self.erase_stderr:
            sys.stderr = None

    def __exit__(self, type, value, traceback):
        elapsed_seconds = time.clock() - self.t

        print('DONE (took %4f seconds)' % elapsed_seconds, flush=True)

        # Recover standard output
        sys.stdout = self.stdout
        sys.stderr = self.stderr

