# Splunk Core Certified User Practice Exam
## Enhanced Edition - 75 Unique Questions

**Instructions:**
- This practice exam contains 75 unique multiple-choice questions
- Questions are weighted according to the official Splunk Core Certified User exam blueprint
- Recommended time: 75 minutes
- Choose the best answer for each question
- The answer key with detailed explanations is provided at the end

**Exam Format:**
- 75 Questions (Enhanced Edition)
- Entry-Level Certification
- Based on official 60-question exam blueprint with additional practice questions

---

## Domain 1.0: Splunk Basics (5% - 4 Questions)

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

**Question 4**  
Which of the following is a default role in Splunk Enterprise?

A. SuperUser  
B. Power  
C. Network_Admin  
D. Auditor

---

## Domain 2.0: Basic Searching (22% - 17 Questions)

**Question 5**  
When running a search, what is the most effective way to limit the number of events retrieved from disk?

A. Use the `head` command  
B. Use the `fields` command  
C. Specify a narrower time range  
D. Use the `table` command

**Question 6**  
What is the correct syntax to search for events containing the exact phrase "failed login"?

A. failed AND login  
B. "failed login"  
C. failed_login  
D. string=failed login

**Question 7**  
Which time picker syntax would you use to search data from the beginning of today?

A. Last 24 hours  
B. -1d  
C. Earliest=@d  
D. Previous business day

**Question 8**  
What does the Timeline visual in search results represent?

A. The time the search took to run  
B. The number of events matching the search query over time  
C. The CPU usage of the indexer  
D. The bandwidth used by the forwarder

**Question 9**  
Which symbol is used to snap a time range to a specific unit (e.g., beginning of the day)?

A. *  
B. $  
C. @  
D. #

**Question 10**  
What does the Search Mode setting (Fast, Smart, Verbose) control?

A. The speed of the indexer  
B. How many events are returned and which fields are discovered  
C. The number of users who can view the search  
D. The expiration time of the search job

**Question 11**  
How do Boolean operators affect search precedence when no parentheses are used?

A. OR is evaluated first  
B. AND is evaluated first  
C. NOT is evaluated first  
D. They are evaluated left-to-right

**Question 12**  
Which command or action allows you to save your search results in CSV format?

A. Export  
B. Save As Report  
C. Save As Dashboard  
D. Print

**Question 13**  
When using the `earliest` and `latest` time modifiers in a search string, what is the correct syntax to look back 15 minutes?

A. earliest=15m  
B. earliest=-15m  
C. time=-15m  
D. start=now-15m

**Question 14**  
What happens when you click on a bar in the Timeline?

A. It deletes the events in that time bucket  
B. It zooms into that specific time range  
C. It highlights the events in red  
D. It exports the data

**Question 15**  
How can you control a running search job?

A. Pause, Stop, or Finalize  
B. Restart or Delete only  
C. Compress or Archive  
D. Forward or Background

**Question 16**  
Which tab allows you to view raw events in a clean list format?

A. Events tab  
B. Statistics tab  
C. Visualization tab  
D. Job Inspector

**Question 17**  
Which of the following is considered a best practice for searching in Splunk?

A. Use wildcards at the beginning of strings (e.g., `*fail`)  
B. Specify the index name  
C. Search `All Time` by default  
D. Use as many OR operators as possible

**Question 18**  
What does the term "event" refer to in Splunk?

A. A user login action  
B. A single piece of data with a timestamp  
C. An alert notification  
D. A scheduled report execution

**Question 19**  
Which symbol is used to perform a wildcard match within a search string?

A. %  
B. *  
C. ?  
D. #

**Question 20**  
Which command is used to combine the results of two searches?

A. append  
B. combine  
C. add  
D. plus

**Question 21**  
What is the purpose of using parentheses in a search query?

A. To create a comment  
B. To group Boolean operations and control evaluation order  
C. To escape special characters  
D. To define a time range

---

## Domain 3.0: Using Fields in Searches (20% - 16 Questions)

**Question 22**  
Where are "Selected Fields" displayed in the Splunk interface?

A. In the main event list, under every event  
B. Only in the Job Inspector  
C. In the Fields sidebar, at the top of the list  
D. In the search bar

**Question 23**  
Which three fields are selected by default in Splunk?

