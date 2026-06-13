from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Ticket
from .serializers import TicketSerializer, TicketStatusSerializer
from .ai import analyze_ticket
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response

class DashboardView(APIView):

    permission_classes = [
        IsAdminUser
    ]

    def get(
        self,
        request
    ):

        return Response({

            "total_tickets":
            Ticket.objects.count(),

            "open_tickets":
            Ticket.objects.filter(
                status="open"
            ).count(),

            "in_progress_tickets":
            Ticket.objects.filter(
                status="in_progress"
            ).count(),

            "resolved_tickets":
            Ticket.objects.filter(
                status="resolved"
            ).count(),
        })
    
class AllTicketsView(
    generics.ListAPIView
):

    queryset = Ticket.objects.all()

    serializer_class = TicketSerializer

    permission_classes = [
        IsAdminUser
    ]
class CreateTicketView(
    generics.CreateAPIView
):

    serializer_class = TicketSerializer

    permission_classes = [
        IsAuthenticated
    ]

    def perform_create(
        self,
        serializer
    ):

        description = (
            serializer.validated_data[
                "description"
            ]
        )

        ai_result = (
            analyze_ticket(
                description
            )
        )

        serializer.save(
            created_by=self.request.user,
            category=ai_result[
                "category"
            ],
            ai_suggestion=ai_result[
                "suggestion"
          
            ]
        )
class MyTicketsView(
    generics.ListAPIView
):

    serializer_class = TicketSerializer

    permission_classes = [
        IsAuthenticated
    ]

    def get_queryset(self):

        return Ticket.objects.filter(
            created_by=self.request.user
        )

class UpdateTicketStatusView(
    generics.UpdateAPIView
):

    queryset = Ticket.objects.all()

    serializer_class = (
        TicketStatusSerializer
    )

    permission_classes = [
        IsAdminUser
    ]