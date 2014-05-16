"""
This module exports all the extensions used by PyBossa.

The objects are:
    * sentinel: for caching data, ratelimiting, etc.
    * signer: for signing emails, cookies, etc.
    * mail: for sending emails,
    * login_manager: to handle account sigin/signout
    * facebook: for Facebook signin
    * twitter: for Twitter signin
    * google: for Google signin
    * misaka: for app.long_description markdown support,
    * babel: for i18n support,
    * gravatar: for Gravatar support,
    * uploader: for file uploads support,
    * csrf: for CSRF protection

"""
import os
__all__ = ['sentinel', 'signer', 'mail', 'login_manager', 'facebook',
           'twitter', 'google', 'misaka', 'babel', 'gravatar',
           'uploader', 'csrf']
# CACHE
if os.environ.get("PYBOSSA_REDIS_CACHE_DISABLED", None) is None:
    from pybossa.sentinel import Sentinel
    sentinel = Sentinel()
else:
    sentinel = None

# Signer
from pybossa.signer import Signer
signer = Signer()

# Mail
from flask.ext.mail import Mail
mail = Mail()

# Login Manager
from flask.ext.login import LoginManager
login_manager = LoginManager()

# Toolbar
# from flask.ext.debugtoolbar import DebugToolbarExtension
# toolbar = DebugToolbarExtension()

# Social Networks
from pybossa.util import Facebook
facebook = Facebook()

from pybossa.util import Twitter
twitter = Twitter()

from pybossa.util import Google
google = Google()

# Markdown support
from flask.ext.misaka import Misaka
misaka = Misaka()

# Babel
from flask.ext.babel import Babel
babel = Babel()

# Gravatar
from flask.ext.gravatar import Gravatar
gravatar = Gravatar(size=100, rating='g', default='mm',
                    force_default=False, force_lower=False)

# Uploader
uploader = None

# CSRF protection
from flask_wtf.csrf import CsrfProtect
csrf = CsrfProtect()
