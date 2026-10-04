---
title: The instanceof Keyword
nav: The instanceof Keyword
description: The instanceof keyword can be used to test if an object is of a specified type.
section: Imported - java2s Archive
order: 1049
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0060__Operators/TheinstanceofKeyword.htm
---
The instanceof keyword can be used to test if an object is of a specified type.

```java title=Example.java
if (objectReference instanceof type)
```

The following if statement returns true.

```java title=Example.java
publicclass MainClass {
  publicstaticvoid main(String[] a) {
    String s = "Hello";
    if (s instanceof java.lang.String) {
      System.out.println("is a String");
    }
  }
}
java title=Example.java
is a String
```

However, applying instanceof on a null reference variable returns false. For example, the following if statement returns false.

```java title=Example.java
publicclass MainClass {
  publicstaticvoid main(String[] a) {
    String s = null;
    if (s instanceof java.lang.String) {
      System.out.println("true");
    } else {
      System.out.println("false");
    }
  }
}
java title=Example.java
false
```

Since a subclass 'is a' type of its superclass, the following if statement, where Child is a subclass of Parent, returns true.

```java title=Example.java
class Parent {
  public Parent() {
  }
}
class Child extends Parent {
  public Child() {
    super();
  }
}
publicclass MainClass {
  publicstaticvoid main(String[] a) {
    Child child = new Child();
    if (child instanceof Parent) {
      System.out.println("true");
    }
  }
}
java title=Example.java
true
```
