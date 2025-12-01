# 🎓 Splunk Core User Certification Practice Exam

A comprehensive, interactive GUI practice exam application designed to help you prepare for the **Splunk Core Certified User** certification exam.

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![License](https://img.shields.io/badge/License-GPL--3.0-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Application Guide](#application-guide)
- [Exam Domains](#exam-domains)
- [File Structure](#file-structure)
- [Disclaimer](#disclaimer)
- [License](#license)

---

## Overview

This practice exam application simulates the real Splunk Core Certified User exam experience with:

- **65 questions** randomly selected from a 100-question bank
- **60-minute countdown timer** matching real exam conditions
- **Domain-weighted question distribution** based on the official exam blueprint
- **Immediate feedback** with detailed explanations for each question
- **Comprehensive scoring** with breakdown by knowledge domain

---

## Features

### ⏱️ Timer System
- **60-minute countdown** displayed in MM:SS format (60:00 → 00:00)
- **Pause button** - Temporarily stop the timer when needed
- **Resume button** - Continue the timer after pausing
- **Stop button** - Completely stop the timer
- **Color-coded display:**
  - 🟢 Green: More than 10 minutes remaining
  - 🟠 Orange: 10 minutes or less remaining
  - 🔴 Red: 5 minutes or less remaining
- **5-minute warning** - Pop-up alert when 5 minutes remain
- **Auto-submit** - Exam automatically grades when timer reaches 00:00

### 📝 Question Features
- **Single-select questions** - Choose one correct answer
- **Multi-select questions** - Select all answers that apply (clearly marked)
- **Question navigation** - Previous/Next buttons and direct jump to any question
- **Progress tracking** - Visual progress bar showing answered questions
- **Immediate feedback** - See if your answer is correct after submitting
- **Detailed explanations** - Learn why each answer is correct or incorrect

### 📊 Scoring & Results
- **Overall score** with percentage
- **Pass/Fail status** (70% passing threshold)
- **Domain-by-domain breakdown** with visual progress bars
- **Time used tracking**
- **Review mode** - Review all questions and explanations after completing

---

## Requirements

### System Requirements
- **Operating System:** Windows 10/11, macOS 10.14+, or Linux (Ubuntu 18.04+, Fedora, etc.)
- **Python:** Version 3.6 or higher
- **tkinter:** Python's standard GUI library (included with most Python installations)

### Installing tkinter (if needed)

**Ubuntu/Debian:**
```bash
sudo apt-get install python3-tk
```

**Fedora/RHEL/CentOS:**
```bash
sudo dnf install python3-tkinter
```

**macOS:**
- tkinter is included with Python from [python.org](https://python.org)
- If using Homebrew Python: `brew install python-tk`

**Windows:**
- tkinter is included with the standard Python installer from [python.org](https://python.org)

---

## Installation

### Option 1: Download and Run
1. Download both files to the same directory:
   - `Splunk_Practice_Exam.py`
   - `start_exam.sh` (for Linux/macOS)

2. Make the shell script executable (Linux/macOS):
   ```bash
   chmod +x start_exam.sh
   ```

### Option 2: Clone from Repository
```bash
git clone https://github.com/yourusername/splunk-practice-exam.git
cd splunk-practice-exam
chmod +x start_exam.sh
```

---

## Usage

### Linux / macOS

**Using the launcher script (recommended):**
```bash
./start_exam.sh
```

**Or run Python directly:**
```bash
python3 Splunk_Practice_Exam.py
```

### Windows

**Using Command Prompt:**
```cmd
python Splunk_Practice_Exam.py
```

**Or double-click** the `Splunk_Practice_Exam.py` file if Python is associated with `.py` files.

---

## Application Guide

### Starting the Exam

1. Launch the application using one of the methods above
2. The exam window will open with:
   - Timer starting automatically at 60:00
   - First question displayed
   - Navigation controls at the bottom

### Answering Questions

1. **Read the question carefully** - Multi-select questions are marked with "(Select ALL that apply)"
2. **Select your answer(s):**
   - Single-select: Click the radio button for your choice
   - Multi-select: Check all boxes that apply
3. **Click "✓ Submit Answer"** to lock in your response
4. **Review the explanation** shown after submission
5. **Navigate** to the next question using "Next →" or the dropdown

### Timer Controls

| Button | Action |
|--------|--------|
| ⏸ Pause | Temporarily stops the countdown |
| ▶ Resume | Continues the countdown after pause |
| ⏹ Stop | Permanently stops the timer |

### Navigation

| Control | Action |
|---------|--------|
| ← Previous | Go to the previous question |
| Next → | Go to the next question |
| Go to: [dropdown] | Jump directly to any question number |
| 🏁 Finish Exam | Submit exam for grading |

### Completing the Exam

The exam ends when you either:
- Click **"🏁 Finish Exam"** manually
- The timer reaches **00:00** (auto-submit)

You'll see a results dialog showing:
- Total score and percentage
- Pass/Fail status
- Breakdown by each domain
- Time used

After completion, you can review all questions and their explanations.

---

## Exam Domains

Questions are distributed according to the official Splunk Core Certified User exam blueprint:

| Domain | Weight | Description |
|--------|--------|-------------|
| **Domain 1.0** | 5% | Splunk Basics |
| **Domain 2.0** | 22% | Basic Searching |
| **Domain 3.0** | 20% | Using Fields in Searches |
| **Domain 4.0** | 15% | Search Language Fundamentals |
| **Domain 5.0** | 15% | Using Basic Transforming Commands |
| **Domain 6.0** | 12% | Creating Reports and Dashboards |
| **Domain 7.0** | 6% | Creating and Using Lookups |
| **Domain 8.0** | 5% | Creating Scheduled Reports and Alerts |

---

## File Structure

```
splunk-practice-exam/
├── Splunk_Practice_Exam.py    # Main Python application
├── start_exam.sh              # Linux/macOS launcher script
├── start_exam.bat             # Windows launcher script (optional)
└── README.md                  # This documentation file
```

---

## Disclaimer

> ⚠️ **IMPORTANT - PLEASE READ**

### Not Official Material
This practice exam is an **independent, unofficial study tool** created for educational purposes only. It is:

- ❌ **NOT** affiliated with, endorsed by, or sponsored by Splunk Inc.
- ❌ **NOT** official Splunk certification material
- ❌ **NOT** a guarantee of passing the actual certification exam
- ❌ **NOT** using actual questions from the real Splunk exam

### No Warranty
This software is provided **"AS IS"** without warranty of any kind, express or implied. The creators and contributors:

- Make no guarantees about the accuracy of the content
- Are not responsible for exam outcomes
- Do not guarantee that this material reflects current exam content

### Trademarks
- **Splunk®** is a registered trademark of Splunk Inc.
- All other trademarks are the property of their respective owners.

### Recommended Study Resources
For official preparation, please use:
- [Splunk Education](https://www.splunk.com/en_us/training.html) - Official training courses
- [Splunk Documentation](https://docs.splunk.com/) - Official documentation
- [Splunk Fundamentals 1](https://www.splunk.com/en_us/training/courses/splunk-fundamentals-1.html) - Free official course

### Use at Your Own Risk
By using this software, you acknowledge that:
1. You understand this is unofficial practice material
2. You will not hold the creators liable for any outcomes
3. You will use this tool as a **supplement** to official study resources

---

## License

This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)**.

```
Copyright (C) 2024 Splunk Practice Exam Project

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
```

---

## Contributing

Contributions are welcome! If you'd like to:
- Report a bug
- Suggest a feature
- Submit a correction to a question
- Improve documentation

Please open an issue or submit a pull request.

---

## Acknowledgments

- Questions based on publicly available Splunk documentation and training materials
- Built with Python and tkinter
- Inspired by the need for accessible certification study tools

---

**Good luck with your Splunk Core Certified User certification! 🚀**
