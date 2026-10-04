---
title: It only looks like you can override a private or private final method
nav: It only looks like you can...
description: It only looks like you can override a private or private final method
section: Imported - java2s Archive
order: 1035
source: https://web.archive.org/web/20081201072023/http://www.java2s.com:80/Code/Java/Class/Itonlylookslikeyoucanoverrideaprivateorprivatefinalmethod.htm
---
It only looks like you can override a private or private final method

```java title=Example.java
// : c06:FinalOverridingIllusion.java
// It only looks like you can override a private or private final method.
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
class WithFinals {
  // Identical to "private" alone:
  private final void f() {
    System.out.println("WithFinals.f()");
  }
  // Also automatically "final":
  private void g() {
    System.out.println("WithFinals.g()");
  }
}
class OverridingPrivate extends WithFinals {
  private final void f() {
    System.out.println("OverridingPrivate.f()");
  }
  private void g() {
    System.out.println("OverridingPrivate.g()");
  }
}
class OverridingPrivate2 extends OverridingPrivate {
  public final void f() {
    System.out.println("OverridingPrivate2.f()");
  }
  public void g() {
    System.out.println("OverridingPrivate2.g()");
  }
}
public class FinalOverridingIllusion {
  public static void main(String[] args) {
    OverridingPrivate2 op2 = new OverridingPrivate2();
    op2.f();
    op2.g();
    // You can upcast:
    OverridingPrivate op = op2;
    // But you can't call the methods:
    //! op.f();
    //! op.g();
    // Same here:
    WithFinals wf = op2;
    //! wf.f();
    //! wf.g();
  }
} ///:~
```

1.  Polymorphism in Java
---  ---
2.  Override Shape
3.  Method override demo
