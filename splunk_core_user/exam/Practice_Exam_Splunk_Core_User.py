#!/usr/bin/env python3
"""
Splunk Core User Certification Practice Exam
Interactive GUI Application with configurable timer and question counts
Copyright (C) 2024 - Licensed under GPL v3
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import re
import os
from typing import List, Dict, Tuple, Optional
import random


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
        self.user_answers: List[str] = []

    def is_correct(self) -> bool:
        """Check if user's answer is correct"""
        return set(self.user_answers) == set(self.correct_answers)

    def is_answered(self) -> bool:
        """Check if question has been answered"""
        return len(self.user_answers) > 0


class StartupDialog:
    """Dialog to configure exam settings before starting"""

    def __init__(self, parent):
        self.result = None
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Exam Configuration")
        self.dialog.geometry("450x350")
        self.dialog.resizable(False, False)
        self.dialog.transient(parent)
        self.dialog.grab_set()

        # Center the dialog
        self.dialog.update_idletasks()
        x = (self.dialog.winfo_screenwidth() - 450) // 2
        y = (self.dialog.winfo_screenheight() - 350) // 2
        self.dialog.geometry(f"+{x}+{y}")

        self.setup_ui()

    def setup_ui(self):
        """Set up the configuration UI"""
        main_frame = ttk.Frame(self.dialog, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Title
        title_label = ttk.Label(main_frame,
                               text="Splunk Core User Practice Exam",
                               font=('Arial', 14, 'bold'))
        title_label.pack(pady=(0, 20))

        # Timer configuration
        timer_frame = ttk.LabelFrame(main_frame, text="Timer Settings", padding="10")
        timer_frame.pack(fill=tk.X, pady=(0, 15))

        self.use_timer = tk.BooleanVar(value=True)
        timer_on = ttk.Radiobutton(timer_frame, text="Use 60-minute timer",
                                   variable=self.use_timer, value=True)
        timer_on.pack(anchor=tk.W)
        timer_off = ttk.Radiobutton(timer_frame, text="No timer (practice mode)",
                                    variable=self.use_timer, value=False)
        timer_off.pack(anchor=tk.W)

        # Question count configuration
        questions_frame = ttk.LabelFrame(main_frame, text="Number of Questions", padding="10")
        questions_frame.pack(fill=tk.X, pady=(0, 15))

        self.question_count = tk.IntVar(value=65)
        q65 = ttk.Radiobutton(questions_frame, text="65 Questions (Standard exam length)",
                              variable=self.question_count, value=65)
        q65.pack(anchor=tk.W)
        q75 = ttk.Radiobutton(questions_frame, text="75 Questions (Extended practice)",
                              variable=self.question_count, value=75)
        q75.pack(anchor=tk.W)
        q100 = ttk.Radiobutton(questions_frame, text="100 Questions (Full advanced exam)",
                               variable=self.question_count, value=100)
        q100.pack(anchor=tk.W)

        # Info label
        info_label = ttk.Label(main_frame,
                              text="Questions are loaded from the Advanced 100 Questions file.\n"
                                   "Selecting fewer questions will use a random subset.",
                              font=('Arial', 9, 'italic'),
                              foreground='gray')
        info_label.pack(pady=(0, 15))

        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X)

        start_button = ttk.Button(button_frame, text="Start Exam",
                                  command=self.start_exam)
        start_button.pack(side=tk.RIGHT, padx=5)

        cancel_button = ttk.Button(button_frame, text="Cancel",
                                   command=self.cancel)
        cancel_button.pack(side=tk.RIGHT, padx=5)

    def start_exam(self):
        """Start the exam with selected settings"""
        self.result = {
            'use_timer': self.use_timer.get(),
            'question_count': self.question_count.get()
        }
        self.dialog.destroy()

    def cancel(self):
        """Cancel and exit"""
        self.result = None
        self.dialog.destroy()


