---
title: Comparing Object Values Using Hash Codes
nav: Comparing Object Values Us...
description: Imported from the java2s.com archive: Comparing Object Values Using Hash Codes
section: Imported - java2s Archive
order: 1011
source: https://web.archive.org/web/20100314200834/http://www.java2s.com:80/Tutorial/Java/0100__Class-Definition/ComparingObjectValuesUsingHashCodes.htm
---
```java title=Example.java
import java.io.File;
public class Main {
  public static void main(String[] argv) throws Exception {
    File file1 = new File("a");
    File file2 = new File("a");
    File file3 = new File("b");
    int hc1 = file1.hashCode();
    System.out.println(hc1);
    int hc2 = file2.hashCode();
    System.out.println(hc2);
    int hc3 = file3.hashCode();
    System.out.println(hc3);
  }
}
```
