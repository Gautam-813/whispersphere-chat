#!/usr/bin/env python3
"""
Render.com startup script for WhisperSphere
"""
import os
import uvicorn
from main import app

if __name__ == "__main__":
    # Get port from environment variable (Render provides this)
    port = int(os.environ.get("PORT", 8000))
    
    # Run the app
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=port,
        log_level="info",  # Enable some logging for deployment monitoring
        access_log=True    # Enable access logs for Render
    )
