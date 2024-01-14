from flask_appbuilder.security.sqla.manager import SecurityManager
from .models import AppUser
from .sec_views import AppUserDBModelView


class AppSecurityManager(SecurityManager):
    user_model = AppUser
    userdbmodelview = AppUserDBModelView
