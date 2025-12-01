# Splunk Core User Certification Practice Exam
## 65 Questions

**Instructions:**
- This exam contains 65 multiple-choice questions
- Questions are weighted according to the official exam blueprint percentages
- Choose the best answer for each question
- The answer key is provided at the end

---

## Domain 1.0: Splunk Basics (5%)

**Question 1**  
Which Splunk component is responsible for parsing incoming data and storing it on disk?

A. Universal Forwarder  
B. Search Head  
C. Indexer  
D. Heavy Forwarder

**Question 2**  
What is the primary function of a Splunk App?

A. To forward data to external systems  
B. To provide a specific collection of configurations, dashboards, and knowledge objects for a use case  
C. To manage user licenses  
D. To compress raw data logs

**Question 3**  
Which of the following is a default role in Splunk Enterprise?

A. Power  
B. SuperUser  
C. Network_Admin  
D. Auditor

---

## Domain 2.0: Basic Searching (22%)

**Question 4**  
When running a search, what is the most effective way to limit the number of events retrieved from the disk?

A. Use the `head` command  
B. Use the `fields` command  
C. Specify a narrower time range  
D. Use the `table` command

**Question 5**  
What is the correct syntax to search for events containing the phrase "failed login"?

A. failed AND login  
B. "failed login"  
C. failed_login  
D. string=failed login

**Question 6**  
Which time picker setting would you use to search data from the "beginning of today"?

A. Last 24 hours  
B. -1d  
C. Earliest=@d  
D. Previous business day

**Question 7**  
How do Boolean operators (AND, OR, NOT) affect search precedence if no parentheses are used?

A. OR is evaluated first  
B. AND is evaluated first  
C. NOT is evaluated first  
D. They are evaluated left-to-right

**Question 8**  
Which symbol is used to snap a time range to a specific unit (e.g., beginning of the minute)?

A. *  
B. $  
C. @  
D. #

**Question 9**  
What does the "Search Mode" setting (Fast, Smart, Verbose) control?

A. The speed of the indexer  
B. How many events are returned and which fields are discovered  
C. The number of users who can view the search  
D. The expiration time of the search job

**Question 10**  
Which command allows you to save your search results to a CSV format?

A. Export  
B. Save As Report  
C. Save As Dashboard  
D. Print

**Question 11**  
In the search results, what does the "Timeline" visual represent?

A. The time the search took to run  
B. The number of events matching the search query over time  
C. The CPU usage of the indexer  
D. The bandwidth used by the forwarder

**Question 12**  
When using the `earliest` and `latest` time modifiers in a search string, what is the correct syntax to look back 15 minutes?

A. earliest=15m  
B. earliest=-15m  
C. time=-15m  
D. start=now-15m

**Question 13**  
Which of the following is NOT a status used to control a search job?

A. Pause  
B. Stop  
C. Finalize  
D. Compress

**Question 14**  
What happens if you click a bar in the Timeline?

A. It deletes the events in that time bucket  
B. It zooms into that specific time range  
C. It highlights the events in red  
D. It exports the data

**Question 15**  
If a search is running too slowly, what can you do to see partial results immediately without stopping the search?

A. Click "Finalize"  
B. Click "Pause"  
C. Click "Send to Background"  
D. Switch to "Real-time"

**Question 16**  
Which of the following is considered a "Best Practice" for searching?

A. Use wildcards at the beginning of strings (e.g., `*fail`)  
B. Specify the index name  
C. Search `All Time` by default  
D. Use as many OR operators as possible

**Question 17**  
What allows you to view the raw events in a clean list format?

A. The Events tab  
B. The Statistics tab  
C. The Visualization tab  
D. The Job Inspector

---

## Domain 3.0: Using Fields in Searches (20%)

**Question 18**  
Where are "Selected Fields" displayed?

A. In the main event list, under every event  
B. Only in the Job Inspector  
C. In the Fields sidebar, at the top of the list  
D. In the search bar

**Question 19**  
Which three fields are selected by default?

A. host, user, ip  
B. host, source, sourcetype  
C. index, source, splunk_server  
D. time, event_id, host

**Question 20**  
What criteria must a field meet to be listed as an "Interesting Field"?

