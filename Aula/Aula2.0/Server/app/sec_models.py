from flask_appbuilder.security.sqla.models import User
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .models import School


class AppUser(User):
    __tablename__ = "ab_user"
    school_id = Column(Integer, ForeignKey("school.id"))
    school = relationship("School")
