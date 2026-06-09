#!/usr/bin/env python3
"""Launch Streamlit UI for SDLC pipeline."""

import subprocess
import sys
from pathlib import Path

if __name__ == "__main__":
    app = Path(__file__).parent / "src" / "ui" / "streamlit_app.py"
    subprocess.run([sys.executable, "-m", "streamlit", "run", str(app), "--server.port", "8501"])
