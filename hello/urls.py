from django.urls import path
from . import views
urlpatterns=[
    path("",views.index, name="index"),
    path("aishwary",views.aishwary,name="aishwary"),
    path("first",views.first, name="first"),
    path("second",views.second, name="second"),
    path("third",views.third, name="third"),
    path("next",views.next, name="next"),
    #path("<str:name>",views.greetold, name="greet"),
    path("<str:name>",views.greet, name="greet")
]