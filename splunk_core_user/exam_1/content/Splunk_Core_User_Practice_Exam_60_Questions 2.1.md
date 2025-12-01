# Splunk Core Certified User Practice Exam
## 60 Questions - Aligned to Official Exam Blueprint

**Instructions:**
- This practice exam contains 60 multiple-choice questions
- Questions are weighted according to the official Splunk Core Certified User exam blueprint
- Time limit: 60 minutes (matching actual exam format)
- Choose the best answer for each question
- The answer key with explanations is provided at the end

**Exam Format:**
- 60 Questions
- Entry-Level Certification
- 60 Minutes (actual exam time)

---

## Domain 1.0: Splunk Basics (5% - 3 Questions)

**Question 1**  
Which Splunk component is responsible for parsing incoming data and storing it on disk?

A. Universal Forwarder  
B. Search Head  
C. Indexer  
D. Heavy Forwarder

**Question 2**  
What is the primary function of a Splunk App?

A. To forward data to external systems  
B. To provide a specific collection of configurations, dashboards, and knowledge objects for a particular use case  
C. To manage user licenses  
D. To compress raw data logs

**Question 3**  
How can you customize your user settings in Splunk?

A. Settings > User preferences  
B. Only through the CLI  
C. Submit a ticket to the admin  
D. Edit the .conf files directly

---

## Domain 2.0: Basic Searching (22% - 13 Questions)

**Question 4**  
When running a search, what is the most effective way to limit the number of events retrieved from disk?

A. Use the `head` command  
B. Use the `fields` command  
C. Specify a narrower time range  
D. Use the `table` command

**Question 5**  
What is the correct syntax to search for events containing the exact phrase "failed login"?

A. failed AND login  
B. "failed login"  
C. failed_login  
D. string=failed login

**Question 6**  
Which time picker syntax would you use to search data from the beginning of today?

A. Last 24 hours  
B. -1d  
C. Earliest=@d  
D. Previous business day

**Question 7**  
What does the Timeline visual in search results represent?

A. The time the search took to run  
B. The number of events matching the search query over time  
C. The CPU usage of the indexer  
D. The bandwidth used by the forwarder

**Question 8**  
Which symbol is used to snap a time range to a specific unit (e.g., beginning of the day)?

A. *  
B. $  
C. @  
D. #

**Question 9**  
What does the Search Mode setting (Fast, Smart, Verbose) control?

A. The speed of the indexer  
B. How many events are returned and which fields are discovered  
C. The number of users who can view the search  
D. The expiration time of the search job

**Question 10**  
How do Boolean operators affect search precedence when no parentheses are used?

A. OR is evaluated first  
B. AND is evaluated first  
C. NOT is evaluated first  
D. They are evaluated left-to-right

**Question 11**  
Which command or action allows you to save your search results in CSV format?

A. Export  
B. Save As Report  
C. Save As Dashboard  
D. Print

**Question 12**  
When using the `earliest` and `latest` time modifiers in a search string, what is the correct syntax to look back 15 minutes?

A. earliest=15m  
B. earliest=-15m  
C. time=-15m  
D. start=now-15m

**Question 13**  
What happens when you click on a bar in the Timeline?

A. It deletes the events in that time bucket  
B. It zooms into that specific time range  
C. It highlights the events in red  
D. It exports the data

**Question 14**  
How can you control a running search job?

A. Pause, Stop, or Finalize  
B. Restart or Delete only  
C. Compress or Archive  
D. Forward or Background

**Question 15**  
Which tab allows you to view raw events in a clean list format?

A. Events tab  
B. Statistics tab  
C. Visualization tab  
D. Job Inspector

**Question 16**  
Which of the following is considered a best practice for searching in Splunk?

A. Use wildcards at the beginning of strings (e.g., `*fail`)  
B. Specify the index name  
C. Search `All Time` by default  
D. Use as many OR operators as possible

---

## Domain 3.0: Using Fields in Searches (20% - 12 Questions)

**Question 17**  
Where are "Selected Fields" displayed in the Splunk interface?

A. In the main event list, under every event  
B. Only in the Job Inspector  
C. In the Fields sidebar, at the top of the list  
D. In the search bar

**Question 18**  
Which three fields are selected by default in Splunk?

A. host, user, ip  
B. host, source, sourcetype  
C. index, source, splunk_server  
D. time, event_id, host

**Question 19**  
What criteria must a field meet to be listed as an "Interesting Field"?

A. It must be a numeric field  
B. It must appear in at least 20% of the events  
C. It must be manually selected by the user  
D. It must contain a unique value

