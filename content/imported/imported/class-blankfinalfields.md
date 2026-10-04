---
title: Blank final fields
nav: Blank final fields
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1135
source: https://web.archive.org/web/20090602122454/http://www.java2s.com:80/Code/Java/Class/Blankfinalfields.htm
---
Blank final fields

```java title=Example.java
// : c06:BlankFinal.java
// "Blank" final fields.
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
class Poppet {
  private int i;
  Poppet(int ii) {
    i = ii;
  }
}
public class BlankFinal {
  private final int i = 0; // Initialized final
  private final int j; // Blank final
  private final Poppet p; // Blank final reference
  // Blank finals MUST be initialized in the constructor:
  public BlankFinal() {
    j = 1; // Initialize blank final
    p = new Poppet(1); // Initialize blank final reference
  }
  public BlankFinal(int x) {
    j = x; // Initialize blank final
    p = new Poppet(x); // Initialize blank final reference
  }
  public static void main(String[] args) {
    new BlankFinal();
    new BlankFinal(47);
  }
} ///:~
```

1.  Java Final variable: Once created and initialized, its value can not be changed
---  ---
2.  Experiment with final args to functions
3.  Using final with method arguments
4.  The effect of final on fields
5.  Making an entire class final