A. It must be a numeric field  
B. It must appear in at least 20% of the events  
C. It must be manually selected by the user  
D. It must contain a unique value

**Question 21**  
How can you add a field to the "Selected Fields" list?

A. Click the field in the "Interesting Fields" list and select "Yes" for Selected  
B. Use the `select` command in SPL  
C. Right-click the event and choose "Promote"  
D. It happens automatically after 10 searches

**Question 22**  
Which command would you use to remove specific fields from the search results?

A. `remove fieldname`  
B. `fields - fieldname`  
C. `delete fieldname`  
D. `exclude fieldname`

**Question 23**  
What is the difference between `source` and `sourcetype`?

A. `source` is the format; `sourcetype` is the file name  
B. `source` is the file name/input stream; `sourcetype` is the data classification/format  
C. They are identical  
D. `sourcetype` is the server name

**Question 24**  
True or False: Field names in Splunk are case-sensitive.

A. True  
B. False

**Question 25**  
If you search `status=404`, "status" is the ______ and "404" is the ______.

A. Value, Field  
B. Field, Value  
C. Tag, Alias  
D. Host, Source

**Question 26**  
Which symbol is used to perform a wildcard match within a field value (e.g., `user=admin*`)?

A. %  
B. ?  
C. *  
D. !

**Question 27**  
What does the `!=` operator do in a field search?

A. It looks for events where the field does NOT equal the value  
B. It sets the field to a new value  
C. It matches values that sound similar  
D. It looks for the field in all indexes

**Question 28**  
Can you search for a value without specifying a field name (e.g., `error` instead of `status=error`)?

A. Yes, using keywords  
B. No, field names are mandatory  
C. Only in Verbose mode  
D. Only for numeric values

**Question 29**  
To display only the `clientip` and `action` fields in the results table, which command should you use?

A. `return clientip, action`  
B. `table clientip, action`  
C. `list clientip, action`  
D. `show clientip, action`

---

## Domain 4.0: Search Fundamentals (16%)

**Question 30**  
Which command sorts the results in ascending order by a specific field?

A. `sort field`  
B. `order field asc`  
C. `arrange field`  
D. `rank field`

**Question 31**  
To rename a field in the search results, which command do you use?

A. `rename old_name as new_name`  
B. `change old_name to new_name`  
C. `alter old_name new_name`  
D. `modify old_name = new_name`

**Question 32**  
Which command removes duplicate events from your search results?

A. `distinct`  
B. `unique`  
C. `dedup`  
D. `remove_duplicates`

**Question 33**  
What does the `head` command do?

A. Returns the first N results  
B. Returns the last N results  
C. Returns results from the header  
D. Returns the metadata

**Question 34**  
What does the `tail` command do?

A. Returns the first N results  
B. Returns the last N results  
C. Returns results from the footer  
D. Returns only errors

**Question 35**  
Which command formats your results into a tabular output?

A. `format`  
B. `table`  
C. `grid`  
D. `matrix`

**Question 36**  
What is the primary purpose of the `table` command?

A. To create a database table  
B. To format results into a tabular display with specified fields as columns  
C. To save results to disk  
D. To compress the results

**Question 37**  
When using `dedup`, which event is kept by default?

A. The oldest event  
B. The most recent event  
C. A random event  
D. The event with the most fields

**Question 38**  
Can you include multiple commands in a single search string?

A. No, only one command per search  
B. Yes, by separating them with a pipe `|`  
C. Yes, by separating them with a comma `,`  
D. Yes, by separating them with the word `AND`

**Question 39**  
Which command allows you to keep only specific fields and discard the rest (except time)?

A. `fields`  
B. `table`  
C. `filter`  
D. `keep`

**Question 40**  
To search specifically in the "web" index, what syntax should you use?

A. `index:web`  
B. `index=web`  
C. `using index web`  
D. `source=web`

---

## Domain 5.0: Using Basic Transforming Commands (15%)

**Question 41**  
Which command finds the most frequent values of a field?

A. `rare`  
B. `top`  
C. `stats`  
D. `common`

**Question 42**  
Which command finds the least frequent values of a field?

A. `bottom`  
B. `rare`  
C. `limit`  
D. `least`

