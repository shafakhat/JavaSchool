---
title: Number formatting helps make your numbers more readable.
nav: Number formatting helps ma...
description: Imported from the java2s.com archive: Number formatting helps make your numbers more readable.
section: Imported - java2s Archive
order: 1105
source: https://web.archive.org/web/2018/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Numberformattinghelpsmakeyournumbersmorereadable.htm
---
```java title=Example.java
import java.text.NumberFormat;
import java.util.Locale;
public class MainClass {
  public static void main(String[] args) {
    NumberFormat nf = NumberFormat.getInstance(Locale.US);
    System.out.println(nf.getClass().getName());
    System.out.println(nf.format(123445));
  }
}
java title=Example.java
java.text.DecimalFormat
123,445
```

- If you use Locale.Germany, you'll get a NumberFormat object that formats numbers according to the German locale.
- If you pass Locale.US, you get one for the US number format.
- The no-argument getInstance method returns a NumberFormat object with the user computer's locale.
