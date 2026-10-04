---
title: Pass long parameters to overloading method
nav: Pass long parameters to ov...
description: Imported from the java2s.com archive: Pass long parameters to overloading method
section: Imported - java2s Archive
order: 1038
source: https://web.archive.org/web/20070707045128/http://www.java2s.com:80/Tutorial/Java/0100__Class-Definition/Passlongparameterstooverloadingmethod.htm
---
It is legal to have these two methods in the same class.

```java title=Example.java
public class MainClass {
  public int printNumber(int i) {
      return i*2;
  }
  public long printNumber(long i) {
      return i*3;
  }
  public static void main(String[] args) {
  }
}
```

printNumber(3) will invoke this method:

```java title=Example.java
public int printNumber(int i)
```

To call the second, pass a long:

```java title=Example.java
printNumber(3L);
```
