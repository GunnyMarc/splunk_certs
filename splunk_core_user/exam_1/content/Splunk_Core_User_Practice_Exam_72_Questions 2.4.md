# Splunk Core Certified User Practice Exam
## Comprehensive Combined Edition - 72 Unique Questions

**Instructions:**
- This practice exam contains 72 unique multiple-choice questions compiled from multiple practice exams
- Questions are weighted according to the official Splunk Core Certified User exam blueprint
- Recommended time: 72 minutes
- Choose the best answer for each question
- The answer key with detailed explanations is provided at the end

**Exam Format:**
- 72 Questions (Comprehensive Combined Edition)
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

## Domain 2.0: Basic Searching (22% - 16 Questions)

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

---

## Domain 3.0: Using Fields in Searches (20% - 15 Questions)

**Question 21**  
Where are "Selected Fields" displayed in the Splunk interface?

A. In the main event list, under every event  
B. Only in the Job Inspector  
C. In the Fields sidebar, at the top of the list  
D. In the search bar

**Question 22**  
Which three fields are selected by default in Splunk?

A. host, user, ip  
B. host, source, sourcetype  
C. index, source, splunk_server  
D. time, event_id, host

**Question 23**  
What criteria must a field meet to be listed as an "Interesting Field"?

A. It must be a numeric field  
B. It must appear in at least 20% of the events  
C. It must be manually selected by the user  
D. It must contain a unique value

**Question 24**  
How can you add a field to the "Selected Fields" list?

A. Click the field in the "Interesting Fields" list and select "Yes" for Selected  
B. Use the `select` command in SPL  
C. Right-click the event and choose "Promote"  
D. It happens automatically after 10 searches

**Question 25**  
Which command would you use to exclude specific fields from the search results?

A. `remove fieldname`  
B. `fields - fieldname`  
C. `delete fieldname`  
D. `exclude fieldname`

**Question 26**  
What is the difference between `source` and `sourcetype`?

A. `source` is the format; `sourcetype` is the file name  
B. `source` is the file path/input stream; `sourcetype` is the data classification/format  
C. They are identical  
D. `sourcetype` is the server name

**Question 27**  
Are field names in Splunk case-sensitive?

A. True - field names are case-sensitive  
B. False - field names are not case-sensitive

**Question 28**  
In the search `status=404`, what does "status" represent?

A. The value  
B. The field name  
C. The tag  
D. The index

**Question 29**  
Which symbol is used to perform a wildcard match within a field value (e.g., `user=admin*`)?

A. %  
B. ?  
C. *  
D. !

**Question 30**  
What does the `!=` operator do in a field search?

A. It looks for events where the field does NOT equal the value  
B. It sets the field to a new value  
C. It matches values that sound similar  
D. It looks for the field in all indexes

**Question 31**  
Can you search for a value without specifying a field name (e.g., `error` instead of `field=error`)?

A. Yes, Splunk searches across all field values  
B. No, field names are mandatory  
C. Only in Verbose mode  
D. Only for numeric values

**Question 32**  
Which field in the Fields sidebar shows the number of events containing that field?

A. Count  
B. Coverage  
C. Frequency  
D. The number is displayed next to each field

**Question 33**  
When using comparison operators with numeric fields, which operator would you use to find values greater than or equal to 100?

A. `field>100`  
B. `field>=100`  
C. `field=>100`  
D. `field==100`

**Question 34**  
Which sidebar link allows you to see fields that appear in less than 20% of events?

A. Rare Fields  
B. All Fields  
C. Hidden Fields  
D. More Fields

**Question 35**  
In the Fields Sidebar, what does the 'a' symbol next to a field name indicate?

A. The field contains string (alphanumeric) values  
B. The field is a number  
C. The field is hidden  
D. The field is automatically extracted

---

## Domain 4.0: Search Language Fundamentals (15% - 11 Questions)

**Question 36**  
Which command sorts the results in ascending order by a specific field?

A. `sort field`  
B. `order field asc`  
C. `arrange field`  
D. `rank field`

**Question 37**  
To rename a field in the search results, which command do you use?

A. `rename old_name as new_name`  
B. `change old_name to new_name`  
C. `alter old_name new_name`  
D. `modify old_name = new_name`

