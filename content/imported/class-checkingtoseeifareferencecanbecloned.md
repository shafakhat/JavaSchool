---
title: Checking to see if a reference can be cloned
nav: Checking to see if a refer...
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1137
source: https://web.archive.org/web/20081009143436/http://www.java2s.com:80/Code/Java/Class/Checkingtoseeifareferencecanbecloned.htm
---
Checking to see if a reference can be cloned

```java title=Example.java
// : appendixa:CheckCloneable.java
// Checking to see if a reference can be cloned.
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
// Can't clone this because it doesn't override clone():
class Ordinary {
}
// Overrides clone, but doesn't implement Cloneable:
class WrongClone extends Ordinary {
  public Object clone() throws CloneNotSupportedException {
    return super.clone(); // Throws exception
  }
}
// Does all the right things for cloning:
class IsCloneable extends Ordinary implements Cloneable {
  public Object clone() throws CloneNotSupportedException {
    return super.clone();
  }
}
// Turn off cloning by throwing the exception:
class NoMore extends IsCloneable {
  public Object clone() throws CloneNotSupportedException {
    throw new CloneNotSupportedException();
  }
}
class TryMore extends NoMore {
  public Object clone() throws CloneNotSupportedException {
    // Calls NoMore.clone(), throws exception:
    return super.clone();
  }
}
class BackOn extends NoMore {
  private BackOn duplicate(BackOn b) {
    // Somehow make a copy of b and return that copy.
    // This is a dummy copy, just to make the point:
    return new BackOn();
  }
  public Object clone() {
    // Doesn't call NoMore.clone():
    return duplicate(this);
  }
}
// You can't inherit from this, so you can't override
// the clone method as you can in BackOn:
final class ReallyNoMore extends NoMore {
}
public class CheckCloneable {
  public static Ordinary tryToClone(Ordinary ord) {
    String id = ord.getClass().getName();
    System.out.println("Attempting " + id);
    Ordinary x = null;
    if (ord instanceof Cloneable) {
      try {
        x = (Ordinary) ((IsCloneable) ord).clone();
        System.out.println("Cloned " + id);
      } catch (CloneNotSupportedException e) {
        System.err.println("Could not clone " + id);
      }
    } else {
      System.out.println("Doesn't implement Cloneable");
    }
    return x;
  }
  public static void main(String[] args) {
    // Upcasting:
    Ordinary[] ord = { new IsCloneable(), new WrongClone(), new NoMore(),
        new TryMore(), new BackOn(), new ReallyNoMore(), };
    Ordinary x = new Ordinary();
    // This won't compile; clone() is protected in Object:
    //! x = (Ordinary)x.clone();
    // Checks first to see if a class implements Cloneable:
    for (int i = 0; i < ord.length; i++)
      tryToClone(ord[i]);
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
7.  You can insert Cloneability at any level of inheritance
8.  Cloning a composed object
9.  Serializable and clone
10.  Go through a few gyrations to add cloning to your own class
11.  The clone operation works for only a few items in the standard Java library
12.  Demonstration of cloning
13.  Simple demo of avoiding side-effects by using Object.clone
14.  Clone demo
