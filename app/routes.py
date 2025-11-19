from flask import Blueprint, request, jsonify
from .storage import USERS, generate_id

bp = Blueprint("api", __name__)

@bp.get("/health")
def health():
    return {"status": "ok"}, 200

# Create
@bp.post("/users")
def create_user():
    data = request.get_json(silent=True) or {}
    # Basic validation
    name = data.get("name")
    email = data.get("email")
    if not name or not email:
        return {"error": "name and email are required"}, 400

    # Uniqueness check
    if any(u.get("email") == email for u in USERS.values()):
        return {"error": "email already exists"}, 409

    user_id = generate_id()
    USERS[user_id] = {
        "id": user_id,
        "name": name,
        "email": email,
        "age": data.get("age"),
        "role": data.get("role", "user"),
    }
    return USERS[user_id], 201

# Read all (with simple pagination)
@bp.get("/users")
def list_users():
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 10))
    items = list(USERS.values())
    start = (page - 1) * per_page
    end = start + per_page
    return {
        "items": items[start:end],
        "page": page,
        "per_page": per_page,
        "total": len(items),
    }, 200

# Read one
@bp.get("/users/<user_id>")
def get_user(user_id):
    user = USERS.get(user_id)
    if not user:
        return {"error": "user not found"}, 404
    return user, 200

# Update (full or partial)
@bp.put("/users/<user_id>")
@bp.patch("/users/<user_id>")
def update_user(user_id):
    user = USERS.get(user_id)
    if not user:
        return {"error": "user not found"}, 404

    data = request.get_json(silent=True) or {}
    # Optional: forbid email conflicts
    new_email = data.get("email")
    if new_email and any(u.get("email") == new_email and u["id"] != user_id for u in USERS.values()):
        return {"error": "email already exists"}, 409

    user["name"] = data.get("name", user["name"])
    user["email"] = data.get("email", user["email"])
    user["age"] = data.get("age", user.get("age"))
    user["role"] = data.get("role", user.get("role", "user"))
    return user, 200

# Delete
@bp.delete("/users/<user_id>")
def delete_user(user_id):
    user = USERS.pop(user_id, None)
    if not user:
        return {"error": "user not found"}, 404
    return user, 200
