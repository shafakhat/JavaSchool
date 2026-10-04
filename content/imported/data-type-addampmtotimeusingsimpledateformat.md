---
title: Add AM PM to time using SimpleDateFormat
nav: Add AM PM to time using Si...
description: 9. Use relative indexes to simplify the creation of a custom time and date format.
section: Imported - java2s Archive
order: 1108
source: https://web.archive.org/web/20090516003608/http://www.java2s.com:80/Code/Java/Data-Type/AddAMPMtotimeusingSimpleDateFormat.htm
---
```java title=Example.java
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] args) {
    Date date = new Date();
    String strDateFormat = "HH:mm:ss a";
    SimpleDateFormat sdf = new SimpleDateFormat(strDateFormat);
    System.out.println(sdf.format(date));
  }
}
//10:20:12 AM
```

1.  Date Era change
---  ---
2.  Date Format
3.  The Time and Date Format Suffixes
4.  Display standard 12-hour time format
5.  Display complete time and date information
6.  Display just hour and minute
7.  Display month by name and number
8.  DateFormat.getDateInstance(DateFormat.SHORT)
9.  Use relative indexes to simplify the creation of a custom time and date format.
10.  Date Format with Locale
11.  Date Format Symbols
12.  Decimal Format with different Symbols
13.  Date format: "dd.MM.yy", "yyyy.MM.dd G 'at' hh:mm:ss z","EEE, MMM d, ''yy", "h:mm a", "H:mm", "H:mm:ss:SSS", "K:mm a,z","yyyy.MMMMM.dd GGG hh:mm aaa"
14.  SimpleDateFormat.getAvailableLocales
15.  DateFormat.SHORT
16.  This is same as MEDIUM: DateFormat.getDateInstance().format(new Date())
17.  This is same as MEDIUM: DateFormat.getDateInstance(DateFormat.DEFAULT).format(new Date())
18.  DateFormat.getTimeInstance(DateFormat.MEDIUM, Locale.CANADA).format(new Date())
19.  DateFormat.getTimeInstance(DateFormat.LONG, Locale.CANADA).format(new Date())
20.  DateFormat.getTimeInstance(DateFormat.FULL, Locale.CANADA).format(new Date())
21.  DateFormat.getTimeInstance(DateFormat.DEFAULT, Locale.CANADA).format(new Date())
22.  DateFormat.getDateInstance(DateFormat.LONG)
23.  DateFormat.getTimeInstance(DateFormat.SHORT)
24.  DateFormat.getTimeInstance(DateFormat.LONG)
25.  Parse date string input with DateFormat.getTimeInstance(DateFormat.DEFAULT, Locale.CANADA)
26.  Simple Date Format Demo
27.  Format date in Medium format
28.  Format date in Long format
29.  Format date in Full format
30.  Format date in Default format
31.  Formatting day of week using SimpleDateFormat
32.  Formatting day of week in EEEE format like Sunday, Monday etc.
33.  Formatting day in d format like 1,2 etc
34.  Formatting day in dd format like 01, 02 etc.
35.  Format hour in h (1-12 in AM/PM) format like 1, 2..12.
36.  Format hour in hh (01-12 in AM/PM) format like 01, 02..12.
37.  Format hour in H (0-23) format like 0, 1...23.
38.  Format hour in HH (00-23) format like 00, 01..23.
39.  Format hour in k (1-24) format like 1, 2..24.
40.  Format hour in kk (01-24) format like 01, 02..24.
41.  Format hour in K (0-11 in AM/PM) format like 0, 1..11.
42.  Format hour in KK (00-11) format like 00, 01,..11.
43.  Formatting minute in m format like 1,2 etc.
44.  Format minutes in mm format like 01, 02 etc.
45.  Format month in M format like 1,2 etc
46.  Format Month in MM format like 01, 02 etc.
47.  Format Month in MMM format like Jan, Feb etc.
48.  Format Month in MMMM format like January, February etc.
49.  Format seconds in s format like 1,2 etc.
50.  Format seconds in ss format like 01, 02 etc.
51.  Format date in dd/mm/yyyy format
52.  Format date in mm-dd-yyyy hh:mm:ss format
53.  Format year in yy format like 07, 08 etc
54.  Format year in yyyy format like 2007, 2008 etc.
55.  new SimpleDateFormat("hh")
56.  new SimpleDateFormat("H") // The hour (0-23)
57.  new SimpleDateFormat("m"): The minutes
58.  new SimpleDateFormat("mm")
59.  SimpleDateFormat("MM"): number based month value
60.  new SimpleDateFormat("s"): The seconds
61.  new SimpleDateFormat("ss")
62.  new SimpleDateFormat("a"): The am/pm marker
63.  new SimpleDateFormat("z"): The time zone
64.  new SimpleDateFormat("zzzz")
65.  new SimpleDateFormat("Z")
66.  new SimpleDateFormat("hh:mm:ss a")
67.  new SimpleDateFormat("HH.mm.ss")
68.  new SimpleDateFormat("HH:mm:ss Z")
69.  SimpleDateFormat("MM/dd/yy")
70.  SimpleDateFormat("dd-MMM-yy")
71.  SimpleDateFormat("E, dd MMM yyyy HH:mm:ss Z")
72.  SimpleDateFormat("yyyy")
73.  The month: SimpleDateFormat("M")
74.  Three letter-month value: SimpleDateFormat("MMM")
75.  Full length of month name: SimpleDateFormat("MMMM")
76.  The day number: SimpleDateFormat("d")
77.  Two digits day number: SimpleDateFormat("dd")
78.  The day in week: SimpleDateFormat("E")
79.  Full day name: SimpleDateFormat("EEEE")
80.  Simply format a date as "YYYYMMDD"
81.  Java SimpleDateFormat Class Example("MM/dd/yyyy")
82.  The format used is EEE, dd MMM yyyy HH:mm:ss Z in US locale.
83.  Date Formatting and Localization
84.  Get a List of Short Month Names
85.  Get a List of Weekday Names
86.  Get a List of Short Weekday Names
87.  Change date formatting symbols
88.  An alternate way to get week days symbols
89.  ISO8601 formatter for date-time without time zone.The format used is yyyy-MM-dd'T'HH:mm:ss.
90.  ISO8601 formatter for date-time with time zone. The format used is yyyy-MM-dd'T'HH:mm:ssZZ.
91.  Parsing custom formatted date string into Date object using SimpleDateFormat
92.  Parse with a custom format
93.  Parsing the Time Using a Custom Format
94.  Parse with a default format
95.  Parse a date and time
96.  Parse string date value input with SimpleDateFormat("E, dd MMM yyyy HH:mm:ss Z")
97.  Parse string date value input with SimpleDateFormat("dd-MMM-yy")
98.  Parse string date value with default format: DateFormat.getDateInstance(DateFormat.DEFAULT)
99.  Find the current date format
100.  Time format viewer
101.  Date format viewer