class QuestionParser:
    """Parses questions from markdown file"""

    @staticmethod
    def parse_markdown_file(filepath: str) -> List[Question]:
        """Parse questions from the markdown file"""
        questions = []

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except FileNotFoundError:
            return questions

        # Split into question sections and answer key
        parts = content.split('# Answer Key')
        if len(parts) < 2:
            return questions

        questions_section = parts[0]
        answers_section = parts[1]

        # Parse answers first
        answers_dict = QuestionParser._parse_answers(answers_section)

        # Parse questions
        current_domain = ""
        question_pattern = re.compile(
            r'\*\*Question (\d+)\*\*\s*\n(.*?)(?=\n\n\*\*Question|\n---|\Z)',
            re.DOTALL
        )

        domain_pattern = re.compile(r'## (Domain \d+\.\d+:.*?)(?=\n)')

        # Find all domains and their positions
        domain_positions = [(m.start(), m.group(1)) for m in domain_pattern.finditer(questions_section)]

        for match in question_pattern.finditer(questions_section):
            q_num = int(match.group(1))
            q_content = match.group(2).strip()

            # Find the domain for this question
            q_pos = match.start()
            for pos, domain in reversed(domain_positions):
                if pos < q_pos:
                    current_domain = domain
                    break

            # Check if multi-select
            is_multi = "(Select all that apply)" in q_content

            # Parse question text and options
            lines = q_content.split('\n')
            q_text = []
            options = {}

            for line in lines:
                line = line.strip()
                if not line:
                    continue
                # Match option lines (A. through F.)
                opt_match = re.match(r'^([A-F])\.\s+(.+)$', line)
                if opt_match:
                    options[opt_match.group(1)] = opt_match.group(2)
                elif not line.startswith('**'):
                    q_text.append(line)

            question_text = ' '.join(q_text)

            # Get answers and explanation from answers_dict
            if q_num in answers_dict:
                correct_answers, explanation = answers_dict[q_num]
            else:
                correct_answers = ['A']
                explanation = "No explanation available."

            if options:  # Only add if we have options
                questions.append(Question(
                    number=q_num,
                    domain=current_domain,
                    text=question_text,
                    options=options,
                    correct_answers=correct_answers,
                    explanation=explanation,
                    is_multi_select=is_multi
                ))

        return questions

    @staticmethod
    def _parse_answers(answers_section: str) -> Dict[int, Tuple[List[str], str]]:
        """Parse the answer key section"""
        answers = {}

        # Pattern to match answer entries like "**1. A, B, C - Explanation**" or "**1. A - Explanation**"
        answer_pattern = re.compile(
            r'\*\*(\d+)\.\s+([A-F](?:,\s*[A-F])*)\s*[-–]\s*([^*]+)\*\*\s*\n?(.*?)(?=\n\*\*\d+\.|\n---|\Z)',
            re.DOTALL
        )

        for match in answer_pattern.finditer(answers_section):
            q_num = int(match.group(1))
            answer_str = match.group(2)
            short_explanation = match.group(3).strip()
            long_explanation = match.group(4).strip()

            # Parse multiple answers
            correct_answers = [a.strip() for a in answer_str.split(',')]

            # Combine explanations
            full_explanation = short_explanation
            if long_explanation:
                full_explanation += " " + long_explanation

            answers[q_num] = (correct_answers, full_explanation)

        return answers


