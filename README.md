# Splunk Core User Certification Practice Exam

An interactive GUI-based practice exam application to help users prepare for the Splunk Core Certified User certification.

**Author:** Marc Aburquez (gunnymarc)
**License:** GNU General Public License v3.0

## Overview

This project provides a comprehensive practice exam tool featuring:

- Interactive Tkinter-based GUI
- Configurable exam modes (timed or untimed practice)
- Flexible question counts (65, 75, or 100 questions)
- 60-minute countdown timer with pause/resume functionality
- Auto-grading with immediate feedback
- Domain-by-domain performance breakdown
- Question flagging for review
- Multi-select question support
- 70% passing threshold (matching official exam)

## Directory Structure

```
splunk_certs/
├── README.md                              # This file
└── splunk_core_user/                      # Main project directory
    ├── README.md                          # Project overview
    └── exam/                              # Practice exam application
        ├── Practice_Exam_Splunk_Core_User.py   # Main Python application
        ├── start_splunk_exam.sh           # Shell launcher script
        ├── README.md                      # Exam documentation
        ├── LICENSE                        # GPL v3 License
        └── content/                       # Question bank directory
            ├── Splunk_Core_User_Practice_Exam_Advanced_100_Questions.md
            ├── Splunk_Core_User_Practice_Exam_75_Questions.md
            ├── Splunk_Core_User_Practice_Exam_72_Questions 2.4.md
            ├── Splunk_Core_User_Practice_Exam_65_Questions 1.0.md
            ├── Splunk_Core_User_Practice_Exam_65_Questions 2.0.md
            ├── Splunk_Core_User_Practice_Exam_65_Questions 2.3.md
            ├── Splunk_Core_User_Practice_Exam_60_Questions 2.1.md
            └── Splunk_Core_User_Practice_Exam_46_questions 2.2.md
```

## Requirements

- Python 3.6 or higher
- Tkinter (included with Python on most systems)

## Installation

```bash
# Clone the repository
git clone https://github.com/gunnymarc/splunk_certs.git
cd splunk_certs

# Verify Python and Tkinter
python3 --version
python3 -c "import tkinter; print('Tkinter OK')"
```

### Installing Tkinter (if not present)

| Platform | Command |
|----------|---------|
| macOS | Included with Python from python.org |
| Ubuntu/Debian | `sudo apt-get install python3-tk` |
| Fedora/RHEL | `sudo dnf install python3-tkinter` |

## Usage

### Method 1: Using the Shell Script (Recommended)

```bash
cd splunk_core_user/exam
./start_splunk_exam.sh
```

### Method 2: Running Python Directly

```bash
cd splunk_core_user/exam
python3 Practice_Exam_Splunk_Core_User.py
```

### Configuration Options

When the application launches, a configuration dialog appears with these options:

**Timer Settings:**
- Use 60-minute timer (simulates real exam conditions)
- No timer (practice/study mode)

**Number of Questions:**
- 65 Questions (Standard exam length)
- 75 Questions (Extended practice)
- 100 Questions (Full advanced exam)

### During the Exam

**Navigation:**
- Use Previous/Next buttons to move between questions
- Use the dropdown to jump directly to any question
- Click Submit Answer to record your response and view feedback

**Timer Controls:**
- Pause Timer: Freeze the countdown
- Resume Timer: Continue from pause
- Stop Timer: Stop the timer completely

**Question Management:**
- Flag for Review: Mark questions to revisit later
- Checkboxes for multi-select questions
- Radio buttons for single-select questions

**Completion:**
- Click Finish Exam to submit all answers
- Timer auto-submits when it expires in timed mode

### Results Display

After submission, results include:
- Overall score and percentage
- Pass/Fail status (70% threshold)
- Domain-by-domain breakdown with percentages
- List of flagged questions for review
- Time used (in timed mode)

## Exam Domains

The exam covers the official Splunk Core Certified User blueprint:

| Domain | Topic | Weight |
|--------|-------|--------|
| 1.0 | Splunk Basics | 5% |
| 2.0 | Basic Searching | 22% |
| 3.0 | Using Fields in Searches | 20% |
| 4.0 | Search Language Fundamentals | 15% |
| 5.0 | Using Basic Transforming Commands | 15% |
| 6.0 | Creating Reports and Dashboards | 12% |
| 7.0 | Creating and Using Lookups | 6% |
| 8.0 | Creating Scheduled Reports and Alerts | 5% |

## File Descriptions

### Practice_Exam_Splunk_Core_User.py

Main Python application containing:

- **Question Class**: Represents a single exam question with text, options, answers, and explanation
- **StartupDialog Class**: Configuration dialog for timer and question count selection
- **QuestionParser Class**: Parses markdown files containing exam questions
- **SplunkPracticeExam Class**: Main application with GUI, timer, navigation, and scoring

### start_splunk_exam.sh

Shell launcher script that:
1. Displays welcome banner and features
2. Validates Python 3 installation
3. Verifies Tkinter availability
4. Checks for content directory
5. Launches the Python application

### content/ Directory

Contains question bank files in markdown format. The primary source is:
- `Splunk_Core_User_Practice_Exam_Advanced_100_Questions.md`

Questions are randomly selected while maintaining domain distribution.

## Usage Examples

**Standard Timed Exam:**
```bash
./start_splunk_exam.sh
# Select: 60-minute timer, 65 questions
```

**Extended Practice Mode:**
```bash
python3 Practice_Exam_Splunk_Core_User.py
# Select: No timer, 100 questions
```

**Quick Review Session:**
```bash
python3 Practice_Exam_Splunk_Core_User.py
# Select: No timer, 75 questions
# Flag difficult questions for later review
```

## Technical Details

**Dependencies:** Python standard library only (no external packages required)

**Modules Used:**
- `tkinter` - GUI framework
- `tkinter.ttk` - Themed widgets
- `tkinter.messagebox` - Dialog boxes
- `tkinter.scrolledtext` - Scrolled text widgets
- `re` - Regular expressions for parsing
- `os` - File operations
- `typing` - Type hints
- `random` - Question selection

**Platform Support:** Cross-platform (macOS, Linux, Windows)

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](splunk_core_user/exam/LICENSE) file for details.
