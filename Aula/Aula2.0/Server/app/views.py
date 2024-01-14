from flask import g
from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi
from flask_appbuilder.models.sqla.filters import get_field_setup_query
from flask_appbuilder.models.sqla.filters import FilterInFunction
from flask_appbuilder.models.filters import BaseFilter

from . import appbuilder, db
from .models import School, Classroom, Foodplace, Foodmenu
from flask_babel import lazy_gettext as _

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


def get_user_schools():
    return set([school.id for school in g.user.schools])
    return g.user.schools


class SchoolModelView(ModelView):
    datamodel = SQLAInterface(School)

    label_columns = {"name": _("Name"), "notes": _("Notes"), "address": _("Address")}
    list_columns = ["name", "notes", "address"]

    show_fieldsets = [
        ("Essential", {"fields": ["name", "school"]}),
        ("Optional", {"fields": ["address"]}),
    ]
    add_columns = ["name", "notes", "address"]
    edit_columns = ["name", "notes", "address"]


class ClassroomModelView(ModelView):
    datamodel = SQLAInterface(Classroom)
    base_filters = [["school_id", FilterInFunction, get_user_schools]]

    label_columns = {"name": _("Name"), "notes": _("Notes"), "school": _("School")}
    list_columns = ["name", "notes", "school"]

    show_fieldsets = [
        ("Essential", {"fields": ["name", "school", "notes"]}),
    ]
    add_columns = ["name", "school", "notes"]
    edit_columns = ["name", "school", "notes"]


class ClassroomAdminModelView(ModelView):
    datamodel = SQLAInterface(Classroom)

    label_columns = {"name": _("Name"), "notes": _("Notes"), "school": _("School")}
    list_columns = ["name", "notes", "school"]

    show_fieldsets = [
        ("Essential", {"fields": ["name", "school", "notes"]}),
    ]
    add_columns = ["name", "school", "notes"]
    edit_columns = ["name", "school", "notes"]


class FoodplaceModelView(ModelView):
    datamodel = SQLAInterface(Foodplace)

    label_columns = {"name": _("Name"), "notes": _("Notes"), "group": _("Group")}
    list_columns = ["name", "notes", "group"]

    show_fieldsets = [
        ("Essential", {"fields": ["name", "group"]}),
        ("Optional", {"fields": ["notes"]}),
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
        ("Essential", {"fields": ["name", "foodplace"]}),
        ("Optional", {"fields": ["notes"]}),
    ]
    add_columns = ["name", "notes", "foodplace"]
    edit_columns = ["name", "notes", "foodplace"]


class SchoolView(ModelView):
    datamodel = SQLAInterface(School)
    related_views = [SchoolModelView]


class ClassroomView(ModelView):
    datamodel = SQLAInterface(Classroom)
    related_views = [ClassroomModelView]


class ClassroomAdminView(ModelView):
    datamodel = SQLAInterface(Classroom)
    related_views = [ClassroomModelView]


class FoodplaceView(ModelView):
    datamodel = SQLAInterface(Foodplace)
    related_views = [FoodplaceModelView]


class FoodmenuView(ModelView):
    datamodel = SQLAInterface(Foodmenu)
    related_views = [FoodmenuModelView]


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
    "List All Classrooms",
    icon="fa-school",
    category="Classrooms",
    label=_("List All Classrooms"),
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
