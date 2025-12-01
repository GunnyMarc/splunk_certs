# Splunk Core Certified User Practice Exam
## Advanced Edition - 100 Questions

**Instructions:**
- This practice exam contains 100 multiple-choice questions with increased difficulty
- Some questions allow **multiple correct answers** - these are marked with **(Select all that apply)**
- Questions are weighted according to the official Splunk Core Certified User exam blueprint
- Recommended time: 100 minutes
- Read each question carefully
- The answer key with detailed explanations is provided at the end

**Exam Format:**
- 100 Questions (Advanced Edition)
- Entry-Level Certification with increased complexity
- Includes single-select and multiple-select questions
- Based on official exam blueprint with deeper technical coverage

---

## Domain 1.0: Splunk Basics (5% - 5 Questions)

**Question 1**  
Which Splunk components are involved in a typical distributed deployment? **(Select all that apply)**

A. Indexers  
B. Search Heads  
C. Forwarders  
D. Deployment Server  
E. License Master

**Question 2**  
What is the primary function of a Splunk App?

A. To forward data to external systems  
B. To provide a specific collection of configurations, dashboards, and knowledge objects for a particular use case  
C. To manage user licenses  
D. To compress raw data logs

**Question 3**  
Which of the following are default roles in Splunk Enterprise? **(Select all that apply)**

A. Admin  
B. Power  
C. User  
D. SuperUser  
E. can_delete

**Question 4**  
In Splunk, what is the purpose of the deployment server?

A. To parse and index data  
B. To distribute apps and configurations to forwarders  
C. To perform searches  
D. To store license information

**Question 5**  
Which file type is used for Splunk configuration files?

A. .xml  
B. .json  
C. .conf  
D. .cfg

---

## Domain 2.0: Basic Searching (22% - 22 Questions)

**Question 6**  
Which of the following are best practices for efficient searching in Splunk? **(Select all that apply)**

A. Specify the index name  
B. Use narrow time ranges  
C. Include filtering keywords early in the search  
D. Use leading wildcards (e.g., *error)  
E. Search "All Time" to ensure completeness

**Question 7**  
What is the correct syntax to search for events containing the exact phrase "failed login"?

A. failed AND login  
B. "failed login"  
C. failed_login  
D. string=failed login

**Question 8**  
Which time modifier syntax would search for events from the last 4 hours?

A. earliest=-4h  
B. earliest=4h  
C. time=-4h  
D. latest=-4h

**Question 9**  
What does the `@` symbol do in time modifiers? **(Select all that apply)**

A. Snaps to the beginning of a time unit  
B. Rounds to the nearest time unit  
C. Can be used with d, h, m, mon, w  
D. Performs a wildcard match

**Question 10**  
In the search `index=web (status=404 OR status=500) earliest=-1h`, what is the order of operations?

A. Time filter, then index filter, then OR operation  
B. Index filter, then OR operation, then time filter  
C. OR operation, then index filter, then time filter  
D. All filters are applied simultaneously

**Question 11**  
Which Search Mode should you use to discover all possible fields in your results?

A. Fast  
B. Smart  
C. Verbose  
D. Complete

**Question 12**  
How can you search for events where a field exists but has no value? **(Select all that apply)**

A. fieldname=*  
B. fieldname=""  
C. | where isnotnull(fieldname) AND fieldname=""  
D. fieldname!=*

**Question 13**  
What does clicking the "Finalize" button do to a running search?

A. Deletes the search job  
B. Stops the search and keeps results found so far  
C. Pauses the search temporarily  
D. Exports the results to CSV

**Question 14**  
Which of the following are valid Boolean operators in Splunk? **(Select all that apply)**

A. AND  
B. OR  
C. NOT  
D. XOR  
E. NAND

**Question 15**  
In the search string `error NOT (user=admin OR user=root)`, which operation is evaluated first?

A. NOT  
B. OR  
C. The entire expression in parentheses  
D. Left to right sequentially

**Question 16**  
What is the difference between `earliest=-1d@d` and `earliest=-1d`?

A. No difference - they are equivalent  
B. `-1d@d` snaps to the beginning of yesterday; `-1d` means exactly 24 hours ago  
C. `-1d@d` is invalid syntax  
D. `-1d` is faster to execute

**Question 17**  
Which command allows you to save search results for use in a future search?

A. save  
B. export  
C. outputcsv  
D. savedsearch

**Question 18**  
How do you search for events that contain either "error" OR "warning" in any field?

A. error | warning  
B. error OR warning  
C. error + warning  
D. (error, warning)

**Question 19**  
What happens when you use `index=* ` in your search?

A. It searches all indexes  
B. It's invalid syntax  
C. It searches only the default index  
D. It searches for literal asterisk characters

