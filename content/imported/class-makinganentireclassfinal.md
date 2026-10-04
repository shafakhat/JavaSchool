---
title: Making an entire class final
nav: Making an entire class final
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1042
source: https://web.archive.org/web/20090602102407/http://www.java2s.com:80/Code/Java/Class/Makinganentireclassfinal.htm
---
Making an entire class final

```java title=Example.java
// : c06:Jurassic.java
// Making an entire class final.
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
class SmallBrain {
}
final class Dinosaur {
  int i = 7;
  int j = 1;
  SmallBrain x = new SmallBrain();
  void f() {
  }
}
//! class Further extends Dinosaur {}
// error: Cannot extend final class 'Dinosaur'
public class Jurassic {
  public static void main(String[] args) {
    Dinosaur n = new Dinosaur();
    n.f();
    n.i = 40;
    n.j++;
  }
} ///:~
```

1.  Java Final variable: Once created and initialized, its value can not be changed
---  ---
2.  Blank final fields
3.  Experiment with final args to functions
4.  Using final with method arguments
5.  The effect of final on fields