**Question 38**  
Which command removes duplicate events from your search results?

A. `distinct`  
B. `unique`  
C. `dedup`  
D. `remove_duplicates`

**Question 39**  
What is the purpose of the search pipeline in Splunk?

A. To physically transport data  
B. To chain commands together using the pipe symbol `|` to process search results  
C. To store backup data  
D. To manage user permissions

**Question 40**  
How do you specify a particular index in your search?

A. `index=indexname`  
B. `source=indexname`  
C. `using index indexname`  
D. `from indexname`

**Question 41**  
Which command displays only specified fields in a table format?

A. `show`  
B. `table`  
C. `display`  
D. `format`

**Question 42**  
What does the `fields` command do?

A. Creates new fields  
B. Includes or excludes fields from the search results  
C. Counts the number of fields  
D. Encrypts field values

**Question 43**  
Can you chain multiple search commands together?

A. No, only one command per search  
B. Yes, by separating them with a pipe `|`  
C. Yes, but only two commands maximum  
D. Only with admin privileges

**Question 44**  
Which command returns the first N results?

A. `top`  
B. `head`  
C. `first`  
D. `initial`

**Question 45**  
What does the `tail` command do?

A. Returns the first N results  
B. Returns the last N results  
C. Returns results from the footer  
D. Returns only errors

**Question 46**  
To search specifically in the 'web' index, what syntax should you use?

A. index:web  
B. index=web  
C. using index web  
D. source=web

---

## Domain 5.0: Using Basic Transforming Commands (15% - 11 Questions)

**Question 47**  
Which command finds the most common values of a field?

A. `rare`  
B. `top`  
C. `stats`  
D. `common`

**Question 48**  
Which command finds the least common values of a field?

A. `bottom`  
B. `rare`  
C. `limit`  
D. `least`

**Question 49**  
What fields are automatically created by the `top` command?

A. `count` and `percent`  
B. `total` and `rate`  
C. `sum` and `avg`  
D. `hits` and `score`

**Question 50**  
Which `stats` function would you use to count the total number of events?

A. `sum`  
B. `count`  
C. `list`  
D. `total`

**Question 51**  
Which `stats` function calculates the distinct (unique) count of a field?

A. `dc` (or `distinct_count`)  
B. `uc`  
C. `uniq`  
D. `count_distinct`

**Question 52**  
What is the correct syntax to calculate the average of a field named "response_time"?

A. `stats avg(response_time)`  
B. `stats average=response_time`  
C. `stats mean of response_time`  
D. `table avg(response_time)`

**Question 53**  
To group stats results by a specific field (e.g., status), which clause do you use?

A. `group by status`  
B. `split status`  
C. `by status`  
D. `for status`

**Question 54**  
By default, how many results does the `top` command return?

A. 5  
B. 10  
C. 20  
D. 100

**Question 55**  
What does the `values` function do within the `stats` command?

A. It lists only the unique values of a field  
B. It counts all values  
C. It calculates the sum  
D. It sorts the values alphabetically

**Question 56**  
Which `stats` function would you use to find the maximum value of a numeric field?

A. `highest`  
B. `max`  
C. `top`  
D. `peak`

**Question 57**  
What does the `list` function do within the `stats` command?

A. It lists every value of the field (including duplicates)  
B. It lists only unique values  
C. It creates a bulleted list in the dashboard  
D. It sorts the values

---

## Domain 6.0: Creating Reports and Dashboards (12% - 8 Questions)

**Question 58**  
How do you save a search as a Report?

A. Click "Save As" > "Report"  
B. Copy the text to a document  
C. Click "Export" > "Report"  
D. Use the `report` command

**Question 59**  
Which visualization is best for showing a trend over time?

A. Pie Chart  
B. Single Value  
C. Line Chart  
D. Gauge

**Question 60**  
What is a "Panel" in a Splunk dashboard?

A. The settings menu  
B. A container for a visualization or report on the dashboard  
C. The user login screen  
D. The search bar

**Question 61**  
How do you add a search to an existing dashboard?

A. Run the search, click "Save As" > "Dashboard Panel", and select the existing dashboard  
B. You must delete the dashboard and recreate it  
C. Drag and drop the search bar  
D. Use the `dashboard` command

