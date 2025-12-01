# Splunk Core Certified User - Comprehensive Practice Exam

## Domain 1.0: Splunk Basics

**1. What is the primary function of a 'Splunk App'?**
* A) To forward data to external systems.
* B) To provide a specific collection of configurations, knowledge objects, and dashboards for a specific use case.
* C) To compress raw data logs.
* D) To manage user licenses.

> **Correct Answer:** B
> **Rationale:** Apps are packaged sets of configurations (like inputs and lookups) and views (dashboards) designed to solve specific problems, such as 'Splunk for Unix' or 'Splunk for AWS'.

**2. Which of the following is a default role in Splunk Enterprise?**
* A) SuperUser
* B) Power
* C) Network_Admin
* D) Auditor

> **Correct Answer:** B
> **Rationale:** The standard default roles are Admin, Power, and User. Power users have more capabilities than standard Users (like creating shared objects) but less than Admins.

---

## Domain 2.0: Basic Searching

**3. What does the 'Search Mode' setting (Fast, Smart, Verbose) primarily control?**
* A) The speed of the indexer's hard drives.
* B) How much data is returned and which fields are automatically discovered.
* C) The expiration time of the search job.
* D) The user's permission level.

> **Correct Answer:** B
> **Rationale:** Search modes balance performance vs. completeness. Fast mode returns fewer fields/event data to be quicker; Verbose returns everything; Smart switches based on the search string.

**4. Which symbol is used to perform a wildcard match within a search string?**
* A) %
* B) *
* C) ?
* D) #

> **Correct Answer:** B
> **Rationale:** The asterisk is the universal wildcard in Splunk for matching any character sequence.

**5. In the search results, what does the 'Timeline' visual represent?**
* A) The distribution of matching events over the selected time range.
* B) The time the search took to execute.
* C) The future prediction of events.
* D) The bandwidth usage of the search.

> **Correct Answer:** A
> **Rationale:** The timeline shows a bar chart of how many events occurred in each time bucket, allowing you to see spikes or gaps in activity.

**6. What happens if you click a specific bar in the Search Timeline?**
* A) It deletes the events in that time bucket.
* B) It exports the data.
* C) It updates the search to focus only on that specific time bucket.
* D) It highlights the events in red.

> **Correct Answer:** C
> **Rationale:** This effectively zooms in on that time slice, updating the search time range.

**7. Which of the following is considered a 'Best Practice' when writing efficient searches?**
* A) Use wildcards at the beginning of strings (e.g., `*fail`).
* B) Specify the index name.
* C) Search 'All Time' by default.
* D) Use `fields *` to extract everything.

> **Correct Answer:** B
> **Rationale:** Searching `index=web` is much faster than searching all indexes because it limits the scope of data on disk.

**8. If a search is running too slowly, what can you do to stop the search but keep the results found so far?**
* A) Click 'Finalize'.
* B) Click 'Pause'.
* C) Click 'Delete'.
* D) Close the browser tab.

> **Correct Answer:** A
> **Rationale:** Finalizing stops the search execution and retains the partial results already retrieved.

**9. What allows you to view the raw events in a clean list format without the timeline or sidebar?**
* A) The Events Tab
* B) Full Screen Mode
* C) The Statistics Tab
* D) The `table` command

> **Correct Answer:** A (Note: While 'Events List' is the standard view, turning off sidebar/timeline is a specific view setting, often accessed via the 'Events' tab context).
> **Rationale:** The Events tab is the standard view, which includes the sidebar.

**10. To search specifically in the 'web' index, what syntax should you use?**
* A) index:web
* B) index=web
* C) using index web
* D) source=web

> **Correct Answer:** B
> **Rationale:** The standard Key=Value syntax applies to the index field.

**11. Which command is used to combine the results of two searches?**
* A) append
* B) combine
* C) add
* D) plus

> **Correct Answer:** A
> **Rationale:** `append` adds the results of a subsearch to the current results.

**12. Which time modifier is used to define the 'snap to' behavior in a relative time range (e.g., snapping to the beginning of the day)?**
* A) @
* B) #
* C) *
* D) !

> **Correct Answer:** A
> **Rationale:** The `@` symbol is used to 'snap' or round down the time to the nearest specified unit (e.g., `@d` for beginning of the day).

---

## Domain 3.0: Using Fields

**13. Where are 'Selected Fields' displayed in the Splunk UI?**
* A) At the bottom of the page.
* B) In the Fields sidebar, at the top of the list.
* C) Only in the Job Inspector.
* D) In the Visualization tab.

> **Correct Answer:** B
> **Rationale:** Selected fields (like host, source, sourcetype) appear at the top of the sidebar and are also shown under every event in the list.

**14. How can you add a field to the 'Selected Fields' list?**
* A) Click the field in the 'Interesting Fields' list and select 'Yes' for Selected.
* B) Right-click the event and choose 'Promote'.
* C) It happens automatically after 10 searches.
* D) Use the `select` command.

> **Correct Answer:** A
> **Rationale:** This effectively promotes an Interesting Field to a Selected Field.

**15. What is the difference between `source` and `sourcetype`?**
* A) `source` is the file name/input stream; `sourcetype` is the data classification/format.
* B) `source` is the format; `sourcetype` is the file name.
* C) They are identical.
* D) `sourcetype` is the server name.

> **Correct Answer:** A
> **Rationale:** `source` tells you where the data came from (e.g., /var/log/syslog), while `sourcetype` tells Splunk how to interpret it (e.g., linux_secure).

**16. True or False: Field names in Splunk (e.g., `ClientIP`) are case-sensitive.**
* A) True
* B) False

> **Correct Answer:** A
> **Rationale:** In Splunk SPL, field *names* are case-sensitive (`ClientIP` != `clientip`), but field *values* are generally case-insensitive.

**17. If you search `status=404`, 'status' is the ______ and '404' is the ______.**
* A) Value, Field
* B) Field, Value
* C) Tag, Alias
* D) Host, Source

> **Correct Answer:** B
> **Rationale:** The syntax is `key=value`, so `status` is the Field Name and `404` is the Field Value.

**18. What does the `!=` operator do in a field search?**
* A) It sets the field to a new value.
* B) It looks for events where the field does NOT equal the value.
* C) It matches values that sound similar.
* D) It acts as a wildcard.

> **Correct Answer:** B
> **Rationale:** It acts as a 'Not Equal To' filter.

**19. Can you search for a value without specifying a field name (e.g., searching just `error`)?**
* A) Yes, using keyword search.
* B) No, field names are mandatory.
* C) Only in Verbose mode.
* D) Only for numeric values.

> **Correct Answer:** A
> **Rationale:** This scans the raw text of the event for the string 'error'.

**20. Which sidebar link allows you to see fields that appear in less than 20% of events?**
* A) Rare Fields
* B) All Fields
* C) Hidden Fields
* D) More Fields

> **Correct Answer:** B
> **Rationale:** Clicking 'All Fields' opens a dialogue showing every field discovered, regardless of frequency.

**21. In the Fields Sidebar, what does the 'a' symbol next to a field name indicate?**
* A) The field contains string (alphanumeric) values.
* B) The field is a number.
* C) The field is hidden.

> **Correct Answer:** A
> **Rationale:** 'a' stands for String; '#' stands for Numeric.

**22. How do you efficiently search for an IP address in a specific subnet using CIDR notation?**
* A) Use the `cidrmatch` command/function.
* B) Use `ip=192.168.*`.
* C) Use `subnet` command.

> **Correct Answer:** A
> **Rationale:** Example: `where
