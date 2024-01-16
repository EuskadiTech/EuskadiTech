from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey, Table, Date
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import relationship
from flask_appbuilder.security.sqla.models import User
from flask import g

"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""


class School(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    address = Column(String(564), unique=False, nullable=True)
    notes = Column(String(564), unique=False, nullable=True)
    foodplace_id = Column(Integer, ForeignKey("foodplace.id"))
    foodplace = relationship("Foodplace", foreign_keys=[foodplace_id])

    def __repr__(self):
        return self.name


assoc_user_school = Table(
    "ab_user_school",
    Model.metadata,
    Column("id", Integer, primary_key=True),
    Column("school_id", Integer, ForeignKey("school.id")),
    Column("appuser_id", Integer, ForeignKey("ab_user.id")),
)


class AppUser(User):
    __tablename__ = "ab_user"
    schools = relationship("School", secondary=assoc_user_school, backref="AppUser")


class Classroom(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=False, nullable=False)
    notes = Column(String(564), unique=False, nullable=True)
    school_id = Column(Integer, ForeignKey("school.id"), nullable=False)
    school = relationship("School", foreign_keys=[school_id])

    def __repr__(self):
        return self.name + ", " + self.school.name

    @declared_attr
    def created_by_fk(cls):
        return Column(
            Integer, ForeignKey("ab_user.id"), default=cls.get_user_id, nullable=False
        )

    @declared_attr
    def created_by(cls):
        return relationship(
            "AppUser",
            primaryjoin="%s.created_by_fk == AppUser.id" % cls.__name__,
            enable_typechecks=False,
        )

    @classmethod
    def get_user_id(cls):
        try:
            return g.user.id
        except Exception:
            return None


class Foodplace(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=False, nullable=False)
    notes = Column(String(564), unique=False, nullable=True)
    group = Column(String(50), unique=False, nullable=True)

    def __repr__(self):
        return self.name + ", " + self.group

    @declared_attr
    def created_by_fk(cls):
        return Column(
            Integer, ForeignKey("ab_user.id"), default=cls.get_user_id, nullable=False
        )

    @declared_attr
    def created_by(cls):
        return relationship(
            "AppUser",
            primaryjoin="%s.created_by_fk == AppUser.id" % cls.__name__,
            enable_typechecks=False,
        )

    @classmethod
    def get_user_id(cls):
        try:
            return g.user.id
        except Exception:
            return None


class Foodmenu(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=False, nullable=False)
    notes = Column(String(564), unique=False, nullable=True)
    foodplace_id = Column(Integer, ForeignKey("foodplace.id"))
    foodplace = relationship("Foodplace", foreign_keys=[foodplace_id])

    def __repr__(self):
        return self.name + ", " + self.foodplace

    @declared_attr
    def created_by_fk(cls):
        return Column(
            Integer, ForeignKey("ab_user.id"), default=cls.get_user_id, nullable=False
        )

    @declared_attr
    def created_by(cls):
        return relationship(
            "AppUser",
            primaryjoin="%s.created_by_fk == AppUser.id" % cls.__name__,
            enable_typechecks=False,
        )

    @classmethod
    def get_user_id(cls):
        try:
            return g.user.id
        except Exception:
            return None


class Food(Model):
    id = Column(Integer, primary_key=True)
    foodmenu_id = Column(Integer, ForeignKey("foodmenu.id"))
    foodmenu = relationship("Foodmenu", foreign_keys=[foodmenu_id])
    date = Column(Date(), unique=False, nullable=True)
    plato1 = Column(String(50), unique=False, nullable=False)
    plato2 = Column(String(50), unique=False, nullable=False)
    plato3 = Column(String(50), unique=False, nullable=False)
    plato4 = Column(String(50), unique=False, nullable=False)

    def __repr__(self):
        return self.name + ", " + self.foodmenu.foodplace

    @declared_attr
    def created_by_fk(cls):
        return Column(
            Integer, ForeignKey("ab_user.id"), default=cls.get_user_id, nullable=False
        )

    @declared_attr
    def created_by(cls):
        return relationship(
            "AppUser",
            primaryjoin="%s.created_by_fk == AppUser.id" % cls.__name__,
            enable_typechecks=False,
        )

    @classmethod
    def get_user_id(cls):
        try:
            return g.user.id
        except Exception:
            return None


class Student(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=False, nullable=False)
    email = Column(String(100), unique=False, nullable=True)
    phone_number = Column(String(100), unique=False, nullable=True)
    classroom_id = Column(Integer, ForeignKey("classroom.id"), nullable=False)
    classroom = relationship("Classroom", foreign_keys=[classroom_id])

    def __repr__(self):
        return self.name + ", " + self.classroom

    @declared_attr
    def created_by_fk(cls):
        return Column(
            Integer, ForeignKey("ab_user.id"), default=cls.get_user_id, nullable=False
        )

    @declared_attr
    def created_by(cls):
        return relationship(
            "AppUser",
            primaryjoin="%s.created_by_fk == AppUser.id" % cls.__name__,
            enable_typechecks=False,
        )

    @classmethod
    def get_user_id(cls):
        try:
            return g.user.id
        except Exception:
            return None


class Taskgroup(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=False, nullable=False)
    classroom_id = Column(Integer, ForeignKey("classroom.id"), nullable=False)
    classroom = relationship("Classroom", foreign_keys=[classroom_id])

    def __repr__(self):
        return self.name + ", " + self.classroom

    @declared_attr
    def created_by_fk(cls):
        return Column(
            Integer, ForeignKey("ab_user.id"), default=cls.get_user_id, nullable=False
        )

    @declared_attr
    def created_by(cls):
        return relationship(
            "AppUser",
            primaryjoin="%s.created_by_fk == AppUser.id" % cls.__name__,
            enable_typechecks=False,
        )

    @classmethod
    def get_user_id(cls):
        try:
            return g.user.id
        except Exception:
            return None


class Tasktype(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=False, nullable=False)
    taskgroup_id = Column(Integer, ForeignKey("taskgroup.id"), nullable=False)
    taskgroup = relationship("Taskgroup", foreign_keys=[taskgroup_id])

    def __repr__(self):
        return self.name + ", " + self.taskgroup

    @declared_attr
    def created_by_fk(cls):
        return Column(
            Integer, ForeignKey("ab_user.id"), default=cls.get_user_id, nullable=False
        )

    @declared_attr
    def created_by(cls):
        return relationship(
            "AppUser",
            primaryjoin="%s.created_by_fk == AppUser.id" % cls.__name__,
            enable_typechecks=False,
        )

    @classmethod
    def get_user_id(cls):
        try:
            return g.user.id
        except Exception:
            return None


class Taskassign(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=False, nullable=False)
    tasktype_id = Column(Integer, ForeignKey("tasktype.id"), nullable=False)
    tasktype = relationship("Tasktype", foreign_keys=[tasktype_id])
    student_id = Column(Integer, ForeignKey("student.id"), nullable=False)
    student = relationship("Student", foreign_keys=[student_id])

    def __repr__(self):
        return self.name + ", " + self.tasktype

    @declared_attr
    def created_by_fk(cls):
        return Column(
            Integer, ForeignKey("ab_user.id"), default=cls.get_user_id, nullable=False
        )

    @declared_attr
    def created_by(cls):
        return relationship(
            "AppUser",
            primaryjoin="%s.created_by_fk == AppUser.id" % cls.__name__,
            enable_typechecks=False,
        )

    @classmethod
    def get_user_id(cls):
        try:
            return g.user.id
        except Exception:
            return None
