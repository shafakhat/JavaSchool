---
title: Java Object Oriented Design - Java Enum Methods
nav: Java Object Oriented Desig...
description: Since an enum type is actually a class type, we can declare everything inside an enum type body that we can declare inside a class body.
section: Imported - java2s Archive
order: 50188
source: https://www.java2s.com/Tutorials/Java/Java_Object_Oriented_Design/0630__Java_Enum_Methods.html
---
```java title=Example.java
« Previous
```

- Next »

Since an enum type is actually a class type, we can declare everything inside an enum type body that we can declare inside a class body.

The following code defines a Level enum with fields, constructors, and methods

```java title=Example.java
public enum Level {
  LOW(30), MEDIUM(15), HIGH(7), URGENT(1);
  // Declare an instance variable
  private int levelValue;
  // Declare a private constructor
  private Level(int levelValue) {
    this.levelValue = levelValue;
  }
  public int getLevelValue() {
    return levelValue;
  }
}
```

The code above declares an instance variable levelValue, which will store a value for each enum constant.

It also defines a private constructor, which accepts an int parameter. It stores the value of its parameter in the instance variable.

We can add multiple constructors to an enum type.

We cannot add a public or protected constructor to an enum type.

Level enum declares a public method getLevelValue().

The enum constant declarations have changed to

```java title=Example.java

LOW(30), MEDIUM(15),  HIGH(7),  URGENT(1);
```

Now every enum constant name is followed by an integer value in parentheses. LOW(30) is shorthand for calling the constructor with an int parameter type.

When an enum constant is created, the value inside the parentheses will be passed to the constructor that we have added.

LOW invokes a default no-args constructor, while LOW(30) calls the constructor with parameter.

## Example

The following code tests the Level enum type. It prints the names of the constants, their ordinals, and their underline value.

```java title=Example.java
enum Level {//fromwww.java2s.com
  LOW(30), MEDIUM(15), HIGH(7), URGENT(1);
  // Declare an instance variable
privateint levelValue;
  // Declare a private constructor
private Level(int levelValue) {
    this.levelValue = levelValue;
  }
  publicint getLevelValue() {
    return levelValue;
  }
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    for (Level s : Level.values()) {
      String name = s.name();
      int ordinal = s.ordinal();
      int underLine = s.getLevelValue();
      System.out.println("name=" + name + ",  ordinal=" + ordinal + ", underLine="
          + underLine);
    }
  }
}
```

The code above generates the following result.

- Next »
- « Previous
