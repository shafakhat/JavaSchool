---
title: Format Month in MMM format like Jan, Feb etc.
nav: Format Month in MMM format...
description: System.out.println("Current Month in MMM format : " + sdf.format(date));
section: Imported
order: 20006
source: http://www.java2s.com:80/Tutorial/Java/0120__Development/FormatMonthinMMMformatlikeJanFebetc.htm
---
```java title=Example.java
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] args) {
    Date date = new Date();
    SimpleDateFormat sdf = new SimpleDateFormat("MMM");
    System.out.println("Current Month in MMM format : " + sdf.format(date));
    }
}
//Current Month in MMM format : Feb
```
