---
title: Accessibility
nav: Accessibility
description: Within a subclass you can access its superclass's public and protected methods and fields , but not the superclass's private methods. If the subclass and the superclass a
section: Imported - java2s Archive
order: 1280
source: https://web.archive.org/web/20140829075625/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Accessibility.htm
---
Within a subclass you can access its superclass's public and protected methods and fields , but not the superclass's private methods. If the subclass and the superclass are in the same package, you can also access the superclass's default methods and fields.

```java title=Example.java
public class P {
  public void publicMethod() {
  }
  protected void protectedMethod() {
  }
  void defaultMethod() {
  }
}
class C extends P {
  public void testMethod() {
    publicMethod();
    protectedMethod();
    defaultMethod();
  }
}
```
