from flask import g
from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView
from flask_appbuilder.models.filters import BaseFilter
from flask_appbuilder.models.sqla.filters import get_field_setup_query
from . import appbuilder, db
from .models import School, Classroom, Foodplace, Foodmenu, Student, Taskassign, Tasktype, Taskgroup, Food
from flask_babel import lazy_gettext as _
from flask_appbuilder.api import ModelRestApi, expose

"""
    Create your Model based REST API::

    class MyModelApi(ModelRestApi):
        datamodel = SQLAInterface(MyModel)

    appbuilder.add_api(MyModelApi)


    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(
        MyModelView,
        "My View",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    )
"""

"""
    Application wide 404 error handler
"""
class FilterInManyFunction(BaseFilter):
    name = "Filter view where field is in a list returned by a function"

    def apply(self, query, func):
        query, field = get_field_setup_query(query, self.model, self.column_name)
        return query.filter(School.id.in_(func()))

def get_user_schools():
    return set([school.id for school in g.user.schools])
    return g.user.schools



class FoodApi(ModelRestApi):
    resource_name = 'food_cal'
    datamodel = SQLAInterface(Food)
class FoodmenuApi(ModelRestApi):
    resource_name = 'food_menu'
    datamodel = SQLAInterface(Foodmenu)
class FoodplaceApi(ModelRestApi):
    resource_name = 'food_place'
    datamodel = SQLAInterface(Foodplace)

class SchoolApi(ModelRestApi):
    resource_name = 'school'
    datamodel = SQLAInterface(School)
class ClassroomApi(ModelRestApi):
    resource_name = 'classroom'
    datamodel = SQLAInterface(Classroom)
class StudentApi(ModelRestApi):
    resource_name = 'student'
    datamodel = SQLAInterface(Student)

class TaskgroupApi(ModelRestApi):
    resource_name = 'task_group'
    datamodel = SQLAInterface(Taskgroup)
class TasktypeApi(ModelRestApi):
    resource_name = 'task_type'
    datamodel = SQLAInterface(Tasktype)
class TaskassignApi(ModelRestApi):
    resource_name = 'task_assign'
    datamodel = SQLAInterface(Taskassign)


class SchoolModelView(ModelView):
    datamodel = SQLAInterface(School)

    label_columns = {"name": _("Name"), "notes": _("Notes"), "address": _("Address"), "foodplace": _("Food Place")}
    list_columns = ["name", "notes", "address", "foodplace"]

    show_fieldsets = [
        (_("Essential"), {"fields": ["name", "school"]}),
        (_("Optional"), {"fields": ["address", "foodplace"]}),
    ]
    add_columns = ["name", "notes", "address", "foodplace"]
    edit_columns = ["name", "notes", "address", "foodplace"]


class ClassroomModelView(ModelView):
    datamodel = SQLAInterface(Classroom)
    base_filters = [["school_id", FilterInManyFunction, get_user_schools]]
    label_columns = {"name": _("Name"), "notes": _("Notes"), "school": _("School")}
    list_columns = ["name", "notes", "school"]

    show_fieldsets = [
        (_("Essential"), {"fields": ["name", "school", "notes"]}),
    ]
    add_columns = ["name", "school", "notes"]
    edit_columns = ["name", "school", "notes"]


class ClassroomAdminModelView(ModelView):
    datamodel = SQLAInterface(Classroom)

    label_columns = {"name": _("Name"), "notes": _("Notes"), "school": _("School")}
    list_columns = ["name", "notes", "school"]

    show_fieldsets = [
        (_("Essential"), {"fields": ["name", "school", "notes"]}),
    ]
    add_columns = ["name", "school", "notes"]
    edit_columns = ["name", "school", "notes"]


class FoodplaceModelView(ModelView):
    datamodel = SQLAInterface(Foodplace)

    label_columns = {"name": _("Name"), "notes": _("Notes"), "group": _("Group")}
    list_columns = ["name", "notes", "group"]

    show_fieldsets = [
        (_("Essential"), {"fields": ["name", "group"]}),
        (_("Optional"), {"fields": ["notes"]}),
    ]
    add_columns = ["name", "notes", "group"]
    edit_columns = ["name", "notes", "group"]


class FoodmenuModelView(ModelView):
    datamodel = SQLAInterface(Foodmenu)

    label_columns = {
        "name": _("Name"),
        "notes": _("Notes"),
        "foodplace": _("Food Place"),
    }
    list_columns = ["name", "notes", "foodplace"]

    show_fieldsets = [
        (_("Essential"), {"fields": ["name", "foodplace"]}),
        (_("Optional"), {"fields": ["notes"]}),
    ]
    add_columns = ["name", "notes", "foodplace"]
    edit_columns = ["name", "notes", "foodplace"]

class StudentModelView(ModelView):
    datamodel = SQLAInterface(Student)

    base_filters = [["classroom.school_id", FilterInManyFunction, get_user_schools]]
    label_columns = {
        "name": _("Name"),
        "email": _("Email Address"),
        "phone_number": _("Phone number"),
        "classroom": _("Classroom"),
    }
    list_columns = ["name", "email", "phone_number", "classroom"]

    show_fieldsets = [
        (_("Essential"), {"fields": ["name", "classroom"]}),
        (_("Optional"), {"fields": ["phone_number", "email"]}),
    ]
    add_columns = ["name", "email", "phone_number", "classroom"]
    edit_columns = ["name", "email", "phone_number", "classroom"]


