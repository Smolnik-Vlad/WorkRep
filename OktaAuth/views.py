from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from OktaAuth.serializers import UserDataLogInSerializer
from OktaAuth.services.OktaService import OktaService


# Create your views here.
class OktaAuthViewSet(viewsets.GenericViewSet):
    http_method_names = ('get', 'post')
    serializer_class = UserDataLogInSerializer

    @action(methods=['post'], detail=False)
    def login_for_session_token(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            okta_service = OktaService()
            session_token_json = okta_service.get_session_token_for_user(serializer.validated_data['username'],
                                                                         serializer.validated_data['password'])
            return Response(session_token_json)

    @action(methods=['post'], detail=False)
    def login_for_bearer_token(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            okta_service = OktaService()
            bearer_token_json = okta_service.get_bearer_token_for_user(serializer.validated_data['username'],
                                                                       serializer.validated_data['password'])
            return Response(bearer_token_json)