A. host, user, ip  
B. host, source, sourcetype  
C. index, source, splunk_server  
D. time, event_id, host

**Question 24**  
What criteria must a field meet to be listed as an "Interesting Field"?

A. It must be a numeric field  
B. It must appear in at least 20% of the events  
C. It must be manually selected by the user  
D. It must contain a unique value

**Question 25**  
How can you add a field to the "Selected Fields" list?

A. Click the field in the "Interesting Fields" list and select "Yes" for Selected  
B. Use the `select` command in SPL  
C. Right-click the event and choose "Promote"  
D. It happens automatically after 10 searches

**Question 26**  
Which command would you use to exclude specific fields from the search results?

A. `remove fieldname`  
B. `fields - fieldname`  
C. `delete fieldname`  
D. `exclude fieldname`

**Question 27**  
What is the difference between `source` and `sourcetype`?

A. `source` is the format; `sourcetype` is the file name  
B. `source` is the file path/input stream; `sourcetype` is the data classification/format  
C. They are identical  
D. `sourcetype` is the server name

**Question 28**  
Are field names in Splunk case-sensitive?

A. True - field names are case-sensitive  
B. False - field names are not case-sensitive

**Question 29**  
In the search `status=404`, what does "status" represent?

A. The value  
B. The field name  
C. The tag  
D. The index

**Question 30**  
Which symbol is used to perform a wildcard match within a field value (e.g., `user=admin*`)?

A. %  
B. ?  
C. *  
D. !

**Question 31**  
What does the `!=` operator do in a field search?

A. It looks for events where the field does NOT equal the value  
B. It sets the field to a new value  
C. It matches values that sound similar  
D. It looks for the field in all indexes

**Question 32**  
Can you search for a value without specifying a field name (e.g., `error` instead of `field=error`)?

A. Yes, Splunk searches across all field values  
B. No, field names are mandatory  
C. Only in Verbose mode  
D. Only for numeric values

**Question 33**  
Which field in the Fields sidebar shows the number of events containing that field?

A. Count  
B. Coverage  
C. Frequency  
D. The number is displayed next to each field

**Question 34**  
When using comparison operators with numeric fields, which operator would you use to find values greater than or equal to 100?

A. `field>100`  
B. `field>=100`  
C. `field=>100`  
D. `field==100`

**Question 35**  
Which sidebar link allows you to see fields that appear in less than 20% of events?

A. Rare Fields  
B. All Fields  
C. Hidden Fields  
D. More Fields

**Question 36**  
In the Fields Sidebar, what does the 'a' symbol next to a field name indicate?

A. The field contains string (alphanumeric) values  
B. The field is a number  
C. The field is hidden  
D. The field is automatically extracted

**Question 37**  
What does the '#' symbol next to a field name in the Fields sidebar indicate?

A. The field is a comment  
B. The field contains numeric values  
C. The field is hidden  
D. The field is a calculated field

---

## Domain 4.0: Search Language Fundamentals (15% - 11 Questions)

**Question 38**  
Which command sorts the results in ascending order by a specific field?

A. `sort field`  
B. `order field asc`  
C. `arrange field`  
D. `rank field`

**Question 39**  
To rename a field in the search results, which command do you use?

A. `rename old_name as new_name`  
B. `change old_name to new_name`  
C. `alter old_name new_name`  
D. `modify old_name = new_name`

**Question 40**  
Which command removes duplicate events from your search results?

A. `distinct`  
B. `unique`  
C. `dedup`  
D. `remove_duplicates`

**Question 41**  
What is the purpose of the search pipeline in Splunk?

A. To physically transport data  
B. To chain commands together using the pipe symbol `|` to process search results  
C. To store backup data  
D. To manage user permissions

**Question 42**  
How do you specify a particular index in your search?

A. `index=indexname`  
B. `source=indexname`  
C. `using index indexname`  
D. `from indexname`

**Question 43**  
Which command displays only specified fields in a table format?

A. `show`  
B. `table`  
C. `display`  
D. `format`

**Question 44**  
What does the `fields` command do?

A. Creates new fields  
B. Includes or excludes fields from the search results  
C. Counts the number of fields  
D. Encrypts field values

**Question 45**  
Can you chain multiple search commands together?

A. No, only one command per search  
B. Yes, by separating them with a pipe `|`  
C. Yes, but only two commands maximum  
D. Only with admin privileges

