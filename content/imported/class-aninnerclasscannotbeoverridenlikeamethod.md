---
title: An inner class cannot be overriden like a method
nav: An inner class cannot be o...
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1131
source: https://web.archive.org/web/20090106053452/http://www.java2s.com:80/Code/Java/Class/Aninnerclasscannotbeoverridenlikeamethod.htm
---
An inner class cannot be overriden like a method

```java title=Example.java
// : c08:BigEgg.java
// An inner class cannot be overriden like a method.
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
class Egg {
  private Yolk y;
  protected class Yolk {
    public Yolk() {
      System.out.println("Egg.Yolk()");
    }
  }
  public Egg() {
    System.out.println("New Egg()");
    y = new Yolk();
  }
}
public class BigEgg extends Egg {
  public class Yolk {
    public Yolk() {
      System.out.println("BigEgg.Yolk()");
    }
  }
  public static void main(String[] args) {
    new BigEgg();
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
14.  Proper inheritance of an inner class
15.  Using inner classes for callbacks
16.  Holds a sequence of Objects
17.  With concrete or abstract classes, inner classes are the only way to produce the effect
18.  Nested Class Static
19.  Static Inner Class
20.  Compiler will generate a synthetic constructor since SyntheticConstructor() is private
