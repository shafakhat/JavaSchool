---
title: Inheritance syntax and properties
nav: Inheritance syntax and pro...
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1029
source: https://web.archive.org/web/20081230020947/http://www.java2s.com:80/Code/Java/Class/Inheritancesyntaxandproperties.htm
---
Inheritance syntax and properties

```java title=Example.java
// : c06:Detergent.java
// Inheritance syntax & properties.
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
class Cleanser {
  private String s = new String("Cleanser");
  public void append(String a) {
    s += a;
  }
  public void dilute() {
    append(" dilute()");
  }
  public void apply() {
    append(" apply()");
  }
  public void scrub() {
    append(" scrub()");
  }
  public String toString() {
    return s;
  }
  public static void main(String[] args) {
    Cleanser x = new Cleanser();
    x.dilute();
    x.apply();
    x.scrub();
    System.out.println(x);
  }
}
public class Detergent extends Cleanser {
  // Change a method:
  public void scrub() {
    append(" Detergent.scrub()");
    super.scrub(); // Call base-class version
  }
  // Add methods to the interface:
  public void foam() {
    append(" foam()");
  }
  // Test the new class:
  public static void main(String[] args) {
    Detergent x = new Detergent();
    x.dilute();
    x.apply();
    x.scrub();
    x.foam();
    System.out.println(x);
    System.out.println("Testing base class:");
    Cleanser.main(args);
  }
} ///:~
```

1.  Combining composition and inheritance
---  ---
2.  Inheritance, constructors and arguments
3.  Composition for code reuse
4.  Cleanup and inheritance
5.  Proper inheritance of an inner class
6.  Extending an interface with inheritance
7.  Inheriting an inner class
