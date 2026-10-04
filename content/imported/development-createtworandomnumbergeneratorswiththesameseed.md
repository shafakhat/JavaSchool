---
title: Create two random number generators with the same seed
nav: Create two random number g...
description: Imported from the java2s.com archive: Create two random number generators with the same seed
section: Imported - java2s Archive
order: 1031
source: https://web.archive.org/web/20101102012916/http://www.java2s.com:80/Tutorial/Java/0120__Development/Createtworandomnumbergeneratorswiththesameseed.htm
---
```java title=Example.java
import java.util.Random;
public class Main {
  public static void main(String[] argv) throws Exception {
    Random rand = new Random();
    long seed = rand.nextLong();
    rand = new Random(seed);
    Random rand2 = new Random(seed);
  }
}
```
