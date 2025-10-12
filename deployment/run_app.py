#!/usr/bin/env python3
"""
Smart Garbage Classification Flask App
Run this script to start the web application
"""

import os
import sys
from flask_app import app

if __name__ == '__main__':
    print("🗑️  Starting Smart Garbage Classification App...")
    print("📱 Open your browser and go to: http://localhost:5001")
    print("🛑 Press Ctrl+C to stop the server")
    print("-" * 50)
    
    try:
        app.run(debug=True, host='0.0.0.0', port=5001)
    except KeyboardInterrupt:
        print("\n👋 Server stopped. Goodbye!")
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        sys.exit(1)
