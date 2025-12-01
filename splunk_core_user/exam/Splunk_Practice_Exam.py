#!/usr/bin/env python3
"""
Splunk Core User Certification Practice Exam
============================================
Interactive GUI Application with 65 questions and 60-minute countdown timer.

Features:
- 65 questions randomly selected from question bank
- 60-minute countdown timer (MM:SS format)
- Pause/Resume/Stop timer functionality
- 5-minute warning dialog
- Auto-grading when timer expires
- Detailed score breakdown by domain

Author: Splunk Practice Exam Project
License: GPL-3.0
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import random
from typing import List, Dict, Tuple, Set


class Question:
    """Represents a single exam question"""
    def __init__(self, number: int, domain: str, text: str, options: Dict[str, str], 
                 correct_answers: List[str], explanation: str, is_multi_select: bool = False):
        self.number = number
        self.domain = domain
        self.text = text
        self.options = options
        self.correct_answers = correct_answers
        self.explanation = explanation
        self.is_multi_select = is_multi_select
        self.user_answers: Set[str] = set()
        
    def is_correct(self) -> bool:
        """Check if user's answer is correct"""
        return self.user_answers == set(self.correct_answers)
    
    def is_answered(self) -> bool:
        """Check if question has been answered"""
        return len(self.user_answers) > 0


