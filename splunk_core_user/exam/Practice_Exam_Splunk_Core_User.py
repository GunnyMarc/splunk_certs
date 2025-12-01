#!/usr/bin/env python3
"""
Splunk Core User Certification Practice Exam
Interactive GUI Application with 65 questions and 60-minute timer
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import re
from typing import List, Dict, Tuple
import random


class Question:
    """Represents a single exam question"""
    def __init__(self, number: int, domain: str, text: str, options: Dict[str, str], 
                 correct_answer: str, explanation: str):
        self.number = number
        self.domain = domain
        self.text = text
        self.options = options  # {'A': 'option text', 'B': 'option text', ...}
        self.correct_answer = correct_answer
        self.explanation = explanation
        self.user_answer = None
        
    def is_correct(self) -> bool:
        """Check if user's answer is correct"""
        return self.user_answer == self.correct_answer
    
    def is_answered(self) -> bool:
        """Check if question has been answered"""
        return self.user_answer is not None


class SplunkPracticeExam:
    """Main application class for the practice exam"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Splunk Core User - Practice Exam")
        self.root.geometry("1000x750")
        
        # Load questions
        self.questions = self.load_questions()
        self.current_question_index = 0
        self.selected_answer = tk.StringVar()
        
        # Track exam state
        self.exam_submitted = False
        
        # Timer variables
        self.total_seconds = 60 * 60  # 60 minutes in seconds
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
        
    def load_questions(self) -> List[Question]:
        """Parse questions from the markdown content"""
        questions = []
        
        # Question data embedded in the application
        question_data = [
            # Domain 1: Splunk Basics (5%)
            (1, "Domain 1.0: Splunk Basics (5%)", 
             "Which Splunk component is responsible for parsing incoming data and storing it on disk?",
             {"A": "Universal Forwarder", "B": "Search Head", "C": "Indexer", "D": "Heavy Forwarder"},
             "C", "The Indexer processes incoming data, parses it, and stores it as events in indexes."),
            
            (2, "Domain 1.0: Splunk Basics (5%)",
             "What is the primary function of a Splunk App?",
             {"A": "To forward data to external systems.", 
              "B": "To provide a specific collection of configurations, dashboards, and knowledge objects for a use case.",
              "C": "To manage user licenses.", 
              "D": "To compress raw data logs."},
             "B", "Apps are collections of knowledge objects and configurations designed for specific use cases."),
            
            (3, "Domain 1.0: Splunk Basics (5%)",
             "Which of the following is a default role in Splunk Enterprise?",
             {"A": "Power", "B": "SuperUser", "C": "Network_Admin", "D": "Auditor"},
             "A", "\"Power\" (along with Admin and User) is a standard default role in Splunk."),
            
            # Domain 2: Basic Searching (22%)
            (4, "Domain 2.0: Basic Searching (22%)",
             "When running a search, what is the most effective way to limit the number of events retrieved from the disk?",
             {"A": "Use the `head` command.", "B": "Use the `fields` command.", 
              "C": "Specify a narrower time range.", "D": "Use the `table` command."},
             "C", "Time range is the most efficient filter because it restricts the data read from the index before processing."),
            
            (5, "Domain 2.0: Basic Searching (22%)",
             "What is the correct syntax to search for events containing the phrase \"failed login\"?",
             {"A": "failed AND login", "B": "\"failed login\"", 
              "C": "failed_login", "D": "string=failed login"},
             "B", "Phrases must be enclosed in double quotes."),
            
            (6, "Domain 2.0: Basic Searching (22%)",
             "Which time picker setting would you use to search data from the \"beginning of today\"?",
             {"A": "Last 24 hours", "B": "-1d", "C": "Earliest=@d", "D": "Previous business day"},
             "C", "`@d` snaps the time to the beginning of the current day (00:00:00)."),
            
            (7, "Domain 2.0: Basic Searching (22%)",
             "How do Boolean operators (AND, OR, NOT) affect search precedence if no parentheses are used?",
             {"A": "OR is evaluated first.", "B": "AND is evaluated first.", 
              "C": "NOT is evaluated first.", "D": "They are evaluated left-to-right."},
             "C", "The order of precedence is NOT, then OR, then AND. If evaluating specific operators: `Keyword1 OR Keyword2 AND Keyword3` is read as `Keyword1 OR (Keyword2 AND Keyword3)`."),
            
            (8, "Domain 2.0: Basic Searching (22%)",
             "Which symbol is used to snap a time range to a specific unit (e.g., beginning of the minute)?",
             {"A": "*", "B": "$", "C": "@", "D": "#"},
             "C", "The `@` symbol is used to round down (snap) to the nearest time unit."),
            
            (9, "Domain 2.0: Basic Searching (22%)",
             "What does the \"Search Mode\" setting (Fast, Smart, Verbose) control?",
             {"A": "The speed of the indexer.", 
              "B": "How many events are returned and which fields are discovered.",
              "C": "The number of users who can view the search.", 
              "D": "The expiration time of the search job."},
             "B", "Modes control field discovery and event data return to optimize performance."),
            
            (10, "Domain 2.0: Basic Searching (22%)",
             "Which command allows you to save your search results to a CSV format?",
             {"A": "Export", "B": "Save As Report", "C": "Save As Dashboard", "D": "Print"},
             "A", "The Export function allows results to be downloaded as CSV, JSON, or XML."),
            
            (11, "Domain 2.0: Basic Searching (22%)",
             "In the search results, what does the \"Timeline\" visual represent?",
             {"A": "The time the search took to run.", 
              "B": "The number of events matching the search query over time.",
              "C": "The CPU usage of the indexer.", 
              "D": "The bandwidth used by the forwarder."},
             "B", "The timeline shows the distribution of event counts over the selected time range."),
            
            (12, "Domain 2.0: Basic Searching (22%)",
             "When using the `earliest` and `latest` time modifiers in a search string, what is the correct syntax to look back 15 minutes?",
             {"A": "earliest=15m", "B": "earliest=-15m", "C": "time=-15m", "D": "start=now-15m"},
             "B", "The minus sign indicates \"ago\"."),
            
            (13, "Domain 2.0: Basic Searching (22%)",
             "Which of the following is NOT a status used to control a search job?",
             {"A": "Pause", "B": "Stop", "C": "Finalize", "D": "Compress"},
             "D", "You can Pause, Stop, or Finalize a job, but \"Compress\" is not a job control."),
            
            (14, "Domain 2.0: Basic Searching (22%)",
             "What happens if you click a bar in the Timeline?",
             {"A": "It deletes the events in that time bucket.", 
              "B": "It zooms into that specific time range.",
              "C": "It highlights the events in red.", 
              "D": "It exports the data."},
             "B", "Clicking a bar zooms the search to that specific time bucket."),
            
            (15, "Domain 2.0: Basic Searching (22%)",
             "If a search is running too slowly, what can you do to see partial results immediately without stopping the search?",
             {"A": "Click \"Finalize\".", "B": "Click \"Pause\".", 
              "C": "Click \"Send to Background\".", "D": "Switch to \"Real-time\"."},
             "A", "Finalize stops the search but keeps the results found so far."),
            
            (16, "Domain 2.0: Basic Searching (22%)",
             "Which of the following is considered a \"Best Practice\" for searching?",
             {"A": "Use wildcards at the beginning of strings (e.g., `*fail`).", 
              "B": "Specify the index name.",
              "C": "Search `All Time` by default.", 
              "D": "Use as many OR operators as possible."},
             "B", "Specifying the index limits the scope and improves performance."),
            
            (17, "Domain 2.0: Basic Searching (22%)",
             "What allows you to view the raw events in a clean list format?",
             {"A": "The Events tab.", "B": "The Statistics tab.", 
              "C": "The Visualization tab.", "D": "The Job Inspector."},
             "A", "The Events tab displays the raw data."),
            
            # Domain 3: Using Fields in Searches (20%)
            (18, "Domain 3.0: Using Fields in Searches (20%)",
             "Where are \"Selected Fields\" displayed?",
             {"A": "In the main event list, under every event.", 
              "B": "Only in the Job Inspector.",
              "C": "In the Fields sidebar, at the top of the list.", 
              "D": "In the search bar."},
             "C", "Selected fields appear at the top of the sidebar and are also visible in the event summaries."),
            
            (19, "Domain 3.0: Using Fields in Searches (20%)",
             "Which three fields are selected by default?",
             {"A": "host, user, ip", "B": "host, source, sourcetype", 
              "C": "index, source, splunk_server", "D": "time, event_id, host"},
             "B", "`host`, `source`, and `sourcetype` are the default selected fields."),
            
            (20, "Domain 3.0: Using Fields in Searches (20%)",
             "What criteria must a field meet to be listed as an \"Interesting Field\"?",
             {"A": "It must be a numeric field.", 
              "B": "It must appear in at least 20% of the events.",
              "C": "It must be manually selected by the user.", 
              "D": "It must contain a unique value."},
             "B", "Interesting fields appear in >20% of search results."),
            
            (21, "Domain 3.0: Using Fields in Searches (20%)",
             "How can you add a field to the \"Selected Fields\" list?",
             {"A": "Click the field in the \"Interesting Fields\" list and select \"Yes\" for Selected.",
              "B": "Use the `select` command in SPL.",
              "C": "Right-click the event and choose \"Promote\".",
              "D": "It happens automatically after 10 searches."},
             "A", "You can manually promote a field via the sidebar."),
            
            (22, "Domain 3.0: Using Fields in Searches (20%)",
             "Which command would you use to remove specific fields from the search results?",
             {"A": "`remove fieldname`", "B": "`fields - fieldname`", 
              "C": "`delete fieldname`", "D": "`exclude fieldname`"},
             "B", "The `fields` command with a minus sign excludes fields."),
            
            (23, "Domain 3.0: Using Fields in Searches (20%)",
             "What is the difference between `source` and `sourcetype`?",
             {"A": "`source` is the format; `sourcetype` is the file name.",
              "B": "`source` is the file name/input stream; `sourcetype` is the data classification/format.",
              "C": "They are identical.",
              "D": "`sourcetype` is the server name."},
             "B", "Source is the origin (e.g., `/var/log/syslog`), Sourcetype is the format (e.g., `linux_secure`)."),
            
            (24, "Domain 3.0: Using Fields in Searches (20%)",
             "True or False: Field names in Splunk are case-sensitive.",
             {"A": "True", "B": "False"},
             "A", "Field _names_ (e.g., `ClientIP` vs `clientip`) are case-sensitive. Field _values_ are generally case-insensitive."),
            
            (25, "Domain 3.0: Using Fields in Searches (20%)",
             "If you search `status=404`, \"status\" is the ______ and \"404\" is the ______.",
             {"A": "Value, Field", "B": "Field, Value", "C": "Tag, Alias", "D": "Host, Source"},
             "B", "Left of the equals sign is the Field Name; right is the Value."),
            
            (26, "Domain 3.0: Using Fields in Searches (20%)",
             "Which symbol is used to perform a wildcard match within a field value (e.g., `user=admin*`)?",
             {"A": "%", "B": "?", "C": "*", "D": "!"},
             "C", "The asterisk is the wildcard in SPL."),
            
            (27, "Domain 3.0: Using Fields in Searches (20%)",
             "What does the `!=` operator do in a field search?",
             {"A": "It looks for events where the field does NOT equal the value.",
              "B": "It sets the field to a new value.",
              "C": "It matches values that sound similar.",
              "D": "It looks for the field in all indexes."},
             "A", "`!=` stands for \"Not Equal\"."),
            
            (28, "Domain 3.0: Using Fields in Searches (20%)",
             "Can you search for a value without specifying a field name (e.g., `error` instead of `status=error`)?",
             {"A": "Yes, using keywords.", "B": "No, field names are mandatory.",
              "C": "Only in Verbose mode.", "D": "Only for numeric values."},
             "A", "Keyword searches scan the raw text for the term."),
            
            (29, "Domain 3.0: Using Fields in Searches (20%)",
             "To display only the `clientip` and `action` fields in the results table, which command should you use?",
             {"A": "`return clientip, action`", "B": "`table clientip, action`",
              "C": "`list clientip, action`", "D": "`show clientip, action`"},
             "B", "`table` creates a formatted table of only the specified fields."),
            
            (30, "Domain 3.0: Using Fields in Searches (20%)",
             "Which command renames a field in search results?",
             {"A": "`change oldname TO newname`", "B": "`rename oldname AS newname`",
              "C": "`alias oldname newname`", "D": "`modify oldname = newname`"},
             "B", "`rename` changes the field name in the output."),
            
            # Domain 4: Using Basic Transforming Commands (15%)
            (31, "Domain 4.0: Using Basic Transforming Commands (15%)",
             "What is a \"Transforming Command\"?",
             {"A": "A command that converts data from CSV to JSON.",
              "B": "A command that changes raw data into a table or visualization.",
              "C": "A command that forwards data.",
              "D": "A command that updates the index."},
             "B", "Transforming commands convert event data into statistical or summary information."),
            
            (32, "Domain 4.0: Using Basic Transforming Commands (15%)",
             "Which command removes duplicate events based on a specified field?",
             {"A": "`unique`", "B": "`dedup`", "C": "`filter`", "D": "`distinct`"},
             "B", "`dedup` removes duplicate values."),
            
            (33, "Domain 4.0: Using Basic Transforming Commands (15%)",
             "What does the `sort` command do?",
             {"A": "It organizes events by time.",
              "B": "It orders results based on specified fields (ascending or descending).",
              "C": "It deletes unsorted data.",
              "D": "It compresses the data."},
             "B", "`sort` can order by field values."),
            
            (34, "Domain 4.0: Using Basic Transforming Commands (15%)",
             "By default, does `sort` order results in ascending or descending order?",
             {"A": "Ascending", "B": "Descending", "C": "Random", "D": "Alphabetical"},
             "A", "`sort` defaults to ascending order."),
            
            (35, "Domain 4.0: Using Basic Transforming Commands (15%)",
             "To reverse the sort order (descending), which prefix do you use?",
             {"A": "reverse", "B": "-", "C": "desc", "D": "down"},
             "B", "A minus sign before the field name (e.g., `sort -count`) sorts in descending order."),
            
            (36, "Domain 4.0: Using Basic Transforming Commands (15%)",
             "Which command is used to format search results into a table?",
             {"A": "`format`", "B": "`table`", "C": "`grid`", "D": "`display`"},
             "B", "`table` is the command to format results into columns."),
            
            (37, "Domain 4.0: Using Basic Transforming Commands (15%)",
             "When using `dedup`, which event is kept by default?",
             {"A": "The oldest event.", "B": "The most recent event.",
              "C": "A random event.", "D": "The event with the most fields."},
             "B", "`dedup` keeps the first result found, which (in standard reverse-chronological order) is the most recent one."),
            
            (38, "Domain 4.0: Using Basic Transforming Commands (15%)",
             "Can you include multiple commands in a single search string?",
             {"A": "No, only one command per search.",
              "B": "Yes, by separating them with a pipe `|`.",
              "C": "Yes, by separating them with a comma `,`.",
              "D": "Yes, by separating them with the word `AND`."},
             "B", "Commands are chained using pipes."),
            
            (39, "Domain 4.0: Using Basic Transforming Commands (15%)",
             "Which command allows you to keep only specific fields and discard the rest (except time)?",
             {"A": "`fields`", "B": "`table`", "C": "`filter`", "D": "`keep`"},
             "A", "`fields` (without a minus) keeps only the listed fields."),
            
            (40, "Domain 4.0: Using Basic Transforming Commands (15%)",
             "To search specifically in the \"web\" index, what syntax should you use?",
             {"A": "`index:web`", "B": "`index=web`", 
              "C": "`using index web`", "D": "`source=web`"},
             "B", "`index=web` is the standard syntax."),
            
            # Domain 5: Using Basic Transforming Commands - Stats (15%)
            (41, "Domain 5.0: Using Basic Transforming Commands (15%)",
             "Which command finds the most frequent values of a field?",
             {"A": "`rare`", "B": "`top`", "C": "`stats`", "D": "`common`"},
             "B", "`top` returns the most frequent values."),
            
            (42, "Domain 5.0: Using Basic Transforming Commands (15%)",
             "Which command finds the least frequent values of a field?",
             {"A": "`bottom`", "B": "`rare`", "C": "`limit`", "D": "`least`"},
             "B", "`rare` returns the least frequent values."),
            
            (43, "Domain 5.0: Using Basic Transforming Commands (15%)",
             "What fields are created by the `top` command by default?",
             {"A": "`count` and `percent`", "B": "`total` and `rate`",
              "C": "`sum` and `avg`", "D": "`hits` and `score`"},
             "A", "`top` calculates the count and the percentage of the total for each value."),
            
            (44, "Domain 5.0: Using Basic Transforming Commands (15%)",
             "Which `stats` function would you use to count the total number of events?",
             {"A": "`sum`", "B": "`count`", "C": "`list`", "D": "`total`"},
             "B", "`count` is the function for counting events."),
            
            (45, "Domain 5.0: Using Basic Transforming Commands (15%)",
             "Which `stats` function calculates the distinct (unique) count of a field?",
             {"A": "`dc` (or `distinct_count`)", "B": "`uc`", 
              "C": "`uniq`", "D": "`count_distinct`"},
             "A", "`dc` stands for Distinct Count."),
            
            (46, "Domain 5.0: Using Basic Transforming Commands (15%)",
             "What is the correct syntax to calculate the average of a field named \"duration\"?",
             {"A": "`stats avg(duration)`", "B": "`stats average=duration`",
              "C": "`stats mean of duration`", "D": "`table avg(duration)`"},
             "A", "`stats` uses functions like `avg(field)`."),
            
            (47, "Domain 5.0: Using Basic Transforming Commands (15%)",
             "To group stats results by a specific field (e.g., User), which clause do you use?",
             {"A": "`group by User`", "B": "`split User`", 
              "C": "`by User`", "D": "`for User`"},
             "C", "The syntax is `stats <function> by <field>`."),
            
            (48, "Domain 5.0: Using Basic Transforming Commands (15%)",
             "By default, how many results does the `top` command return?",
             {"A": "5", "B": "10", "C": "20", "D": "100"},
             "B", "`top` defaults to the top 10 results."),
            
            (49, "Domain 5.0: Using Basic Transforming Commands (15%)",
             "Which command allows you to calculate statistics (like sum, avg, max) from your search results?",
             {"A": "`calc`", "B": "`stats`", "C": "`math`", "D": "`evaluate`"},
             "B", "`stats` is the primary statistical command."),
            
            (50, "Domain 5.0: Using Basic Transforming Commands (15%)",
             "What does the `list` function do within the `stats` command?",
             {"A": "It lists every value of the field.",
              "B": "It lists only unique values.",
              "C": "It creates a bulleted list in the dashboard.",
              "D": "It sorts the values."},
             "A", "`list(field)` lists all values (use `values(field)` for unique ones)."),
            
            # Domain 6: Creating Reports and Dashboards (12%)
            (51, "Domain 6.0: Creating Reports and Dashboards (12%)",
             "How do you turn a search into a Report?",
             {"A": "Click \"Save As\" > \"Report\".",
              "B": "Copy the text to a Word doc.",
              "C": "Click \"Export\" > \"Report\".",
              "D": "Use the `report` command."},
             "A", "Reports are created via the Save As menu."),
            
            (52, "Domain 6.0: Creating Reports and Dashboards (12%)",
             "Can a Report be scheduled to run automatically?",
             {"A": "Yes.", "B": "No."},
             "A", "Reports can be scheduled (Scheduled Reports)."),
            
            (53, "Domain 6.0: Creating Reports and Dashboards (12%)",
             "Which visualization is best for showing a trend over time?",
             {"A": "Pie Chart", "B": "Single Value", "C": "Line Chart", "D": "Gauge"},
             "C", "Line charts (typically from `timechart`) are best for trends."),
            
            (54, "Domain 6.0: Creating Reports and Dashboards (12%)",
             "What is a \"Panel\" in a dashboard?",
             {"A": "The settings menu.",
              "B": "A container for a visualization or report on the dashboard.",
              "C": "The user login screen.",
              "D": "The search bar."},
             "B", "Dashboards are composed of one or more Panels."),
            
            (55, "Domain 6.0: Creating Reports and Dashboards (12%)",
             "How do you add a search to an existing dashboard?",
             {"A": "Run the search, click \"Save As\" > \"Dashboard Panel\", and select the existing dashboard.",
              "B": "You must delete the dashboard and recreate it.",
              "C": "Drag and drop the search bar.",
              "D": "Use the `dashboard` command."},
             "A", "You can add to existing dashboards via the Save menu."),
            
            (56, "Domain 6.0: Creating Reports and Dashboards (12%)",
             "What is the XML source in a dashboard used for?",
             {"A": "To compile the code.",
              "B": "To edit the dashboard layout and behavior (advanced editing).",
              "C": "To store user passwords.",
              "D": "To connect to the internet."},
             "B", "The dashboard definition is stored in Simple XML, which can be edited."),
            
            (57, "Domain 6.0: Creating Reports and Dashboards (12%)",
             "Which visualization would be appropriate for comparing the \"share\" or \"percentage\" of a whole?",
             {"A": "Line Chart", "B": "Pie Chart", "C": "Marker Map", "D": "Scatter Plot"},
             "B", "Pie charts display parts of a whole."),
            
            (58, "Domain 6.0: Creating Reports and Dashboards (12%)",
             "Can you edit a dashboard using a drag-and-drop interface?",
             {"A": "Yes, using the UI Editor.", "B": "No, only XML is supported."},
             "A", "Splunk provides a UI editor for moving panels."),
            
            # Domain 7: Creating and Using Lookups (6%)
            (59, "Domain 7.0: Creating and Using Lookups (6%)",
             "What is a \"Lookup\" used for?",
             {"A": "To search the internet.",
              "B": "To enrich event data with static fields from an external file (e.g., CSV).",
              "C": "To look up other users.",
              "D": "To find lost data."},
             "B", "Lookups match field values in events to data in a file to add more context (e.g., adding \"Product Name\" based on \"Product ID\")."),
            
            (60, "Domain 7.0: Creating and Using Lookups (6%)",
             "Which file type is most commonly used for lookups?",
             {"A": ".exe", "B": ".csv", "C": ".docx", "D": ".mp3"},
             "B", "CSV (Comma Separated Values) is the standard format."),
            
            (61, "Domain 7.0: Creating and Using Lookups (6%)",
             "What are the two main steps to create a file-based lookup?",
             {"A": "1. Upload the file, 2. Create a Lookup Definition.",
              "B": "1. Email the file to support, 2. Wait.",
              "C": "1. Put the file on the desktop, 2. Run `inputlookup`.",
              "D": "1. Rename the file, 2. Zip the file."},
             "A", "You must upload the file and then define it so Splunk knows how to use it."),
            
            (62, "Domain 7.0: Creating and Using Lookups (6%)",
             "Which command loads a lookup table into search results?",
             {"A": "`load`", "B": "`inputlookup` (or `lookup`)", 
              "C": "`find`", "D": "`search_file`"},
             "B", "`inputlookup` reads the table; `lookup` matches it against events."),
            
            # Domain 8: Creating Scheduled Reports and Alerts (5%)
            (63, "Domain 8.0: Creating Scheduled Reports and Alerts (5%)",
             "What distinguishes an \"Alert\" from a \"Scheduled Report\"?",
             {"A": "Alerts are manual; Reports are automatic.",
              "B": "Alerts are triggered by specific conditions (e.g., errors > 5) and perform actions; Reports run on a schedule to present data.",
              "C": "Alerts cost money; Reports are free.",
              "D": "Alerts are only for admins."},
             "B", "Alerts are condition-based triggers."),
            
            (64, "Domain 8.0: Creating Scheduled Reports and Alerts (5%)",
             "Which of the following is a valid \"Alert Action\"?",
             {"A": "Send an email.", "B": "Reboot the server.", 
              "C": "Print the screen.", "D": "Delete the user."},
             "A", "Sending an email (or logging to an index, running a script) is a standard action."),
            
            (65, "Domain 8.0: Creating Scheduled Reports and Alerts (5%)",
             "Where can you view alerts that have recently triggered?",
             {"A": "Activity > Triggered Alerts.", "B": "Settings > Indexes.",
              "C": "Help > About.", "D": "The Login Screen."},
             "A", "The \"Triggered Alerts\" page lists fired instances."),
        ]
        
        # Create Question objects
        for data in question_data:
            questions.append(Question(*data))
        
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
            self.pause_button.config(text="⏸ Pause Timer", command=self.pause_timer)
    
    def pause_timer(self):
        """Pause the countdown timer"""
        if self.timer_running and not self.timer_paused:
            self.timer_paused = True
            if self.timer_id:
                self.root.after_cancel(self.timer_id)
            self.pause_button.config(text="▶ Resume Timer", command=self.resume_timer)
    
    def resume_timer(self):
        """Resume the countdown timer"""
        if self.timer_running and self.timer_paused:
            self.timer_paused = False
            self.update_timer()
            self.pause_button.config(text="⏸ Pause Timer", command=self.pause_timer)
    
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
        self.timer_label.config(text=f"⏱ Time Remaining: {time_str}")
        
        # Change color based on time remaining
        if self.remaining_seconds <= 300:  # 5 minutes or less
            self.timer_label.config(foreground='red', font=('Arial', 14, 'bold'))
        elif self.remaining_seconds <= 600:  # 10 minutes or less
            self.timer_label.config(foreground='orange', font=('Arial', 14, 'bold'))
        else:
            self.timer_label.config(foreground='green', font=('Arial', 14, 'bold'))
        
        # Show warning at 5 minutes
        if self.remaining_seconds == 300 and not self.five_minute_warning_shown:
            self.five_minute_warning_shown = True
            messagebox.showwarning(
                "Time Warning",
                "⚠️ 5 Minutes Remaining!\n\n"
                "You have 5 minutes left to complete the exam.\n"
                "Make sure to review and submit your answers.",
                parent=self.root
            )
        
        # Check if time expired
        if self.remaining_seconds <= 0:
            self.stop_timer()
            self.timer_label.config(text="⏱ Time's Up!", foreground='red')
            messagebox.showwarning(
                "Time Expired",
                "⏰ Time has expired!\n\n"
                "The exam will now be automatically graded based on your answers.",
                parent=self.root
            )
            self.finish_exam()
            return
        
        # Decrement time
        self.remaining_seconds -= 1
        
        # Schedule next update
        self.timer_id = self.root.after(1000, self.update_timer)
    
    def setup_ui(self):
        """Set up the user interface"""
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Main container
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(3, weight=1)
        
        # Header frame
        header_frame = ttk.Frame(main_frame)
        header_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        header_frame.columnconfigure(1, weight=1)
        
        # Title
        title_label = ttk.Label(header_frame, text="Splunk Core User Certification Practice Exam",
                               font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 5))
        
        # Timer display (prominent position)
        self.timer_label = ttk.Label(header_frame, text="⏱ Time Remaining: 60:00",
                                     font=('Arial', 14, 'bold'), foreground='green')
        self.timer_label.grid(row=1, column=0, columnspan=3, pady=(0, 5))
        
        # Timer controls frame
        timer_controls = ttk.Frame(header_frame)
        timer_controls.grid(row=2, column=0, columnspan=3, pady=(0, 10))
        
        self.pause_button = ttk.Button(timer_controls, text="⏸ Pause Timer", 
                                      command=self.pause_timer)
        self.pause_button.grid(row=0, column=0, padx=5)
        
        self.stop_button = ttk.Button(timer_controls, text="⏹ Stop Timer", 
                                     command=self.stop_timer)
        self.stop_button.grid(row=0, column=1, padx=5)
        
        # Progress info
        self.progress_label = ttk.Label(header_frame, text="", font=('Arial', 10))
        self.progress_label.grid(row=3, column=0, sticky=tk.W)
        
        self.score_label = ttk.Label(header_frame, text="", font=('Arial', 10))
        self.score_label.grid(row=3, column=2, sticky=tk.E)
        
        # Domain label
        self.domain_label = ttk.Label(main_frame, text="", font=('Arial', 11, 'italic'),
                                     foreground='#0066cc')
        self.domain_label.grid(row=1, column=0, sticky=tk.W, pady=(0, 10))
        
        # Question frame with scrollbar
        question_frame = ttk.LabelFrame(main_frame, text="Question", padding="15")
        question_frame.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        question_frame.columnconfigure(0, weight=1)
        question_frame.rowconfigure(0, weight=1)
        
        # Question text
        self.question_text = scrolledtext.ScrolledText(question_frame, wrap=tk.WORD, 
                                                      height=4, font=('Arial', 11))
        self.question_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.question_text.config(state='disabled')
        
        # Options frame
        self.options_frame = ttk.LabelFrame(main_frame, text="Answer Options", padding="15")
        self.options_frame.grid(row=3, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Create radio buttons (will be populated dynamically)
        self.option_buttons = {}
        
        # Explanation frame
        self.explanation_frame = ttk.LabelFrame(main_frame, text="Explanation", padding="15")
        self.explanation_frame.grid(row=4, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        self.explanation_frame.columnconfigure(0, weight=1)
        self.explanation_frame.rowconfigure(0, weight=1)
        
        self.explanation_text = scrolledtext.ScrolledText(self.explanation_frame, wrap=tk.WORD,
                                                         height=4, font=('Arial', 10))
        self.explanation_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.explanation_text.config(state='disabled')
        self.explanation_frame.grid_remove()  # Hidden by default
        
        # Navigation frame
        nav_frame = ttk.Frame(main_frame)
        nav_frame.grid(row=5, column=0, sticky=(tk.W, tk.E))
        
        # Navigation buttons
        self.prev_button = ttk.Button(nav_frame, text="← Previous", command=self.prev_question)
        self.prev_button.grid(row=0, column=0, padx=5)
        
        self.submit_button = ttk.Button(nav_frame, text="Submit Answer", 
                                       command=self.submit_answer, style='Accent.TButton')
        self.submit_button.grid(row=0, column=1, padx=5)
        
        self.next_button = ttk.Button(nav_frame, text="Next →", command=self.next_question)
        self.next_button.grid(row=0, column=2, padx=5)
        
        # Spacer
        nav_frame.columnconfigure(3, weight=1)
        
        # Flag button
        self.flag_button = ttk.Button(nav_frame, text="⚑ Flag for Review", 
                                     command=self.toggle_flag)
        self.flag_button.grid(row=0, column=4, padx=5)
        
        # Jump to question
        ttk.Label(nav_frame, text="Jump to:").grid(row=0, column=5, padx=(20, 5))
        self.jump_var = tk.StringVar()
        self.jump_combo = ttk.Combobox(nav_frame, textvariable=self.jump_var, 
                                      values=[str(i) for i in range(1, 66)], 
                                      width=5, state='readonly')
        self.jump_combo.grid(row=0, column=6, padx=5)
        self.jump_combo.bind('<<ComboboxSelected>>', self.jump_to_question)
        
        # Finish exam button
        self.finish_button = ttk.Button(nav_frame, text="Finish Exam", 
                                       command=self.finish_exam)
        self.finish_button.grid(row=0, column=7, padx=5)
        
        # Create style for correct/incorrect indication
        style.configure('Correct.TRadiobutton', foreground='green')
        style.configure('Incorrect.TRadiobutton', foreground='red')
        
    def display_question(self):
        """Display the current question"""
        q = self.questions[self.current_question_index]
        
        # Update progress
        answered = sum(1 for q in self.questions if q.is_answered())
        self.progress_label.config(text=f"Question {q.number} of {len(self.questions)}")
        self.score_label.config(text=f"Answered: {answered}/{len(self.questions)}")
        
        # Update domain
        self.domain_label.config(text=q.domain)
        
        # Update question text
        self.question_text.config(state='normal')
        self.question_text.delete(1.0, tk.END)
        self.question_text.insert(1.0, q.text)
        self.question_text.config(state='disabled')
        
        # Clear and recreate option buttons
        for widget in self.options_frame.winfo_children():
            widget.destroy()
        
        self.option_buttons = {}
        self.selected_answer.set(q.user_answer if q.user_answer else "")
        
        for i, (key, value) in enumerate(sorted(q.options.items())):
            rb = ttk.Radiobutton(self.options_frame, text=f"{key}. {value}",
                               variable=self.selected_answer, value=key,
                               command=self.on_answer_selected)
            rb.grid(row=i, column=0, sticky=tk.W, pady=5, padx=10)
            self.option_buttons[key] = rb
        
        # Update navigation buttons
        self.prev_button.config(state='normal' if self.current_question_index > 0 else 'disabled')
        self.next_button.config(state='normal' if self.current_question_index < len(self.questions) - 1 else 'disabled')
        
        # Update jump combo
        self.jump_var.set(str(q.number))
        
        # Show/hide explanation based on whether question is answered
        if q.is_answered() and not self.exam_submitted:
            self.show_explanation(submitted=False)
        elif self.exam_submitted:
            self.show_explanation(submitted=True)
        else:
            self.explanation_frame.grid_remove()
        
    def on_answer_selected(self):
        """Handle answer selection"""
        # Enable submit button when an answer is selected
        self.submit_button.config(state='normal')
    
    def submit_answer(self):
        """Submit the current answer"""
        if not self.selected_answer.get():
            messagebox.showwarning("No Answer", "Please select an answer before submitting.")
            return
        
        q = self.questions[self.current_question_index]
        q.user_answer = self.selected_answer.get()
        
        # Show explanation
        self.show_explanation(submitted=False)
        
        # Update display
        self.display_question()
        
        messagebox.showinfo("Answer Submitted", 
                          "Correct!" if q.is_correct() else "Incorrect. Review the explanation.")
    
    def show_explanation(self, submitted=False):
        """Show the explanation for the current question"""
        q = self.questions[self.current_question_index]
        
        # Show explanation frame
        self.explanation_frame.grid()
        
        # Update explanation text
        self.explanation_text.config(state='normal')
        self.explanation_text.delete(1.0, tk.END)
        
        if q.is_answered() or submitted:
            result = "✓ Correct!" if q.is_correct() else "✗ Incorrect"
            self.explanation_text.insert(1.0, f"{result}\n\n")
            self.explanation_text.insert(tk.END, f"Correct Answer: {q.correct_answer}\n\n")
            self.explanation_text.insert(tk.END, f"Explanation: {q.explanation}")
            
            # Highlight correct/incorrect answers
            if submitted or q.is_answered():
                for key, rb in self.option_buttons.items():
                    if key == q.correct_answer:
                        rb.config(style='Correct.TRadiobutton')
                    elif key == q.user_answer and key != q.correct_answer:
                        rb.config(style='Incorrect.TRadiobutton')
        
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
        question_num = int(self.jump_var.get())
        self.current_question_index = question_num - 1
        self.display_question()
    
    def toggle_flag(self):
        """Toggle flag for current question (placeholder for future feature)"""
        messagebox.showinfo("Feature", "Flag feature - mark questions for later review")
    
    def finish_exam(self):
        """Finish the exam and show results"""
        # Stop the timer
        self.stop_timer()
        
        # Check if all questions are answered
        unanswered = [q.number for q in self.questions if not q.is_answered()]
        
        if unanswered and not self.exam_submitted:
            result = messagebox.askyesno("Unanswered Questions",
                                        f"You have {len(unanswered)} unanswered question(s).\n"
                                        f"Questions: {', '.join(map(str, unanswered[:10]))}"
                                        f"{'...' if len(unanswered) > 10 else ''}\n\n"
                                        "Do you want to finish anyway?")
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
        
        # Show results
        result_message = f"""