**Question 62**  
Can you edit a report after it has been created?

A. Yes, reports can be edited  
B. No, reports are immutable  
C. Only within 24 hours of creation  
D. Only by the admin

**Question 63**  
Which visualization would be appropriate for comparing the share or percentage of a whole?

A. Line Chart  
B. Pie Chart  
C. Marker Map  
D. Scatter Plot

**Question 64**  
What type of search results are required to create a visualization (chart)?

A. Raw events only  
B. Results from transforming commands (stats, top, etc.)  
C. Text-only results  
D. Binary data

**Question 65**  
What is the purpose of dashboard permissions?

A. To control network access  
B. To determine who can view and edit the dashboard  
C. To manage server resources  
D. To encrypt dashboard data

---

## Domain 7.0: Creating and Using Lookups (6% - 4 Questions)

**Question 66**  
What is the primary purpose of a lookup in Splunk?

A. To search the internet  
B. To enrich event data with additional information from an external file  
C. To look up other users  
D. To find lost data

**Question 67**  
Which file type is most commonly used for lookup files?

A. .exe  
B. .csv  
C. .docx  
D. .json

**Question 68**  
What are the two main steps to create a file-based lookup in Splunk?

A. 1. Upload the lookup file, 2. Create a Lookup Definition  
B. 1. Email the file to support, 2. Wait for approval  
C. 1. Place the file on the desktop, 2. Run `inputlookup`  
D. 1. Rename the file, 2. Compress the file

**Question 69**  
Which command is used to reference a lookup table in a search?

A. `load`  
B. `lookup` or `inputlookup`  
C. `find`  
D. `search_file`

---

## Domain 8.0: Creating Scheduled Reports and Alerts (5% - 3 Questions)

**Question 70**  
What distinguishes an Alert from a Scheduled Report?

A. Alerts are manual; Reports are automatic  
B. Alerts are triggered by specific conditions and can perform actions; Scheduled Reports run on a schedule to present data  
C. Alerts cost money; Reports are free  
D. Alerts are only for administrators

**Question 71**  
Which of the following is a valid Alert Action?

A. Send an email  
B. Reboot the server  
C. Print to console  
D. Delete the user account

**Question 72**  
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
The most effective way to reduce the number of events retrieved from disk is to narrow the time range of your search. This limits the amount of data Splunk needs to scan from the indexes. Commands like `head` and `fields` only affect what's displayed after the data has already been retrieved from disk, so they don't improve the efficiency of data retrieval.

**6. B - "failed login"**  
Using quotation marks searches for the exact phrase "failed login" as it appears. Without quotes, Splunk would search for events containing both "failed" AND "login" anywhere in the event, which could return different results.

**7. C - Earliest=@d**  
The `@d` syntax snaps to the beginning of the current day (midnight). The `@` symbol is the time snap operator that rounds to the nearest specified time unit.

**8. B - The number of events matching the search query over time**  
The Timeline displays a visual histogram showing the distribution of events over the search time range, with bars representing event counts in different time buckets. This helps identify patterns and spikes in your data.

**9. C - @**  
The `@` (at) symbol is used to snap time to the nearest time unit. For example, `@d` snaps to the beginning of the day, `@h` to the beginning of the hour, `@mon` to the beginning of the month.

**10. B - How many events are returned and which fields are discovered**  
Search Mode controls field discovery behavior: Fast mode returns events with minimal field extraction for speed; Smart mode (default) balances performance and field discovery; Verbose mode discovers all possible fields but is slower.

**11. B - AND is evaluated first**  
In Boolean logic without parentheses, AND has higher precedence than OR. NOT has the highest precedence of all. So "A OR B AND C" is evaluated as "A OR (B AND C)".

**12. A - Export**  
The Export option allows you to save search results in various formats including CSV, XML, JSON, and raw event format. This is different from saving as a Report, which saves the search itself for reuse.

**13. B - earliest=-15m**  
The minus sign (-) indicates time in the past relative to now. `earliest=-15m` means "15 minutes ago." The format is always `earliest=-<time><unit>` where unit can be s (seconds), m (minutes), h (hours), d (days), etc.

