#!/bin/bash
# ========================================================
#   Splunk Core User Certification Practice Exam Launcher
# ========================================================

echo "╔══════════════════════════════════════════════════════════╗"
echo "║   🎓 Splunk Core User Certification Practice Exam        ║"
echo "║   ⏱  65 Questions | 60-Minute Timer                      ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""
echo "Features:"
echo "  ✓ 65 randomly selected questions from 100-question bank"
echo "  ✓ 60-minute countdown timer (60:00 → 00:00)"
echo "  ✓ Pause/Resume/Stop timer controls"
echo "  ✓ Color-coded timer: Green → Orange → Red"
echo "  ✓ 5-minute warning dialog"
echo "  ✓ Auto-grading when time expires"
echo "  ✓ Detailed score breakdown by domain"
echo ""

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed."
    echo "   Please install Python 3 and try again."
    exit 1
fi

# Check Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "✓ Using Python $python_version"

# Check if tkinter is available
if ! python3 -c "import tkinter" 2>/dev/null; then
    echo ""
    echo "❌ Warning: tkinter is not installed."
    echo "   On Ubuntu/Debian: sudo apt-get install python3-tk"
    echo "   On Fedora/RHEL:   sudo dnf install python3-tkinter"
    echo "   On macOS:         tkinter is included with Python from python.org"
    echo "   On Windows:       tkinter is included with standard Python install"
    echo ""
    exit 1
fi

echo "✓ tkinter is available"
echo ""
echo "🚀 Starting exam..."
echo "   (A GUI window will open)"
echo ""

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Launch the application
python3 "$SCRIPT_DIR/Splunk_Practice_Exam.py"

echo ""
echo "══════════════════════════════════════════════════════════"
echo "Thank you for using the Splunk Practice Exam! 📚"
echo "Good luck with your certification!"
echo "══════════════════════════════════════════════════════════"
