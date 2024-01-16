from rest_framework import routers

from OktaAuth.views import OktaAuthViewSet

Okta_router = routers.SimpleRouter()
Okta_router.register('okta', OktaAuthViewSet, basename='OktaAuth')
