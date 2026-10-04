---
title: Convert a String to Date
nav: Convert a String to Date
description: SimpleDateFormat dateFormat = new SimpleDateFormat("dd/MM/yyyy");
section: Imported - java2s Archive
order: 1041
source: https://web.archive.org/web/20101006234318/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/ConvertaStringtoDate.htm
---
```java title=Example.java
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] args) throws Exception {
    SimpleDateFormat dateFormat = new SimpleDateFormat("dd/MM/yyyy");
    Date theDate = dateFormat.parse("01/01/2009");
    System.out.println(dateFormat.format(theDate));
  }
}
//01/01/2009
```
