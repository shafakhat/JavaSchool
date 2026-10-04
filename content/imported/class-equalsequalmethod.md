---
title: Equals(Equal) Method
nav: Equals(Equal) Method
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1013
source: https://web.archive.org/web/20090530094149/http://www.java2s.com:80/Code/Java/Class/EqualsEqualMethod.htm
---
```java title=Example.java
//: c03:EqualsMethod2.java
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
class Value {
  int i;
}
public class EqualsMethod2 {
  public static void main(String[] args) {
    Value v1 = new Value();
    Value v2 = new Value();
    v1.i = v2.i = 100;
    System.out.println(v1.equals(v2));
  }
} ///:~
```

1.  Equals Method
2.  Equivalence