**Question 20**  
Which of the following time range specifications are valid? **(Select all that apply)**

A. earliest=-30m latest=now  
B. earliest=@d latest=now  
C. earliest=-1d@d latest=@d  
D. earliest=today latest=tomorrow

**Question 21**  
What is the purpose of the Job Inspector?

A. To view detailed execution statistics for a search  
B. To manage user permissions  
C. To configure indexes  
D. To create dashboards

**Question 22**  
In a search, what does the `_time` field represent?

A. The time the search was run  
B. The timestamp of when the event occurred  
C. The time the event was indexed  
D. The current system time

**Question 23**  
Which search string will find events where the status field equals 404 or 500?

A. status=404 OR 500  
B. status=(404 OR 500)  
C. status=404 OR status=500  
D. status IN (404,500)

**Question 24**  
What is the maximum time that search job results are retained by default?

A. 6 hours  
B. 24 hours  
C. 7 days  
D. 10 minutes

**Question 25**  
Which characters require escaping in Splunk searches? **(Select all that apply)**

A. " (double quote)  
B. \ (backslash)  
C. * (asterisk)  
D. = (equals)

**Question 26**  
How do you search for events that occurred exactly at midnight on January 1, 2024?

A. earliest=2024-01-01 latest=2024-01-01  
B. earliest="01/01/2024:00:00:00" latest="01/01/2024:00:00:01"  
C. _time=2024-01-01T00:00:00  
D. date="2024-01-01" time="00:00:00"

**Question 27**  
What does the "Send to Background" option do for a search?

A. Deletes the search  
B. Allows the search to continue running while you do other work  
C. Pauses the search  
D. Lowers the search priority

---

## Domain 3.0: Using Fields in Searches (20% - 20 Questions)

**Question 28**  
Which three fields are default Selected Fields in Splunk? **(Select all that apply)**

A. host  
B. source  
C. sourcetype  
D. index  
E. _time

**Question 29**  
What criteria must a field meet to be listed as an "Interesting Field"?

A. It must be a numeric field  
B. It must appear in at least 20% of the events  
C. It must be manually selected by the user  
D. It must contain a unique value

**Question 30**  
Which field extraction methods does Splunk use? **(Select all that apply)**

A. Automatic extraction (default)  
B. Regular expressions  
C. Delimiters  
D. Key-value pairs  
E. JSON parsing

**Question 31**  
How do you search for events where the response_time field is greater than 1000?

A. response_time>1000  
B. response_time gt 1000  
C. where response_time>1000  
D. response_time>=1001

**Question 32**  
Which command would you use to exclude multiple fields from the search results? **(Select all that apply)**

A. `fields - fieldname1, fieldname2`  
B. `fields - fieldname1 - fieldname2`  
C. `table * - fieldname1 - fieldname2`  
D. `remove fieldname1, fieldname2`

**Question 33**  
What is the difference between `host` and `source`?

A. host is the machine name; source is the file path or input  
B. They are identical  
C. host is the file; source is the machine  
D. host is mandatory; source is optional

**Question 34**  
Are field names in Splunk case-sensitive?

A. Yes, field names are case-sensitive  
B. No, field names are not case-sensitive  
C. Only when using regex  
D. Depends on the sourcetype

**Question 35**  
Which comparison operators can be used with fields in Splunk? **(Select all that apply)**

A. =  
B. !=  
C. <  
D. >  
E. <=  
F. >=

**Question 36**  
How do you search for events where a field does NOT exist?

A. NOT fieldname=*  
B. fieldname=""  
C. | where isnull(fieldname)  
D. fieldname!=*

**Question 37**  
What does the `_raw` field contain?

A. The original, unparsed event text  
B. The field extraction results  
C. The index name  
D. The timestamp

**Question 38**  
Which search finds events where the user field starts with "admin"?

A. user=admin*  
B. user="admin*"  
C. user LIKE "admin%"  
D. user STARTSWITH admin

**Question 39**  
In the Fields sidebar, what does the '#' symbol indicate?

A. The field is commented out  
B. The field contains numeric values  
C. The field is hidden  
D. The field is a calculated field

**Question 40**  
How do you search for events with an IP address in the range 192.168.1.0/24?

A. ip=192.168.1.*  
B. | where cidrmatch("192.168.1.0/24", ip)  
C. ip IN 192.168.1.0/24  
D. ip BETWEEN 192.168.1.0 AND 192.168.1.255

**Question 41**  
Which of the following are internal (metadata) fields in Splunk? **(Select all that apply)**

A. _time  
B. _raw  
C. index  
D. host  
E. source

**Question 42**  
What is the purpose of field aliases?