**Question 43**  
What fields are created by the `top` command by default?

A. `count` and `percent`  
B. `total` and `rate`  
C. `sum` and `avg`  
D. `hits` and `score`

**Question 44**  
Which `stats` function would you use to count the total number of events?

A. `sum`  
B. `count`  
C. `list`  
D. `total`

**Question 45**  
Which `stats` function calculates the distinct (unique) count of a field?

A. `dc` (or `distinct_count`)  
B. `uc`  
C. `uniq`  
D. `count_distinct`

**Question 46**  
What is the correct syntax to calculate the average of a field named "duration"?

A. `stats avg(duration)`  
B. `stats average=duration`  
C. `stats mean of duration`  
D. `table avg(duration)`

**Question 47**  
To group stats results by a specific field (e.g., User), which clause do you use?

A. `group by User`  
B. `split User`  
C. `by User`  
D. `for User`

**Question 48**  
By default, how many results does the `top` command return?

A. 5  
B. 10  
C. 20  
D. 100

**Question 49**  
Which command allows you to calculate statistics (like sum, avg, max) from your search results?

A. `calc`  
B. `stats`  
C. `math`  
D. `evaluate`

**Question 50**  
What does the `list` function do within the `stats` command?

A. It lists every value of the field  
B. It lists only unique values  
C. It creates a bulleted list in the dashboard  
D. It sorts the values

---

## Domain 6.0: Creating Reports and Dashboards (12%)

**Question 51**  
How do you turn a search into a Report?

A. Click "Save As" > "Report"  
B. Copy the text to a Word doc  
C. Click "Export" > "Report"  
D. Use the `report` command

**Question 52**  
Can a Report be scheduled to run automatically?

A. Yes  
B. No

**Question 53**  
Which visualization is best for showing a trend over time?

A. Pie Chart  
B. Single Value  
C. Line Chart  
D. Gauge

**Question 54**  
What is a "Panel" in a dashboard?

A. The settings menu  
B. A container for a visualization or report on the dashboard  
C. The user login screen  
D. The search bar

**Question 55**  
How do you add a search to an existing dashboard?

A. Run the search, click "Save As" > "Dashboard Panel", and select the existing dashboard  
B. You must delete the dashboard and recreate it  
C. Drag and drop the search bar  
D. Use the `dashboard` command

**Question 56**  
What is the XML source in a dashboard used for?

A. To compile the code  
B. To edit the dashboard layout and behavior (advanced editing)  
C. To store user passwords  
D. To connect to the internet

**Question 57**  
Which visualization would be appropriate for comparing the "share" or "percentage" of a whole?

A. Line Chart  
B. Pie Chart  
C. Marker Map  
D. Scatter Plot

**Question 58**  
Can you edit a dashboard using a drag-and-drop interface?

A. Yes, using the UI Editor  
B. No, only XML is supported

---

## Domain 7.0: Creating and Using Lookups (6%)

**Question 59**  
What is a "Lookup" used for?

A. To search the internet  
B. To enrich event data with static fields from an external file (e.g., CSV)  
C. To look up other users  
D. To find lost data

**Question 60**  
Which file type is most commonly used for lookups?

A. .exe  
B. .csv  
C. .docx  
D. .mp3

**Question 61**  
What are the two main steps to create a file-based lookup?

A. 1. Upload the file, 2. Create a Lookup Definition  
B. 1. Email the file to support, 2. Wait  
C. 1. Put the file on the desktop, 2. Run `inputlookup`  
D. 1. Rename the file, 2. Zip the file

**Question 62**  
Which command loads a lookup table into search results?

A. `load`  
B. `inputlookup` (or `lookup`)  
C. `find`  
D. `search_file`

---

## Domain 8.0: Creating Scheduled Reports and Alerts (5%)

**Question 63**  
What distinguishes an "Alert" from a "Scheduled Report"?

A. Alerts are manual; Reports are automatic  
B. Alerts are triggered by specific conditions (e.g., errors > 5) and perform actions; Reports run on a schedule to present data  
C. Alerts cost money; Reports are free  
D. Alerts are only for admins

**Question 64**  
Which of the following is a valid "Alert Action"?

