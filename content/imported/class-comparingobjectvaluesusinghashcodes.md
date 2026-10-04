---
title: Comparing Object Values Using Hash Codes
nav: Comparing Object Values Us...
description: Imported from the java2s.com archive: Comparing Object Values Using Hash Codes
section: Imported - java2s Archive
order: 1147
source: https://web.archive.org/web/20100206154041/http://java2s.com/Code/Java/Class/ComparingObjectValuesUsingHashCodes.htm
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

1.  Get the identity hash codes
