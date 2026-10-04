---
title: Java Tutorial - Java Class Access Control
nav: Java Tutorial - Java Class...
description: We can control the access level for class member variables and methods through access specifiers.
section: Imported - java2s Archive
order: 50442
source: https://www.java2s.com/Tutorials/Java/Java_Language/5040__Java_Access_Control.html
---
```java title=Example.java
« Previous
```

- Next »

We can control the access level for class member variables and methods through access specifiers.

Java's access specifiers are public, private, protected and a default access level.

## Level

- A public class member can be accessed by any other code.
- A private class member can only be accessed within its class.
- A default access class member has no access specifiers. A class's default features are accessible to any class in the same package.
- A protected feature of a class is available to all classes in the same package(like a default) and to its subclasses.

protected features are more accessible than default features.

To understand the effects of public and private access, consider the following program:

```java title=Example.java
class Test {//www.java2s.comint a;        // default access
publicint b; // public access
privateint c; // private access
// methods to access c
void setc(int i) {
    c = i;
  }
  int getc() {
    return c;
  }
}
publicclass Main {
  publicstaticvoid main(String args[]) {
    Test ob = new Test();
    ob.a = 1;
    ob.b = 2;
    // This is not OK and will cause an error
// ob.c = 100; // Error!
// You must access c through its methods
    ob.setc(100); // OK
    System.out.println("a, b, and c: " + ob.a +
         " " + ob.b + " " + ob.getc());
  }
}
```

The output:

## Member Access and Inheritance

A subclass cannot access the private members of the superclass. For example, consider the following simple class hierarchy. If you try to compile the following program, you will get the error message.

```java title=Example.java
class A {//fromwww.java2s.comprivateint j; // private to A
}
class B extends A {
  int total;
  void sum() {
    total = j; // ERROR, j is not accessible here
  }
}
```

The output:

## Access matrix for Java

The following table shows the access matrix for Java. Yes means accessible, no means not accessible.

| Position | Private | No modifier | Protected | Public |
|---|---|---|---|---|
| Same class | Yes | Yes | Yes | Yes |
| Same package subclass | No | Yes | Yes | Yes |
| Same package non-subclass | No | Yes | Yes | Yes |
| Different package subclass | No | No | Yes | Yes |
| Different package non-subclass | No | No | No | Yes |

## Access Modifiers and their targets

Not all modifiers can be applied to all features. Top-level classes may not be protected. Methods may not be transient. Static can apply it to free-floating blocks of code.

The following table shows all possible combinations of features and modifiers. yes means we can use that modifier to control the access for the corresponding entities.

| Modifier | Class | Variable | Method | Constructor | Code Block |
|---|---|---|---|---|---|
| public | yes | yes | yes | yes | no |
| protected | no | yes | yes | yes | no |
| empty accessor | yes | yes | yes | yes | yes |
| private | no | yes | yes | yes | no |
| final | yes | yes | yes | no | no |
| abstract | yes | no | yes | no | no |
| static | no | yes | yes | no | yes |
| native | no | no | yes | no | no |
| transient | no | yes | no | no | no |
| volatile | no | yes | no | no | no |
| synchronized | no | no | yes | no | yes |

- Next »
- « Previous
