---
title: Get the identity hash codes
nav: Get the identity hash codes
description: Imported from the java2s.com archive: Get the identity hash codes
section: Imported - java2s Archive
order: 1027
source: https://web.archive.org/web/20100314200839/http://www.java2s.com:80/Tutorial/Java/0100__Class-Definition/Gettheidentityhashcodes.htm
---
```java title=Example.java
import java.io.File;
public class Main {
  public static void main(String[] argv) throws Exception {
    File file1 = new File("a");
    File file2 = new File("a");
    File file3 = new File("b");
    int ihc1 = System.identityHashCode(file1);
    System.out.println(ihc1);
    int ihc2 = System.identityHashCode(file2);
    System.out.println(ihc2);
    int ihc3 = System.identityHashCode(file3);
    System.out.println(ihc3);
  }
}
```
