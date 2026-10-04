---
title: Display a percentage
nav: Display a percentage
description: Imported from the java2s.com archive: Display a percentage
section: Imported - java2s Archive
order: 1089
source: https://web.archive.org/web/20100525043620/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/Displayapercentage.htm
---
```java title=Example.java
import java.text.DecimalFormat;
public class Main {
  public static void main(String[] argv) throws Exception {
    DecimalFormat df = new DecimalFormat("#%");
    System.out.println(df.format(0.19));
    System.out.println(df.format(-0.19));
  }
}
/*19%
-19%
*/
```
