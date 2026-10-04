---
title: Parse string date value with default format
nav: Parse string date value wi...
description: Date date = DateFormat.getDateInstance(DateFormat.DEFAULT).parse("Feb 28, 2002");
section: Imported - java2s Archive
order: 1232
source: https://web.archive.org/web/2018/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ParsestringdatevaluewithdefaultformatDateFormatgetDateInstanceDateFormatDEFAULT.htm
---
```java title=Example.java
import java.text.DateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] argv) throws Exception {
    Date date = DateFormat.getDateInstance(DateFormat.DEFAULT).parse("Feb 28, 2002");
    System.out.println(date);
  }
}
```