A. To rename fields permanently  
B. To create alternate names for existing fields  
C. To delete unwanted fields  
D. To encrypt field values

**Question 43**  
How do you search for events where the status field is either empty or equals 200?

A. status="" OR status=200  
B. status IN ("",200)  
C. | where status=="" OR status=200  
D. Both A and C

**Question 44**  
What does the `eval` command do in relation to fields?

A. Evaluates the search for errors  
B. Creates or modifies fields using calculations or functions  
C. Validates field formats  
D. Evaluates field permissions

**Question 45**  
Which search correctly uses a wildcard to find users starting with "admin" or "root"?

A. user=admin* OR user=root*  
B. user=(admin* OR root*)  
C. user IN (admin*, root*)  
D. user MATCHES (admin|root)*

**Question 46**  
How can you view all fields in your data, even those appearing in less than 20% of events?

A. Click "All Fields" in the Fields sidebar  
B. Use Search Mode: Verbose  
C. Use the command `| fieldsummary`  
D. All of the above

**Question 47**  
What is the difference between `fields` and `table` commands?

A. No difference - they are aliases  
B. `fields` controls which fields are kept/removed; `table` formats output and reorders fields  
C. `table` is faster  
D. `fields` only works with numeric data

---

## Domain 4.0: Search Language Fundamentals (15% - 15 Questions)

**Question 48**  
Which command removes duplicate events based on the user field?

A. `unique user`  
B. `dedup user`  
C. `distinct user`  
D. `remove_duplicates user`

**Question 49**  
What is the correct syntax to rename multiple fields? **(Select all that apply)**

A. `rename user as username, ip as ipaddress`  
B. `rename user=username, ip=ipaddress`  
C. `rename user TO username | rename ip TO ipaddress`  
D. `rename user as username | rename ip as ipaddress`

**Question 50**  
Which command would you use to sort results by count in descending order?

A. `sort count`  
B. `sort -count`  
C. `sort count desc`  
D. `order by count desc`

**Question 51**  
What does the pipe symbol `|` do in a Splunk search?

A. Performs an OR operation  
B. Chains commands together in a pipeline  
C. Creates a comment  
D. Escapes special characters

**Question 52**  
How do you limit search results to a specific index and sourcetype?

A. `index=web AND sourcetype=access_combined`  
B. `index=web sourcetype=access_combined`  
C. `index=web | where sourcetype="access_combined"`  
D. Both A and B

**Question 53**  
Which commands are considered transforming commands? **(Select all that apply)**

A. stats  
B. top  
C. rare  
D. chart  
E. fields  
F. rename

**Question 54**  
What does the `head 20` command do?

A. Returns the last 20 results  
B. Returns the first 20 results  
C. Returns 20 random results  
D. Splits results into 20 groups

**Question 55**  
How do you search for events in multiple indexes?

A. `index=web OR index=security`  
B. `index IN (web, security)`  
C. `index=web,security`  
D. Both A and C

**Question 56**  
What is the purpose of the `rex` command?

A. To export results  
B. To extract fields using regular expressions  
C. To exclude events  
D. To reverse the order of results

**Question 57**  
Which command would you use to add a new field to events?

A. `addfield`  
B. `eval`  
C. `create`  
D. `newfield`

**Question 58**  
What does the `where` command do?

A. Filters results using eval expressions  
B. Identifies the location of events  
C. Creates a location field  
D. Sorts results by location

**Question 59**  
How do you return only the last 15 results?

A. `head 15`  
B. `tail 15`  
C. `last 15`  
D. `bottom 15`

**Question 60**  
Which search language command can you use to return results in reverse time order?

A. `reverse`  
B. `sort -_time`  
C. `order desc`  
D. `tail`

**Question 61**  
What is the difference between `rename` and `eval` for changing field names?

A. No difference  
B. `rename` only changes the field name; `eval` can also transform the value  
C. `rename` is faster  
D. `eval` is deprecated

**Question 62**  
Which command retrieves the first field value encountered for each unique combination of other fields?

A. `first`  
B. `head`  
C. `stats first()`  
D. `initial`

---

## Domain 5.0: Using Basic Transforming Commands (15% - 15 Questions)

**Question 63**  
Which `stats` functions can be used with numeric fields? **(Select all that apply)**

A. sum  
B. avg  
C. max  
D. min  
E. median  
F. stdev

**Question 64**  
What is the correct syntax to count events by status and host?

A. `stats count by status, host`  
B. `stats count(status, host)`  
C. `count by status AND host`  
D. `stats count WHERE status BY host`

**Question 65**  
What does the `top` command do by default?

A. Returns top 5 results  
B. Returns top 10 results with count and percent  
C. Returns top 20 results  
D. Returns all results sorted in descending order

**Question 66**  
How do you specify a custom limit for the `top` command?

