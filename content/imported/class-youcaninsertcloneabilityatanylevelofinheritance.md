---
title: You can insert Cloneability at any level of inheritance
nav: You can insert Cloneabilit...
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1103
source: https://web.archive.org/web/20081009150835/http://www.java2s.com:80/Code/Java/Class/YoucaninsertCloneabilityatanylevelofinheritance.htm
---
```java title=Example.java
// : appendixa:HorrorFlick.java
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
class Person {
}
class Hero extends Person {
}
class Scientist extends Person implements Cloneable {
  public Object clone() {
    try {
      return super.clone();
    } catch (CloneNotSupportedException e) {
      // This should never happen: It's Cloneable already!
      throw new RuntimeException(e);
    }
  }
}
class MadScientist extends Scientist {
}
public class HorrorFlick {
  public static void main(String[] args) {
    Person p = new Person();
    Hero h = new Hero();
    Scientist s = new Scientist();
    MadScientist m = new MadScientist();
    //! p = (Person)p.clone(); // Compile error
    //! h = (Hero)h.clone(); // Compile error
    s = (Scientist) s.clone();
    m = (MadScientist) m.clone();
  }
} ///:~
```

1.  A Cloning Example
---  ---
2.  Creating a Deep Copy
3.  Shallow Copy Test
4.  Deep Copy Test
5.  Tests cloning to see if destination of references are also cloned
6.  Creating local copies with clone
7.  Cloning a composed object
8.  Serializable and clone
9.  Go through a few gyrations to add cloning to your own class
10.  Checking to see if a reference can be cloned
11.  The clone operation works for only a few items in the standard Java library
12.  Demonstration of cloning
13.  Simple demo of avoiding side-effects by using Object.clone
14.  Clone demo
