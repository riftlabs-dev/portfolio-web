"""
Web server for serving the pygame application and handling web deployment.
Provides HTTP server for static files and game embedding.
"""

import asyncio
import os
import subprocess
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler
import socketserver
import threading
import webbrowser
from urllib.parse import urlparse, parse_qs
import json

class GameHTTPRequestHandler(SimpleHTTPRequestHandler):
    """Custom HTTP request handler for serving game files."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.getcwd(), **kwargs)
    
    def end_headers(self):
        """Add CORS headers for web compatibility."""
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()
    
    def do_GET(self):
        """Handle GET requests."""
        if self.path == '/' or self.path == '/index.html':
            self.serve_index()
        elif self.path == '/game':
            self.serve_game()
        elif self.path.startswith('/static/'):
            # Serve static files
            super().do_GET()
        else:
            super().do_GET()
    
    def serve_index(self):
        """Serve the main index page."""
        try:
            with open('templates/index.html', 'r') as f:
                content = f.read()
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(content.encode())
        except FileNotFoundError:
            self.send_error(404, "Index page not found")
    
    def serve_game(self):
        """Serve game status or launch game."""
        response = {
            "status": "ready",
            "message": "Game is ready to play",
            "controls": {
                "space": "Add random ball (+10 pts)",
                "click": "Add ball at cursor (+5 pts)",
                "r": "Reset game",
                "esc": "Exit"
            }
        }
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())
    
    def log_message(self, format, *args):
        """Override to provide cleaner logging."""
        print(f"[{self.address_string()}] {format % args}")

class WebGameServer:
    """Main web server class for hosting the pygame application."""
    
    def __init__(self, port=5000, host='0.0.0.0'):
        self.port = port
        self.host = host
        self.httpd = None
        self.game_process = None
    
    def start_server(self):
        """Start the HTTP server."""
        try:
            handler = GameHTTPRequestHandler
            self.httpd = HTTPServer((self.host, self.port), handler)
            
            print(f"Server starting on http://{self.host}:{self.port}")
            print(f"Game will be accessible at: http://{self.host}:{self.port}")
            print("Press Ctrl+C to stop the server")
            
            self.httpd.serve_forever()
            
        except KeyboardInterrupt:
            print("\nShutting down server...")
            self.stop_server()
        except Exception as e:
            print(f"Error starting server: {e}")
    
    def stop_server(self):
        """Stop the HTTP server."""
        if self.httpd:
            self.httpd.shutdown()
            self.httpd.server_close()
        
        if self.game_process:
            self.game_process.terminate()

def check_pygame_web():
    """Check if pygame-web/pygbag is available."""
    try:
        import pygbag
        return True
    except ImportError:
        try:
            result = subprocess.run(['pygbag', '--version'], 
                                  capture_output=True, text=True)
            return result.returncode == 0
        except FileNotFoundError:
            return False

def install_pygame_web():
    """Attempt to install pygame-web dependencies."""
    print("Installing pygame-web dependencies...")
    try:
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'pygbag'], 
                      check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to install pygame-web: {e}")
        return False

async def run_web_server():
    """Run the web server asynchronously."""
    # Check for pygame-web availability
    if not check_pygame_web():
        print("pygame-web (pygbag) not found. Attempting to install...")
        if not install_pygame_web():
            print("Could not install pygame-web. Running basic web server...")
    
    # Create and start the web server
    server = WebGameServer()
    
    # Run server in a separate thread to allow async operation
    def run_server():
        server.start_server()
    
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()
    
    # Keep the async function running
    try:
        while server_thread.is_alive():
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        print("Stopping web server...")
        server.stop_server()

if __name__ == "__main__":
    asyncio.run(run_web_server())