A. `top limit=20 fieldname`  
B. `top fieldname limit 20`  
C. `top 20 fieldname`  
D. `top fieldname count=20`

**Question 67**  
Which `stats` function returns the number of unique values of a field?

A. `unique()`  
B. `distinct()`  
C. `dc()`  
D. `count_unique()`

**Question 68**  
What is the difference between `values()` and `list()` in stats? **(Select all that apply)**

A. `values()` returns unique values only  
B. `list()` returns all values including duplicates  
C. `values()` is sorted alphabetically  
D. `list()` maintains original order

**Question 69**  
How do you calculate both the count and average response time by host?

A. `stats count, avg(response_time) by host`  
B. `stats count AND avg(response_time) by host`  
C. `stats count avg(response_time) GROUP BY host`  
D. `count by host | avg response_time by host`

**Question 70**  
What does the `rare` command show?

A. The most common values  
B. The least common values  
C. Unusual statistical outliers  
D. Deleted events

**Question 71**  
Which command would you use to create a time-based statistical chart?

A. `timechart`  
B. `chart`  
C. `stats by _time`  
D. All of the above

**Question 72**  
How do you find the earliest and latest times in your results?

A. `stats earliest(_time), latest(_time)`  
B. `stats min(_time), max(_time)`  
C. `timechart span=1d`  
D. Both A and B

**Question 73**  
What does `stats sum(bytes) as total_bytes by host` do?

A. Counts the bytes field for each host  
B. Sums the bytes field for each host and names the result total_bytes  
C. Creates a new field called total_bytes  
D. Filters bytes by host

**Question 74**  
Which `stats` functions return aggregate values over multiple events? **(Select all that apply)**

A. count  
B. sum  
C. avg  
D. list  
E. values  
F. first

**Question 75**  
How can you calculate a percentage using stats?

A. `stats count by status | eval percent=count/total*100`  
B. Use the `top` command which includes percentages  
C. `stats count percentage by status`  
D. Both A and B

**Question 76**  
What does `| stats count by status | sort - count` do?

A. Counts events by status and sorts by status name  
B. Counts events by status and sorts by count in descending order  
C. Sorts events by count then counts by status  
D. Invalid syntax

**Question 77**  
Which command would you use to create statistical groups based on numeric ranges?

A. `bucket`  
B. `group`  
C. `range`  
D. `bin`

---

## Domain 6.0: Creating Reports and Dashboards (12% - 12 Questions)

**Question 78**  
Which of the following are valid report components? **(Select all that apply)**

A. Search query  
B. Time range  
C. Visualization type  
D. Permissions  
E. Schedule

**Question 79**  
What types of visualizations can display time-series data effectively? **(Select all that apply)**

A. Line Chart  
B. Area Chart  
C. Pie Chart  
D. Column Chart  
E. Single Value

**Question 80**  
How do you make a dashboard available to all users in your organization?

A. Set permissions to "Everyone"  
B. Set permissions to "Shared in App"  
C. Export and email to all users  
D. Save in a public folder

**Question 81**  
What is required to create a visualization in Splunk?

A. Raw events  
B. Results from a transforming command  
C. Admin permissions  
D. A dashboard

**Question 82**  
Which visualization would you use to show geographic distribution of data?

A. Choropleth Map  
B. Pie Chart  
C. Line Chart  
D. Single Value

**Question 83**  
How can you add a report to multiple dashboards?

A. Copy and paste the report  
B. Save the report and add it as a panel to each dashboard  
C. Create a dashboard link  
D. Reports can only be on one dashboard

**Question 84**  
What happens when you edit a report that's used in a dashboard?

A. The dashboard panel updates automatically  
B. You must manually update the dashboard  
C. The dashboard breaks  
D. A new report is created

**Question 85**  
Which of the following can be added to a dashboard panel? **(Select all that apply)**

A. Saved searches  
B. Inline searches  
C. Static images  
D. HTML content  
E. Input forms

**Question 86**  
What is the purpose of dashboard tokens?

A. To encrypt dashboard data  
B. To enable dynamic content based on user input  
C. To authenticate users  
D. To schedule dashboard refreshes

**Question 87**  
How do you create a drilldown from a dashboard panel?

A. Edit the panel and configure drilldown settings  
B. Use JavaScript  
C. Create a workflow action  
D. Drilldowns are automatic

**Question 88**  
Which file format is used for dashboard definitions?

A. JSON  
B. XML  
C. HTML  
D. YAML

**Question 89**  
What is the difference between a dashboard and a form?

A. No difference - they're the same  
B. Forms include input elements for user interaction  
C. Dashboards are read-only  
D. Forms require admin privileges

---

