from django.shortcuts import render


def login_page(request):
    return render(request, "login.html")


def register_page(request):
    return render(request, "register.html")


def dashboard_page(request):
    return render(request, "dashboard.html")


def create_ticket_page(request):
    return render(request, "create_ticket.html")

def register_page(request):
    return render(request, "register.html")
    
def create_ticket_page(request):
    return render(
        request,
        "create_ticket.html"
    )
def admin_dashboard_page(request):
    return render(
        request,
        "admin_dashboard.html"
    )
