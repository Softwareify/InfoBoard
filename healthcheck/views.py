from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from healthcheck.services import HealthCheckService


class HealthCheckView(APIView):
    service = HealthCheckService

    def get(self, _request):
        if not HealthCheckService.health_check():
            return Response(
                {"healthy": False}, status=status.HTTP_503_SERVICE_UNAVAILABLE
            )
        return Response({"healthy": True}, status=status.HTTP_200_OK)