## Domain 7.0: Creating and Using Lookups (6% - 6 Questions)

**Question 90**  
What is the primary purpose of a lookup in Splunk?

A. To search external databases  
B. To enrich event data with additional information from external files  
C. To look up user information  
D. To find missing events

**Question 91**  
Which commands can be used to work with lookups? **(Select all that apply)**

A. lookup  
B. inputlookup  
C. outputlookup  
D. appendlookup  
E. lookupedit

**Question 92**  
What are the steps to create an automatic lookup? **(Select all that apply)**

A. Upload the lookup file  
B. Create a lookup definition  
C. Configure automatic lookup settings  
D. Restart Splunk  
E. Create a props.conf entry

**Question 93**  
Which field type must exist for a lookup to work properly?

A. A time field  
B. A matching field between your events and the lookup table  
C. An index field  
D. A source field

**Question 94**  
How do you use `inputlookup` to view the contents of a lookup table?

A. `| inputlookup tablename`  
B. `inputlookup file=tablename`  
C. `lookup tablename`  
D. `| viewlookup tablename`

**Question 95**  
What does the `outputlookup` command do?

A. Displays lookup results  
B. Writes search results to a lookup file  
C. Exports lookups to CSV  
D. Deletes lookup tables

---

## Domain 8.0: Creating Scheduled Reports and Alerts (5% - 5 Questions)

**Question 96**  
Which of the following are valid trigger conditions for alerts? **(Select all that apply)**

A. Number of results  
B. Number of hosts  
C. Number of sources  
D. Custom condition based on search results  
E. Time of day

**Question 97**  
What is the difference between a real-time alert and a scheduled alert?

A. Real-time alerts run continuously; scheduled alerts run at specified intervals  
B. No difference  
C. Real-time alerts are faster  
D. Scheduled alerts are more accurate

**Question 98**  
Which alert actions are available in Splunk? **(Select all that apply)**

A. Send email  
B. Run a script  
C. Webhook  
D. Add to triggered alerts  
E. Reboot server  
F. Log event

**Question 99**  
How do you prevent an alert from triggering too frequently?

A. Set throttling options  
B. Decrease the search frequency  
C. Use a longer time window  
D. All of the above

**Question 100**  
Where can you view the history of triggered alerts?

A. Activity > Triggered Alerts  
B. Settings > Alert History  
C. Reports > Alerts  
D. Search > Alert Log

---
---

# Answer Key with Detailed Explanations

## Domain 1.0: Splunk Basics (5%)

**1. A, B, C, D, E - All are correct**  
A typical distributed Splunk deployment includes: Indexers (store and index data), Search Heads (coordinate searches), Forwarders (collect and send data), Deployment Server (manages configurations), and License Master (manages licensing). All of these components work together in an enterprise deployment.

**2. B - To provide a specific collection of configurations, dashboards, and knowledge objects for a particular use case**  
Splunk Apps bundle together configurations, dashboards, reports, searches, and field extractions for specific use cases like security monitoring, IT operations, or business analytics.

**3. A, B, C - Admin, Power, User**  
The three default roles in Splunk Enterprise are Admin (full access), Power (can create shared knowledge objects and schedule searches), and User (basic search capabilities). SuperUser and can_delete are not default roles.

**4. B - To distribute apps and configurations to forwarders**  
The Deployment Server centrally manages and distributes apps, configurations, and updates to deployment clients (typically forwarders) across your Splunk infrastructure.

**5. C - .conf**  
Splunk uses .conf files for all configuration settings. These are text files with a specific format that control various aspects of Splunk behavior.

---

## Domain 2.0: Basic Searching (22%)

**6. A, B, C - Specify the index name, Use narrow time ranges, Include filtering keywords early**  
Best practices include specifying the index to limit data scanned, using narrow time ranges to reduce disk I/O, and including filtering keywords early to eliminate irrelevant events. Leading wildcards and searching "All Time" are inefficient practices.

**7. B - "failed login"**  
Quotation marks search for exact phrases. Without quotes, Splunk searches for events containing both words anywhere in the event.

**8. A - earliest=-4h**  
The syntax `earliest=-4h` means "starting 4 hours ago". The minus sign indicates time in the past relative to now.

**9. A, B, C - Snaps to the beginning of a time unit, Rounds to the nearest time unit, Can be used with d, h, m, mon, w**  
The `@` symbol snaps or rounds time to specified units: @d (day), @h (hour), @m (minute), @mon (month), @w (week). It does not perform wildcard matching.

**10. B - Index filter, then OR operation, then time filter**  
Splunk processes searches by first applying index and source type filters, then keyword and field filters, then time range filters.

**11. C - Verbose**  
Verbose mode discovers all possible fields but is slower. Fast mode extracts minimal fields for speed. Smart mode (default) balances performance and field discovery.

