
try: 
    from .local import *
except:
    # from .base import *

    from .production import *

# Import staging specific settings if they exist 
# (staging.py is manually placed in the settings module on the staging server)
try:
    from .staging import *
except:
    pass