class SplunkPracticeExam:
    """Main application class for the practice exam"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Splunk Core User - Practice Exam (65 Questions)")
        self.root.geometry("1100x850")
        self.root.minsize(900, 700)
        
        # Load all questions and select 65 randomly
        all_questions = self.load_all_questions()
        self.questions = self.select_exam_questions(all_questions, 65)
        self.current_question_index = 0
        
        # Answer tracking variables
        self.answer_vars: Dict[str, tk.BooleanVar] = {}
        
        # Track exam state
        self.exam_submitted = False
        
        # Timer variables (60 minutes = 3600 seconds)
        self.total_seconds = 60 * 60
        self.remaining_seconds = self.total_seconds
        self.timer_running = False
        self.timer_paused = False
        self.timer_id = None
        self.five_minute_warning_shown = False
        
        # Set up UI
        self.setup_ui()
        self.display_question()
        
        # Start the timer automatically
        self.start_timer()
        
        # Handle window close
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def select_exam_questions(self, all_questions: List[Question], count: int) -> List[Question]:
        """Select questions maintaining domain distribution"""
        # Group questions by domain
        domain_questions = {}
        for q in all_questions:
            domain = q.domain.split(':')[0].strip()
            if domain not in domain_questions:
                domain_questions[domain] = []
            domain_questions[domain].append(q)
        
        # Domain weights based on exam blueprint
        domain_weights = {
            "Domain 1.0": 0.05,  # 5%
            "Domain 2.0": 0.22,  # 22%
            "Domain 3.0": 0.20,  # 20%
            "Domain 4.0": 0.15,  # 15%
            "Domain 5.0": 0.15,  # 15%
            "Domain 6.0": 0.12,  # 12%
            "Domain 7.0": 0.06,  # 6%
            "Domain 8.0": 0.05,  # 5%
        }
        
        selected = []
        for domain, weight in domain_weights.items():
            domain_count = max(1, round(count * weight))
            available = domain_questions.get(domain, [])
            if available:
                sample_size = min(domain_count, len(available))
                selected.extend(random.sample(available, sample_size))
        
        # If we need more questions to reach count, add randomly
        remaining = count - len(selected)
        if remaining > 0:
            unused = [q for q in all_questions if q not in selected]
            if unused:
                selected.extend(random.sample(unused, min(remaining, len(unused))))
        
        # Shuffle and renumber
        random.shuffle(selected)
        for i, q in enumerate(selected):
            q.number = i + 1
        
        return selected[:count]
    
    def load_all_questions(self) -> List[Question]:
        """Load all 100 questions from embedded data"""
        questions = []
        
        # Question data: (original_num, domain, text, options, correct_answers, explanation, is_multi)
        question_data = [
            # Domain 1.0: Splunk Basics (5%)
            (1, "Domain 1.0: Splunk Basics (5%)",
             "Which Splunk components are involved in a typical distributed deployment? (Select all that apply)",
             {"A": "Indexers", "B": "Search Heads", "C": "Forwarders", "D": "Deployment Server", "E": "License Master"},
             ["A", "B", "C", "D", "E"],
             "All components are involved: Indexers (store/index data), Search Heads (coordinate searches), Forwarders (collect/send data), Deployment Server (manages configurations), License Master (manages licensing).",
             True),
            
            (2, "Domain 1.0: Splunk Basics (5%)",
             "What is the primary function of a Splunk App?",
             {"A": "To forward data to external systems", "B": "To provide a specific collection of configurations, dashboards, and knowledge objects for a particular use case", "C": "To manage user licenses", "D": "To compress raw data logs"},
             ["B"],
             "Splunk Apps bundle together configurations, dashboards, reports, searches, and field extractions for specific use cases.",
             False),
            
            (3, "Domain 1.0: Splunk Basics (5%)",
             "Which of the following are default roles in Splunk Enterprise? (Select all that apply)",
             {"A": "Admin", "B": "Power", "C": "User", "D": "SuperUser", "E": "can_delete"},
             ["A", "B", "C"],
             "The three default roles are Admin (full access), Power (can create shared knowledge objects), and User (basic search capabilities).",
             True),
            
            (4, "Domain 1.0: Splunk Basics (5%)",
             "In Splunk, what is the purpose of the deployment server?",
             {"A": "To parse and index data", "B": "To distribute apps and configurations to forwarders", "C": "To perform searches", "D": "To store license information"},
             ["B"],
             "The Deployment Server centrally manages and distributes apps, configurations, and updates to deployment clients.",
             False),
            
            (5, "Domain 1.0: Splunk Basics (5%)",
             "Which file type is used for Splunk configuration files?",
             {"A": ".xml", "B": ".json", "C": ".conf", "D": ".cfg"},
             ["C"],
             "Splunk uses .conf files for all configuration settings.",
             False),
            
            # Domain 2.0: Basic Searching (22%)
            (6, "Domain 2.0: Basic Searching (22%)",
             "Which of the following are best practices for efficient searching in Splunk? (Select all that apply)",
             {"A": "Specify the index name", "B": "Use narrow time ranges", "C": "Include filtering keywords early in the search", "D": "Use leading wildcards (e.g., *error)", "E": "Search 'All Time' to ensure completeness"},
             ["A", "B", "C"],
             "Best practices: specify index, narrow time ranges, filter early. Leading wildcards and 'All Time' searches are inefficient.",
             True),
            
            (7, "Domain 2.0: Basic Searching (22%)",
             'What is the correct syntax to search for events containing the exact phrase "failed login"?',
             {"A": "failed AND login", "B": '"failed login"', "C": "failed_login", "D": "string=failed login"},
             ["B"],
             "Quotation marks search for exact phrases.",
             False),
            
            (8, "Domain 2.0: Basic Searching (22%)",
             "Which time modifier syntax would search for events from the last 4 hours?",
             {"A": "earliest=-4h", "B": "earliest=4h", "C": "time=-4h", "D": "latest=-4h"},
             ["A"],
             "The syntax earliest=-4h means 'starting 4 hours ago'. The minus sign indicates time in the past.",
             False),
            
            (9, "Domain 2.0: Basic Searching (22%)",
             "What does the @ symbol do in time modifiers? (Select all that apply)",
             {"A": "Snaps to the beginning of a time unit", "B": "Rounds to the nearest time unit", "C": "Can be used with d, h, m, mon, w", "D": "Performs a wildcard match"},
             ["A", "B", "C"],
             "The @ symbol snaps/rounds time to specified units: @d (day), @h (hour), @m (minute), etc.",
             True),
            
            (10, "Domain 2.0: Basic Searching (22%)",
             "In the search `index=web (status=404 OR status=500) earliest=-1h`, what is the order of operations?",
             {"A": "Time filter, then index filter, then OR operation", "B": "Index filter, then OR operation, then time filter", "C": "OR operation, then index filter, then time filter", "D": "All filters are applied simultaneously"},
             ["B"],
             "Splunk processes: index/sourcetype filters first, then keyword/field filters, then time range filters.",
             False),
            
            (11, "Domain 2.0: Basic Searching (22%)",
             "Which Search Mode should you use to discover all possible fields in your results?",
             {"A": "Fast", "B": "Smart", "C": "Verbose", "D": "Complete"},
             ["C"],
             "Verbose mode discovers all possible fields but is slower. Fast mode extracts minimal fields for speed.",
             False),
            
            (12, "Domain 2.0: Basic Searching (22%)",
             "How can you search for events where a field exists but has no value? (Select all that apply)",
             {"A": "fieldname=*", "B": 'fieldname=""', "C": '| where isnotnull(fieldname) AND fieldname=""', "D": "fieldname!=*"},
             ["B", "C"],
             'fieldname="" finds empty values. Combined with isnotnull() finds fields that exist but are empty.',
             True),
            
            (13, "Domain 2.0: Basic Searching (22%)",
             'What does clicking the "Finalize" button do to a running search?',
             {"A": "Deletes the search job", "B": "Stops the search and keeps results found so far", "C": "Pauses the search temporarily", "D": "Exports the results to CSV"},
             ["B"],
             "Finalize completes the search immediately with whatever results have been gathered.",
             False),
            
            (14, "Domain 2.0: Basic Searching (22%)",
             "Which of the following are valid Boolean operators in Splunk? (Select all that apply)",
             {"A": "AND", "B": "OR", "C": "NOT", "D": "XOR", "E": "NAND"},
             ["A", "B", "C"],
             "The three Boolean operators in Splunk are AND, OR, and NOT. XOR and NAND are not supported.",
             True),
            
            (15, "Domain 2.0: Basic Searching (22%)",
             "In the search string `error NOT (user=admin OR user=root)`, which operation is evaluated first?",
             {"A": "NOT", "B": "OR", "C": "The entire expression in parentheses", "D": "Left to right sequentially"},
             ["C"],
             "Parentheses have the highest precedence and are evaluated first.",
             False),
            
            (16, "Domain 2.0: Basic Searching (22%)",
             "What is the difference between `earliest=-1d@d` and `earliest=-1d`?",
             {"A": "No difference - they are equivalent", "B": "-1d@d snaps to the beginning of yesterday; -1d means exactly 24 hours ago", "C": "-1d@d is invalid syntax", "D": "-1d is faster to execute"},
             ["B"],
             "-1d@d means '1 day ago, snapped to midnight'. -1d means exactly 24 hours ago from now.",
             False),
            
            (17, "Domain 2.0: Basic Searching (22%)",
             "Which command allows you to save search results for use in a future search?",
             {"A": "save", "B": "export", "C": "outputcsv", "D": "savedsearch"},
             ["C"],
             "The outputcsv command writes search results to a CSV file that can be used in future searches.",
             False),
            
            (18, "Domain 2.0: Basic Searching (22%)",
             'How do you search for events that contain either "error" OR "warning" in any field?',
             {"A": "error | warning", "B": "error OR warning", "C": "error + warning", "D": "(error, warning)"},
             ["B"],
             "Use the OR operator to search for events containing either term.",
             False),
            
            (19, "Domain 2.0: Basic Searching (22%)",
             "What happens when you use `index=*` in your search?",
             {"A": "It searches all indexes", "B": "It's invalid syntax", "C": "It searches only the default index", "D": "It searches for literal asterisk characters"},
             ["A"],
             "index=* is a wildcard that searches across all available indexes the user has permission to search.",
             False),
            
            (20, "Domain 2.0: Basic Searching (22%)",
             "Which of the following time range specifications are valid? (Select all that apply)",
             {"A": "earliest=-30m latest=now", "B": "earliest=@d latest=now", "C": "earliest=-1d@d latest=@d", "D": "earliest=today latest=tomorrow"},
             ["A", "B", "C"],
             "Options A, B, and C use valid time modifiers. 'today' and 'tomorrow' are not valid Splunk syntax.",
             True),
            
            (21, "Domain 2.0: Basic Searching (22%)",
             "What is the purpose of the Job Inspector?",
             {"A": "To view detailed execution statistics for a search", "B": "To manage user permissions", "C": "To configure indexes", "D": "To create dashboards"},
             ["A"],
             "The Job Inspector provides detailed information about search execution, including processing time and events scanned.",
             False),
            
            (22, "Domain 2.0: Basic Searching (22%)",
             "In a search, what does the `_time` field represent?",
             {"A": "The time the search was run", "B": "The timestamp of when the event occurred", "C": "The time the event was indexed", "D": "The current system time"},
             ["B"],
             "The _time field contains the timestamp extracted from the event data, representing when the event occurred.",
             False),
            
            (23, "Domain 2.0: Basic Searching (22%)",
             "Which search string will find events where the status field equals 404 or 500?",
             {"A": "status=404 OR 500", "B": "status=(404 OR 500)", "C": "status=404 OR status=500", "D": "status IN (404,500)"},
             ["C"],
             "Each field-value pair must be specified completely: status=404 OR status=500.",
             False),
            
            (24, "Domain 2.0: Basic Searching (22%)",
             "What is the maximum time that search job results are retained by default?",
             {"A": "6 hours", "B": "24 hours", "C": "7 days", "D": "10 minutes"},
             ["C"],
             "By default, search job results are retained for 7 days before being automatically deleted.",
             False),
            
            (25, "Domain 2.0: Basic Searching (22%)",
             "Which characters require escaping in Splunk searches? (Select all that apply)",
             {"A": '" (double quote)', "B": "\\ (backslash)", "C": "* (asterisk)", "D": "= (equals)"},
             ["A", "B"],
             "Double quotes and backslashes require escaping. Asterisks are wildcards and equals are operators.",
             True),
            
            (26, "Domain 2.0: Basic Searching (22%)",
             "How do you search for events that occurred exactly at midnight on January 1, 2024?",
             {"A": "earliest=2024-01-01 latest=2024-01-01", "B": 'earliest="01/01/2024:00:00:00" latest="01/01/2024:00:00:01"', "C": "_time=2024-01-01T00:00:00", "D": 'date="2024-01-01" time="00:00:00"'},
             ["B"],
             "To search for a specific moment, specify a very narrow time window using earliest and latest with timestamps.",
             False),
            
            (27, "Domain 2.0: Basic Searching (22%)",
             'What does the "Send to Background" option do for a search?',
             {"A": "Deletes the search", "B": "Allows the search to continue running while you do other work", "C": "Pauses the search", "D": "Lowers the search priority"},
             ["B"],
             "'Send to Background' moves the search job to the background, allowing it to continue while you navigate away.",
             False),
            
            # Domain 3.0: Using Fields in Searches (20%)
            (28, "Domain 3.0: Using Fields in Searches (20%)",
             "Which three fields are default Selected Fields in Splunk? (Select all that apply)",
             {"A": "host", "B": "source", "C": "sourcetype", "D": "index", "E": "_time"},
             ["A", "B", "C"],
             "The three default Selected Fields are host, source, and sourcetype.",
             True),
            
            (29, "Domain 3.0: Using Fields in Searches (20%)",
             'What criteria must a field meet to be listed as an "Interesting Field"?',
             {"A": "It must be a numeric field", "B": "It must appear in at least 20% of the events", "C": "It must be manually selected by the user", "D": "It must contain a unique value"},
             ["B"],
             "Fields appearing in 20% or more of the returned events are classified as 'Interesting Fields'.",
             False),
            
            (30, "Domain 3.0: Using Fields in Searches (20%)",
             "Which field extraction methods does Splunk use? (Select all that apply)",
             {"A": "Automatic extraction (default)", "B": "Regular expressions", "C": "Delimiters", "D": "Key-value pairs", "E": "JSON parsing"},
             ["A", "B", "C", "D", "E"],
             "Splunk uses multiple extraction methods: automatic, regex, delimiters, key-value pairs, and JSON parsing.",
             True),
            
            (31, "Domain 3.0: Using Fields in Searches (20%)",
             "How do you search for events where the response_time field is greater than 1000?",
             {"A": "response_time>1000", "B": "response_time gt 1000", "C": "where response_time>1000", "D": "response_time>=1001"},
             ["A"],
             "For numeric comparisons at search time, use the comparison operator directly: response_time>1000.",
             False),
            
            (32, "Domain 3.0: Using Fields in Searches (20%)",
             "Which command would you use to exclude multiple fields from search results? (Select all that apply)",
             {"A": "`fields - fieldname1, fieldname2`", "B": "`fields - fieldname1 - fieldname2`", "C": "`table * - fieldname1 - fieldname2`", "D": "`remove fieldname1, fieldname2`"},
             ["A"],
             "The correct syntax is `fields - field1, field2` with a comma-separated list after the minus sign.",
             True),
            
            (33, "Domain 3.0: Using Fields in Searches (20%)",
             "What is the difference between `host` and `source`?",
             {"A": "host is the machine name; source is the file path or input", "B": "They are identical", "C": "host is the file; source is the machine", "D": "host is mandatory; source is optional"},
             ["A"],
             "`host` identifies the machine that generated the data. `source` identifies the specific file or input.",
             False),
            
            (34, "Domain 3.0: Using Fields in Searches (20%)",
             "Are field names in Splunk case-sensitive?",
             {"A": "Yes, field names are case-sensitive", "B": "No, field names are not case-sensitive", "C": "Only when using regex", "D": "Depends on the sourcetype"},
             ["A"],
             "Field names in Splunk are case-sensitive (Status ≠ status), but field values are not case-sensitive by default.",
             False),
            
            (35, "Domain 3.0: Using Fields in Searches (20%)",
             "Which comparison operators can be used with fields in Splunk? (Select all that apply)",
             {"A": "=", "B": "!=", "C": "<", "D": ">", "E": "<=", "F": ">="},
             ["A", "B", "C", "D", "E", "F"],
             "Splunk supports all standard comparison operators: =, !=, <, >, <=, >=.",
             True),
            
            (36, "Domain 3.0: Using Fields in Searches (20%)",
             "How do you search for events where a field does NOT exist?",
             {"A": "NOT fieldname=*", "B": 'fieldname=""', "C": "| where isnull(fieldname)", "D": "fieldname!=*"},
             ["A"],
             "NOT fieldname=* finds events where the field does not exist. The wildcard * matches any value.",
             False),
            
            (37, "Domain 3.0: Using Fields in Searches (20%)",
             "What does the `_raw` field contain?",
             {"A": "The original, unparsed event text", "B": "The field extraction results", "C": "The index name", "D": "The timestamp"},
             ["A"],
             "_raw contains the complete original event text before any field extraction or parsing.",
             False),
            
            (38, "Domain 3.0: Using Fields in Searches (20%)",
             'Which search finds events where the user field starts with "admin"?',
             {"A": "user=admin*", "B": 'user="admin*"', "C": 'user LIKE "admin%"', "D": "user STARTSWITH admin"},
             ["A"],
             "Use the wildcard * after the prefix to match any characters following 'admin': user=admin*.",
             False),
            
            (39, "Domain 3.0: Using Fields in Searches (20%)",
             "In the Fields sidebar, what does the '#' symbol indicate?",
             {"A": "The field is commented out", "B": "The field contains numeric values", "C": "The field is hidden", "D": "The field is a calculated field"},
             ["B"],
             "The # symbol indicates the field contains numeric values.",
             False),
            
            (40, "Domain 3.0: Using Fields in Searches (20%)",
             "How do you search for events with an IP address in the range 192.168.1.0/24?",
             {"A": "ip=192.168.1.*", "B": '| where cidrmatch("192.168.1.0/24", ip)', "C": "ip IN 192.168.1.0/24", "D": "ip BETWEEN 192.168.1.0 AND 192.168.1.255"},
             ["B"],
             "Use the cidrmatch() function for CIDR notation IP range searches.",
             False),
            
            (41, "Domain 3.0: Using Fields in Searches (20%)",
             "Which of the following are internal (metadata) fields in Splunk? (Select all that apply)",
             {"A": "_time", "B": "_raw", "C": "index", "D": "host", "E": "source"},
             ["A", "B"],
             "_time and _raw are internal metadata fields (prefixed with underscore). index, host, source are default fields.",
             True),
            
            (42, "Domain 3.0: Using Fields in Searches (20%)",
             "What is the purpose of field aliases?",
             {"A": "To rename fields permanently", "B": "To create alternate names for existing fields", "C": "To delete unwanted fields", "D": "To encrypt field values"},
             ["B"],
             "Field aliases create alternate names for existing fields without changing the original field name.",
             False),
            
            (43, "Domain 3.0: Using Fields in Searches (20%)",
             "How do you search for events where the status field is either empty or equals 200?",
             {"A": 'status="" OR status=200', "B": 'status IN ("",200)', "C": '| where status=="" OR status=200', "D": "Both A and C"},
             ["D"],
             "Both syntaxes work: direct field comparison or using the where command with eval expressions.",
             False),
            
            (44, "Domain 3.0: Using Fields in Searches (20%)",
             "What does the `eval` command do in relation to fields?",
             {"A": "Evaluates the search for errors", "B": "Creates or modifies fields using calculations or functions", "C": "Validates field formats", "D": "Evaluates field permissions"},
             ["B"],
             "The eval command creates new fields or modifies existing ones using calculations, string operations, or functions.",
             False),
            
            (45, "Domain 3.0: Using Fields in Searches (20%)",
             'Which search correctly uses a wildcard to find users starting with "admin" or "root"?',
             {"A": "user=admin* OR user=root*", "B": "user=(admin* OR root*)", "C": "user IN (admin*, root*)", "D": "user MATCHES (admin|root)*"},
             ["A"],
             "Each field-value comparison must be complete: user=admin* OR user=root*.",
             False),
            
            (46, "Domain 3.0: Using Fields in Searches (20%)",
             "How can you view all fields in your data, even those appearing in less than 20% of events?",
             {"A": 'Click "All Fields" in the Fields sidebar', "B": "Use Search Mode: Verbose", "C": "Use the command `| fieldsummary`", "D": "All of the above"},
             ["D"],
             "All three methods reveal fields in less than 20% of events.",
             False),
            
            (47, "Domain 3.0: Using Fields in Searches (20%)",
             "What is the difference between `fields` and `table` commands?",
             {"A": "No difference - they are aliases", "B": "`fields` controls which fields are kept/removed; `table` formats output and reorders fields", "C": "`table` is faster", "D": "`fields` only works with numeric data"},
             ["B"],
             "`fields` includes or excludes fields from processing. `table` formats the output as a table and can reorder columns.",
             False),
            
            # Domain 4.0: Search Language Fundamentals (15%)
            (48, "Domain 4.0: Search Language Fundamentals (15%)",
             "Which command removes duplicate events based on the user field?",
             {"A": "`unique user`", "B": "`dedup user`", "C": "`distinct user`", "D": "`remove_duplicates user`"},
             ["B"],
             "The dedup (de-duplication) command removes duplicate events: dedup user keeps only the first occurrence.",
             False),
            
            (49, "Domain 4.0: Search Language Fundamentals (15%)",
             "What is the correct syntax to rename multiple fields? (Select all that apply)",
             {"A": "`rename user as username, ip as ipaddress`", "B": "`rename user=username, ip=ipaddress`", "C": "`rename user TO username | rename ip TO ipaddress`", "D": "`rename user as username | rename ip as ipaddress`"},
             ["A", "D"],
             "Valid syntaxes: multiple renames in one command with 'as', or chained commands.",
             True),
            
            (50, "Domain 4.0: Search Language Fundamentals (15%)",
             "Which command would you use to sort results by count in descending order?",
             {"A": "`sort count`", "B": "`sort -count`", "C": "`sort count desc`", "D": "`order by count desc`"},
             ["B"],
             "The minus sign (-) before a field name sorts in descending order: sort -count.",
             False),
            
            (51, "Domain 4.0: Search Language Fundamentals (15%)",
             "What does the pipe symbol `|` do in a Splunk search?",
             {"A": "Performs an OR operation", "B": "Chains commands together in a pipeline", "C": "Creates a comment", "D": "Escapes special characters"},
             ["B"],
             "The pipe symbol chains commands in a pipeline, passing results from one command to the next.",
             False),
            
            (52, "Domain 4.0: Search Language Fundamentals (15%)",
             "How do you limit search results to a specific index and sourcetype?",
             {"A": "`index=web AND sourcetype=access_combined`", "B": "`index=web sourcetype=access_combined`", "C": '`index=web | where sourcetype="access_combined"`', "D": "Both A and B"},
             ["D"],
             "Both syntaxes work: explicit AND or implicit AND (space between conditions).",
             False),
            
            (53, "Domain 4.0: Search Language Fundamentals (15%)",
             "Which commands are considered transforming commands? (Select all that apply)",
             {"A": "stats", "B": "top", "C": "rare", "D": "chart", "E": "fields", "F": "rename"},
             ["A", "B", "C", "D"],
             "Transforming commands change the format of results: stats, top, rare, and chart. fields and rename are non-transforming.",
             True),
            
            (54, "Domain 4.0: Search Language Fundamentals (15%)",
             "What does the `head 20` command do?",
             {"A": "Returns the last 20 results", "B": "Returns the first 20 results", "C": "Returns 20 random results", "D": "Splits results into 20 groups"},
             ["B"],
             "head 20 returns the first 20 events from the search results.",
             False),
            
            (55, "Domain 4.0: Search Language Fundamentals (15%)",
             "How do you search for events in multiple indexes?",
             {"A": "`index=web OR index=security`", "B": "`index IN (web, security)`", "C": "`index=web,security`", "D": "Both A and C"},
             ["A"],
             "Use OR to search multiple indexes: index=web OR index=security.",
             False),
            
            (56, "Domain 4.0: Search Language Fundamentals (15%)",
             "What is the purpose of the `rex` command?",
             {"A": "To export results", "B": "To extract fields using regular expressions", "C": "To exclude events", "D": "To reverse the order of results"},
             ["B"],
             "The rex command extracts fields from events using regular expressions.",
             False),
            
            (57, "Domain 4.0: Search Language Fundamentals (15%)",
             "Which command would you use to add a new field to events?",
             {"A": "`addfield`", "B": "`eval`", "C": "`create`", "D": "`newfield`"},
             ["B"],
             "The eval command creates new fields or modifies existing fields using expressions.",
             False),
            
            (58, "Domain 4.0: Search Language Fundamentals (15%)",
             "What does the `where` command do?",
             {"A": "Filters results using eval expressions", "B": "Identifies the location of events", "C": "Creates a location field", "D": "Sorts results by location"},
             ["A"],
             "The where command filters results based on eval expressions, allowing complex filtering conditions.",
             False),
            
            (59, "Domain 4.0: Search Language Fundamentals (15%)",
             "How do you return only the last 15 results?",
             {"A": "`head 15`", "B": "`tail 15`", "C": "`last 15`", "D": "`bottom 15`"},
             ["B"],
             "The tail command returns the last N results: tail 15 returns the last 15.",
             False),
            
            (60, "Domain 4.0: Search Language Fundamentals (15%)",
             "Which search language command can you use to return results in reverse time order?",
             {"A": "`reverse`", "B": "`sort -_time`", "C": "`order desc`", "D": "`tail`"},
             ["B"],
             "sort -_time sorts results by time in descending order (most recent first).",
             False),
            
            (61, "Domain 4.0: Search Language Fundamentals (15%)",
             "What is the difference between `rename` and `eval` for changing field names?",
             {"A": "No difference", "B": "`rename` only changes the field name; `eval` can also transform the value", "C": "`rename` is faster", "D": "`eval` is deprecated"},
             ["B"],
             "rename changes only the field name. eval can create new fields with transformed values or different names.",
             False),
            
            (62, "Domain 4.0: Search Language Fundamentals (15%)",
             "Which command retrieves the first field value encountered for each unique combination of other fields?",
             {"A": "`first`", "B": "`head`", "C": "`stats first()`", "D": "`initial`"},
             ["C"],
             "The stats first(fieldname) function returns the first value encountered for each group.",
             False),
            
            # Domain 5.0: Using Basic Transforming Commands (15%)
            (63, "Domain 5.0: Using Basic Transforming Commands (15%)",
             "Which `stats` functions can be used with numeric fields? (Select all that apply)",
             {"A": "sum", "B": "avg", "C": "max", "D": "min", "E": "median", "F": "stdev"},
             ["A", "B", "C", "D", "E", "F"],
             "All listed functions work with numeric fields: sum, avg, max, min, median, and stdev.",
             True),
            
            (64, "Domain 5.0: Using Basic Transforming Commands (15%)",
             "What is the correct syntax to count events by status and host?",
             {"A": "`stats count by status, host`", "B": "`stats count(status, host)`", "C": "`count by status AND host`", "D": "`stats count WHERE status BY host`"},
             ["A"],
             "Use comma-separated fields after 'by' to group by multiple fields: stats count by status, host.",
             False),
            
            (65, "Domain 5.0: Using Basic Transforming Commands (15%)",
             "What does the `top` command do by default?",
             {"A": "Returns top 5 results", "B": "Returns top 10 results with count and percent", "C": "Returns top 20 results", "D": "Returns all results sorted in descending order"},
             ["B"],
             "By default, top returns the 10 most common values along with count and percentage fields.",
             False),
            
            (66, "Domain 5.0: Using Basic Transforming Commands (15%)",
             "How do you specify a custom limit for the `top` command?",
             {"A": "`top limit=20 fieldname`", "B": "`top fieldname limit 20`", "C": "`top 20 fieldname`", "D": "`top fieldname count=20`"},
             ["A"],
             "Specify a custom limit using the limit parameter: top limit=20 fieldname.",
             False),
            
            (67, "Domain 5.0: Using Basic Transforming Commands (15%)",
             "Which `stats` function returns the number of unique values of a field?",
             {"A": "`unique()`", "B": "`distinct()`", "C": "`dc()`", "D": "`count_unique()`"},
             ["C"],
             "The dc() function (distinct count) returns the number of unique values.",
             False),
            
            (68, "Domain 5.0: Using Basic Transforming Commands (15%)",
             "What is the difference between `values()` and `list()` in stats? (Select all that apply)",
             {"A": "`values()` returns unique values only", "B": "`list()` returns all values including duplicates", "C": "`values()` is sorted alphabetically", "D": "`list()` maintains original order"},
             ["A", "B", "C", "D"],
             "values() returns unique values sorted alphabetically. list() returns all values including duplicates in order encountered.",
             True),
            
            (69, "Domain 5.0: Using Basic Transforming Commands (15%)",
             "How do you calculate both the count and average response time by host?",
             {"A": "`stats count, avg(response_time) by host`", "B": "`stats count AND avg(response_time) by host`", "C": "`stats count avg(response_time) GROUP BY host`", "D": "`count by host | avg response_time by host`"},
             ["A"],
             "Multiple aggregations can be comma-separated: stats count, avg(response_time) by host.",
             False),
            
            (70, "Domain 5.0: Using Basic Transforming Commands (15%)",
             "What does the `rare` command show?",
             {"A": "The most common values", "B": "The least common values", "C": "Unusual statistical outliers", "D": "Deleted events"},
             ["B"],
             "The rare command shows the least frequently occurring values of a field.",
             False),
            
            (71, "Domain 5.0: Using Basic Transforming Commands (15%)",
             "Which command would you use to create a time-based statistical chart?",
             {"A": "`timechart`", "B": "`chart`", "C": "`stats by _time`", "D": "All of the above"},
             ["D"],
             "timechart, chart, and stats by _time can all create time-based statistical charts.",
             False),
            
            (72, "Domain 5.0: Using Basic Transforming Commands (15%)",
             "How do you find the earliest and latest times in your results?",
             {"A": "`stats earliest(_time), latest(_time)`", "B": "`stats min(_time), max(_time)`", "C": "`timechart span=1d`", "D": "Both A and B"},
             ["D"],
             "Both work: earliest(_time)/latest(_time) and min(_time)/max(_time) return the time boundaries.",
             False),
            
            (73, "Domain 5.0: Using Basic Transforming Commands (15%)",
             "What does `stats sum(bytes) as total_bytes by host` do?",
             {"A": "Counts the bytes field for each host", "B": "Sums the bytes field for each host and names the result total_bytes", "C": "Creates a new field called total_bytes", "D": "Filters bytes by host"},
             ["B"],
             "This sums the bytes field grouped by host, and aliases the result as total_bytes.",
             False),
            
            (74, "Domain 5.0: Using Basic Transforming Commands (15%)",
             "Which `stats` functions return aggregate values over multiple events? (Select all that apply)",
             {"A": "count", "B": "sum", "C": "avg", "D": "list", "E": "values", "F": "first"},
             ["A", "B", "C", "D", "E", "F"],
             "All listed functions aggregate over multiple events: count, sum, avg, list, values, and first.",
             True),
            
            (75, "Domain 5.0: Using Basic Transforming Commands (15%)",
             "How can you calculate a percentage using stats?",
             {"A": "`stats count by status | eval percent=count/total*100`", "B": "Use the `top` command which includes percentages", "C": "`stats count percentage by status`", "D": "Both A and B"},
             ["D"],
             "You can calculate percentages with eval after stats, or use top which automatically includes percentages.",
             False),
            
            (76, "Domain 5.0: Using Basic Transforming Commands (15%)",
             "What does `| stats count by status | sort - count` do?",
             {"A": "Counts events by status and sorts by status name", "B": "Counts events by status and sorts by count in descending order", "C": "Sorts events by count then counts by status", "D": "Invalid syntax"},
             ["B"],
             "This counts events grouped by status, then sorts by count in descending order (most to least).",
             False),
            
            (77, "Domain 5.0: Using Basic Transforming Commands (15%)",
             "Which command would you use to create statistical groups based on numeric ranges?",
             {"A": "`bucket`", "B": "`group`", "C": "`range`", "D": "`bin`"},
             ["D"],
             "The bin command (also called bucket) creates statistical groups based on numeric ranges or time spans.",
             False),
            
            # Domain 6.0: Creating Reports and Dashboards (12%)
            (78, "Domain 6.0: Creating Reports and Dashboards (12%)",
             "Which of the following are valid report components? (Select all that apply)",
             {"A": "Search query", "B": "Time range", "C": "Visualization type", "D": "Permissions", "E": "Schedule"},
             ["A", "B", "C", "D", "E"],
             "Reports include search query, time range, visualization type, permissions, and optional scheduling.",
             True),
            
            (79, "Domain 6.0: Creating Reports and Dashboards (12%)",
             "What types of visualizations can display time-series data effectively? (Select all that apply)",
             {"A": "Line Chart", "B": "Area Chart", "C": "Pie Chart", "D": "Column Chart", "E": "Single Value"},
             ["A", "B", "D"],
             "Line, Area, and Column charts effectively display time-series data. Pie charts show proportions.",
             True),
            
            (80, "Domain 6.0: Creating Reports and Dashboards (12%)",
             "How do you make a dashboard available to all users in your organization?",
             {"A": 'Set permissions to "Everyone"', "B": 'Set permissions to "Shared in App"', "C": "Export and email to all users", "D": "Save in a public folder"},
             ["B"],
             "Setting permissions to 'Shared in App' makes the dashboard available to all users who have access to that app.",
             False),
            
            (81, "Domain 6.0: Creating Reports and Dashboards (12%)",
             "What is required to create a visualization in Splunk?",
             {"A": "Raw events", "B": "Results from a transforming command", "C": "Admin permissions", "D": "A dashboard"},
             ["B"],
             "Visualizations require data transformed by commands like stats, chart, timechart, top, or rare.",
             False),
            
            (82, "Domain 6.0: Creating Reports and Dashboards (12%)",
             "Which visualization would you use to show geographic distribution of data?",
             {"A": "Choropleth Map", "B": "Pie Chart", "C": "Line Chart", "D": "Single Value"},
             ["A"],
             "Choropleth maps display geographic data by shading regions based on data values.",
             False),
            
            (83, "Domain 6.0: Creating Reports and Dashboards (12%)",
             "How can you add a report to multiple dashboards?",
             {"A": "Copy and paste the report", "B": "Save the report and add it as a panel to each dashboard", "C": "Create a dashboard link", "D": "Reports can only be on one dashboard"},
             ["B"],
             "Reports are saved separately and can be added as panels to multiple dashboards.",
             False),
            
            (84, "Domain 6.0: Creating Reports and Dashboards (12%)",
             "What happens when you edit a report that's used in a dashboard?",
             {"A": "The dashboard panel updates automatically", "B": "You must manually update the dashboard", "C": "The dashboard breaks", "D": "A new report is created"},
             ["A"],
             "When you edit a saved report, all dashboard panels using that report automatically reflect the changes.",
             False),
            
            (85, "Domain 6.0: Creating Reports and Dashboards (12%)",
             "Which of the following can be added to a dashboard panel? (Select all that apply)",
             {"A": "Saved searches", "B": "Inline searches", "C": "Static images", "D": "HTML content", "E": "Input forms"},
             ["A", "B", "C", "D", "E"],
             "Dashboard panels can contain saved searches, inline searches, static images, HTML content, and input forms.",
             True),
            
            (86, "Domain 6.0: Creating Reports and Dashboards (12%)",
             "What is the purpose of dashboard tokens?",
             {"A": "To encrypt dashboard data", "B": "To enable dynamic content based on user input", "C": "To authenticate users", "D": "To schedule dashboard refreshes"},
             ["B"],
             "Tokens allow dashboard content to change dynamically based on user selections in input forms.",
             False),
            
            (87, "Domain 6.0: Creating Reports and Dashboards (12%)",
             "How do you create a drilldown from a dashboard panel?",
             {"A": "Edit the panel and configure drilldown settings", "B": "Use JavaScript", "C": "Create a workflow action", "D": "Drilldowns are automatic"},
             ["A"],
             "Drilldowns are configured in the panel settings, defining what happens when users click on visualization elements.",
             False),
            
            (88, "Domain 6.0: Creating Reports and Dashboards (12%)",
             "Which file format is used for dashboard definitions?",
             {"A": "JSON", "B": "XML", "C": "HTML", "D": "YAML"},
             ["B"],
             "Dashboards are defined in XML format, which can be edited directly for advanced customization.",
             False),
            
            (89, "Domain 6.0: Creating Reports and Dashboards (12%)",
             "What is the difference between a dashboard and a form?",
             {"A": "No difference - they're the same", "B": "Forms include input elements for user interaction", "C": "Dashboards are read-only", "D": "Forms require admin privileges"},
             ["B"],
             "Forms are dashboards with input elements (dropdowns, text boxes, time pickers) that users interact with.",
             False),
            
            # Domain 7.0: Creating and Using Lookups (6%)
            (90, "Domain 7.0: Creating and Using Lookups (6%)",
             "What is the primary purpose of a lookup in Splunk?",
             {"A": "To search external databases", "B": "To enrich event data with additional information from external files", "C": "To look up user information", "D": "To find missing events"},
             ["B"],
             "Lookups add fields from external files (usually CSV) to events based on matching field values.",
             False),
            
            (91, "Domain 7.0: Creating and Using Lookups (6%)",
             "Which commands can be used to work with lookups? (Select all that apply)",
             {"A": "lookup", "B": "inputlookup", "C": "outputlookup", "D": "appendlookup", "E": "lookupedit"},
             ["A", "B", "C"],
             "Valid lookup commands: lookup (enriches events), inputlookup (reads table), outputlookup (writes to table).",
             True),
            
            (92, "Domain 7.0: Creating and Using Lookups (6%)",
             "What are the steps to create an automatic lookup? (Select all that apply)",
             {"A": "Upload the lookup file", "B": "Create a lookup definition", "C": "Configure automatic lookup settings", "D": "Restart Splunk", "E": "Create a props.conf entry"},
             ["A", "B", "C"],
             "Automatic lookups require uploading the file, creating a definition, and configuring automatic lookup settings.",
             True),
            
            (93, "Domain 7.0: Creating and Using Lookups (6%)",
             "Which field type must exist for a lookup to work properly?",
             {"A": "A time field", "B": "A matching field between your events and the lookup table", "C": "An index field", "D": "A source field"},
             ["B"],
             "Lookups require at least one common field between events and the lookup table to match and enrich data.",
             False),
            
            (94, "Domain 7.0: Creating and Using Lookups (6%)",
             "How do you use `inputlookup` to view the contents of a lookup table?",
             {"A": "`| inputlookup tablename`", "B": "`inputlookup file=tablename`", "C": "`lookup tablename`", "D": "`| viewlookup tablename`"},
             ["A"],
             "Use | inputlookup tablename to view the contents of a lookup table as search results.",
             False),
            
            (95, "Domain 7.0: Creating and Using Lookups (6%)",
             "What does the `outputlookup` command do?",
             {"A": "Displays lookup results", "B": "Writes search results to a lookup file", "C": "Exports lookups to CSV", "D": "Deletes lookup tables"},
             ["B"],
             "outputlookup writes current search results to a lookup file, creating or updating it.",
             False),
            
            # Domain 8.0: Creating Scheduled Reports and Alerts (5%)
            (96, "Domain 8.0: Creating Scheduled Reports and Alerts (5%)",
             "Which of the following are valid trigger conditions for alerts? (Select all that apply)",
             {"A": "Number of results", "B": "Number of hosts", "C": "Number of sources", "D": "Custom condition based on search results", "E": "Time of day"},
             ["A", "B", "C", "D"],
             "Valid triggers: number of results, hosts, sources, and custom conditions. 'Time of day' is a schedule setting.",
             True),
            
            (97, "Domain 8.0: Creating Scheduled Reports and Alerts (5%)",
             "What is the difference between a real-time alert and a scheduled alert?",
             {"A": "Real-time alerts run continuously; scheduled alerts run at specified intervals", "B": "No difference", "C": "Real-time alerts are faster", "D": "Scheduled alerts are more accurate"},
             ["A"],
             "Real-time alerts continuously monitor data as it arrives. Scheduled alerts run at specified times.",
             False),
            
            (98, "Domain 8.0: Creating Scheduled Reports and Alerts (5%)",
             "Which alert actions are available in Splunk? (Select all that apply)",
             {"A": "Send email", "B": "Run a script", "C": "Webhook", "D": "Add to triggered alerts", "E": "Reboot server", "F": "Log event"},
             ["A", "B", "C", "D", "F"],
             "Valid actions: send email, run script, webhook, add to triggered alerts, log event. Not 'reboot server'.",
             True),
            
            (99, "Domain 8.0: Creating Scheduled Reports and Alerts (5%)",
             "How do you prevent an alert from triggering too frequently?",
             {"A": "Set throttling options", "B": "Decrease the search frequency", "C": "Use a longer time window", "D": "All of the above"},
             ["D"],
             "Prevent frequent triggering by throttling, decreasing frequency, or using longer time windows.",
             False),
            
            (100, "Domain 8.0: Creating Scheduled Reports and Alerts (5%)",
             "Where can you view the history of triggered alerts?",
             {"A": "Activity > Triggered Alerts", "B": "Settings > Alert History", "C": "Reports > Alerts", "D": "Search > Alert Log"},
             ["A"],
             "View alert history at Activity > Triggered Alerts, which shows when alerts fired and their results.",
             False),
        ]
        
        # Create Question objects
        for data in question_data:
            num, domain, text, options, correct, explanation, is_multi = data
            questions.append(Question(num, domain, text, options, correct, explanation, is_multi))
        
        return questions
    
    def format_time(self, seconds: int) -> str:
        """Format seconds into MM:SS format"""
        minutes = seconds // 60
        secs = seconds % 60
        return f"{minutes:02d}:{secs:02d}"
    
    def start_timer(self):
        """Start the countdown timer"""
        if not self.timer_running:
            self.timer_running = True
            self.timer_paused = False
            self.update_timer()
            self.pause_button.config(text="⏸ Pause", command=self.pause_timer)
    
    def pause_timer(self):
        """Pause the countdown timer"""
        if self.timer_running and not self.timer_paused:
            self.timer_paused = True
            if self.timer_id:
                self.root.after_cancel(self.timer_id)
            self.pause_button.config(text="▶ Resume", command=self.resume_timer)
            self.timer_label.config(text=f"⏸ PAUSED - {self.format_time(self.remaining_seconds)}")
    
    def resume_timer(self):
        """Resume the countdown timer"""
        if self.timer_running and self.timer_paused:
            self.timer_paused = False
            self.update_timer()
            self.pause_button.config(text="⏸ Pause", command=self.pause_timer)
    
    def stop_timer(self):
        """Stop the countdown timer"""
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
        self.timer_running = False
        self.timer_paused = False
    
    def update_timer(self):
        """Update the timer display and countdown"""
        if not self.timer_running or self.timer_paused or self.exam_submitted:
            return
        
        # Update timer display
        time_str = self.format_time(self.remaining_seconds)
        self.timer_label.config(text=f"⏱ {time_str}")
        
        # Change color based on time remaining
        if self.remaining_seconds <= 300:  # 5 minutes or less - RED
            self.timer_label.config(foreground='red', font=('Arial', 16, 'bold'))
        elif self.remaining_seconds <= 600:  # 10 minutes or less - ORANGE
            self.timer_label.config(foreground='orange', font=('Arial', 16, 'bold'))
        else:  # Normal - GREEN
            self.timer_label.config(foreground='green', font=('Arial', 16, 'bold'))
        
        # Show warning at 5 minutes
        if self.remaining_seconds == 300 and not self.five_minute_warning_shown:
            self.five_minute_warning_shown = True
            # Pause timer during dialog
            self.timer_paused = True
            messagebox.showwarning(
                "⚠️ 5 Minutes Remaining!",
                "You have 5 MINUTES left to complete the exam.\n\n"
                "• Review any flagged questions\n"
                "• Make sure all questions are answered\n"
                "• Click OK to continue\n\n"
                "The exam will auto-submit when time expires.",
                parent=self.root
            )
            self.timer_paused = False
        
        # Check if time expired
        if self.remaining_seconds <= 0:
            self.stop_timer()
            self.timer_label.config(text="⏱ 00:00 - TIME'S UP!", foreground='red')
            messagebox.showwarning(
                "⏰ Time Expired!",
                "Time has expired!\n\n"
                "The exam will now be automatically graded\n"
                "based on your current answers.",
                parent=self.root
            )
            self.finish_exam(auto_submit=True)
            return
        
        # Decrement time
        self.remaining_seconds -= 1
        
        # Schedule next update (1 second)
        self.timer_id = self.root.after(1000, self.update_timer)
    
    def setup_ui(self):
        """Set up the user interface"""
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Custom styles
        style.configure('Correct.TCheckbutton', foreground='green')
        style.configure('Incorrect.TCheckbutton', foreground='red')
        style.configure('Timer.TLabel', font=('Arial', 16, 'bold'))
        style.configure('Title.TLabel', font=('Arial', 18, 'bold'))
        style.configure('Domain.TLabel', font=('Arial', 11, 'italic'), foreground='#0066cc')
        
        # Main container
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(4, weight=1)
        
        # ===== HEADER FRAME =====
        header_frame = ttk.Frame(main_frame)
        header_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        header_frame.columnconfigure(1, weight=1)
        
        # Title
        title_label = ttk.Label(header_frame, text="🎓 Splunk Core User Certification Practice Exam",
                               style='Title.TLabel')
        title_label.grid(row=0, column=0, columnspan=4, pady=(0, 10))
        
        # Timer display (prominent, center)
        timer_frame = ttk.LabelFrame(header_frame, text="Exam Timer", padding="10")
        timer_frame.grid(row=1, column=0, columnspan=4, pady=(0, 10))
        
        self.timer_label = ttk.Label(timer_frame, text="⏱ 60:00", style='Timer.TLabel',
                                     foreground='green')
        self.timer_label.grid(row=0, column=0, padx=20)
        
        # Timer control buttons
        self.pause_button = ttk.Button(timer_frame, text="⏸ Pause", command=self.pause_timer, width=12)
        self.pause_button.grid(row=0, column=1, padx=5)
        
        self.stop_button = ttk.Button(timer_frame, text="⏹ Stop", command=self.stop_timer, width=12)
        self.stop_button.grid(row=0, column=2, padx=5)
        
        # Progress info
        progress_frame = ttk.Frame(header_frame)
        progress_frame.grid(row=2, column=0, columnspan=4, sticky=(tk.W, tk.E))
        progress_frame.columnconfigure(1, weight=1)
        
        self.progress_label = ttk.Label(progress_frame, text="Question 1 of 65", font=('Arial', 11))
        self.progress_label.grid(row=0, column=0, sticky=tk.W)
        
        self.answered_label = ttk.Label(progress_frame, text="Answered: 0/65", font=('Arial', 11))
        self.answered_label.grid(row=0, column=2, sticky=tk.E)
        
        # Progress bar
        self.progress_bar = ttk.Progressbar(progress_frame, length=400, mode='determinate', maximum=65)
        self.progress_bar.grid(row=0, column=1, padx=20, sticky=(tk.W, tk.E))
        
        # ===== DOMAIN LABEL =====
        self.domain_label = ttk.Label(main_frame, text="", style='Domain.TLabel')
        self.domain_label.grid(row=1, column=0, sticky=tk.W, pady=(0, 5))
        
        # ===== QUESTION FRAME =====
        question_frame = ttk.LabelFrame(main_frame, text="Question", padding="15")
        question_frame.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        question_frame.columnconfigure(0, weight=1)
        question_frame.rowconfigure(0, weight=1)
        
        # Question text with scroll
        self.question_text = scrolledtext.ScrolledText(question_frame, wrap=tk.WORD, 
                                                      height=5, font=('Arial', 12),
                                                      state='disabled', bg='#f8f8f8', fg='#1a1a1a')
        self.question_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # ===== OPTIONS FRAME =====
        self.options_frame = ttk.LabelFrame(main_frame, text="Answer Options", padding="15")
        self.options_frame.grid(row=3, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        self.options_frame.columnconfigure(0, weight=1)
        
        # Options will be created dynamically
        self.option_widgets = []
        
        # ===== EXPLANATION FRAME =====
        self.explanation_frame = ttk.LabelFrame(main_frame, text="Explanation", padding="15")
        self.explanation_frame.grid(row=4, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        self.explanation_frame.columnconfigure(0, weight=1)
        self.explanation_frame.rowconfigure(0, weight=1)
        
        self.explanation_text = scrolledtext.ScrolledText(self.explanation_frame, wrap=tk.WORD,
                                                         height=4, font=('Arial', 10),
                                                         state='disabled', bg='#fffef0', fg='#1a1a1a')
        self.explanation_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.explanation_frame.grid_remove()  # Hidden by default
        
        # ===== NAVIGATION FRAME =====
        nav_frame = ttk.Frame(main_frame)
        nav_frame.grid(row=5, column=0, sticky=(tk.W, tk.E), pady=(10, 0))
        
        # Left navigation buttons
        self.prev_button = ttk.Button(nav_frame, text="← Previous", command=self.prev_question, width=12)
        self.prev_button.grid(row=0, column=0, padx=5)
        
        self.submit_button = ttk.Button(nav_frame, text="✓ Submit Answer", 
                                       command=self.submit_answer, width=15)
        self.submit_button.grid(row=0, column=1, padx=5)
        
        self.next_button = ttk.Button(nav_frame, text="Next →", command=self.next_question, width=12)
        self.next_button.grid(row=0, column=2, padx=5)
        
        # Center spacer
        nav_frame.columnconfigure(3, weight=1)
        
        # Jump to question
        ttk.Label(nav_frame, text="Go to:").grid(row=0, column=4, padx=(20, 5))
        self.jump_var = tk.StringVar()
        self.jump_combo = ttk.Combobox(nav_frame, textvariable=self.jump_var, 
                                      values=[str(i) for i in range(1, 66)], 
                                      width=5, state='readonly')
        self.jump_combo.grid(row=0, column=5, padx=5)
        self.jump_combo.bind('<<ComboboxSelected>>', self.jump_to_question)
        
        # Finish exam button
        self.finish_button = ttk.Button(nav_frame, text="🏁 Finish Exam", 
                                       command=self.finish_exam, width=15)
        self.finish_button.grid(row=0, column=6, padx=(20, 5))
    
    def display_question(self):
        """Display the current question"""
        q = self.questions[self.current_question_index]
        
        # Update progress
        answered = sum(1 for q in self.questions if q.is_answered())
        self.progress_label.config(text=f"Question {q.number} of {len(self.questions)}")
        self.answered_label.config(text=f"Answered: {answered}/{len(self.questions)}")
        self.progress_bar['value'] = answered
        
        # Update domain
        self.domain_label.config(text=q.domain)
        
        # Update question text
        self.question_text.config(state='normal')
        self.question_text.delete(1.0, tk.END)
        
        question_display = f"Q{q.number}. {q.text}"
        if q.is_multi_select:
            question_display += "\n\n📋 (Select ALL that apply - multiple answers required)"
        
        self.question_text.insert(1.0, question_display)
        self.question_text.config(state='disabled')
        
        # Clear old options
        for widget in self.option_widgets:
            widget.destroy()
        self.option_widgets = []
        self.answer_vars = {}
        
        # Create new options
        for i, (key, value) in enumerate(sorted(q.options.items())):
            var = tk.BooleanVar(value=key in q.user_answers)
            self.answer_vars[key] = var
            
            if q.is_multi_select:
                widget = ttk.Checkbutton(self.options_frame, text=f"{key}. {value}",
                                        variable=var, command=self.on_answer_changed)
            else:
                widget = ttk.Radiobutton(self.options_frame, text=f"{key}. {value}",
                                        variable=self.answer_vars.get('_single', tk.StringVar()),
                                        value=key, command=lambda k=key: self.on_single_select(k))
                if '_single' not in self.answer_vars:
                    self.answer_vars['_single'] = tk.StringVar()
                    widget.config(variable=self.answer_vars['_single'])
                else:
                    widget.config(variable=self.answer_vars['_single'])
                
                # Set current selection
                if key in q.user_answers:
                    self.answer_vars['_single'].set(key)
            
            widget.grid(row=i, column=0, sticky=tk.W, pady=4, padx=10)
            self.option_widgets.append(widget)
        
        # Update navigation buttons
        self.prev_button.config(state='normal' if self.current_question_index > 0 else 'disabled')
        self.next_button.config(state='normal' if self.current_question_index < len(self.questions) - 1 else 'disabled')
        
        # Update jump combo
        self.jump_var.set(str(q.number))
        
        # Show/hide explanation
        if q.is_answered() and not self.exam_submitted:
            self.show_explanation(submitted=False)
        elif self.exam_submitted:
            self.show_explanation(submitted=True)
        else:
            self.explanation_frame.grid_remove()
    
    def on_single_select(self, key: str):
        """Handle single-select radio button selection"""
        q = self.questions[self.current_question_index]
        q.user_answers = {key}
        self.submit_button.config(state='normal')
    
    def on_answer_changed(self):
        """Handle checkbox selection changes"""
        self.submit_button.config(state='normal')
    
    def submit_answer(self):
        """Submit the current answer"""
        q = self.questions[self.current_question_index]
        
        if q.is_multi_select:
            # Collect all checked options
            q.user_answers = {k for k, v in self.answer_vars.items() if v.get() and k != '_single'}
        else:
            # Single select
            selected = self.answer_vars.get('_single')
            if selected and selected.get():
                q.user_answers = {selected.get()}
        
        if not q.user_answers:
            messagebox.showwarning("No Answer", "Please select an answer before submitting.")
            return
        
        # Show explanation
        self.show_explanation(submitted=False)
        
        # Update display
        self.display_question()
        
        # Show result
        if q.is_correct():
            messagebox.showinfo("✓ Correct!", "Great job! Your answer is correct.")
        else:
            correct_str = ", ".join(sorted(q.correct_answers))
            messagebox.showinfo("✗ Incorrect", f"The correct answer is: {correct_str}\n\nReview the explanation below.")
    
    def show_explanation(self, submitted=False):
        """Show the explanation for the current question"""
        q = self.questions[self.current_question_index]
        
        # Show explanation frame
        self.explanation_frame.grid()
        
        # Update explanation text
        self.explanation_text.config(state='normal')
        self.explanation_text.delete(1.0, tk.END)
        
        if q.is_answered() or submitted:
            result = "✓ CORRECT!" if q.is_correct() else "✗ INCORRECT"
            self.explanation_text.insert(1.0, f"{result}\n\n")
            
            correct_str = ", ".join(sorted(q.correct_answers))
            self.explanation_text.insert(tk.END, f"Correct Answer(s): {correct_str}\n\n")
            
            if q.user_answers:
                user_str = ", ".join(sorted(q.user_answers))
                self.explanation_text.insert(tk.END, f"Your Answer(s): {user_str}\n\n")
            
            self.explanation_text.insert(tk.END, f"Explanation: {q.explanation}")
        
        self.explanation_text.config(state='disabled')
    
    def prev_question(self):
        """Go to previous question"""
        if self.current_question_index > 0:
            self.current_question_index -= 1
            self.display_question()
    
    def next_question(self):
        """Go to next question"""
        if self.current_question_index < len(self.questions) - 1:
            self.current_question_index += 1
            self.display_question()
    
    def jump_to_question(self, event=None):
        """Jump to a specific question"""
        try:
            question_num = int(self.jump_var.get())
            self.current_question_index = question_num - 1
            self.display_question()
        except ValueError:
            pass
    
    def finish_exam(self, auto_submit=False):
        """Finish the exam and show results"""
        # Stop the timer
        self.stop_timer()
        
        # Check for unanswered questions
        unanswered = [q.number for q in self.questions if not q.is_answered()]
        
        if unanswered and not auto_submit and not self.exam_submitted:
            result = messagebox.askyesno(
                "Unanswered Questions",
                f"You have {len(unanswered)} unanswered question(s).\n\n"
                f"Questions: {', '.join(map(str, unanswered[:15]))}"
                f"{'...' if len(unanswered) > 15 else ''}\n\n"
                "Do you want to finish anyway?"
            )
            if not result:
                # Resume timer if user wants to continue
                if self.remaining_seconds > 0:
                    self.start_timer()
                return
        
        # Calculate score
        correct = sum(1 for q in self.questions if q.is_correct())
        total = len(self.questions)
        percentage = (correct / total) * 100
        
        # Mark exam as submitted
        self.exam_submitted = True
        
        # Calculate time used
        time_used_seconds = self.total_seconds - self.remaining_seconds
        time_used = self.format_time(time_used_seconds)
        
        # Calculate domain scores
        domain_scores = {}
        for q in self.questions:
            domain = q.domain.split(':')[0].strip()
            if domain not in domain_scores:
                domain_scores[domain] = {'correct': 0, 'total': 0}
            domain_scores[domain]['total'] += 1
            if q.is_correct():
                domain_scores[domain]['correct'] += 1
        
        # Build results message
        result_message = f"""
