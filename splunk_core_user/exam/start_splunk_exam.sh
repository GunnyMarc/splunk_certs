#!/bin/bash
# Splunk Practice Exam Launcher
# Copyright (C) 2024 - Licensed under GPL v3

echo "========================================================"
echo "  Splunk Core User Certification Practice Exam"
echo "========================================================"
echo ""
echo "Features:"
echo "  - Choose timed (60 min) or practice mode"
echo "  - Select 65, 75, or 100 questions"
echo "  - Questions from Advanced 100 Questions file"
echo "  - Timer displayed as MM:SS"
echo "  - Pause/Resume timer functionality"
echo "  - 5-minute warning alert"
echo "  - Auto-grading when time expires"
echo "  - Domain score breakdown"
echo ""

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed."
    echo "Please install Python 3 and try again."
    exit 1
fi

# Check Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "Using Python $python_version"

# Check if tkinter is available
if ! python3 -c "import tkinter" 2>/dev/null; then
    echo ""
    echo "Warning: tkinter is not installed."
    echo "On macOS: tkinter should be included with Python"
    echo "On Ubuntu/Debian: sudo apt-get install python3-tk"
    echo "On Fedora/RHEL: sudo dnf install python3-tkinter"
    echo ""
    exit 1
fi

# Check if the content directory exists
if [ ! -d "$SCRIPT_DIR/content" ]; then
    echo "Error: content directory not found."
    echo "Please ensure the content directory exists with question files."
    exit 1
fi

echo ""
echo "Starting the practice exam..."
echo ""

# Launch the application
cd "$SCRIPT_DIR"
python3 Practice_Exam_Splunk_Core_User.py

echo ""
echo "Thank you for using the Splunk Practice Exam!"
echo "Review your results and keep studying!"