**12. A, C - fieldname=*, | where isnotnull(fieldname) AND fieldname=""**  
`fieldname=*` finds events where the field exists. Combined with `fieldname=""` or using `where` with `isnotnull()` and checking for empty string finds fields that exist but are empty.

**13. B - Stops the search and keeps results found so far**  
Finalize completes the search immediately with whatever results have been gathered, allowing you to work with partial results.

**14. A, B, C - AND, OR, NOT**  
The three Boolean operators in Splunk are AND, OR, and NOT. XOR and NAND are not supported.

**15. C - The entire expression in parentheses**  
Parentheses have the highest precedence and are evaluated first, so `(user=admin OR user=root)` is evaluated before the NOT operation.

**16. B - `-1d@d` snaps to the beginning of yesterday; `-1d` means exactly 24 hours ago**  
`-1d@d` means "1 day ago, snapped to the beginning of that day" (midnight yesterday). `-1d` means exactly 24 hours ago from the current moment.

**17. C - outputcsv**  
The `outputcsv` command writes search results to a CSV file that can be used in future searches.

**18. B - error OR warning**  
Use the OR operator to search for events containing either term: `error OR warning`.

**19. A - It searches all indexes**  
`index=*` is a wildcard that searches across all available indexes (that the user has permission to search).

**20. A, B, C - All are valid except D**  
Options A, B, and C use valid time modifiers. Option D ("today" and "tomorrow") is not valid Splunk syntax for time ranges.

**21. A - To view detailed execution statistics for a search**  
The Job Inspector provides detailed information about search execution, including processing time, events scanned, and search optimization data.

**22. B - The timestamp of when the event occurred**  
The `_time` field contains the timestamp extracted from the event data, representing when the event actually occurred.

**23. C - status=404 OR status=500**  
Each field-value pair must be specified completely: `status=404 OR status=500`.

**24. C - 7 days**  
By default, search job results are retained for 7 days before being automatically deleted.

**25. A, B - " (double quote), \ (backslash)**  
Double quotes and backslashes require escaping in Splunk searches. Asterisks are wildcards and equals signs are operators, not requiring escaping.

**26. B - earliest="01/01/2024:00:00:00" latest="01/01/2024:00:00:01"**  
To search for a specific moment, specify a very narrow time window using earliest and latest with specific timestamps.

**27. B - Allows the search to continue running while you do other work**  
"Send to Background" moves the search job to the background, allowing it to continue while you navigate away to perform other tasks.

---

## Domain 3.0: Using Fields in Searches (20%)

**28. A, B, C - host, source, sourcetype**  
The three default Selected Fields are host (machine name), source (file path/input), and sourcetype (data format classification).

**29. B - It must appear in at least 20% of the events**  
Fields appearing in 20% or more of the returned events are automatically classified as "Interesting Fields".

**30. A, B, C, D, E - All are correct**  
Splunk uses multiple field extraction methods including automatic extraction based on sourcetype, regular expressions, delimiters, key-value pairs, and JSON parsing.

**31. A - response_time>1000**  
For numeric comparisons at search time, use the comparison operator directly: `response_time>1000`.

**32. A - `fields - fieldname1, fieldname2`**  
The correct syntax is `fields - field1, field2` with a comma-separated list after the minus sign.

**33. A - host is the machine name; source is the file path or input**  
`host` identifies the machine that generated the data. `source` identifies the specific file, network stream, or input that provided the data.

**34. A - Yes, field names are case-sensitive**  
Field names in Splunk are case-sensitive (`Status` ≠ `status`), but field values are not case-sensitive by default.

**35. A, B, C, D, E, F - All are correct**  
Splunk supports all standard comparison operators: = (equal), != (not equal), < (less than), > (greater than), <= (less than or equal), >= (greater than or equal).

**36. A - NOT fieldname=***  
`NOT fieldname=*` finds events where the field does not exist. The wildcard `*` matches any value, so NOT excludes events where the field has any value.

**37. A - The original, unparsed event text**  
`_raw` contains the complete original event text before any field extraction or parsing.

**38. A - user=admin***  
Use the wildcard `*` after the prefix to match any characters following "admin": `user=admin*`.

**39. B - The field contains numeric values**  
The '#' symbol indicates a numeric field, which enables numeric operations and comparisons.

**40. B - | where cidrmatch("192.168.1.0/24", ip)**  
The `cidrmatch()` function checks if an IP address falls within a CIDR range: `| where cidrmatch("192.168.1.0/24", ip)`.

**41. A, B, C, D, E - All are correct**  
All listed fields are internal/metadata fields: `_time` (timestamp), `_raw` (original event), `index`, `host`, and `source`.

