#!/usr/bin/env python3

import http.server
import socketserver
import json

class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    
    def do_GET(self):
        """Gère les requêtes GET"""
        
        if self.path == "/":
            # Page d'accueil
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            message = "Hello, this is a simple API!"
            self.wfile.write(message.encode('utf-8'))
            
        elif self.path == "/data":
            # Endpoint pour les données JSON
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            
            json_response = json.dumps(data)
            self.wfile.write(json_response.encode('utf-8'))
            
        elif self.path == "/status":
            # Endpoint pour vérifier le statut
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            message = "OK"
            self.wfile.write(message.encode('utf-8'))
            
        else:
            # Gestion des endpoints non trouvés (404)
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            message = "Endpoint not found"
            self.wfile.write(message.encode('utf-8'))

if __name__ == "__main__":
    port = 8000
    
    with socketserver.TCPServer(("", port), SimpleAPIHandler) as httpd:
        print(f"🚀 Serveur démarré sur http://localhost:{port}")
        print("Endpoints disponibles:")
        print(f"  • http://localhost:{port}/")
        print(f"  • http://localhost:{port}/data")
        print(f"  • http://localhost:{port}/status")
        print("\nAppuyez sur Ctrl+C pour arrêter le serveur")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Serveur arrêté")
