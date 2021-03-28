from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.homeview, name='home'),
    path('dashboard',views.index, name='dashboard'),
    path('tools',views.tools, name='tools'),
    path('level/<str:gametype>',views.levelview, name='level'),
    path('reactiontimeone',views.reactiontimeone, name='reactiontimeone'),
    path('reactiontimetwo',views.reactiontimetwo, name='reactiontimetwo'),
    path('memoryone',views.memoryone, name='memoryone'),
    path('memorytwo',views.memorytwo, name='memorytwo'),
    path('spatialmemoryone',views.spatialmemoryone, name='spatialmemoryone'),
    path('pairedalmazeone',views.pairedalmazeone, name='pairedalmazeone'),
    path('pairedalmazetwo',views.pairedalmazetwo, name='pairedalmazetwo'),
    path('rapidvisualone',views.rapidvisualone, name='rapidvisualone'),
]