#!/bin/bash
# Splunk Practice Exam Launcher (Timer Version)

echo "========================================================"
echo "  Splunk Core User Certification Practice Exam"
echo "  🆕 WITH 60-MINUTE COUNTDOWN TIMER"
echo "========================================================"
echo ""
echo "Features:"
echo "  ✓ 60-minute countdown timer"
echo "  ✓ Pause/Resume functionality"
echo "  ✓ 5-minute warning alert"
echo "  ✓ Auto-grading when time expires"
echo "  ✓ Color-coded time display"
echo ""
echo "Starting the timed practice exam..."
echo ""

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
    echo "On Ubuntu/Debian, install with: sudo apt-get install python3-tk"
    echo ""
    exit 1
fi

echo ""
echo "⏱️  Timer will start automatically when exam loads..."
echo "💡 Tip: You can pause the timer at any time!"
echo ""

# Launch the application
python3 splunk_practice_exam_with_timer.py

echo ""
echo "Thank you for using the Splunk Practice Exam!"
echo "Review your results and keep studying! 📚"