**Question 20**  
How can you add a field to the "Selected Fields" list?

A. Click the field in the "Interesting Fields" list and select "Yes" for Selected  
B. Use the `select` command in SPL  
C. Right-click the event and choose "Promote"  
D. It happens automatically after 10 searches

**Question 21**  
Which command would you use to exclude specific fields from the search results?

A. `remove fieldname`  
B. `fields - fieldname`  
C. `delete fieldname`  
D. `exclude fieldname`

**Question 22**  
What is the difference between `source` and `sourcetype`?

A. `source` is the format; `sourcetype` is the file name  
B. `source` is the file path/input stream; `sourcetype` is the data classification/format  
C. They are identical  
D. `sourcetype` is the server name

**Question 23**  
Are field names in Splunk case-sensitive?

A. True - field names are case-sensitive  
B. False - field names are not case-sensitive

**Question 24**  
In the search `status=404`, what does "status" represent?

A. The value  
B. The field name  
C. The tag  
D. The index

**Question 25**  
Which symbol is used to perform a wildcard match within a field value (e.g., `user=admin*`)?

A. %  
B. ?  
C. *  
D. !

**Question 26**  
What does the `!=` operator do in a field search?

A. It looks for events where the field does NOT equal the value  
B. It sets the field to a new value  
C. It matches values that sound similar  
D. It looks for the field in all indexes

**Question 27**  
Can you search for a value without specifying a field name (e.g., `error` instead of `field=error`)?

A. Yes, Splunk searches across all field values  
B. No, field names are mandatory  
C. Only in Verbose mode  
D. Only for numeric values

**Question 28**  
Which field in the Fields sidebar shows the number of events containing that field?

A. Count  
B. Coverage  
C. Frequency  
D. The number is displayed next to each field

---

## Domain 4.0: Search Language Fundamentals (15% - 9 Questions)

**Question 29**  
Which command sorts the results in ascending order by a specific field?

A. `sort field`  
B. `order field asc`  
C. `arrange field`  
D. `rank field`

**Question 30**  
To rename a field in the search results, which command do you use?

A. `rename old_name as new_name`  
B. `change old_name to new_name`  
C. `alter old_name new_name`  
D. `modify old_name = new_name`

**Question 31**  
Which command removes duplicate events from your search results?

A. `distinct`  
B. `unique`  
C. `dedup`  
D. `remove_duplicates`

**Question 32**  
What is the purpose of the search pipeline in Splunk?

A. To physically transport data  
B. To chain commands together using the pipe symbol `|` to process search results  
C. To store backup data  
D. To manage user permissions

**Question 33**  
How do you specify a particular index in your search?

A. `index=indexname`  
B. `source=indexname`  
C. `using index indexname`  
D. `from indexname`

**Question 34**  
Which command displays only specified fields in a table format?

A. `show`  
B. `table`  
C. `display`  
D. `format`

**Question 35**  
What does the `fields` command do?

A. Creates new fields  
B. Includes or excludes fields from the search results  
C. Counts the number of fields  
D. Encrypts field values

**Question 36**  
Can you chain multiple search commands together?

A. No, only one command per search  
B. Yes, by separating them with a pipe `|`  
C. Yes, but only two commands maximum  
D. Only with admin privileges

**Question 37**  
Which command returns the first N results?

A. `top`  
B. `head`  
C. `first`  
D. `initial`

---

## Domain 5.0: Using Basic Transforming Commands (15% - 9 Questions)

**Question 38**  
Which command finds the most common values of a field?

A. `rare`  
B. `top`  
C. `stats`  
D. `common`

**Question 39**  
Which command finds the least common values of a field?

A. `bottom`  
B. `rare`  
C. `limit`  
D. `least`

**Question 40**  
What fields are automatically created by the `top` command?

A. `count` and `percent`  
B. `total` and `rate`  
C. `sum` and `avg`  
D. `hits` and `score`

**Question 41**  
Which `stats` function would you use to count the total number of events?

A. `sum`  
B. `count`  
C. `list`  
D. `total`

**Question 42**  
Which `stats` function calculates the distinct (unique) count of a field?

A. `dc` (or `distinct_count`)  
B. `uc`  
C. `uniq`  
D. `count_distinct`

**Question 43**  
What is the correct syntax to calculate the average of a field named "response_time"?

A. `stats avg(response_time)`  
B. `stats average=response_time`  
C. `stats mean of response_time`  
D. `table avg(response_time)`

**Question 44**  
To group stats results by a specific field (e.g., status), which clause do you use?

