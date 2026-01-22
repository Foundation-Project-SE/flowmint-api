from django.http import JsonResponse
from django.db import connection
from django.db.utils import OperationalError

def health_check(request):
    # Verifica respuesta desde el Servidor
    data = {
        "status": "ok",
        "service": "foundation-backend",
    }
    
    # Conexión con DB
    try:
        connection.ensure_connection()
        data["database"] = "connected"
    except OperationalError:
        data["database"] = "unavailable"
        
    return JsonResponse(data)