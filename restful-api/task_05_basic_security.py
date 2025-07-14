#!/usr/bin/env python3

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (JWTManager, create_access_token, jwt_required,
                                get_jwt_identity, get_jwt)
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta

# Initialisation de l'application Flask
app = Flask(__name__)

# Configuration pour JWT
app.config['JWT_SECRET_KEY'] = 'super-secret-key-change-in-production'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

# Initialisation des extensions
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# Stockage des utilisateurs en mémoire
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# Configuration des gestionnaires d'erreurs JWT
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


# Authentification basique
@auth.verify_password
def verify_password(username, password):
    """Vérifie les identifiants pour l'authentification basique"""
    if (username in users and
            check_password_hash(users[username]['password'], password)):
        return username
    return None


@auth.error_handler
def auth_error(status):
    return jsonify({"error": "Unauthorized access"}), 401


# Routes principales
@app.route('/')
def home():
    """Page d'accueil"""
    return jsonify({
        "message": "Welcome to the Secure API",
        "endpoints": {
            "login": "POST /login",
            "basic_protected": "GET /basic-protected (Basic Auth)",
            "jwt_protected": "GET /jwt-protected (JWT)",
            "admin_only": "GET /admin-only (JWT + Admin role)"
        }
    })


# Authentification basique
@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """Route protégée par authentification basique"""
    return "Basic Auth: Access Granted"


# Authentification JWT
@app.route('/login', methods=['POST'])
def login():
    """Endpoint de connexion pour obtenir un token JWT"""
    data = request.get_json()

    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Username and password required"}), 400

    username = data['username']
    password = data['password']

    # Vérifier les identifiants
    if (username in users and
            check_password_hash(users[username]['password'], password)):
        # Créer le token avec des informations utilisateur
        additional_claims = {
            "role": users[username]['role'],
            "username": username
        }
        access_token = create_access_token(
            identity=username,
            additional_claims=additional_claims
        )

        return jsonify({
            "access_token": access_token,
            "user": {
                "username": username,
                "role": users[username]['role']
            }
        })
    else:
        return jsonify({"error": "Invalid credentials"}), 401


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """Route protégée par JWT"""
    current_user = get_jwt_identity()
    return f"JWT Auth: Access Granted for {current_user}"


@app.route('/admin-only')
@jwt_required()
def admin_only():
    """Route accessible uniquement aux administrateurs"""
    current_user = get_jwt_identity()
    claims = get_jwt()

    # Vérifier le rôle
    if claims.get('role') != 'admin':
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


# Routes additionnelles utiles
@app.route('/profile')
@jwt_required()
def profile():
    """Profil de l'utilisateur connecté"""
    current_user = get_jwt_identity()
    claims = get_jwt()

    return jsonify({
        "username": current_user,
        "role": claims.get('role'),
        "message": f"Welcome to your profile, {current_user}!"
    })


@app.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    """Rafraîchir le token JWT"""
    current_user = get_jwt_identity()
    new_token = create_access_token(identity=current_user)
    return jsonify({"access_token": new_token})


# Gestion des erreurs
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500


if __name__ == '__main__':
    print("🔐 Démarrage de l'API sécurisée...")
    print("\nComptes de test disponibles:")
    print("  • user1:password (rôle: user)")
    print("  • admin1:password (rôle: admin)")
    print("\nEndpoints:")
    print("  • POST /login : Obtenir un token JWT")
    print("  • GET  /basic-protected : Authentification basique")
    print("  • GET  /jwt-protected : Authentification JWT")
    print("  • GET  /admin-only : Accès admin uniquement")
    print("  • GET  /profile : Profil utilisateur")
    print("\nExemples de test:")
    print("  curl -u user1:password http://localhost:5000/basic-protected")
    cmd = ("curl -X POST -H 'Content-Type: application/json' "
           "-d '{\"username\":\"user1\",\"password\":\"password\"}' "
           "http://localhost:5000/login")
    print(f"  {cmd}")

    app.run(debug=True, host='0.0.0.0', port=5000)
