#!/usr/bin/env python3
"""Run the SDLC agent pipeline from CLI."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from src.ui.cli import main

if __name__ == "__main__":
    raise SystemExit(main())
