---
title: Formatting date with full day and month name and show time up to milliseconds with AM/PM
nav: Formatting date with full ...
description: Format formatter = new SimpleDateFormat("EEEE, dd MMMM yyyy, hh:mm:ss.SSS a");
section: Imported
order: 20014
source: http://www.java2s.com:80/Tutorial/Java/0120__Development/FormattingdatewithfulldayandmonthnameandshowtimeuptomillisecondswithAMPM.htm
---
```java title=Example.java
import java.text.Format;
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] argv) throws Exception {
    Format formatter = new SimpleDateFormat("EEEE, dd MMMM yyyy, hh:mm:ss.SSS a");
    String today = formatter.format(new Date());
    System.out.println("Today : " + today);
  }
}
```
