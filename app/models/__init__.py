"""
These imports enable us to make all defined models members of the models
module (as opposed to just their python files)
"""

from .user import *  # noqa
# from .miscellaneous import *  # noqa
from .restaurant import *
from .table import *
from .booking import *
#from .category import *
#from .billing import *
#from .menu import *
# from .order import *
from .schemas import *
