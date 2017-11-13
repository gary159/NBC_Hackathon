from django.conf.urls import include, url
from .views import PsBotView
urlpatterns = [
				url(r'^a5a7e87dd662e5ff2d5097d49cc06688384cc84c2e774633f5/?$', PsBotView.as_view()) 
			]