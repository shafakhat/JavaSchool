---
title: Parse string date value input with SimpleDateFormat('dd-MMM-yy')
nav: Parse string date value in...
description: Imported from the java2s.com archive: Parse string date value input with SimpleDateFormat('dd-MMM-yy')
section: Imported - java2s Archive
order: 1241
source: https://web.archive.org/web/2020/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ParsestringdatevalueinputwithSimpleDateFormatddMMMyy.htm
---
```java title=Example.java
import java.text.Format;
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] argv) throws Exception {
    Format formatter = new SimpleDateFormat("dd-MMM-yy");
    Date date = (Date) formatter.parseObject("29-Jan-02");
    System.out.println(date);
  }
}
```
