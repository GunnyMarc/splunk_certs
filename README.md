# Splunk Certification Study Materials

A collection of study resources and practice tools for Splunk certification preparation.

## Overview

This repository contains practice exam materials and study aids designed to help you prepare for Splunk certifications. Currently focused on the **Splunk Core Certified User** certification.

## Directory Structure

```
splunk_certs/
├── README.md
└── splunk_core_user/
    └── exam/
        ├── Splunk_Practice_Exam.py          # Interactive GUI practice exam application
        ├── start_exam.sh                     # Linux/macOS launcher script
        ├── README.md                         # Detailed exam application documentation
        ├── LICENSE                           # GPL-3.0 license
        └── content/
            ├── Splunk_Core_User_Practice_Exam_65_Questions 1.0.md
            ├── Splunk_Core_User_Practice_Exam_65_Questions 2.0.md
            ├── Splunk_Core_User_Practice_Exam_60_Questions 2.1.md
            ├── Splunk_Core_User_Practice_Exam_46_questions 2.2.md
            ├── Splunk_Core_User_Practice_Exam_65_Questions 2.3.md
            ├── Splunk_Core_User_Practice_Exam_72_Questions 2.4.md
            ├── Splunk_Core_User_Practice_Exam_75_Questions.md
            └── Splunk_Core_User_Practice_Exam_Advanced_100_Questions.md
```

## Features

### Practice Exam Application

The main component is an interactive GUI practice exam that simulates real exam conditions:

- **100-question bank** with 65 questions randomly selected per exam
- **60-minute countdown timer** with pause/resume functionality
- **Domain-weighted distribution** based on official exam blueprint
- **Immediate feedback** with detailed explanations
- **Score breakdown** by knowledge domain
- **Color-coded timer** warnings (green > orange > red)
- **Auto-submit** when time expires

### Exam Domains Covered

| Domain | Weight | Topic |
|--------|--------|-------|
| 1.0 | 5% | Splunk Basics |
| 2.0 | 22% | Basic Searching |
| 3.0 | 20% | Using Fields in Searches |
| 4.0 | 15% | Search Language Fundamentals |
| 5.0 | 15% | Using Basic Transforming Commands |
| 6.0 | 12% | Creating Reports and Dashboards |
| 7.0 | 6% | Creating and Using Lookups |
| 8.0 | 5% | Creating Scheduled Reports and Alerts |

## Requirements

- **Python 3.6+**
- **tkinter** (usually included with Python)

### Installing tkinter

**Ubuntu/Debian:**
```bash
sudo apt-get install python3-tk
```

**Fedora/RHEL:**
```bash
sudo dnf install python3-tkinter
```

**macOS/Windows:**
Included with Python from [python.org](https://python.org)

## Quick Start

### Linux/macOS
```bash
cd splunk_core_user/exam
chmod +x start_exam.sh
./start_exam.sh
```

### Windows
```cmd
cd splunk_core_user\exam
python Splunk_Practice_Exam.py
```

## Disclaimer

This is an **unofficial, independent study tool** created for educational purposes only. It is:

- NOT affiliated with, endorsed by, or sponsored by Splunk Inc.
- NOT official Splunk certification material
- NOT using actual questions from real Splunk exams

**Splunk** is a registered trademark of Splunk Inc.

For official preparation, use:
- [Splunk Education](https://www.splunk.com/en_us/training.html)
- [Splunk Documentation](https://docs.splunk.com/)
- [Splunk Fundamentals 1](https://www.splunk.com/en_us/training/courses/splunk-fundamentals-1.html) (Free)

## License

This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)**.

See the [LICENSE](splunk_core_user/exam/LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit corrections to questions
- Improve documentation

Please open an issue or submit a pull request.
