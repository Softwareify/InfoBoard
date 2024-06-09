from django.db import connections, OperationalError


class HealthCheckService:
    @staticmethod
    def health_check() -> bool:
        for connection in connections:
            try:
                connections[connection].ensure_connection()
            except Exception as e:
                print(f"Connection error: {str(e)}")
                return False
        return True
