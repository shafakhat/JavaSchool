---
title: Format hour in kk (01-24) format like 01, 02..24.
nav: Format hour in kk (01-24) ...
description: System.out.println("hour in kk format : " + sdf.format(date));
section: Imported
order: 20002
source: http://www.java2s.com:80/Tutorial/Java/0120__Development/Formathourinkk0124formatlike010224.htm
---
```java title=Example.java
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] args) {
    Date date = new Date();
    SimpleDateFormat sdf = new SimpleDateFormat("kk");
    System.out.println("hour in kk format : " + sdf.format(date));
  }
}
//hour in h format : 11
```
