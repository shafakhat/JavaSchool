---
title: The java.util.Date Class
nav: The java.util.Date Class
description: Times can also be represented as a long. See the discussion of the currentTimeMillis method of the java.lang.System
section: Imported - java2s Archive
order: 1215
source: https://web.archive.org/web/20070319192803/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/ThejavautilDateClass.htm
---
- java.util.Date, a class normally used to represent dates and times.
- java.util.Calendar, often used to manipulate dates.

Times can also be represented as a long. See the discussion of the currentTimeMillis method of the java.lang.System

```java title=Example.java
     public Date ()
     public Date (long time)
```

- The no-argument constructor creates a Date object representing the current date and time.
- The second constructor creates a Date that represents the specified number of milliseconds since January 1, 1970, 00:00:00 GMT.

```java title=Example.java
import java.util.Date;
public class MainClass{
  public static void main(String[] args){
     Date date = new Date(1111111111);
     System.out.println(date);
  }
}
java title=Example.java
Tue Jan 13 12:38:31 PST 1970
```
