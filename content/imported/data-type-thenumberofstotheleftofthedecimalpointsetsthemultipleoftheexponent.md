---
title: The number of #'s to the left of the decimal point sets the multiple of the exponent.
nav: The number of #'s to the l...
description: DecimalFormat formatter = new DecimalFormat("#E0"); // exponent can be any
section: Imported - java2s Archive
order: 1359
source: https://web.archive.org/web/20140829084028/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Thenumberofstotheleftofthedecimalpointsetsthemultipleoftheexponent.htm
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

| 2.47.1. | new DecimalFormat(abc#) |
|---|---|
| 2.47.2. | DecimalFormat("00E00") |
| 2.47.3. | DecimalFormat("000E00") |
| 2.47.4. | DecimalFormat("0000000000E0") |
| 2.47.5. | new DecimalFormat("0.######E0") |
| 2.47.6. | Use new DecimalFormat("0.#####E0") to format double |
| 2.47.7. | new DecimalFormat("000000E0") |
| 2.47.8. | Use java.text.DecimalFormat to format integer |
| 2.47.9. | Display numbers with leading zeroes |
| 2.47.10. | Display a percentage |
| 2.47.11. | Display a currency value |
| 2.47.12. | Force minimum number of digits to left and right of decimal point |
| 2.47.13. | DecimalFormat("00.00E0") |
| 2.47.14. | The number of #'s to the left of the decimal point sets the multiple of the exponent. |
| 2.47.15. | DecimalFormat("##E0") (exponent must be multiple of 2) |
| 2.47.16. | DecimalFormat("###E0") (exponent must be multiple of 3) |
| 2.47.17. | Change the decimal separator is set to "." |
| 2.47.18. | Round number to fewer decimals |
| 2.47.19. | Display numbers with commas |
| 2.47.20. | Display numbers in scientific notation |
