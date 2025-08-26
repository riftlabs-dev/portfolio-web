#!/usr/bin/env python3
"""
Main entry point for the pygame web application.
This file handles the web server setup and game initialization.
"""

import asyncio
import sys
import os
from web_server import run_web_server

async def main():
    """Main function to start the web server and handle game deployment."""
    try:
        print("Starting Pygame Web Application...")
        print("Server will be accessible at http://0.0.0.0:5000")
        
        # Start the web server
        await run_web_server()
        
    except Exception as e:
        print(f"Error starting application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Check if we're running in a web context (pygbag)
    if "--web" in sys.argv or os.getenv("PYGAME_WEB", False):
        # Import and run the game directly for web deployment
        from game import main as game_main
        asyncio.run(game_main())
    else:
        # Run the web server for local/Replit deployment
        asyncio.run(main())
