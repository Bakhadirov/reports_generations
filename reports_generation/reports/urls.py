from django.urls import path

from reports_generation.reports.api.views.reports import EventsView, Installs1View, ReportsView

urlpatterns = [
    path('events/', EventsView.as_view()),
    path('installs1/', Installs1View.as_view(),),
    path('reports_generations/', ReportsView.as_view(),),
]