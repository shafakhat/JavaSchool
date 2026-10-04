---
title: Type Casting
nav: Type Casting
description: With objects, you can cast an instance of a subclass to its parent class. Casting an object to a parent class is called upcasting.
section: Imported - java2s Archive
order: 1296
source: https://web.archive.org/web/20140829075203/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/TypeCasting.htm
---
With objects, you can cast an instance of a subclass to its parent class. Casting an object to a parent class is called upcasting.

```java title=Example.java
Child child = new Child ();
Parent parent = child;
```

To upcast a Child object, all you need to do is assign the object to a reference variable of type Parent. The parent reference variable cannot access the members that are only available in Child.
Because parent references an object of type Child, you can cast it back to Child. It is called downcasting because you are casting an object to a class down the inheritance hierarchy. Downcasting requires that you write the child type in brackets. For example:

```java title=Example.java
Child child2 = (Child) parent;
```