**Question 46**  
Which command returns the first N results?

A. `top`  
B. `head`  
C. `first`  
D. `initial`

**Question 47**  
What does the `tail` command do?

A. Returns the first N results  
B. Returns the last N results  
C. Returns results from the footer  
D. Returns only errors

**Question 48**  
To search specifically in the 'web' index, what syntax should you use?

A. index:web  
B. index=web  
C. using index web  
D. source=web

---

## Domain 5.0: Using Basic Transforming Commands (15% - 11 Questions)

**Question 49**  
Which command finds the most common values of a field?

A. `rare`  
B. `top`  
C. `stats`  
D. `common`

**Question 50**  
Which command finds the least common values of a field?

A. `bottom`  
B. `rare`  
C. `limit`  
D. `least`

**Question 51**  
What fields are automatically created by the `top` command?

A. `count` and `percent`  
B. `total` and `rate`  
C. `sum` and `avg`  
D. `hits` and `score`

**Question 52**  
Which `stats` function would you use to count the total number of events?

A. `sum`  
B. `count`  
C. `list`  
D. `total`

**Question 53**  
Which `stats` function calculates the distinct (unique) count of a field?

A. `dc` (or `distinct_count`)  
B. `uc`  
C. `uniq`  
D. `count_distinct`

**Question 54**  
What is the correct syntax to calculate the average of a field named "response_time"?

A. `stats avg(response_time)`  
B. `stats average=response_time`  
C. `stats mean of response_time`  
D. `table avg(response_time)`

**Question 55**  
To group stats results by a specific field (e.g., status), which clause do you use?

A. `group by status`  
B. `split status`  
C. `by status`  
D. `for status`

**Question 56**  
By default, how many results does the `top` command return?

A. 5  
B. 10  
C. 20  
D. 100

**Question 57**  
What does the `values` function do within the `stats` command?

A. It lists only the unique values of a field  
B. It counts all values  
C. It calculates the sum  
D. It sorts the values alphabetically

**Question 58**  
Which `stats` function would you use to find the maximum value of a numeric field?

A. `highest`  
B. `max`  
C. `top`  
D. `peak`

**Question 59**  
What does the `list` function do within the `stats` command?

A. It lists every value of the field (including duplicates)  
B. It lists only unique values  
C. It creates a bulleted list in the dashboard  
D. It sorts the values

---

## Domain 6.0: Creating Reports and Dashboards (12% - 9 Questions)

**Question 60**  
How do you save a search as a Report?

A. Click "Save As" > "Report"  
B. Copy the text to a document  
C. Click "Export" > "Report"  
D. Use the `report` command

**Question 61**  
Which visualization is best for showing a trend over time?

A. Pie Chart  
B. Single Value  
C. Line Chart  
D. Gauge

**Question 62**  
What is a "Panel" in a Splunk dashboard?

A. The settings menu  
B. A container for a visualization or report on the dashboard  
C. The user login screen  
D. The search bar

**Question 63**  
How do you add a search to an existing dashboard?

A. Run the search, click "Save As" > "Dashboard Panel", and select the existing dashboard  
B. You must delete the dashboard and recreate it  
C. Drag and drop the search bar  
D. Use the `dashboard` command

**Question 64**  
Can you edit a report after it has been created?

A. Yes, reports can be edited  
B. No, reports are immutable  
C. Only within 24 hours of creation  
D. Only by the admin

**Question 65**  
Which visualization would be appropriate for comparing the share or percentage of a whole?

A. Line Chart  
B. Pie Chart  
C. Marker Map  
D. Scatter Plot

**Question 66**  
What type of search results are required to create a visualization (chart)?

A. Raw events only  
B. Results from transforming commands (stats, top, etc.)  
C. Text-only results  
D. Binary data

**Question 67**  
What is the purpose of dashboard permissions?

A. To control network access  
B. To determine who can view and edit the dashboard  
C. To manage server resources  
D. To encrypt dashboard data

**Question 68**  
Which visualization type would you use to display a single metric value?

A. Line Chart  
B. Column Chart  
C. Single Value  
D. Table

---

## Domain 7.0: Creating and Using Lookups (6% - 4 Questions)

**Question 69**  
What is the primary purpose of a lookup in Splunk?

A. To search the internet  
B. To enrich event data with additional information from an external file  
C. To look up other users  
D. To find lost data

