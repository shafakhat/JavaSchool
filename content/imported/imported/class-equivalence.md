---
title: Equivalence
nav: Equivalence
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1015
source: https://web.archive.org/web/20090530100136/http://www.java2s.com:80/Code/Java/Class/Equivalence.htm
---
Equivalence

```java title=Example.java
//: c03:Equivalence.java
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
public class Equivalence {
  static Test monitor = new Test();
  public static void main(String[] args) {
    Integer n1 = new Integer(47);
    Integer n2 = new Integer(47);
    System.out.println(n1 == n2);
    System.out.println(n1 != n2);
  }
} ///:~
```

1.  Equals(Equal) Method
2.  Equals Method
