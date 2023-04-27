import http.server
server = http.server.HTTPServer    # classe du serveur HTTP
handler = http.server.CGIHTTPRequestHandler    # classe du gestionnaire
handler.cgi_directories = ["/cgi-bin"]
PORT = 8080
server_address = ("", PORT)
httpd = server(server_address, handler)   # objet "serveur"
httpd.serve_forever()

""" après exécution aller sur 127.0.0.1:[port choisi]/index.html
    lien pour copier coller:
    127.0.0.1:8080/index.html
"""