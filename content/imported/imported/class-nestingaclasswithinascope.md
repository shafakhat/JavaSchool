---
title: Nesting a class within a scope
nav: Nesting a class within a s...
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1047
source: https://web.archive.org/web/20090106041547/http://www.java2s.com:80/Code/Java/Class/Nestingaclasswithinascope.htm
---
Nesting a class within a scope

```java title=Example.java
// : c08:Parcel5.java
// Nesting a class within a scope.
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
public class Parcel5 {
  private void internalTracking(boolean b) {
    if (b) {
      class TrackingSlip {
        private String id;
        TrackingSlip(String s) {
          id = s;
        }
        String getSlip() {
          return id;
        }
      }
      TrackingSlip ts = new TrackingSlip("slip");
      String s = ts.getSlip();
    }
    // Can't use it here! Out of scope:
    //! TrackingSlip ts = new TrackingSlip("x");
  }
  public void track() {
    internalTracking(true);
  }
  public static void main(String[] args) {
    Parcel5 p = new Parcel5();
    p.track();
  }
} ///:~
```

1.  Nested classes can access all members of all levels of the classes they are nested within
---  ---
2.  Creating inner classes
3.  Creating instances of inner classes
4.  Returning a reference to an inner class
5.  Putting test code in a nested class
6.  Inheriting an inner class
7.  Creating a constructor for an anonymous inner class
8.  This file is to show what happens if you try to access an inner class created in another class
9.  Demonstrate an Inner Child class
10.  Demonstrate simple inner class
11.  Just to show that there is no such thing as inner methods in Java
12.  A named inner class is used to
13.  An inner class cannot be overriden like a method
14.  Proper inheritance of an inner class
15.  Using inner classes for callbacks
16.  Holds a sequence of Objects
17.  With concrete or abstract classes, inner classes are the only way to produce the effect
18.  Nested Class Static
19.  Static Inner Class
20.  Compiler will generate a synthetic constructor since SyntheticConstructor() is private
