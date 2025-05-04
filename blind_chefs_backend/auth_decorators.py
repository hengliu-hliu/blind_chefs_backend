from functools import wraps
from django.http import JsonResponse
from jose import jwt, JWTError
import requests
from django.conf import settings

def jwt_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        auth = request.headers.get('Authorization')
        if not auth or not auth.startswith('Bearer '):
            return JsonResponse({'error': 'Authorization header missing or invalid'}, status=401)
        token = auth.split(' ')[1]

        try:
            unverified_header = jwt.get_unverified_header(token)
        except JWTError:
            return JsonResponse({'error': 'Invalid JWT header'}, status=401)

        jwks_url = f"https://{settings.AUTH0_DOMAIN}/.well-known/jwks.json"

        jwks = requests.get(jwks_url).json()
        rsa_key = {}
        for key in jwks["keys"]:
            if key["kid"] == unverified_header["kid"]:
                rsa_key = {
                    "kty": key["kty"],
                    "kid": key["kid"],
                    "use": key["use"],
                    "n": key["n"],
                    "e": key["e"]
                }
        if not rsa_key:
            return JsonResponse({'error': 'Appropriate key not found'}, status=401)

        try:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=settings.AUTH0_ALGORITHMS,
                audience=settings.AUTH0_API_AUDIENCE,
                issuer=f"https://{settings.AUTH0_DOMAIN}/"
            )
        except JWTError:
            return JsonResponse({'error': 'Invalid token'}, status=401)

        # Optionally attach payload to request for use in view
        request.jwt_payload = payload
        return view_func(request, *args, **kwargs)
    return _wrapped_view
