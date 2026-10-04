---
title: To obtain a date part, such as the hour, the month, or the year, use the get method
nav: To obtain a date part, suc...
description: To use it, pass a valid field to the get method. A valid field is one of the following values:
section: Imported - java2s Archive
order: 1091
source: https://web.archive.org/web/20140616104413/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Toobtainadatepartsuchasthehourthemonthortheyearusethegetmethod.htm
---
```java title=Example.java
public int get (int field)
```

To use it, pass a valid field to the get method. A valid field is one of the following values:
---
Calendar.YEAR, Calendar.MONTH, Calendar.DATE, Calendar.HOUR, Calendar.MINUTE, Calendar.SECOND, and Calendar.MILLISECOND.
get(Calendar.MONTH) returns a zero-based index of the month, with 0 representing January, 1 February, and 11 December.

```java title=Example.java
import java.util.Calendar;
public class MainClass{
  public static void main(String[] args){
     Calendar calendar = Calendar.getInstance ();
     System.out.println(calendar.get(Calendar.YEAR));
     System.out.println(calendar.get(Calendar.MONTH));
     System.out.println(calendar.get(Calendar.DATE));
     System.out.println(calendar.get(Calendar.HOUR));
     System.out.println(calendar.get(Calendar.MINUTE));
     System.out.println(calendar.get(Calendar.SECOND));
     System.out.println(calendar.get(Calendar.MILLISECOND));
  }
}
java title=Example.java
2007
0
30
8
32
42
805
```
