---
title: Composition for code reuse
nav: Composition for code reuse
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1148
source: https://web.archive.org/web/20081230140541/http://www.java2s.com:80/Code/Java/Class/Compositionforcodereuse.htm
---
```java title=Example.java
// : c06:SprinklerSystem.java
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
class WaterSource {
  private String s;
  WaterSource() {
    System.out.println("WaterSource()");
    s = new String("Constructed");
  }
  public String toString() {
    return s;
  }
}
public class SprinklerSystem {
  private String valve1, valve2, valve3, valve4;
  private WaterSource source;
  private int i;
  private float f;
  public String toString() {
    return "valve1 = " + valve1 + "\n" + "valve2 = " + valve2 + "\n"
        + "valve3 = " + valve3 + "\n" + "valve4 = " + valve4 + "\n"
        + "i = " + i + "\n" + "f = " + f + "\n" + "source = " + source;
  }
  public static void main(String[] args) {
    SprinklerSystem sprinklers = new SprinklerSystem();
    System.out.println(sprinklers);
  }
} ///:~
```

1.  Combining composition and inheritance
---  ---
2.  Inheritance, constructors and arguments
3.  Inheritance syntax and properties
4.  Cleanup and inheritance
5.  Proper inheritance of an inner class
6.  Extending an interface with inheritance
7.  Inheriting an inner class
