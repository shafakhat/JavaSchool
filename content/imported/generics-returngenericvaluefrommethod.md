---
title: Return generic value from method
nav: Return generic value from ...
description: 2. Java generic: Ambiguity caused by erasure on overloaded methods.
section: Imported - java2s Archive
order: 1047
source: https://web.archive.org/web/20090625011233/http://www.java2s.com:80/Code/Java/Generics/Returngenericvaluefrommethod.htm
---
Return generic value from method

```java title=Example.java
import java.io.Serializable;
class Base {
}
class Sub1 extends Base implements Serializable {
  public void run() {
  }
}
class Sub2 extends Base implements Serializable {
  public void run() {
  }
}
public class TypeInference {
  static <T extends Base> T infer(T t1, T t2) {
    return null;
  }
  public static void main(String[] args) {
    Base base = infer(new Sub1(), new Sub2());
    Serializable runnable = infer(new Sub1(), new Sub2());
  }
}
```

1.  Demonstrate a simple generic method.
---  ---
2.  Java generic: Ambiguity caused by erasure on overloaded methods.
3.  Overriding a generic method in a generic class.
4.  Java generic: A situation that creates a bridge method.
