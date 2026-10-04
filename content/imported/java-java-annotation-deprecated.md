---
title: Java Annotation @Deprecated
nav: Java Annotation @Deprecated
description: Use the @Deprecated annotation to mark the deprecated method.
section: Imported - java2s Archive
order: 1011
source: https://web.archive.org/web/2016/http://www.java2s.com/ref/java/java-annotation-deprecated.html
---
- java.lang.annotation
- java.lang.annotation Annotation

## Introduction

Use the @Deprecated annotation to mark the deprecated method.

Use the @Deprecated Javadoc tag to mark the method as deprecated within the documentation.

```java title=Example.java
import java.math.BigInteger;
public class Main {
   public static void main(String[] args) {
      BigInteger[] arr = new BigInteger[2];
      arr[0] = new BigInteger("1");
      arr[1] = new BigInteger("25");
// Use the older, deprecated method   System.out.println(addNumbers(1, 25));
      // Use the newer, non-deprecated method System.out.println(addNumbers(arr));
   } /**
    * Accepts two values and returns their sum.
    *
    * @param x
    * @param y
    * @return
    * @deprecated The newer, more robust addNumbers(BigInteger[]) should now be
    *             used
    */
   @Deprecated public static int addNumbers(int x, int y) {
      return x + y;
   }
   /**
    * Newer, better method that accepts an unlimited number of values and returns
    * the sum.
    *
    * @param nums
    * @return
    */ public static BigInteger addNumbers(BigInteger[] nums) {
      BigInteger result = new BigInteger("0");
      for (BigInteger num : nums) {
         result = result.add(num);
      }
      return result;
   }
}
```

PreviousNext

## Related

- Java Annotation with single member
- Java Annotation built-In annotations
- Java annotation @SafeVarargs
- Java RuntimeMXBean class
- Java OperatingSystemMXBean class
