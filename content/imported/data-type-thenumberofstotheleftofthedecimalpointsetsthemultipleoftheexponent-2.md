---
title: The number of #'s to the left of the decimal point sets the multiple of the exponent.
nav: The number of #'s to the l...
description: DecimalFormat formatter = new DecimalFormat("#E0"); // exponent can be any
section: Imported - java2s Archive
order: 1217
source: https://web.archive.org/web/20100525043635/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/Thenumberofstotheleftofthedecimalpointsetsthemultipleoftheexponent.htm
---
```java title=Example.java
import java.text.DecimalFormat;
public class Main {
  public static void main(String[] argv) throws Exception {
    DecimalFormat formatter = new DecimalFormat("#E0"); // exponent can be any
                                                        // value
    String s = formatter.format(-1234.567);
    System.out.println(s);
    s = formatter.format(-.1234567);
    System.out.println(s);
  }
}
//-.1E4
//-.1E0
```
