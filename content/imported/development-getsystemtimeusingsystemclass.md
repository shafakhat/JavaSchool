---
title: Get system time using System class
nav: Get system time using Syst...
description: System.out.println("Milliseconds since midnight, January 1, 1970 UTC : " + lnSystemTime);
section: Imported - java2s Archive
order: 1722
source: https://web.archive.org/web/20140829081332/http://www.java2s.com/Tutorial/Java/0120__Development/GetsystemtimeusingSystemclass.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] args) {
    long lnSystemTime = System.currentTimeMillis();
    System.out.println("Milliseconds since midnight, January 1, 1970 UTC : " + lnSystemTime);
  }
}
```

| 6.20.1. | Compute and display elapsed time of an operation |
|---|---|
| 6.20.2. | Get system time using System class |
| 6.20.3. | Get elapsed time in milliseconds |
| 6.20.4. | Get elapsed time in seconds |
| 6.20.5. | Get elapsed time in minutes |
| 6.20.6. | Get elapsed time in hours |
| 6.20.7. | Get elapsed time in days |
| 6.20.8. | Returns a String in the format Xhrs, Ymins, Z sec, for the time difference between two times |
| 6.20.9. | Returns a formatted String from time |
| 6.20.10. | Convert milliseconds to readable string |