**Question 70**  
Which file type is most commonly used for lookup files?

A. .exe  
B. .csv  
C. .docx  
D. .json

**Question 71**  
What are the two main steps to create a file-based lookup in Splunk?

A. 1. Upload the lookup file, 2. Create a Lookup Definition  
B. 1. Email the file to support, 2. Wait for approval  
C. 1. Place the file on the desktop, 2. Run `inputlookup`  
D. 1. Rename the file, 2. Compress the file

**Question 72**  
Which command is used to reference a lookup table in a search?

A. `load`  
B. `lookup` or `inputlookup`  
C. `find`  
D. `search_file`

---

## Domain 8.0: Creating Scheduled Reports and Alerts (5% - 3 Questions)

**Question 73**  
What distinguishes an Alert from a Scheduled Report?

A. Alerts are manual; Reports are automatic  
B. Alerts are triggered by specific conditions and can perform actions; Scheduled Reports run on a schedule to present data  
C. Alerts cost money; Reports are free  
D. Alerts are only for administrators

**Question 74**  
Which of the following is a valid Alert Action?

A. Send an email  
B. Reboot the server  
C. Print to console  
D. Delete the user account

**Question 75**  
Where can you view alerts that have recently been triggered?

A. Activity > Triggered Alerts  
B. Settings > Indexes  
C. Help > About  
D. The Login Screen

---
---

# Answer Key with Detailed Explanations

## Domain 1.0: Splunk Basics (5%)

**1. C - Indexer**  
The Indexer is the core component responsible for parsing incoming data, creating indexes, and storing events on disk in a searchable format. Universal Forwarders collect and forward data but don't parse or store it. Search Heads coordinate searches across indexers. Heavy Forwarders can parse and route data but typically don't store it permanently.

**2. B - To provide a specific collection of configurations, dashboards, and knowledge objects for a particular use case**  
Splunk Apps are pre-packaged solutions that bundle together related dashboards, reports, searches, field extractions, and configurations for specific use cases such as IT operations, security monitoring, or business analytics. They provide a customized interface and functionality for particular domains like 'Splunk for Unix' or 'Splunk for AWS'.

**3. A - Settings > User preferences**  
Users can customize their personal settings through the Settings > User preferences menu, where they can configure time zones, default apps, interface preferences, and other personalization options without requiring admin privileges.

**4. B - Power**  
The standard default roles in Splunk Enterprise are Admin, Power, and User. Power users have more capabilities than standard Users (like creating shared objects and scheduling searches) but fewer administrative privileges than Admins. SuperUser, Network_Admin, and Auditor are not default roles.

---

## Domain 2.0: Basic Searching (22%)

**5. C - Specify a narrower time range**  
The most effective way to reduce the number of events retrieved from disk is to narrow the time range of your search. This limits the amount of data Splunk needs to scan from the indexes. Commands like `head` and `fields` only affect what's displayed after the data has already been retrieved from disk.

**6. B - "failed login"**  
Using quotation marks searches for the exact phrase "failed login" as it appears. Without quotes, Splunk would search for events containing both "failed" AND "login" anywhere in the event.

**7. C - Earliest=@d**  
The `@d` syntax snaps to the beginning of the current day (midnight). The `@` symbol is the time snap operator that rounds to the nearest specified time unit.

**8. B - The number of events matching the search query over time**  
The Timeline displays a visual histogram showing the distribution of events over the search time range, with bars representing event counts in different time buckets.

**9. C - @**  
The `@` (at) symbol is used to snap time to the nearest time unit. For example, `@d` snaps to the beginning of the day, `@h` to the beginning of the hour.

**10. B - How many events are returned and which fields are discovered**  
Search Mode controls field discovery behavior: Fast mode returns events with minimal field extraction for speed; Smart mode (default) balances performance and field discovery; Verbose mode discovers all possible fields but is slower.

**11. B - AND is evaluated first**  
In Boolean logic without parentheses, AND has higher precedence than OR. NOT has the highest precedence of all.

**12. A - Export**  
The Export option allows you to save search results in various formats including CSV, XML, JSON, and raw event format.

**13. B - earliest=-15m**  
The minus sign (-) indicates time in the past relative to now. `earliest=-15m` means "15 minutes ago."

