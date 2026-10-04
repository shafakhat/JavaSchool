---
title: Convert a String Date Such as 2003/01/10 into a java.util.Date Object
nav: Convert a String Date Such...
description: SimpleDateFormat formatter = new SimpleDateFormat("yyyy/MM/dd");
section: Imported - java2s Archive
order: 1040
source: https://web.archive.org/web/20070324082058/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/ConvertaStringDateSuchas20030110intoajavautilDateObject.htm
---
```java title=Example.java
import java.text.ParseException;
import java.text.SimpleDateFormat;
public class MainClass {
  public static void main(String[] args) {
    SimpleDateFormat formatter = new SimpleDateFormat("yyyy/MM/dd");
    String date = "2003/01/10";
    java.util.Date utilDate = null;
    try {
      utilDate = formatter.parse(date);
    } catch (ParseException e) {
      // TODO Auto-generated catch block
      e.printStackTrace();
    }
    System.out.println("date:" + date);
    System.out.println("utilDate:" + utilDate);
  }
}
```

```java title=Example.java
date:2003/01/10
utilDate:Fri Jan 10 00:00:00 PST 2003
```