**42. B - To create alternate names for existing fields**  
Field aliases allow you to create additional names for fields without changing the original field name, useful for standardization.

**43. D - Both A and C**  
Both syntaxes are valid: `status="" OR status=200` at search time, or `| where status=="" OR status=200` using the where command.

**44. B - Creates or modifies fields using calculations or functions**  
The `eval` command creates new fields or modifies existing ones using calculations, string operations, or functions.

**45. A - user=admin* OR user=root***  
Each field-value comparison must be complete: `user=admin* OR user=root*`.

**46. D - All of the above**  
All three methods reveal fields in less than 20% of events: clicking "All Fields", using Verbose mode, or using `fieldsummary`.

**47. B - `fields` controls which fields are kept/removed; `table` formats output and reorders fields**  
`fields` includes or excludes fields from processing. `table` formats the output as a table and can reorder columns.

---

## Domain 4.0: Search Language Fundamentals (15%)

**48. B - `dedup user`**  
The `dedup` (de-duplication) command removes duplicate events: `dedup user` keeps only the first occurrence of each unique user value.

**49. A, D - Both are correct**  
Valid syntaxes are `rename user as username, ip as ipaddress` (multiple in one command) or `rename user as username | rename ip as ipaddress` (chained commands).

**50. B - `sort -count`**  
The minus sign (-) before a field name sorts in descending order: `sort -count`.

**51. B - Chains commands together in a pipeline**  
The pipe symbol `|` chains commands in a pipeline, passing results from one command to the next.

**52. D - Both A and B**  
Both syntaxes work: `index=web AND sourcetype=access_combined` explicitly uses AND, while `index=web sourcetype=access_combined` implicitly ANDs the conditions.

**53. A, B, C, D - stats, top, rare, chart**  
Transforming commands change the format of results: stats, top, rare, and chart are transforming. Fields and rename are non-transforming.

**54. B - Returns the first 20 results**  
`head 20` returns the first 20 events from the search results.

**55. A - `index=web OR index=security`**  
Use OR to search multiple indexes: `index=web OR index=security`.

**56. B - To extract fields using regular expressions**  
The `rex` command extracts fields from events using regular expressions.

**57. B - `eval`**  
The `eval` command creates new fields or modifies existing fields using expressions.

**58. A - Filters results using eval expressions**  
The `where` command filters results based on eval expressions, allowing complex filtering conditions.

**59. B - `tail 15`**  
The `tail` command returns the last N results: `tail 15` returns the last 15.

**60. B - `sort -_time`**  
`sort -_time` sorts results by time in descending order (most recent first).

**61. B - `rename` only changes the field name; `eval` can also transform the value**  
`rename` changes only the field name. `eval` can create new fields with transformed values or different names.

**62. C - `stats first()`**  
The `stats first(fieldname)` function returns the first value encountered for each group.

---

## Domain 5.0: Using Basic Transforming Commands (15%)

**63. A, B, C, D, E, F - All are correct**  
All listed functions work with numeric fields: sum, avg, max, min, median (p50), and stdev (standard deviation).

**64. A - `stats count by status, host`**  
Use comma-separated fields after `by` to group by multiple fields: `stats count by status, host`.

**65. B - Returns top 10 results with count and percent**  
By default, `top` returns the 10 most common values along with count and percentage fields.

**66. A - `top limit=20 fieldname`**  
Specify a custom limit using the limit parameter: `top limit=20 fieldname`.

**67. C - `dc()`**  
The `dc()` function (distinct count) returns the number of unique values: `stats dc(fieldname)`.

**68. A, B, C - values() returns unique values only, list() returns all including duplicates, values() is sorted**  
`values()` returns unique values in alphabetical order. `list()` returns all values including duplicates in the order encountered.

**69. A - `stats count, avg(response_time) by host`**  
Multiple aggregations can be comma-separated: `stats count, avg(response_time) by host`.

**70. B - The least common values**  
The `rare` command shows the least frequently occurring values of a field.

**71. D - All of the above**  
`timechart`, `chart`, and `stats by _time` can all create time-based statistical charts, with `timechart` being specifically optimized for time-series data.

**72. D - Both A and B**  
Both work: `stats earliest(_time), latest(_time)` and `stats min(_time), max(_time)` return the earliest and latest times.

**73. B - Sums the bytes field for each host and names the result total_bytes**  
This sums the bytes field grouped by host, and aliases the result as total_bytes.

**74. A, B, C, D, E, F - All are correct**  
All listed functions aggregate over multiple events: count, sum, avg, list (all values), values (unique values), and first (first value).

**75. D - Both A and B**  
You can calculate percentages with `eval` after stats, or use `top` which automatically includes percentages.