class SplunkPracticeExam:
    """Main application class for the practice exam"""

    def __init__(self, root, config: Dict):
        self.root = root
        self.root.title("Splunk Core User - Practice Exam")
        self.root.geometry("1000x800")

        self.use_timer = config['use_timer']
        self.question_count = config['question_count']

        # Load questions from markdown file
        self.all_questions = self.load_questions()
        self.questions = self.select_questions()

        if not self.questions:
            messagebox.showerror("Error", "No questions could be loaded. Please check the content directory.")
            self.root.destroy()
            return

        self.current_question_index = 0
        self.selected_answers: Dict[str, tk.BooleanVar] = {}

        # Track exam state
        self.exam_submitted = False
        self.flagged_questions: set = set()

        # Timer variables (60 minutes)
        self.total_seconds = 60 * 60
        self.remaining_seconds = self.total_seconds
        self.timer_running = False
        self.timer_paused = False
        self.timer_id = None
        self.five_minute_warning_shown = False

        # Set up UI
        self.setup_ui()
        self.display_question()

        # Start the timer if enabled
        if self.use_timer:
            self.start_timer()
        else:
            self.timer_label.config(text="Timer: Disabled", foreground='gray')
            self.pause_button.config(state='disabled')
            self.stop_button.config(state='disabled')

    def load_questions(self) -> List[Question]:
        """Load questions from markdown file"""
        # Get the directory where this script is located
        script_dir = os.path.dirname(os.path.abspath(__file__))
        content_dir = os.path.join(script_dir, 'content')

        # Try to load from the Advanced 100 Questions file
        filepath = os.path.join(content_dir, 'Splunk_Core_User_Practice_Exam_Advanced_100_Questions.md')

        questions = QuestionParser.parse_markdown_file(filepath)

        if not questions:
            # Fallback: try current directory
            filepath = 'content/Splunk_Core_User_Practice_Exam_Advanced_100_Questions.md'
            questions = QuestionParser.parse_markdown_file(filepath)

        return questions

    def select_questions(self) -> List[Question]:
        """Select the requested number of questions"""
        if len(self.all_questions) <= self.question_count:
            return self.all_questions

        # Randomly select questions while maintaining domain distribution
        # Group questions by domain
        domain_questions: Dict[str, List[Question]] = {}
        for q in self.all_questions:
            if q.domain not in domain_questions:
                domain_questions[q.domain] = []
            domain_questions[q.domain].append(q)

        # Calculate proportional selection from each domain
        selected = []
        ratio = self.question_count / len(self.all_questions)

        for domain, questions in domain_questions.items():
            num_to_select = max(1, int(len(questions) * ratio))
            selected.extend(random.sample(questions, min(num_to_select, len(questions))))

        # If we need more, add randomly
        while len(selected) < self.question_count:
            remaining = [q for q in self.all_questions if q not in selected]
            if not remaining:
                break
            selected.append(random.choice(remaining))

        # If we have too many, trim
        if len(selected) > self.question_count:
            selected = selected[:self.question_count]

        # Sort by question number
        selected.sort(key=lambda q: q.number)

        # Renumber questions
        for i, q in enumerate(selected, 1):
            q.number = i

        return selected

    def format_time(self, seconds: int) -> str:
        """Format seconds into MM:SS format"""
        minutes = seconds // 60
        secs = seconds % 60
        return f"{minutes:02d}:{secs:02d}"

    def start_timer(self):
        """Start the countdown timer"""
        if not self.timer_running and self.use_timer:
            self.timer_running = True
            self.timer_paused = False
            self.update_timer()
            self.pause_button.config(text="Pause Timer", command=self.pause_timer)

    def pause_timer(self):
        """Pause the countdown timer"""
        if self.timer_running and not self.timer_paused:
            self.timer_paused = True
            if self.timer_id:
                self.root.after_cancel(self.timer_id)
            self.pause_button.config(text="Resume Timer", command=self.resume_timer)

    def resume_timer(self):
        """Resume the countdown timer"""
        if self.timer_running and self.timer_paused:
            self.timer_paused = False
            self.update_timer()
            self.pause_button.config(text="Pause Timer", command=self.pause_timer)

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

        # Update timer display with MM:SS format
        time_str = self.format_time(self.remaining_seconds)
        self.timer_label.config(text=f"Time Remaining: {time_str}")

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
                "5 Minutes Remaining!\n\n"
                "You have 5 minutes left to complete the exam.\n"
                "Make sure to review and submit your answers.",
                parent=self.root
            )

        # Check if time expired
        if self.remaining_seconds <= 0:
            self.stop_timer()
            self.timer_label.config(text="Time's Up!", foreground='red')
            messagebox.showwarning(
                "Time Expired",
                "Time has expired!\n\n"
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

        # Exam info
        timer_mode = "Timed" if self.use_timer else "Practice"
        info_label = ttk.Label(header_frame,
                              text=f"Mode: {timer_mode} | Questions: {len(self.questions)}",
                              font=('Arial', 10))
        info_label.grid(row=1, column=0, columnspan=3, pady=(0, 5))

        # Timer display
        self.timer_label = ttk.Label(header_frame, text="Time Remaining: 60:00",
                                     font=('Arial', 14, 'bold'), foreground='green')
        self.timer_label.grid(row=2, column=0, columnspan=3, pady=(0, 5))

        # Timer controls frame
        timer_controls = ttk.Frame(header_frame)
        timer_controls.grid(row=3, column=0, columnspan=3, pady=(0, 10))

        self.pause_button = ttk.Button(timer_controls, text="Pause Timer",
                                      command=self.pause_timer)
        self.pause_button.grid(row=0, column=0, padx=5)

        self.stop_button = ttk.Button(timer_controls, text="Stop Timer",
                                     command=self.stop_timer)
        self.stop_button.grid(row=0, column=1, padx=5)

        # Progress info
        self.progress_label = ttk.Label(header_frame, text="", font=('Arial', 10))
        self.progress_label.grid(row=4, column=0, sticky=tk.W)

        self.score_label = ttk.Label(header_frame, text="", font=('Arial', 10))
        self.score_label.grid(row=4, column=2, sticky=tk.E)

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

        # Explanation frame
        self.explanation_frame = ttk.LabelFrame(main_frame, text="Explanation", padding="15")
        self.explanation_frame.grid(row=4, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        self.explanation_frame.columnconfigure(0, weight=1)
        self.explanation_frame.rowconfigure(0, weight=1)

        self.explanation_text = scrolledtext.ScrolledText(self.explanation_frame, wrap=tk.WORD,
                                                         height=4, font=('Arial', 10))
        self.explanation_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.explanation_text.config(state='disabled')
        self.explanation_frame.grid_remove()

        # Navigation frame
        nav_frame = ttk.Frame(main_frame)
        nav_frame.grid(row=5, column=0, sticky=(tk.W, tk.E))

        # Navigation buttons
        self.prev_button = ttk.Button(nav_frame, text="Previous", command=self.prev_question)
        self.prev_button.grid(row=0, column=0, padx=5)

        self.submit_button = ttk.Button(nav_frame, text="Submit Answer",
                                       command=self.submit_answer)
        self.submit_button.grid(row=0, column=1, padx=5)

        self.next_button = ttk.Button(nav_frame, text="Next", command=self.next_question)
        self.next_button.grid(row=0, column=2, padx=5)

        # Spacer
        nav_frame.columnconfigure(3, weight=1)

        # Flag button
        self.flag_button = ttk.Button(nav_frame, text="Flag for Review",
                                     command=self.toggle_flag)
        self.flag_button.grid(row=0, column=4, padx=5)

        # Jump to question
        ttk.Label(nav_frame, text="Jump to:").grid(row=0, column=5, padx=(20, 5))
        self.jump_var = tk.StringVar()
        self.jump_combo = ttk.Combobox(nav_frame, textvariable=self.jump_var,
                                      values=[str(i) for i in range(1, len(self.questions) + 1)],
                                      width=5, state='readonly')
        self.jump_combo.grid(row=0, column=6, padx=5)
        self.jump_combo.bind('<<ComboboxSelected>>', self.jump_to_question)

        # Finish exam button
        self.finish_button = ttk.Button(nav_frame, text="Finish Exam",
                                       command=self.finish_exam)
        self.finish_button.grid(row=0, column=7, padx=5)

        # Create styles for correct/incorrect indication
        style.configure('Correct.TCheckbutton', foreground='green')
        style.configure('Incorrect.TCheckbutton', foreground='red')
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
        question_display = q.text
        if q.is_multi_select:
            question_display += "\n\n(Select all that apply)"
        self.question_text.insert(1.0, question_display)
        self.question_text.config(state='disabled')

        # Clear and recreate option widgets
        for widget in self.options_frame.winfo_children():
            widget.destroy()

        self.selected_answers = {}

        if q.is_multi_select:
            # Use checkboxes for multi-select
            for i, (key, value) in enumerate(sorted(q.options.items())):
                var = tk.BooleanVar(value=key in q.user_answers)
                self.selected_answers[key] = var
                cb = ttk.Checkbutton(self.options_frame, text=f"{key}. {value}",
                                    variable=var)
                cb.grid(row=i, column=0, sticky=tk.W, pady=5, padx=10)
        else:
            # Use radio buttons for single-select
            self.single_answer_var = tk.StringVar(
                value=q.user_answers[0] if q.user_answers else ""
            )
            for i, (key, value) in enumerate(sorted(q.options.items())):
                rb = ttk.Radiobutton(self.options_frame, text=f"{key}. {value}",
                                    variable=self.single_answer_var, value=key)
                rb.grid(row=i, column=0, sticky=tk.W, pady=5, padx=10)

        # Update navigation buttons
        self.prev_button.config(state='normal' if self.current_question_index > 0 else 'disabled')
        self.next_button.config(state='normal' if self.current_question_index < len(self.questions) - 1 else 'disabled')

        # Update jump combo
        self.jump_var.set(str(q.number))

        # Update flag button
        if q.number in self.flagged_questions:
            self.flag_button.config(text="Unflag")
        else:
            self.flag_button.config(text="Flag for Review")

        # Show/hide explanation
        if q.is_answered() and not self.exam_submitted:
            self.show_explanation(submitted=False)
        elif self.exam_submitted:
            self.show_explanation(submitted=True)
        else:
            self.explanation_frame.grid_remove()

    def submit_answer(self):
        """Submit the current answer"""
        q = self.questions[self.current_question_index]

        if q.is_multi_select:
            answers = [key for key, var in self.selected_answers.items() if var.get()]
            if not answers:
                messagebox.showwarning("No Answer", "Please select at least one answer.")
                return
            q.user_answers = answers
        else:
            answer = self.single_answer_var.get()
            if not answer:
                messagebox.showwarning("No Answer", "Please select an answer.")
                return
            q.user_answers = [answer]

        # Show explanation
        self.show_explanation(submitted=False)

        # Update display
        self.display_question()

        if q.is_correct():
            messagebox.showinfo("Answer Submitted", "Correct!")
        else:
            messagebox.showinfo("Answer Submitted", "Incorrect. Review the explanation.")

    def show_explanation(self, submitted=False):
        """Show the explanation for the current question"""
        q = self.questions[self.current_question_index]

        self.explanation_frame.grid()

        self.explanation_text.config(state='normal')
        self.explanation_text.delete(1.0, tk.END)

        if q.is_answered() or submitted:
            result = "Correct!" if q.is_correct() else "Incorrect"
            self.explanation_text.insert(1.0, f"{result}\n\n")
            correct_str = ", ".join(q.correct_answers)
            self.explanation_text.insert(tk.END, f"Correct Answer(s): {correct_str}\n\n")
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
        question_num = int(self.jump_var.get())
        self.current_question_index = question_num - 1
        self.display_question()

    def toggle_flag(self):
        """Toggle flag for current question"""
        q = self.questions[self.current_question_index]
        if q.number in self.flagged_questions:
            self.flagged_questions.remove(q.number)
            self.flag_button.config(text="Flag for Review")
        else:
            self.flagged_questions.add(q.number)
            self.flag_button.config(text="Unflag")

    def finish_exam(self):
        """Finish the exam and show results"""
        self.stop_timer()

        unanswered = [q.number for q in self.questions if not q.is_answered()]

        if unanswered and not self.exam_submitted:
            result = messagebox.askyesno("Unanswered Questions",
                                        f"You have {len(unanswered)} unanswered question(s).\n"
                                        f"Questions: {', '.join(map(str, unanswered[:10]))}"
                                        f"{'...' if len(unanswered) > 10 else ''}\n\n"
                                        "Do you want to finish anyway?")
            if not result:
                if self.use_timer and self.remaining_seconds > 0:
                    self.start_timer()
                return

        # Calculate score
        correct = sum(1 for q in self.questions if q.is_correct())
        total = len(self.questions)
        percentage = (correct / total) * 100

        self.exam_submitted = True

        # Calculate time used
        time_used_seconds = self.total_seconds - self.remaining_seconds
        time_used = self.format_time(time_used_seconds) if self.use_timer else "N/A (Practice Mode)"

        # Build results message
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

        # Passing criteria (70% for Splunk certifications)
        passing = percentage >= 70
        result_message += f"\n\nStatus: {'PASSED' if passing else 'FAILED'}"
        result_message += f"\n(Passing score: 70%)"

        if self.flagged_questions:
            result_message += f"\n\nFlagged for review: {', '.join(map(str, sorted(self.flagged_questions)))}"

        messagebox.showinfo("Exam Results", result_message)

        # Update timer display
        if self.use_timer:
            self.timer_label.config(text=f"Exam Completed - Time Used: {time_used}")
        else:
            self.timer_label.config(text="Exam Completed (Practice Mode)")

        self.display_question()


def main():
    """Main entry point"""
    root = tk.Tk()
    root.withdraw()  # Hide main window while showing dialog

    # Show startup dialog
    dialog = StartupDialog(root)
    root.wait_window(dialog.dialog)

    if dialog.result is None:
        root.destroy()
        return

    # Show main window and start exam
    root.deiconify()
    app = SplunkPracticeExam(root, dialog.result)
    root.mainloop()


if __name__ == "__main__":
    main()
