from functools import wraps
from flask import request, jsonify, abort # type: ignore

# Simple token for authentication
VALID_TOKEN = "secure-token"

def generate_token(username: str) -> str:
    return VALID_TOKEN  # In reality, generate a unique token

def authenticate(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")
        if token != VALID_TOKEN:
            abort(401, "Unauthorized")
        return f(*args, **kwargs)
    return wrapper