A. Send an email  
B. Reboot the server  
C. Print the screen  
D. Delete the user

**Question 65**  
Where can you view alerts that have recently triggered?

A. Activity > Triggered Alerts  
B. Settings > Indexes  
C. Help > About  
D. The Login Screen

---
---

# Answer Key

## Domain 1.0: Splunk Basics (5%)
1. **C** - Indexer
2. **B** - To provide a specific collection of configurations, dashboards, and knowledge objects for a use case
3. **A** - Power

## Domain 2.0: Basic Searching (22%)
4. **C** - Specify a narrower time range
5. **B** - "failed login"
6. **C** - Earliest=@d
7. **B** - AND is evaluated first (in context of AND vs OR)
8. **C** - @
9. **B** - How many events are returned and which fields are discovered
10. **A** - Export
11. **B** - The number of events matching the search query over time
12. **B** - earliest=-15m
13. **D** - Compress
14. **B** - It zooms into that specific time range
15. **A** - Click "Finalize"
16. **B** - Specify the index name
17. **A** - The Events tab

## Domain 3.0: Using Fields in Searches (20%)
18. **C** - In the Fields sidebar, at the top of the list
19. **B** - host, source, sourcetype
20. **B** - It must appear in at least 20% of the events
21. **A** - Click the field in the "Interesting Fields" list and select "Yes" for Selected
22. **B** - `fields - fieldname`
23. **B** - `source` is the file name/input stream; `sourcetype` is the data classification/format
24. **A** - True
25. **B** - Field, Value
26. **C** - *
27. **A** - It looks for events where the field does NOT equal the value
28. **A** - Yes, using keywords
29. **B** - `table clientip, action`

## Domain 4.0: Search Fundamentals (16%)
30. **A** - `sort field`
31. **A** - `rename old_name as new_name`
32. **C** - `dedup`
33. **A** - Returns the first N results
34. **B** - Returns the last N results
35. **B** - `table`
36. **B** - To format results into a tabular display with specified fields as columns
37. **B** - The most recent event
38. **B** - Yes, by separating them with a pipe `|`
39. **A** - `fields`
40. **B** - `index=web`

## Domain 5.0: Using Basic Transforming Commands (15%)
41. **B** - `top`
42. **B** - `rare`
43. **A** - `count` and `percent`
44. **B** - `count`
45. **A** - `dc` (or `distinct_count`)
46. **A** - `stats avg(duration)`
47. **C** - `by User`
48. **B** - 10
49. **B** - `stats`
50. **A** - It lists every value of the field

## Domain 6.0: Creating Reports and Dashboards (12%)
51. **A** - Click "Save As" > "Report"
52. **A** - Yes
53. **C** - Line Chart
54. **B** - A container for a visualization or report on the dashboard
55. **A** - Run the search, click "Save As" > "Dashboard Panel", and select the existing dashboard
56. **B** - To edit the dashboard layout and behavior (advanced editing)
57. **B** - Pie Chart
58. **A** - Yes, using the UI Editor

## Domain 7.0: Creating and Using Lookups (6%)
59. **B** - To enrich event data with static fields from an external file (e.g., CSV)
60. **B** - .csv
61. **A** - 1. Upload the file, 2. Create a Lookup Definition
62. **B** - `inputlookup` (or `lookup`)

## Domain 8.0: Creating Scheduled Reports and Alerts (5%)
63. **B** - Alerts are triggered by specific conditions (e.g., errors > 5) and perform actions; Reports run on a schedule to present data
64. **A** - Send an email
65. **A** - Activity > Triggered Alerts

---

**Exam Domain Distribution:**
- Domain 1 (Splunk Basics): 3 questions (5%)
- Domain 2 (Basic Searching): 14 questions (22%)
- Domain 3 (Using Fields): 12 questions (20%)
- Domain 4 (Search Fundamentals): 11 questions (16%)
- Domain 5 (Transforming Commands): 10 questions (15%)
- Domain 6 (Reports & Dashboards): 8 questions (12%)
- Domain 7 (Lookups): 4 questions (6%)
- Domain 8 (Scheduled Reports & Alerts): 3 questions (5%)

**Total: 65 Questions**
