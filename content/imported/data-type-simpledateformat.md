---
title: SimpleDateFormat
nav: SimpleDateFormat
description: With SimpleDateFormat, you can set your own date patterns. For example, dd/mm/yyyy, mm/dd/yyyy, yyyy-mm-dd, and so on.
section: Imported - java2s Archive
order: 1113
source: https://web.archive.org/web/20070319212123/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/SimpleDateFormat.htm
---
With SimpleDateFormat, you can set your own date patterns. For example, dd/mm/yyyy, mm/dd/yyyy, yyyy-mm-dd, and so on.

The following pattern letters are defined (all other characters from 'A' to 'Z' and from 'a' to 'z' are reserved):

```java title=Example.java
Letter   Date or Time Component   Presentation       Examples
G        Era designator             Text                AD
y        Year                       Year                1996;    96
M        Month in year               Month               July; Jul; 07
w        Week in year               Number               27
W        Week in month               Number               2
D        Day in year               Number               189
d        Day in month               Number               10
F        Day of week in month       Number               2
E        Day in week               Text               Tuesday; Tue
a        Am/pm marker               Text               PM
H        Hour in day (0-23)       Number               0
k        Hour in day (1-24)       Number               24
K        Hour in am/pm (0-11)       Number               0
h        Hour in am/pm (1-12)       Number               12
m        Minute in hour           Number               30
s        Second in minute           Number               55
S        Millisecond                Number               978
z        Time zone                   General time zone   Pacific Standard Time; PST; GMT-08:00
Z        Time zone                  RFC 822 time zone   -0800
(from Java API doc)
```

The more commonly used patterns can be used by a combination of y (representing a year digit), M (representing a month digit) and d (representing a date digit).

Examples of patterns are dd/MM/yyyy, dd-MM-yyyy, MM/dd/yyyy, yyyy-MM-dd.

```java title=Example.java
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
public class MainClass {
  public static void main(String[] args) {
    String pattern = "MM/dd/yyyy";
    SimpleDateFormat format = new SimpleDateFormat(pattern);
    try {
      Date date = format.parse("12/31/2006");
      System.out.println(date);
    } catch (ParseException e) {
      e.printStackTrace();
    }
    // formatting
    System.out.println(format.format(new Date()));
  }
}
```

```java title=Example.java
Sun Dec 31 00:00:00 PST 2006
01/26/2007
```
