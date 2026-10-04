---
title: Constructors and polymorphism don't produce what you might expect
nav: Constructors and polymorph...
description: System.out.println("RoundGlyph.RoundGlyph(), radius = " + radius);
section: Imported - java2s Archive
order: 1114
source: https://web.archive.org/web/20140829082410/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Constructorsandpolymorphismdontproducewhatyoumightexpect.htm
---
```java title=Example.java
abstract class Glyph {
  abstract void draw();
  Glyph() {
    System.out.println("Glyph() before draw()");
    draw();
    System.out.println("Glyph() after draw()");
  }
}
class RoundGlyph extends Glyph {
  private int radius = 1;
  RoundGlyph(int r) {
    radius = r;
    System.out.println("RoundGlyph.RoundGlyph(), radius = " + radius);
  }
  void draw() {
    System.out.println("RoundGlyph.draw(), radius = " + radius);
  }
}
public class MainClass {
  public static void main(String[] args) {
    new RoundGlyph(5);
  }
}
java title=Example.java
Glyph() before draw()
RoundGlyph.draw(), radius = 0
Glyph() after draw()
RoundGlyph.RoundGlyph(), radius = 5
```

| 5.24.1. | Polymorphism |
|---|---|
| 5.24.2. | An example of polymorphism |
| 5.24.3. | Downcasting and Run-Time Type Identification (RTTI) |
| 5.24.4. | Constructors and polymorphism don't produce what you might expect |
| 5.24.5. | Dynamic Method Dispatch |
| 5.24.6. | Using run-time polymorphism. |
