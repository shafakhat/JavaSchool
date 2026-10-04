---
title: The java.util.Calendar Class
nav: The java.util.Calendar Class
description: To create a java.util.Calendar object, you have to use its static getInstance method.
section: Imported - java2s Archive
order: 1055
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ThejavautilCalendarClass.htm
---
To create a java.util.Calendar object, you have to use its static getInstance method.

```java title=Example.java
publicstatic Calendar getInstance ()
publicstatic Calendar getInstance (Locale locale)
```

The first overload returns an instance that employs the computer's locale.

```java title=Example.java
import java.util.Calendar;
publicclass MainClass{
  publicstaticvoid main(String[] args){
     Calendar calendar = Calendar.getInstance ();
  }
}
```
