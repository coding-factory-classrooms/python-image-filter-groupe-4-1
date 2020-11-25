
class GaussianException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return "Error : {0}".format(self.message)
        else:
            return "Error has been raised"


raise GaussianException("GaussianBlur error, parameter number must be positive and odd ")
