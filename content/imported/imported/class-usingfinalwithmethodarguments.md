---
title: Using final with method arguments
nav: Using final with method ar...
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1098
source: https://web.archive.org/web/20090602121557/http://www.java2s.com:80/Code/Java/Class/Usingfinalwithmethodarguments.htm
---
Using final with method arguments

```java title=Example.java
// : c06:FinalArguments.java
// Using final with method arguments.
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
class Gizmo {
  public void spin() {
  }
}
public class FinalArguments {
  void with(final Gizmo g) {
    //! g = new Gizmo(); // Illegal -- g is final
  }
  void without(Gizmo g) {
    g = new Gizmo(); // OK -- g not final
    g.spin();
  }
  // void f(final int i) { i++; } // Can't change
  // You can only read from a final primitive:
  int g(final int i) {
    return i + 1;
  }
  public static void main(String[] args) {
    FinalArguments bf = new FinalArguments();
    bf.without(null);
    bf.with(null);
  }
} ///:~
```

1.  Java Final variable: Once created and initialized, its value can not be changed
---  ---
2.  Blank final fields
3.  Experiment with final args to functions
4.  The effect of final on fields
5.  Making an entire class final