**14. B - It zooms into that specific time range**  
Clicking on a Timeline bar automatically adjusts your search time range to zoom into that specific time bucket, allowing you to examine the events in that period more closely.

**15. A - Pause, Stop, or Finalize**  
Search jobs can be controlled in several ways: Pause temporarily suspends the search, Stop cancels it completely, and Finalize completes the search immediately with the results gathered so far. "Compress" is not a valid search job control.

**16. A - Events tab**  
The Events tab displays raw events in list format with relevant fields highlighted and extracted. This is the default view when you run a search and provides the most detailed event information.

**17. B - Specify the index name**  
Specifying the index (e.g., `index=web`) narrows the search scope and significantly improves performance by limiting where Splunk looks for data. Using leading wildcards (*fail), searching "All Time", and excessive OR operators all reduce search efficiency.

**18. B - A single piece of data with a timestamp**  
In Splunk terminology, an "event" is a single record of data with an associated timestamp. Events are the fundamental unit of data in Splunk - each event represents one occurrence, log entry, or data point.

**19. B - ***  
The asterisk (*) is the universal wildcard in Splunk for matching any character sequence. It can be used to match zero or more characters in searches.

**20. A - append**  
The `append` command is used to combine the results of two searches by adding the results of a subsearch to the current results. This allows you to merge data from different searches into a single result set.

---

## Domain 3.0: Using Fields in Searches (20%)

**21. C - In the Fields sidebar, at the top of the list**  
Selected Fields appear at the top section of the Fields sidebar (on the left side of the search interface). These fields are automatically extracted and displayed in the event viewer, making them easy to see and use in searches.

**22. B - host, source, sourcetype**  
These three default fields are always selected in Splunk because they provide fundamental metadata about where the data originated. `host` identifies the machine that generated the data, `source` identifies the specific file or input, and `sourcetype` classifies the data format.

**23. B - It must appear in at least 20% of the events**  
Splunk automatically identifies fields as "Interesting" if they appear in at least 20% of the events in the search results. This helps surface fields that are common enough to be useful but not so ubiquitous as to be overwhelming.

**24. A - Click the field in the "Interesting Fields" list and select "Yes" for Selected**  
You can promote fields from the Interesting Fields section to Selected Fields by clicking on the field name in the sidebar and choosing "Yes" for Selected. This makes the field appear in the Selected Fields section and display in event listings.

**25. B - `fields - fieldname`**  
The `fields` command with a minus sign (-) excludes specified fields from search results. For example, `fields - _raw` excludes the raw event text. To include specific fields, use `fields + fieldname` or just `fields fieldname`.

**26. B - `source` is the file path/input stream; `sourcetype` is the data classification/format**  
The `source` field identifies where the data came from (e.g., the specific file path like /var/log/auth.log or network stream). The `sourcetype` field classifies the data format/type (e.g., apache_access, syslog, cisco:asa, linux_secure), which determines how Splunk parses and interprets the data.

**27. A - True - field names are case-sensitive**  
Field names in Splunk are case-sensitive, meaning `Status`, `status`, and `STATUS` would be treated as three different fields. However, field values are case-insensitive by default in searches.

**28. B - The field name**  
In the field-value pair `status=404`, "status" is the field name (the attribute) and "404" is the value (the specific data for that attribute). The syntax follows the pattern `fieldname=value`.

**29. C - ***  
The asterisk (*) is the wildcard character in Splunk, matching zero or more characters. For example, `user=admin*` would match "admin", "administrator", "admin123", etc.

**30. A - It looks for events where the field does NOT equal the value**  
The `!=` operator is the "not equal to" comparison operator. For example, `status!=200` finds all events where the status field does not equal 200. It acts as a 'Not Equal To' filter.

**31. A - Yes, Splunk searches across all field values**  
You can use keywords without specifying field names. Splunk will search across all field values and the raw event text. For example, searching for just `error` will find events containing "error" anywhere in the event or its fields.

**32. D - The number is displayed next to each field**  
In the Fields sidebar, each field name is followed by a number showing how many events in the current search results contain that field. This helps you understand field coverage in your data.

