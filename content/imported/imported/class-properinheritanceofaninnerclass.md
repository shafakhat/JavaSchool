---
title: Proper inheritance of an inner class
nav: Proper inheritance of an i...
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1061
source: https://web.archive.org/web/20081230140552/http://www.java2s.com:80/Code/Java/Class/Properinheritanceofaninnerclass.htm
---
```java title=Example.java
// : c08:BigEgg2.java
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
class Egg2 {
  protected class Yolk {
    public Yolk() {
      System.out.println("Egg2.Yolk()");
    }
    public void f() {
      System.out.println("Egg2.Yolk.f()");
    }
  }
  private Yolk y = new Yolk();
  public Egg2() {
    System.out.println("New Egg2()");
  }
  public void insertYolk(Yolk yy) {
    y = yy;
  }
  public void g() {
    y.f();
  }
}
public class BigEgg2 extends Egg2 {
  public class Yolk extends Egg2.Yolk {
    public Yolk() {
      System.out.println("BigEgg2.Yolk()");
    }
    public void f() {
      System.out.println("BigEgg2.Yolk.f()");
    }
  }
  public BigEgg2() {
    insertYolk(new Yolk());
  }
  public static void main(String[] args) {
    Egg2 e2 = new BigEgg2();
    e2.g();
  }
} ///:~
```

1.  Nested classes can access all members of all levels of the classes they are nested within
---  ---
2.  Creating inner classes
3.  Creating instances of inner classes
4.  Returning a reference to an inner class
5.  Nesting a class within a scope
6.  Putting test code in a nested class
7.  Inheriting an inner class
8.  Creating a constructor for an anonymous inner class
9.  This file is to show what happens if you try to access an inner class created in another class
10.  Demonstrate an Inner Child class
11.  Demonstrate simple inner class
12.  Just to show that there is no such thing as inner methods in Java
13.  A named inner class is used to
14.  An inner class cannot be overriden like a method
15.  Using inner classes for callbacks
16.  Holds a sequence of Objects
17.  With concrete or abstract classes, inner classes are the only way to produce the effect
18.  Nested Class Static
19.  Static Inner Class
20.  Compiler will generate a synthetic constructor since SyntheticConstructor() is private
