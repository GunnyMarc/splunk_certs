# Splunk Core User Practice Exam

A comprehensive practice exam application for the Splunk Core Certified User certification.

## Description

This project provides an interactive GUI-based practice exam to help you prepare for the Splunk Core Certified User certification. The application loads questions from the included question bank and provides a realistic exam experience with optional timing.

### Features

- **Configurable Timer**: Choose between a 60-minute timed exam or untimed practice mode
- **Flexible Question Count**: Select 65, 75, or 100 questions per session
- **Timer Display**: Countdown shown in MM:SS format (e.g., 60:00, 05:30)
- **Timer Controls**: Pause, resume, and stop functionality
- **5-Minute Warning**: Alert notification when 5 minutes remain
- **Auto-Grading**: Automatic scoring when time expires or exam is submitted
- **Multi-Select Support**: Handles both single-answer and multiple-answer questions
- **Question Flagging**: Mark questions for later review
- **Domain Score Breakdown**: Performance breakdown by exam domain
- **Pass/Fail Status**: 70% passing threshold (matches official exam)

### Exam Domains Covered

Questions are organized according to the official Splunk Core Certified User exam blueprint:

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

## Question Bank

The practice exam questions are sourced from:

- **`content/Splunk_Core_User_Practice_Exam_Advanced_100_Questions.md`** - Contains 100 advanced practice questions with detailed explanations, including single-select and multi-select question types.

## Requirements

- Python 3.6 or higher
- Tkinter (typically included with Python)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/gunnymarc/splunk_certs.git
   cd splunk_certs/splunk_core_user/exam
   ```

2. Verify Python and Tkinter are installed:
   ```bash
   python3 --version
   python3 -c "import tkinter; print('Tkinter OK')"
   ```

   If Tkinter is not installed:
   - **macOS**: Included with Python from python.org
   - **Ubuntu/Debian**: `sudo apt-get install python3-tk`
   - **Fedora/RHEL**: `sudo dnf install python3-tkinter`

## Usage

### Using the Shell Script (Recommended)

```bash
./start_splunk_exam.sh
```

### Running Python Directly

```bash
python3 Practice_Exam_Splunk_Core_User.py
```

### Exam Configuration

At startup, you'll be prompted to configure:

1. **Timer Settings**
   - Use 60-minute timer (simulates real exam)
   - No timer (practice/study mode)

2. **Number of Questions**
   - 65 Questions - Standard exam length
   - 75 Questions - Extended practice
   - 100 Questions - Full question bank

## Project Structure

```
exam/
├── Practice_Exam_Splunk_Core_User.py    # Main application
├── start_splunk_exam.sh                  # Shell launcher
├── README.md                             # This file
├── LICENSE                               # GPL v3 License
└── content/                              # Question bank directory
    ├── Splunk_Core_User_Practice_Exam_Advanced_100_Questions.md  # Primary question file (100 questions)
    ├── Splunk_Core_User_Practice_Exam_75_Questions.md            # 75 question set
    ├── Splunk_Core_User_Practice_Exam_72_Questions 2.4.md        # 72 question set (v2.4)
    ├── Splunk_Core_User_Practice_Exam_65_Questions 1.0.md        # 65 question set (v1.0)
    ├── Splunk_Core_User_Practice_Exam_65_Questions 2.0.md        # 65 question set (v2.0)
    ├── Splunk_Core_User_Practice_Exam_65_Questions 2.3.md        # 65 question set (v2.3)
    ├── Splunk_Core_User_Practice_Exam_60_Questions 2.1.md        # 60 question set (v2.1)
    └── Splunk_Core_User_Practice_Exam_46_questions 2.2.md        # 46 question set (v2.2)
```

## Content Directory

The `content/` subdirectory contains all practice exam question files:

| File | Questions | Description |
|------|-----------|-------------|
| `Splunk_Core_User_Practice_Exam_Advanced_100_Questions.md` | 100 | **Primary file** - Advanced questions with multi-select support |
| `Splunk_Core_User_Practice_Exam_75_Questions.md` | 75 | Extended practice set |
| `Splunk_Core_User_Practice_Exam_72_Questions 2.4.md` | 72 | Version 2.4 question set |
| `Splunk_Core_User_Practice_Exam_65_Questions 1.0.md` | 65 | Version 1.0 - Original set |
| `Splunk_Core_User_Practice_Exam_65_Questions 2.0.md` | 65 | Version 2.0 - Updated set |
| `Splunk_Core_User_Practice_Exam_65_Questions 2.3.md` | 65 | Version 2.3 - Revised set |
| `Splunk_Core_User_Practice_Exam_60_Questions 2.1.md` | 60 | Version 2.1 question set |
| `Splunk_Core_User_Practice_Exam_46_questions 2.2.md` | 46 | Version 2.2 question set |

The application currently uses `Splunk_Core_User_Practice_Exam_Advanced_100_Questions.md` as the primary question source.

## License

This project is free software: you can redistribute it and/or modify it under the terms of the **GNU General Public License v3.0** as published by the Free Software Foundation.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the [LICENSE](LICENSE) file for details.

## Disclaimer

This practice exam is an independent study tool and is **not affiliated with, endorsed by, or officially associated with Splunk Inc.** The questions are designed to help prepare for the certification exam but do not guarantee exam success. Always refer to official Splunk documentation and training materials for the most accurate information.

## Author

Marc Aburquez (gunnymarc)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
