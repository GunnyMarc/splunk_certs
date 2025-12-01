# Splunk Certification Study Materials

A collection of study resources and practice tools for Splunk certification preparation.

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python](https://img.shields.io/badge/Python-3.6+-green.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)]()

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

> ⚠️ **IMPORTANT NOTICE**

This is an **unofficial, independent study tool** created for educational purposes only. It is:

- ❌ **NOT** affiliated with, endorsed by, or sponsored by Splunk Inc.
- ❌ **NOT** official Splunk certification material
- ❌ **NOT** using actual questions from real Splunk exams
- ❌ **NOT** a guarantee of passing the actual certification exam

**Splunk®** is a registered trademark of Splunk Inc.

For official preparation, use:
- [Splunk Education](https://www.splunk.com/en_us/training.html)
- [Splunk Documentation](https://docs.splunk.com/)
- [Splunk Fundamentals 1](https://www.splunk.com/en_us/training/courses/splunk-fundamentals-1.html) (Free)

---

## License

This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)**.

### What This Means

You are free to:
- ✅ **Use** — Run the software for any purpose
- ✅ **Study** — Examine and learn from the source code
- ✅ **Share** — Copy and distribute the software
- ✅ **Modify** — Make changes and improvements

Under the following conditions:
- 📋 **Disclose Source** — Source code must be made available when distributing
- 📋 **License & Copyright Notice** — Include the original license and copyright
- 📋 **Same License** — Modifications must be released under GPL-3.0
- 📋 **State Changes** — Document changes made to the original code

### License Summary

```
Splunk Certification Study Materials
Copyright (C) 2024

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

### License Links

| Resource | Link |
|----------|------|
| Full License Text | [LICENSE](splunk_core_user/exam/LICENSE) |
| GPL-3.0 Official Page | [https://www.gnu.org/licenses/gpl-3.0.en.html](https://www.gnu.org/licenses/gpl-3.0.en.html) |
| GPL-3.0 Quick Guide | [https://choosealicense.com/licenses/gpl-3.0/](https://choosealicense.com/licenses/gpl-3.0/) |
| GPL FAQ | [https://www.gnu.org/licenses/gpl-faq.html](https://www.gnu.org/licenses/gpl-faq.html) |

---

## Contributing

Contributions are welcome! Feel free to:
- 🐛 Report bugs
- 💡 Suggest features
- ✏️ Submit corrections to questions
- 📝 Improve documentation

Please open an issue or submit a pull request.

### Contributor License

By contributing to this project, you agree that your contributions will be licensed under the GPL-3.0 license.

---

## Acknowledgments

- Questions based on publicly available Splunk documentation and training materials
- Built with Python and tkinter
- Inspired by the need for accessible certification study tools

---

**Good luck with your Splunk certification! 🚀**