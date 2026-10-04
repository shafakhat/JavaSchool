---
title: Create a new instance of a class by calling a constructor with arguments
nav: Create a new instance of a...
description: Create a new instance of a class by calling a constructor with arguments
section: Imported - java2s Archive
order: 1154
source: https://web.archive.org/web/20100206183330/http://java2s.com/Code/Java/Class/Createanewinstanceofaclassbycallingaconstructorwitharguments.htm
---
```java title=Example.java
import java.lang.reflect.Constructor;
/**
 * Handy reflection routines.
 */
public abstract class Reflect {
  /**
   */
  public static Object newInstance(String className, Class[] signature, Object[] args)
      throws Exception {
    Class cls = Class.forName(className);
    Constructor constructor = cls.getConstructor(signature);
    return constructor.newInstance(args);
  }
}
```

1.  Paying attention to exceptions in constructors
---  ---
2.  Order of constructor calls
3.  Constructors and polymorphism don't produce what you might expect
4.  Constructor initialization with composition
5.  Demonstration of a simple constructor
6.  Constructors can have arguments
7.  Show Constructors conflicting
8.  Show that if your class has no constructors, your superclass constructors still get called
9.  Constructor calls during inheritance
10.  A constructor for copying an object of the same