class TaskgroupModelView(ModelView):
    datamodel = SQLAInterface(Taskgroup)

    base_filters = [["classroom.school_id", FilterInManyFunction, get_user_schools]]
    label_columns = {
        "name": _("Name"),
        "classroom": _("Classroom"),
    }
    list_columns = ["name", "classroom"]

    show_fieldsets = [
        (_("Essential"), {"fields": ["name", "classroom"]}),
    ]
    add_columns = ["name", "classroom"]
    edit_columns = ["name", "classroom"]


class TasktypeModelView(ModelView):
    datamodel = SQLAInterface(Tasktype)

    base_filters = [["taskgroup.classroom.school.id", FilterInManyFunction, get_user_schools]]
    label_columns = {
        "name": _("Name"),
        "taskgroup": _("Task Group"),
    }
    list_columns = ["name", "taskgroup"]

    show_fieldsets = [
        (_("Essential"), {"fields": ["name", "taskgroup"]}),
    ]
    add_columns = ["name", "taskgroup"]
    edit_columns = ["name", "taskgroup"]

class TaskassignModelView(ModelView):
    datamodel = SQLAInterface(Taskassign)

    base_filters = [["tasktype.taskgroup.classroom.school_id", FilterInManyFunction, get_user_schools]]
    label_columns = {
        "name": _("Name"),
        "tasktype": _("Task Type"),
        "student": _("Student")
    }
    list_columns = ["name", "tasktype","student"]

    show_fieldsets = [
        (_("Essential"), {"fields": ["name", "tasktype","student"]}),
    ]
    add_columns = ["name", "tasktype"]
    edit_columns = ["name", "tasktype","student"]


class FoodModelView(ModelView):
    datamodel = SQLAInterface(Food)

    label_columns = {
        "date": _("Date"),
        "plato1": _("Plate 1"),
        "plato2": _("Plate 2"),
        "plato3": _("Plate 3"),
        "plato4": _("Plate 4"),
        "foodmenu": _("Food Menu"),
    }
    list_columns = ["date", "plato1", "plato2", "plato3", "plato4", "foodmenu"]

    show_fieldsets = [
        (_("Essential"), {"fields": ["date", "foodmenu"]}),
        (_("Plates"), {"fields": ["plato1", "plato2", "plato3", "plato4"]}),
    ]
    add_columns = ["date", "plato1", "plato2", "plato3", "plato4", "foodmenu"]
    edit_columns = ["date", "plato1", "plato2", "plato3", "plato4", "foodmenu"]


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )


db.create_all()

appbuilder.add_view(
    SchoolModelView,
    "List Schools",
    icon="fa-folder-open-o",
    category="Classrooms",
    category_icon="fa-school",
    label=_("List Schools"),
)
appbuilder.add_view(
    ClassroomModelView,
    "List Classrooms",
    icon="fa-school",
    category="Classrooms",
    label=_("List Classrooms"),
)
appbuilder.add_view(
    ClassroomAdminModelView,
    "List Classrooms",
    icon="fa-school",
    category="Admin",
    label=_("List Classrooms"),
)

appbuilder.add_view(
    FoodplaceModelView,
    "List Food Places",
    icon="fa-folder-open-o",
    category="Food",
    category_icon="fa-utensils",
    label=_("List Food Places"),
)
appbuilder.add_view(
    FoodmenuModelView,
    "List Food Menus",
    icon="fa-folder-open-o",
    category="Food",
    category_icon="fa-utensils",
    label=_("List Food Menus"),
)

appbuilder.add_view(
    FoodModelView,
    "Food Calendar",
    icon="fa-calendar",
    category="Food",
    category_icon="fa-utensils",
    label=_("Food Calendar"),
)

appbuilder.add_view(
    StudentModelView,
    "List Students",
    icon="fa-school",
    category="Classrooms",
    label=_("List Students"),
)

appbuilder.add_view(
    TaskassignModelView,
    "Task Calendar",
    icon="fa-school",
    category="Tasks",
    label=_("Task Calendar"),
)

appbuilder.add_view(
    TaskgroupModelView,
    "List Task Groups",
    icon="fa-school",
    category="Tasks",
    label=_("List Task Groups"),
)

appbuilder.add_view(
    TasktypeModelView,
    "List Task Types",
    icon="fa-school",
    category="Tasks",
    label=_("List Task Types"),
)
appbuilder.add_api(FoodApi)
appbuilder.add_api(FoodmenuApi)
appbuilder.add_api(FoodplaceApi)
appbuilder.add_api(SchoolApi)
appbuilder.add_api(ClassroomApi)
appbuilder.add_api(StudentApi)
appbuilder.add_api(TaskgroupApi)
appbuilder.add_api(TasktypeApi)
appbuilder.add_api(TaskassignApi)