**14. B - It zooms into that specific time range**  
Clicking on a Timeline bar automatically adjusts your search time range to zoom into that specific time bucket.

**15. A - Pause, Stop, or Finalize**  
Search jobs can be paused (temporarily stopped), stopped (cancelled), or finalized (completed immediately with current results).

**16. A - Events tab**  
The Events tab displays raw events in list format with relevant fields highlighted and extracted.

**17. B - Specify the index name**  
Specifying the index (e.g., `index=web`) narrows the search scope and significantly improves performance by limiting where Splunk looks for data.

**18. B - A single piece of data with a timestamp**  
In Splunk terminology, an "event" is a single record of data with an associated timestamp.

**19. B - ***  
The asterisk (*) is the universal wildcard in Splunk for matching any character sequence.

**20. A - append**  
The `append` command is used to combine the results of two searches by adding the results of a subsearch to the current results.

**21. B - To group Boolean operations and control evaluation order**  
Parentheses in search queries allow you to group Boolean operations and explicitly control the order of evaluation. For example, `(error OR warning) AND status=500` ensures the OR operation is evaluated first before the AND.

---

## Domain 3.0: Using Fields in Searches (20%)

**22. C - In the Fields sidebar, at the top of the list**  
Selected Fields appear at the top section of the Fields sidebar on the left side of the search interface.

**23. B - host, source, sourcetype**  
These three default fields are always selected because they provide fundamental metadata about where the data originated.

**24. B - It must appear in at least 20% of the events**  
Splunk automatically identifies fields as "Interesting" if they appear in at least 20% of the events in the search results.

**25. A - Click the field in the "Interesting Fields" list and select "Yes" for Selected**  
You can promote fields from the Interesting Fields section to Selected Fields by clicking on the field name and choosing "Yes" for Selected.

**26. B - `fields - fieldname`**  
The `fields` command with a minus sign (-) excludes specified fields from search results.

**27. B - `source` is the file path/input stream; `sourcetype` is the data classification/format**  
The `source` field identifies where the data came from (file path or network stream). The `sourcetype` field classifies the data format (e.g., apache_access, syslog).

**28. A - True - field names are case-sensitive**  
Field names in Splunk are case-sensitive. However, field values are case-insensitive by default in searches.

**29. B - The field name**  
In the field-value pair `status=404`, "status" is the field name and "404" is the value.

**30. C - ***  
The asterisk (*) is the wildcard character in Splunk, matching zero or more characters.

**31. A - It looks for events where the field does NOT equal the value**  
The `!=` operator is the "not equal to" comparison operator.

**32. A - Yes, Splunk searches across all field values**  
You can use keywords without specifying field names. Splunk will search across all field values and the raw event text.

**33. D - The number is displayed next to each field**  
In the Fields sidebar, each field name is followed by a number showing how many events contain that field.

**34. B - `field>=100`**  
The `>=` operator means "greater than or equal to."

**35. B - All Fields**  
Clicking the "All Fields" link shows every field discovered, regardless of their frequency.

**36. A - The field contains string (alphanumeric) values**  
The 'a' symbol indicates string (alphanumeric) values. The '#' symbol indicates numeric fields.

**37. B - The field contains numeric values**  
The '#' symbol in the Fields sidebar indicates that the field contains numeric values, which enables numeric operations and comparisons on that field.

---

## Domain 4.0: Search Language Fundamentals (15%)

**38. A - `sort field`**  
The `sort` command sorts results by the specified field in ascending order by default.

**39. A - `rename old_name as new_name`**  
The `rename` command changes field names using the syntax `rename old_name as new_name`.

**40. C - `dedup`**  
The `dedup` command removes duplicate events based on specified fields.

**41. B - To chain commands together using the pipe symbol `|` to process search results**  
The search pipeline allows you to chain multiple commands together using the pipe symbol `|`.

**42. A - `index=indexname`**  
Specify an index using `index=indexname` at the beginning of your search.

**43. B - `table`**  
The `table` command formats search results into a tabular display with only the specified fields as columns.

**44. B - Includes or excludes fields from the search results**  
The `fields` command controls which fields appear in search results.

**45. B - Yes, by separating them with a pipe `|`**  
Commands are chained together using the pipe symbol `|`.

**46. B - `head`**  
The `head` command returns the first N results from your search.

**47. B - Returns the last N results**  
The `tail` command returns the last N results from your search.