A. `group by status`  
B. `split status`  
C. `by status`  
D. `for status`

**Question 45**  
By default, how many results does the `top` command return?

A. 5  
B. 10  
C. 20  
D. 100

**Question 46**  
What does the `values` function do within the `stats` command?

A. It lists only the unique values of a field  
B. It counts all values  
C. It calculates the sum  
D. It sorts the values alphabetically

---

## Domain 6.0: Creating Reports and Dashboards (12% - 7 Questions)

**Question 47**  
How do you save a search as a Report?

A. Click "Save As" > "Report"  
B. Copy the text to a document  
C. Click "Export" > "Report"  
D. Use the `report` command

**Question 48**  
Which visualization is best for showing a trend over time?

A. Pie Chart  
B. Single Value  
C. Line Chart  
D. Gauge

**Question 49**  
What is a "Panel" in a Splunk dashboard?

A. The settings menu  
B. A container for a visualization or report on the dashboard  
C. The user login screen  
D. The search bar

**Question 50**  
How do you add a search to an existing dashboard?

A. Run the search, click "Save As" > "Dashboard Panel", and select the existing dashboard  
B. You must delete the dashboard and recreate it  
C. Drag and drop the search bar  
D. Use the `dashboard` command

**Question 51**  
Can you edit a report after it has been created?

A. Yes, reports can be edited  
B. No, reports are immutable  
C. Only within 24 hours of creation  
D. Only by the admin

**Question 52**  
Which visualization would be appropriate for comparing the share or percentage of a whole?

A. Line Chart  
B. Pie Chart  
C. Marker Map  
D. Scatter Plot

**Question 53**  
What type of search results are required to create a visualization (chart)?

A. Raw events only  
B. Results from transforming commands (stats, top, etc.)  
C. Text-only results  
D. Binary data

---

## Domain 7.0: Creating and Using Lookups (6% - 4 Questions)

**Question 54**  
What is the primary purpose of a lookup in Splunk?

A. To search the internet  
B. To enrich event data with additional information from an external file  
C. To look up other users  
D. To find lost data

**Question 55**  
Which file type is most commonly used for lookup files?

A. .exe  
B. .csv  
C. .docx  
D. .json

**Question 56**  
What are the two main steps to create a file-based lookup in Splunk?

A. 1. Upload the lookup file, 2. Create a Lookup Definition  
B. 1. Email the file to support, 2. Wait for approval  
C. 1. Place the file on the desktop, 2. Run `inputlookup`  
D. 1. Rename the file, 2. Compress the file

**Question 57**  
Which command is used to reference a lookup table in a search?

A. `load`  
B. `lookup` or `inputlookup`  
C. `find`  
D. `search_file`

---

## Domain 8.0: Creating Scheduled Reports and Alerts (5% - 3 Questions)

**Question 58**  
What distinguishes an Alert from a Scheduled Report?

A. Alerts are manual; Reports are automatic  
B. Alerts are triggered by specific conditions and can perform actions; Scheduled Reports run on a schedule to present data  
C. Alerts cost money; Reports are free  
D. Alerts are only for administrators

**Question 59**  
Which of the following is a valid Alert Action?

A. Send an email  
B. Reboot the server  
C. Print to console  
D. Delete the user account

**Question 60**  
Where can you view alerts that have recently been triggered?

A. Activity > Triggered Alerts  
B. Settings > Indexes  
C. Help > About  
D. The Login Screen

---
---

# Answer Key with Explanations

## Domain 1.0: Splunk Basics (5%)

**1. C - Indexer**  
The Indexer is responsible for parsing incoming data, creating indexes, and storing events on disk. Universal Forwarders collect data, Search Heads coordinate searches, and Heavy Forwarders can parse and route data but don't typically store it.

**2. B - To provide a specific collection of configurations, dashboards, and knowledge objects for a particular use case**  
Splunk Apps package together related dashboards, reports, searches, and configurations for specific use cases (e.g., IT operations, security, business analytics).

**3. A - Settings > User preferences**  
Users can customize their settings through Settings > User preferences, where they can set time zones, default apps, and other personal configurations.

---

## Domain 2.0: Basic Searching (22%)

**4. C - Specify a narrower time range**  
The most effective way to reduce the number of events retrieved from disk is to narrow the time range. This limits the data Splunk needs to read from the index. Commands like `head` and `fields` only affect what's displayed, not what's retrieved.

**5. B - "failed login"**  
Using quotes searches for the exact phrase. Without quotes, Splunk would search for events containing both "failed" AND "login" anywhere in the event.

