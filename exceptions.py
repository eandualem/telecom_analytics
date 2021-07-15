class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class ObjectNotFound(Exception):
  """
      An exception risen when an expected object is not found
  """
  pass


class InvalidOperations(Exception):
  """
      An exception risen when attempted operation does not make sense
  """
  pass