**48. B - index=web**  
To search specifically in the 'web' index, use the syntax `index=web`.

---

## Domain 5.0: Using Basic Transforming Commands (15%)

**49. B - `top`**  
The `top` command automatically calculates and displays the most common values of a field.

**50. B - `rare`**  
The `rare` command shows the least common values of a field.

**51. A - `count` and `percent`**  
The `top` command automatically creates two fields: `count` and `percent`.

**52. B - `count`**  
The `count` function tallies the number of events.

**53. A - `dc` (or `distinct_count`)**  
The `dc()` function counts the number of unique values.

**54. A - `stats avg(response_time)`**  
The `avg()` function calculates the arithmetic mean.

**55. C - `by status`**  
Use the `by` clause to group statistics by field values.

**56. B - 10**  
By default, the `top` command returns the top 10 most common values.

**57. A - It lists only the unique values of a field**  
The `values()` function returns a list of all unique values for a field.

**58. B - `max`**  
The `max()` function finds the maximum value of a numeric field.

**59. A - It lists every value of the field (including duplicates)**  
The `list()` function returns all values of a field, including duplicates.

---

## Domain 6.0: Creating Reports and Dashboards (12%)

**60. A - Click "Save As" > "Report"**  
After running a search, click "Save As" and select "Report" to save it as a reusable report.

**61. C - Line Chart**  
Line charts are ideal for displaying trends and changes over time.

**62. B - A container for a visualization or report on the dashboard**  
A panel is a single container element on a dashboard that holds one visualization or report.

**63. A - Run the search, click "Save As" > "Dashboard Panel", and select the existing dashboard**  
To add a search to an existing dashboard, save it as a Dashboard Panel and select the target dashboard.

**64. A - Yes, reports can be edited**  
Reports can be modified at any time by users with appropriate permissions.

**65. B - Pie Chart**  
Pie charts are best for showing proportions or percentages that make up a whole.

**66. B - Results from transforming commands (stats, top, etc.)**  
Visualizations require aggregated or transformed data from commands like `stats`, `timechart`, `top`, or `chart`.

**67. B - To determine who can view and edit the dashboard**  
Dashboard permissions control access rights, determining which users or roles can view or edit the dashboard.

**68. C - Single Value**  
The Single Value visualization displays a single metric value prominently, often used for KPIs or summary statistics like total count, average response time, or current status.

---

## Domain 7.0: Creating and Using Lookups (6%)

**69. B - To enrich event data with additional information from an external file**  
Lookups enable you to add fields from external sources to your events based on matching field values.

**70. B - .csv**  
CSV files are the most common format for lookup tables in Splunk.

**71. A - 1. Upload the lookup file, 2. Create a Lookup Definition**  
First upload the CSV file, then create a lookup definition that tells Splunk how to use it.

**72. B - `lookup` or `inputlookup`**  
Use the `lookup` command to add fields from a lookup table, or `inputlookup` to retrieve entire lookup table contents.

---

## Domain 8.0: Creating Scheduled Reports and Alerts (5%)

**73. B - Alerts are triggered by specific conditions and can perform actions; Scheduled Reports run on a schedule to present data**  
Alerts trigger when specific criteria are met and can perform actions. Scheduled reports run at regular intervals to generate results.

**74. A - Send an email**  
Valid alert actions include sending email notifications, running scripts, or creating incidents in ticketing systems.

**75. A - Activity > Triggered Alerts**  
View recently triggered alerts by navigating to Activity > Triggered Alerts.

---

## Exam Domain Distribution Summary

- **Domain 1 (Splunk Basics):** 4 questions (5.3%)
- **Domain 2 (Basic Searching):** 17 questions (22.7%)
- **Domain 3 (Using Fields in Searches):** 16 questions (21.3%)
- **Domain 4 (Search Language Fundamentals):** 11 questions (14.7%)
- **Domain 5 (Using Basic Transforming Commands):** 11 questions (14.7%)
- **Domain 6 (Creating Reports and Dashboards):** 9 questions (12.0%)
- **Domain 7 (Creating and Using Lookups):** 4 questions (5.3%)
- **Domain 8 (Creating Scheduled Reports and Alerts):** 3 questions (4.0%)

**Total: 75 Questions**

Good luck with your Splunk Core Certified User certification!