**6. C - Earliest=@d**  
The `@d` syntax snaps to the beginning of the current day. The `@` symbol is used to snap to a time unit.

**7. B - The number of events matching the search query over time**  
The Timeline shows a visual histogram of event counts over the search time range.

**8. C - @**  
The `@` symbol snaps time to the nearest time unit. For example, `@d` snaps to the beginning of the day, `@h` to the beginning of the hour.

**9. B - How many events are returned and which fields are discovered**  
Search Mode controls field discovery: Fast mode returns events but minimal fields, Smart mode balances performance and fields, and Verbose mode discovers all fields.

**10. B - AND is evaluated first**  
In Boolean logic without parentheses, AND has higher precedence than OR. NOT has the highest precedence.

**11. A - Export**  
The Export option allows you to save search results in various formats including CSV, XML, JSON, and raw.

**12. B - earliest=-15m**  
The minus sign indicates "ago" from the current time. `earliest=-15m` means 15 minutes ago.

**13. B - It zooms into that specific time range**  
Clicking a Timeline bar zooms the search into that specific time bucket, allowing you to focus on events in that period.

**14. A - Pause, Stop, or Finalize**  
Search jobs can be paused (temporarily stopped), stopped (cancelled), or finalized (completed immediately with current results). "Compress" is not a search job control option.

**15. A - Events tab**  
The Events tab displays raw events in list format with relevant fields highlighted.

**16. B - Specify the index name**  
Specifying the index narrows the search and improves performance. Leading wildcards and searching "All Time" are inefficient practices.

---

## Domain 3.0: Using Fields in Searches (20%)

**17. C - In the Fields sidebar, at the top of the list**  
Selected Fields appear at the top of the Fields sidebar and are automatically extracted and displayed in the event list.

**18. B - host, source, sourcetype**  
These three default fields are always selected and provide fundamental information about where the data came from.

**19. B - It must appear in at least 20% of the events**  
Interesting Fields are automatically identified based on appearing in at least 20% of the returned events.

**20. A - Click the field in the "Interesting Fields" list and select "Yes" for Selected**  
You can promote fields to Selected Fields through the Fields sidebar interface.

**21. B - `fields - fieldname`**  
The minus sign excludes fields. Use `fields + fieldname` or `fields fieldname` to include specific fields.

**22. B - `source` is the file path/input stream; `sourcetype` is the data classification/format**  
Source identifies where the data came from (file path, network stream), while sourcetype classifies the data format (apache_access, syslog, etc.).

**23. A - True - field names are case-sensitive**  
Field names in Splunk are case-sensitive, but field values are not by default.

**24. B - The field name**  
In the field-value pair `status=404`, "status" is the field name and "404" is the value.

**25. C - ***  
The asterisk (*) is the wildcard character for matching zero or more characters.

**26. A - It looks for events where the field does NOT equal the value**  
The `!=` operator is the "not equal" comparison operator.

**27. A - Yes, Splunk searches across all field values**  
You can use keywords without specifying a field name. Splunk will search across all fields.

**28. D - The number is displayed next to each field**  
The Fields sidebar shows the count of events containing each field next to the field name.

---

## Domain 4.0: Search Language Fundamentals (15%)

**29. A - `sort field`**  
The `sort` command sorts by the specified field in ascending order by default. Use `sort -field` for descending order.

**30. A - `rename old_name as new_name`**  
The rename command uses the syntax `rename old_name as new_name` or `rename old_name AS new_name`.

**31. C - `dedup`**  
The `dedup` command removes duplicate events based on specified fields. For example, `dedup user` keeps only the first occurrence of each unique user.

**32. B - To chain commands together using the pipe symbol `|` to process search results**  
The search pipeline allows you to string together multiple commands, with each command processing the results from the previous command.

**33. A - `index=indexname`**  
Specify an index using `index=indexname` at the beginning of your search. Multiple indexes can be specified: `index=main OR index=security`.

**34. B - `table`**  
The `table` command formats results with only the specified fields as columns.

**35. B - Includes or excludes fields from the search results**  
The `fields` command controls which fields appear in results: `fields + field1, field2` includes fields, `fields - field1` excludes fields.

**36. B - Yes, by separating them with a pipe `|`**  
Commands are chained using the pipe symbol. For example: `index=web | stats count by status | sort -count`

**37. B - `head`**  
The `head` command returns the first N results. For example, `head 20` returns the first 20 results.

---

## Domain 5.0: Using Basic Transforming Commands (15%)

**38. B - `top`**  
The `top` command automatically finds and displays the most common values of a field with counts and percentages.