**76. B - Counts events by status and sorts by count in descending order**  
This counts events grouped by status, then sorts the results by the count field in descending order (most to least).

**77. D - `bin`**  
The `bin` command (also called `bucket`) creates statistical groups based on numeric ranges or time spans.

---

## Domain 6.0: Creating Reports and Dashboards (12%)

**78. A, B, C, D, E - All are correct**  
Reports include search query, time range, visualization type, permissions, and optional scheduling.

**79. A, B, D - Line Chart, Area Chart, Column Chart**  
Line, Area, and Column charts effectively display time-series data. Pie charts show proportions, not trends over time.

**80. B - Set permissions to "Shared in App"**  
Setting permissions to "Shared in App" makes the dashboard available to all users who have access to that app.

**81. B - Results from a transforming command**  
Visualizations require data transformed by commands like stats, chart, timechart, top, or rare.

**82. A - Choropleth Map**  
Choropleth maps display geographic data by shading regions based on data values.

**83. B - Save the report and add it as a panel to each dashboard**  
Reports are saved separately and can be added as panels to multiple dashboards.

**84. A - The dashboard panel updates automatically**  
When you edit a saved report, all dashboard panels using that report automatically reflect the changes.

**85. A, B, C, D, E - All are correct**  
Dashboard panels can contain saved searches, inline searches, static images, HTML content, and input forms.

**86. B - To enable dynamic content based on user input**  
Tokens allow dashboard content to change dynamically based on user selections in input forms.

**87. A - Edit the panel and configure drilldown settings**  
Drilldowns are configured in the panel settings, defining what happens when users click on visualization elements.

**88. B - XML**  
Dashboards are defined in XML format, which can be edited directly for advanced customization.

**89. B - Forms include input elements for user interaction**  
Forms are dashboards with input elements (dropdowns, text boxes, time pickers) that users interact with to modify searches.

---

## Domain 7.0: Creating and Using Lookups (6%)

**90. B - To enrich event data with additional information from external files**  
Lookups add fields from external files (usually CSV) to events based on matching field values.

**91. A, B, C - lookup, inputlookup, outputlookup**  
Valid lookup commands: `lookup` (enriches events), `inputlookup` (reads lookup table), `outputlookup` (writes to lookup table).

**92. A, B, C - Upload the file, Create a lookup definition, Configure automatic lookup settings**  
Automatic lookups require uploading the file, creating a lookup definition, and configuring the automatic lookup to specify when it applies.

**93. B - A matching field between your events and the lookup table**  
Lookups require at least one common field between events and the lookup table to match and enrich data.

**94. A - `| inputlookup tablename`**  
Use `| inputlookup tablename` to view the contents of a lookup table as search results.

**95. B - Writes search results to a lookup file**  
`outputlookup` writes current search results to a lookup file, creating or updating it.

---

## Domain 8.0: Creating Scheduled Reports and Alerts (5%)

**96. A, B, C, D - All except E**  
Valid alert triggers include number of results, number of hosts, number of sources, and custom conditions based on field values. "Time of day" is a schedule setting, not a trigger condition.

**97. A - Real-time alerts run continuously; scheduled alerts run at specified intervals**  
Real-time alerts continuously monitor data as it arrives. Scheduled alerts run at specified times (every hour, daily, etc.).

**98. A, B, C, D, F - All except E (Reboot server)**  
Valid alert actions: send email, run script, webhook, add to triggered alerts, and log event. Destructive actions like rebooting servers are not available.

**99. D - All of the above**  
Prevent frequent triggering by setting throttling (suppress for X minutes), decreasing search frequency, or using longer time windows.

**100. A - Activity > Triggered Alerts**  
View alert history at Activity > Triggered Alerts, which shows when alerts fired and their results.

---

## Exam Domain Distribution Summary

- **Domain 1 (Splunk Basics):** 5 questions (5%)
- **Domain 2 (Basic Searching):** 22 questions (22%)
- **Domain 3 (Using Fields in Searches):** 20 questions (20%)
- **Domain 4 (Search Language Fundamentals):** 15 questions (15%)
- **Domain 5 (Using Basic Transforming Commands):** 15 questions (15%)
- **Domain 6 (Creating Reports and Dashboards):** 12 questions (12%)
- **Domain 7 (Creating and Using Lookups):** 6 questions (6%)
- **Domain 8 (Creating Scheduled Reports and Alerts):** 5 questions (5%)

**Total: 100 Questions**

**Question Types:**
- Single-select: 71 questions
- Multiple-select: 29 questions

This advanced exam tests deeper understanding of Splunk concepts with more complex scenarios, command syntax variations, and multi-select questions that require comprehensive knowledge.

Good luck with your Splunk Core Certified User certification!