╔══════════════════════════════════════════╗
║           EXAM RESULTS                    ║
╚══════════════════════════════════════════╝

⏱  Time Used: {time_used}
📊 Score: {correct} / {total} ({percentage:.1f}%)

═══════════════════════════════════════════
BREAKDOWN BY DOMAIN:
═══════════════════════════════════════════
"""
        
        for domain, scores in sorted(domain_scores.items()):
            pct = (scores['correct'] / scores['total']) * 100 if scores['total'] > 0 else 0
            bar = "█" * int(pct / 10) + "░" * (10 - int(pct / 10))
            result_message += f"\n{domain}:\n  {scores['correct']}/{scores['total']} ({pct:.0f}%) {bar}"
        
        # Passing criteria (typically 70% for Splunk certifications)
        passing = percentage >= 70
        result_message += f"""

═══════════════════════════════════════════
STATUS: {'🎉 PASSED ✓' if passing else '❌ FAILED ✗'}
(Passing score: 70%)
═══════════════════════════════════════════
"""
        
        if passing:
            result_message += "\nCongratulations! You're ready for the real exam!"
        else:
            result_message += "\nKeep studying! Review the explanations for missed questions."
        
        # Show results in a larger dialog
        self.show_results_dialog(result_message, percentage, passing)
        
        # Update timer display
        self.timer_label.config(text=f"✓ Completed - {time_used}")
        
        # Update display to show all explanations
        self.display_question()
    
    def show_results_dialog(self, message: str, percentage: float, passed: bool):
        """Show exam results in a custom dialog"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Exam Results")
        dialog.geometry("500x600")
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Center the dialog
        dialog.update_idletasks()
        x = (dialog.winfo_screenwidth() - 500) // 2
        y = (dialog.winfo_screenheight() - 600) // 2
        dialog.geometry(f"+{x}+{y}")
        
        # Results text
        text = scrolledtext.ScrolledText(dialog, wrap=tk.WORD, font=('Courier', 10),
                                        width=60, height=30)
        text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        text.insert(1.0, message)
        text.config(state='disabled')
        
        # Close button
        close_btn = ttk.Button(dialog, text="Close", command=dialog.destroy)
        close_btn.pack(pady=10)
    
    def on_closing(self):
        """Handle window close event"""
        if not self.exam_submitted:
            result = messagebox.askyesno(
                "Exit Exam",
                "Are you sure you want to exit?\n\n"
                "Your progress will be lost!"
            )
            if not result:
                return
        
        self.stop_timer()
        self.root.destroy()


def main():
    """Main entry point"""
    root = tk.Tk()
    
    # Set window icon (if available)
    try:
        root.iconbitmap('splunk.ico')
    except:
        pass
    
    app = SplunkPracticeExam(root)
    root.mainloop()


if __name__ == "__main__":
    main()