Exam Complete!

Time Used: {time_used}
Score: {correct} / {total} ({percentage:.1f}%)

Breakdown by Domain:
"""
        
        # Calculate domain scores
        domain_scores = {}
        for q in self.questions:
            if q.domain not in domain_scores:
                domain_scores[q.domain] = {'correct': 0, 'total': 0}
            domain_scores[q.domain]['total'] += 1
            if q.is_correct():
                domain_scores[q.domain]['correct'] += 1
        
        for domain, scores in sorted(domain_scores.items()):
            pct = (scores['correct'] / scores['total']) * 100
            result_message += f"\n{domain}: {scores['correct']}/{scores['total']} ({pct:.1f}%)"
        
        # Passing criteria (typically 70% for Splunk certifications)
        passing = percentage >= 70
        result_message += f"\n\nStatus: {'PASSED ✓' if passing else 'FAILED ✗'}"
        result_message += f"\n(Passing score: 70%)"
        
        messagebox.showinfo("Exam Results", result_message)
        
        # Update timer display
        self.timer_label.config(text=f"⏱ Exam Completed - Time Used: {time_used}")
        
        # Update display to show all explanations
        self.display_question()


def main():
    """Main entry point"""
    root = tk.Tk()
    app = SplunkPracticeExam(root)
    root.mainloop()


if __name__ == "__main__":
    main()
