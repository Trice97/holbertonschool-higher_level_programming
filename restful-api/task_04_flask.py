#!/usr/bin/env python3

from flask import Flask, jsonify, request

# Initialisation de l'application Flask
app = Flask(__name__)

# Stockage en mémoire des utilisateurs
users = {}


@app.route('/')
def home():
    """Page d'accueil de l'API"""
    return "Welcome to the Flask API!"


@app.route('/status')
def status():
    """Endpoint pour vérifier le statut de l'API"""
    return "OK"


@app.route('/data')
def get_data():
    """Endpoint qui retourne la liste de tous les noms d'utilisateurs"""
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route('/users/<username>')
def get_user(username):
    """Endpoint pour récupérer un utilisateur spécifique"""
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Endpoint pour ajouter un nouvel utilisateur"""
    # Récupérer les données JSON de la requête
    data = request.get_json()

    # Vérifier que le username est fourni
    if not data or 'username' not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data['username']

    # Créer l'objet utilisateur complet
    user_data = {
        "username": username,
        "name": data.get('name', ''),
        "age": data.get('age', 0),
        "city": data.get('city', '')
    }

    # Ajouter l'utilisateur au dictionnaire
    users[username] = user_data

    # Retourner une confirmation avec les données de l'utilisateur
    return jsonify({
        "message": "User added",
        "user": user_data
    }), 201


# Endpoints additionnels utiles


@app.route('/users')
def get_all_users():
    """Endpoint pour récupérer tous les utilisateurs (données complètes)"""
    return jsonify(users)


@app.route('/users/<username>', methods=['PUT'])
def update_user(username):
    """Endpoint pour mettre à jour un utilisateur"""
    if username not in users:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    # Mettre à jour les champs fournis
    for key in ['name', 'age', 'city']:
        if key in data:
            users[username][key] = data[key]

    return jsonify({
        "message": "User updated",
        "user": users[username]
    })


@app.route('/users/<username>', methods=['DELETE'])
def delete_user(username):
    """Endpoint pour supprimer un utilisateur"""
    if username not in users:
        return jsonify({"error": "User not found"}), 404

    deleted_user = users.pop(username)
    return jsonify({
        "message": "User deleted",
        "user": deleted_user
    })


@app.errorhandler(404)
def not_found(error):
    """Gestion des erreurs 404"""
    return jsonify({"error": "Endpoint not found"}), 404


@app.errorhandler(500)
def internal_error(error):
    """Gestion des erreurs 500"""
    return jsonify({"error": "Internal server error"}), 500


if __name__ == '__main__':
    # Démarrage du serveur en mode debug
    print("🚀 Démarrage de l'API Flask...")
    print("Endpoints disponibles:")
    print("  • GET  / : Page d'accueil")
    print("  • GET  /status : Statut de l'API")
    print("  • GET  /data : Liste des usernames")
    print("  • GET  /users : Tous les utilisateurs")
    print("  • GET  /users/<username> : Utilisateur spécifique")
    print("  • POST /add_user : Ajouter un utilisateur")
    print("  • PUT  /users/<username> : Modifier un utilisateur")
    print("  • DELETE /users/<username> : Supprimer un utilisateur")

    app.run(debug=True, host='0.0.0.0', port=5000)
