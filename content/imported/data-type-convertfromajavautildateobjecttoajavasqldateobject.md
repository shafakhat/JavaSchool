---
title: Convert from a java.util.Date Object to a java.sql.Date Object
nav: Convert from a java.util.D...
description: java.sql.Date sqlDate = new java.sql.Date(utilDate.getTime());
section: Imported - java2s Archive
order: 1045
source: https://web.archive.org/web/20070319212943/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/ConvertfromajavautilDateObjecttoajavasqlDateObject.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    java.util.Date utilDate = new java.util.Date();
    java.sql.Date sqlDate = new java.sql.Date(utilDate.getTime());
    System.out.println("utilDate:" + utilDate);
    System.out.println("sqlDate:" + sqlDate);
  }
}
```

```java title=Example.java

utilDate:Fri Feb 02 12:55:46 PST 2007
sqlDate:2007-02-02
```
