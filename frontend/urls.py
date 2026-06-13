from django.urls import path
from .views import *

urlpatterns = [

    path(
        "",
        login_page,
        name="login-page"
    ),

    path(
        "register/",
        register_page,
        name="register-page"
    ),

    path(
        "dashboard/",
        dashboard_page,
        name="dashboard-page"
    ),

    path(
        "create-ticket/",
        create_ticket_page,
        name="create-ticket-page"
    ),

    path(
        "admin-dashboard/",
        admin_dashboard_page,
        name="admin-dashboard"
    ),
    path( "register/",register_page,name="register"),

    path(
    "create-ticket/",
    create_ticket_page,
    name="create-ticket"
)
 
]