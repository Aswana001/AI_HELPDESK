from django.urls import path

from .views import (
    AllTicketsView,
    CreateTicketView,
    MyTicketsView,
    UpdateTicketStatusView,
    DashboardView
)

urlpatterns = [

    path(
        "create/",
        CreateTicketView.as_view()
    ),

    path("my-tickets/",MyTicketsView.as_view()
    ),
    path( "all/", AllTicketsView.as_view(),name="all-tickets"),
    path("<int:pk>/update-status/",UpdateTicketStatusView.as_view(),name="update-ticket-status"),
    path("dashboard/",  DashboardView.as_view(), name="dashboard")
]