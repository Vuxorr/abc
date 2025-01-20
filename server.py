import http.server
import ssl

# Ustawienie konfiguracji serwera HTTPS
server_address = ('localhost', 443)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)

# Załaduj certyfikaty SSL
httpd.socket = ssl.wrap_socket(httpd.socket, 
                               keyfile="key.pem", 
                               certfile="cert.pem", 
                               server_side=True)

print("Serwer HTTPS działa na https://localhost")
httpd.serve_forever()