**33. B - `field>=100`**  
The `>=` operator means "greater than or equal to." For numeric comparisons in Splunk, use standard operators: `>` (greater than), `<` (less than), `>=` (greater than or equal to), `<=` (less than or equal to), `=` (equal to), `!=` (not equal to).

**34. B - All Fields**  
Clicking the "All Fields" link in the sidebar opens a dialogue showing every field discovered in the search results, regardless of their frequency. This includes fields that appear in less than 20% of events (which wouldn't appear as Interesting Fields).

**35. A - The field contains string (alphanumeric) values**  
In the Fields Sidebar, the 'a' symbol next to a field name indicates that the field contains string (alphanumeric) values. The '#' symbol indicates numeric fields. This helps you quickly identify the data type of each field.

---

## Domain 4.0: Search Language Fundamentals (15%)

**36. A - `sort field`**  
The `sort` command sorts results by the specified field in ascending order by default. For example, `sort count` sorts by count in ascending order. Use `sort -field` (with a minus sign) to sort in descending order, or use `sort +field` to explicitly specify ascending.

**37. A - `rename old_name as new_name`**  
The `rename` command changes field names in your results using the syntax `rename old_name as new_name`. You can also use uppercase AS: `rename old_name AS new_name`. Multiple fields can be renamed in one command: `rename field1 as newfield1, field2 as newfield2`.

**38. C - `dedup`**  
The `dedup` (de-duplication) command removes duplicate events based on specified fields. For example, `dedup user` keeps only the first occurrence of each unique user value. You can specify multiple fields: `dedup user, host`.

**39. B - To chain commands together using the pipe symbol `|` to process search results**  
The search pipeline is fundamental to Splunk's Search Processing Language (SPL). It allows you to chain multiple commands together using the pipe symbol `|`, where each command processes the output from the previous command. For example: `index=web | stats count by status | sort -count`.

**40. A - `index=indexname`**  
Specify an index using `index=indexname` at the beginning of your search. You can search multiple indexes using OR: `index=main OR index=security`. Specifying the index is a best practice that improves search performance. The standard Key=Value syntax applies to the index field.

**41. B - `table`**  
The `table` command formats search results into a tabular display with only the specified fields as columns. For example, `table user, action, time` creates a table with just those three fields.

**42. B - Includes or excludes fields from the search results**  
The `fields` command controls which fields appear in search results. Use `fields + field1, field2` to include only specific fields, or `fields - field1` to exclude fields. This doesn't delete fields from events, just controls what's displayed.

**43. B - Yes, by separating them with a pipe `|`**  
Commands are chained together using the pipe symbol `|`. Each command processes the output from the previous command. For example: `index=web status=404 | stats count by uri | sort -count | head 10` chains together stats, sort, and head commands.

**44. B - `head`**  
The `head` command returns the first N results from your search. For example, `head 20` returns the first 20 results. By default (if no number is specified), `head` returns the first 10 results.

**45. B - Returns the last N results**  
The `tail` command returns the last N results from your search. For example, `tail 15` returns the last 15 results. This is the opposite of the `head` command.

**46. B - index=web**  
To search specifically in the 'web' index, use the syntax `index=web`. This follows the standard Key=Value syntax that applies to the index field in Splunk SPL.

---

## Domain 5.0: Using Basic Transforming Commands (15%)

**47. B - `top`**  
The `top` command automatically calculates and displays the most common (frequent) values of a field along with their counts and percentages. For example, `top user` shows the users who appear most frequently in your search results.

**48. B - `rare`**  
The `rare` command is the opposite of `top`, showing the least common (rarest) values of a field. For example, `rare status` displays the status codes that appear least frequently.

**49. A - `count` and `percent`**  
The `top` command automatically creates two fields in its output: `count` (the number of occurrences of each value) and `percent` (the percentage of total events that value represents).

**50. B - `count`**  
The `count` function tallies the number of events or occurrences. Use it as `stats count` to count all events, or `stats count by field` to count events grouped by field values.

**51. A - `dc` (or `distinct_count`)**  
The `dc()` function (distinct count) counts the number of unique values. For example, `stats dc(user)` counts how many different unique users appear in the results. This is different from `count`, which counts all occurrences.

**52. A - `stats avg(response_time)`**  
The `avg()` function calculates the arithmetic mean (average). The syntax is `stats avg(field_name)`. For example, `stats avg(response_time)` calculates the average response time across all events.

**53. C - `by status`**  
Use the `by` clause to group statistics by field values. For example, `stats count by status` groups the event count by each unique status value. You can group by multiple fields: `stats count by status, host`.

**54. B - 10**  
By default, the `top` command returns the top 10 most common values. You can change this using the `limit` parameter, for example: `top limit=20 user` returns the top 20 users.

**55. A - It lists only the unique values of a field**  
The `values()` function returns a list of all unique (distinct) values for a field. For example, `stats values(user) by host` shows all unique users per host. This differs from `list()`, which returns all values including duplicates.

**56. B - `max`**  
The `max()` function finds the maximum (highest) value of a numeric field. For example, `stats max(response_time)` returns the largest response time value. Similarly, `min()` finds the minimum value.

**57. A - It lists every value of the field (including duplicates)**  
The `list()` function within the `stats` command returns all values of a field, including duplicates. This is different from `values()`, which returns only unique values. Use `stats list(field)` to see all occurrences.

---

## Domain 6.0: Creating Reports and Dashboards (12%)

**58. A - Click "Save As" > "Report"**  
After running a search, click the "Save As" button and select "Report" to save the search as a reusable report. You can then specify the report name, description, and permissions.

**59. C - Line Chart**  
Line charts are ideal for displaying trends and changes over time, with time typically on the x-axis and values on the y-axis. They clearly show how metrics increase, decrease, or fluctuate across a time period.

**60. B - A container for a visualization or report on the dashboard**  
A panel is a single container element on a dashboard that holds one visualization, report, table, or other display element. Dashboards are composed of multiple panels arranged in rows and columns.

**61. A - Run the search, click "Save As" > "Dashboard Panel", and select the existing dashboard**  
To add a search to an existing dashboard, run the search, click "Save As", choose "Dashboard Panel", then select whether to add to a new or existing dashboard and choose the target dashboard from the list.

**62. A - Yes, reports can be edited**  
Reports can be modified at any time by users with appropriate permissions (typically the report owner or those with edit permissions). You can edit the search query, time range, scheduling, and other report properties.

**63. B - Pie Chart**  
Pie charts are best for showing proportions or percentages that make up a whole (100%). They effectively display how different categories contribute to a total, making it easy to compare relative sizes of parts to the whole.

**64. B - Results from transforming commands (stats, top, etc.)**  
Visualizations require aggregated or transformed data, not raw events. You need to use transforming commands like `stats`, `timechart`, `top`, `rare`, or `chart` to create the structured data that visualizations can display.

**65. B - To determine who can view and edit the dashboard**  
Dashboard permissions control access rights, determining which users or roles can view the dashboard, edit it, or change its permissions. This ensures sensitive dashboards are only accessible to authorized users.

---

## Domain 7.0: Creating and Using Lookups (6%)

**66. B - To enrich event data with additional information from an external file**  
Lookups enable you to add fields from external sources (typically CSV files) to your events based on matching field values. For example, you might enrich IP addresses with geographic location data, or add employee information based on user IDs.

**67. B - .csv**  
CSV (comma-separated values) files are the most common format for lookup tables in Splunk. They're simple text files where each row represents a record and columns are separated by commas. Other formats like .xlsx can be used but must be converted to CSV first.

**68. A - 1. Upload the lookup file, 2. Create a Lookup Definition**  
Creating a lookup involves two steps: First, upload the CSV file to Splunk (Settings > Lookups > Lookup table files > New). Second, create a lookup definition (Settings > Lookups > Lookup definitions > New) that tells Splunk how to use the uploaded file, including field mappings.

**69. B - `lookup` or `inputlookup`**  
Use the `lookup` command to add fields from a lookup table to your events based on matching field values. Use `inputlookup` to retrieve and display the entire contents of a lookup table. Automatic lookups can also be configured to apply automatically without explicit commands.

---

## Domain 8.0: Creating Scheduled Reports and Alerts (5%)

**70. B - Alerts are triggered by specific conditions and can perform actions; Scheduled Reports run on a schedule to present data**  
Alerts are conditional notifications that trigger when specific criteria are met (e.g., "alert when error count > 100"). They can perform actions like sending emails or running scripts. Scheduled reports run at regular intervals (daily, weekly, etc.) to generate and present results, regardless of what the results show.

**71. A - Send an email**  
Valid alert actions include sending email notifications, running custom scripts, adding to triggered alerts, logging events, creating incidents in ticketing systems, or sending messages to collaboration tools. Destructive actions like rebooting servers or deleting accounts are not available as alert actions.

**72. A - Activity > Triggered Alerts**  
View recently triggered alerts by navigating to Activity > Triggered Alerts in the Splunk interface. This page shows a history of when alerts fired, their severity, and associated information. You can also view alerts from the specific alert's configuration page.

---

## Exam Domain Distribution Summary

This comprehensive combined practice exam contains unique questions from multiple sources:

- **Domain 1 (Splunk Basics):** 4 questions (5.6% ≈ 5%)
- **Domain 2 (Basic Searching):** 16 questions (22.9% ≈ 22%)
- **Domain 3 (Using Fields in Searches):** 15 questions (21.4% ≈ 20%)
- **Domain 4 (Search Language Fundamentals):** 11 questions (15.7% ≈ 15%)
- **Domain 5 (Using Basic Transforming Commands):** 11 questions (15.7% ≈ 15%)
- **Domain 6 (Creating Reports and Dashboards):** 8 questions (11.4% ≈ 12%)
- **Domain 7 (Creating and Using Lookups):** 4 questions (5.7% ≈ 6%)
- **Domain 8 (Creating Scheduled Reports and Alerts):** 3 questions (4.3% ≈ 5%)

**Total: 72 Unique Questions**

---

## Study Recommendations

Based on the exam blueprint, prioritize your study efforts on these areas:

### High-Priority Topics (22-20%)
1. **Basic Searching (22%)** - Master search syntax, time ranges, Boolean operators, wildcards, search modes, timeline, and search job controls
2. **Using Fields in Searches (20%)** - Understand field extraction, the fields sidebar, field-based searches, comparison operators, wildcards, and field indicators

### Medium-Priority Topics (15% each)
3. **Search Language Fundamentals (15%)** - Practice with fundamental commands: table, rename, fields, dedup, sort, head, tail, index specification
4. **Using Basic Transforming Commands (15%)** - Master stats, top, rare and their various functions (count, avg, sum, max, min, dc, values, list)

### Lower-Priority Topics (12-5%)
5. **Creating Reports and Dashboards (12%)** - Know how to create, edit, and manage reports and dashboards; understand different visualization types and permissions
6. **Creating and Using Lookups (6%)** - Understand lookup creation, configuration, and usage with the lookup and inputlookup commands
7. **Creating Scheduled Reports and Alerts (5%)** - Know the difference between scheduled reports and alerts, and how to configure them
8. **Splunk Basics (5%)** - Understand Splunk architecture, components, apps, roles, and basic navigation

### Recommended Study Resources
- **Splunk Fundamentals 1** (free eLearning course)
- **Splunk Quick Reference Guide** (downloadable PDF)
- **Splunk Documentation** (docs.splunk.com)
- **Splunk Search Tutorial** (interactive in-product tutorial)
- **Hands-on Practice** - Most important! Practice searches in a Splunk instance

### Practice Tips
1. Set up a practice Splunk instance (free Splunk Enterprise trial or Splunk Cloud trial)
2. Work through all the questions in this practice exam
3. For any questions you miss, review the explanation and practice that concept
4. Focus extra study time on domains where you score lowest
5. Create your own sample data and practice writing searches
6. Time yourself - the actual exam is 60 questions in 60 minutes
7. Review the exam blueprint and ensure you understand all listed objectives

### Key Concepts to Master
- **Search Pipeline:** Understanding how to chain commands with `|`
- **Time Modifiers:** Using `@`, `earliest`, `latest`, and relative time
- **Field Operations:** Selecting, excluding, renaming, and filtering by fields
- **Transforming Commands:** stats with various functions, top, rare, chart
- **Best Practices:** Specifying index, narrowing time range, avoiding leading wildcards
- **Visualizations:** Matching the right chart type to your data and use case

Good luck with your Splunk Core Certified User certification exam!
