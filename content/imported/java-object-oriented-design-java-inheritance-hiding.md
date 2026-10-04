---
title: Java Object Oriented Design - Java Inheritance Hiding
nav: Java Object Oriented Desig...
description: A class inherits all non-private static methods from its superclass.
section: Imported - java2s Archive
order: 50168
source: https://www.java2s.com/Tutorials/Java/Java_Object_Oriented_Design/0330__Java_Inheritance_Hiding.html
---
```java title=Example.java
```

## Method Hiding

A class inherits all non-private static methods from its superclass.

Redefining an inherited static method in a class is known as method hiding.

The redefined static method in a subclass hides the static method of its superclass.

Redefining a non-static method in a class is called method overriding.

All rules about the redefined method (name, access level, return types, and exception) for method hiding are the same as for method overriding.

```java title=Example.java
class MySuper {publicstaticvoid print() {
    System.out.println("Inside MySuper.print()");
  }
}
class MySubclass extends MySuper {
  publicstaticvoid print() {
    System.out.println("Inside MySubclass.print()");
  }
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    MySuper mhSuper = new MySubclass();
    MySubclass mhSub = new MySubclass();
    MySuper.print();
    MySubclass.print();
    ((MySuper) mhSub).print();
    mhSuper = mhSub;
    mhSuper.print();
    ((MySubclass) mhSuper).print();
  }
}
```

The code above generates the following result.

## Field Hiding

A field declaration, static or non-static, in a class hides the inherited field with the same name in its superclass.

The type of the field and its access level are not considered in the case of field hiding.

Field hiding occurs solely based on the field name.

```java title=Example.java
class MySuper {protectedint num = 100;
  protected String name = "Tom";
}
class MySub extends MySuper {
  publicvoid print() {
    System.out.println("num: " + num);
    System.out.println("name: " + name);
  }
}
class MySub2 extends MySuper {
  // Hides num field in MySuper class
privateint num = 200;
  // Hides name field in MySuper class
private String name = "Jack";
  publicvoid print() {
    System.out.println("num: " + num);
    System.out.println("name: " + name);
  }
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    MySub fhSub = new MySub();
    fhSub.print();
    MySub2 fhSub2 = new MySub2();
    fhSub2.print();
  }
}
```

The code above generates the following result.

## Example

The following code shows how to Access Hidden Fields of Superclass Using the super Keyword

```java title=Example.java
class MySuper {protectedint num = 100;
  protected String name = "Tom";
}
class MySub extends MySuper {
  // Hides the num field in MySuper class
privateint num = 200;
  // Hides the name field in MySuper class
private String name = "Jack";
  publicvoid print() {
    System.out.println("num: " + num);
    System.out.println("super.num: " + super.num);
    System.out.println("name: " + name);
    System.out.println("super.name: " + super.name);
  }
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    MySub s = new MySub();
    s.print();
  }
}
```

The code above generates the following result.

Field hiding occurs when a class declares a variable with the same name as an inherited variable from its superclass.

Field hiding occurs only based on the name of the field.

A class should use the keyword super to access the hidden fields of the superclass.

The class can use the simple names to access the redefined fields in its body.

- « Previous