**39. B - `rare`**  
The `rare` command is the opposite of `top`, showing the least common values.

**40. A - `count` and `percent`**  
The `top` command automatically creates two fields: `count` (number of occurrences) and `percent` (percentage of total).

**41. B - `count`**  
The `count` function tallies the number of events: `stats count` or `stats count by field`.

**42. A - `dc` (or `distinct_count`)**  
The `dc()` function counts unique values: `stats dc(user)` counts the number of unique users.

**43. A - `stats avg(response_time)`**  
The `avg()` function calculates the average: `stats avg(field_name)`.

**44. C - `by status`**  
Use `by field` to group results: `stats count by status` groups the count by each status value.

**45. B - 10**  
By default, the `top` command returns the top 10 results. Use `top limit=N` to change this.

**46. A - It lists only the unique values of a field**  
The `values()` function returns all unique values of a field, while `list()` returns all values including duplicates.

---

## Domain 6.0: Creating Reports and Dashboards (12%)

**47. A - Click "Save As" > "Report"**  
After running a search, click "Save As" and choose "Report" to save it as a reusable report.

**48. C - Line Chart**  
Line charts are ideal for showing trends and changes over time, with time on the x-axis.

**49. B - A container for a visualization or report on the dashboard**  
Each panel on a dashboard holds a single visualization, report, or element.

**50. A - Run the search, click "Save As" > "Dashboard Panel", and select the existing dashboard**  
You can add searches to existing dashboards by saving them as dashboard panels.

**51. A - Yes, reports can be edited**  
Reports can be modified at any time by the owner or users with appropriate permissions.

**52. B - Pie Chart**  
Pie charts are best for showing proportions or percentages that make up a whole (100%).

**53. B - Results from transforming commands (stats, top, etc.)**  
Visualizations require aggregated data from transforming commands like `stats`, `timechart`, `top`, or `chart`.

---

## Domain 7.0: Creating and Using Lookups (6%)

**54. B - To enrich event data with additional information from an external file**  
Lookups add fields from external sources (like CSV files) to your events based on matching field values.

**55. B - .csv**  
CSV (comma-separated values) files are the most common format for lookup tables in Splunk.

**56. A - 1. Upload the lookup file, 2. Create a Lookup Definition**  
First upload the CSV file to Splunk, then create a lookup definition that tells Splunk how to use the file.

**57. B - `lookup` or `inputlookup`**  
Use `lookup` to add fields to events, or `inputlookup` to retrieve entire lookup table contents. For automatic lookups, configuration is done in the UI.

---

## Domain 8.0: Creating Scheduled Reports and Alerts (5%)

**58. B - Alerts are triggered by specific conditions and can perform actions; Scheduled Reports run on a schedule to present data**  
Alerts trigger when conditions are met (e.g., error count > 10) and can send notifications or run scripts. Scheduled reports run on a schedule and present results.

**59. A - Send an email**  
Common alert actions include sending emails, running scripts, adding to triggered alerts, logging events, or creating tickets in external systems.

**60. A - Activity > Triggered Alerts**  
View recently triggered alerts under Activity > Triggered Alerts, which shows alert history and details.

---

## Exam Domain Distribution Summary

This practice exam aligns with the official Splunk Core Certified User exam blueprint:

- **Domain 1 (Splunk Basics):** 3 questions (5%)
- **Domain 2 (Basic Searching):** 13 questions (22%)
- **Domain 3 (Using Fields in Searches):** 12 questions (20%)
- **Domain 4 (Search Language Fundamentals):** 9 questions (15%)
- **Domain 5 (Using Basic Transforming Commands):** 9 questions (15%)
- **Domain 6 (Creating Reports and Dashboards):** 7 questions (12%)
- **Domain 7 (Creating and Using Lookups):** 4 questions (6%)
- **Domain 8 (Creating Scheduled Reports and Alerts):** 3 questions (5%)

**Total: 60 Questions**

---

## Study Recommendations

Based on the exam blueprint, focus your study efforts on:

1. **Basic Searching (22%)** - Master search syntax, time ranges, Boolean operators, and search modes
2. **Using Fields in Searches (20%)** - Understand field extraction, the fields sidebar, and field-based searches
3. **Search Language Fundamentals & Transforming Commands (30% combined)** - Practice with commands like stats, top, rare, table, sort, dedup, rename

Additional Resources:
- Splunk Fundamentals 1 training course
- Splunk Documentation (docs.splunk.com)
- Splunk Quick Reference Guide
- Practice searches in a Splunk instance

Good luck with your Splunk Core Certified User certification!
