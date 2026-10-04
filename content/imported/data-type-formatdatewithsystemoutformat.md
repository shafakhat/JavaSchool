---
title: Format Date with System.out.format
nav: Format Date with System.ou...
description: * Copyright (c) 1995 - 2008 Sun Microsystems, Inc. All rights reserved.
section: Imported - java2s Archive
order: 1081
source: https://web.archive.org/web/20140829090921/http://www.java2s.com/Tutorial/Java/0040__Data-Type/FormatDatewithSystemoutformat.htm
---
```java title=Example.java
/*
 * Copyright (c) 1995 - 2008 Sun Microsystems, Inc.  All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 *
 *   - Redistributions of source code must retain the above copyright
 *     notice, this list of conditions and the following disclaimer.
 *
 *   - Redistributions in binary form must reproduce the above copyright
 *     notice, this list of conditions and the following disclaimer in the
 *     documentation and/or other materials provided with the distribution.
 *
 *   - Neither the name of Sun Microsystems nor the names of its
 *     contributors may be used to endorse or promote products derived
 *     from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
 * IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
 * THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
 * PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR
 * CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
 * PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
 * PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
 * LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
 * NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 * SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */
import java.util.Calendar;
import java.util.Locale;
public class TestFormat {
  public static void main(String[] args) {
    long n = 461012;
    System.out.format("%d%n", n);
    System.out.format("%08d%n", n);
    System.out.format("%+8d%n", n);
    System.out.format("%,8d%n", n);
    System.out.format("%+,8d%n%n", n);
    double pi = Math.PI;
    System.out.format("%f%n", pi);
    System.out.format("%.3f%n", pi);
    System.out.format("%10.3f%n", pi);
    System.out.format("%-10.3f%n", pi);
    System.out.format(Locale.FRANCE, "%-10.4f%n%n", pi);
    Calendar c = Calendar.getInstance();
    System.out.format("%tB %te, %tY%n", c, c, c);
    System.out.format("%tl:%tM %tp%n", c, c, c);
    System.out.format("%tD%n", c);
  }
}
```

| 2.41.1. | Date Parsing and Formatting with DateFormat |
|---|---|
| 2.41.2. | Parsing the Time Using a Custom Format |
| 2.41.3. | Parse with a custom format |
| 2.41.4. | Parse with a default format |
| 2.41.5. | Parse string date value input with SimpleDateFormat('dd-MMM-yy') |
| 2.41.6. | Parse a date and time |
| 2.41.7. | Parse string date value input with SimpleDateFormat('E, dd MMM yyyy HH:mm:ss Z') |
| 2.41.8. | Parse string date value with default format: DateFormat.getDateInstance(DateFormat.DEFAULT) |
| 2.41.9. | Leniency |
| 2.41.10. | Formatting String Symbols for SimpleDateFormat |
| 2.41.11. | SimpleDateFormat: hh:mm:ss, dd MMM yyyy hh:mm:ss zzz, E MMM dd yyyy |
| 2.41.12. | Simply format a date as YYYYMMDD |
| 2.41.13. | Express a duration in term of HH:MM:SS |
| 2.41.14. | Date Format with SimpleDateFormat |
| 2.41.15. | Demonstrate date formats with different DateFormat constants |
| 2.41.16. | Demonstrate time formats. |
| 2.41.17. | DateFormat.getDateTimeInstance(DateFormat.FULL,DateFormat.MEDIUM) |
| 2.41.18. | print out the current date and time |
| 2.41.19. | Date Era change |
| 2.41.20. | Format Date with System.out.format |
| 2.41.21. | SimpleDateFormat |
| 2.41.22. | Formatting Dates and Times |
| 2.41.23. | Four different date formats for four countries: US, UK, GERMANY, FRANCE |
| 2.41.24. | Various Date format |
| 2.41.25. | Display date with day name in a short format |
| 2.41.26. | Display date with a short day and month name |
| 2.41.27. | Format a date into dd/mm/yyyy |
| 2.41.28. | Format current date and time with the SimpleDateFormat: dd/MM/yyyy |
| 2.41.29. | Format current date and time with the SimpleDateFormat: HH:mm:ss |
| 2.41.30. | Formatting Symbols for SimpleDateFormat |
| 2.41.31. | Formatting the Time Using a Custom Format |
| 2.41.32. | Change date formatting symbols |
| 2.41.33. | Get a List of Short Month Names |
| 2.41.34. | Get a List of Weekday Names |
| 2.41.35. | Get a List of Short Weekday Names |
| 2.41.36. | Time in 12-hour format |
| 2.41.37. | Time in 24-hour format |
| 2.41.38. | Date and time with month |
| 2.41.39. | Date and time with day and month fully spelled-out |
| 2.41.40. | Output current time: %tc |
| 2.41.41. | Formatter that caches formatted date information |
| 2.41.42. | RFC date format |
| 2.41.43. | A formatter that formats dates to show the elapsed time relative to some base date. |
