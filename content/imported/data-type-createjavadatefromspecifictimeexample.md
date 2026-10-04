---
title: Create java Date from specific time example
nav: Create java Date from spec...
description: Imported from the java2s.com archive: Create java Date from specific time example
section: Imported - java2s Archive
order: 1081
source: https://web.archive.org/web/20140829090501/http://www.java2s.com/Tutorial/Java/0040__Data-Type/CreatejavaDatefromspecifictimeexample.htm
---
```java title=Example.java
import java.util.Date;
public class Main {
  public static void main(String[] args) {
    Date d = new Date(365L * 24L * 60L * 60L * 1000L);
    System.out.println(d);
  }
}
```
