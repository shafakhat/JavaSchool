---
title: BeanUtil Array Utils Example
nav: BeanUtil Array Utils Example
description: Imported from the java2s.com archive: BeanUtil Array Utils Example
section: Imported - java2s Archive
order: 1006
source: https://web.archive.org/web/20070119101608/http://www.java2s.com:80/Code/Java/Apache-Common/BeanUtilArrayUtilsExample.htm
---
```java title=Example.java
import org.apache.commons.lang.ArrayUtils;
public class ArrayUtilsExampleV1 {
  public static void main(String args[]) {
    long[] longArray = new long[] {10000, 30, 99};
    String[] stringArray = new String[] {"abc", "def", "fgh"};
    long[] clonedArray = ArrayUtils.clone(longArray);
    System.err.println(
      ArrayUtils.toString((ArrayUtils.toObject(clonedArray))));
    System.err.println(ArrayUtils.indexOf(stringArray, "def"));
    ArrayUtils.reverse(stringArray);
    System.err.println(ArrayUtils.toString(stringArray));
  }
}
```

Download: BeanUtilArrayUtilsExampleV1.zip ( 392 K )
Related examples in the same category
