---
title: Java Object Oriented Design - Java Enum Types
nav: Java Object Oriented Desig...
description: An enum type creates an ordered list of constants as a type. It specifies constants in a specific order.
section: Imported - java2s Archive
order: 50185
source: https://www.java2s.com/Tutorials/Java/Java_Object_Oriented_Design/0600__Java_Enum_Types.html
---
```java title=Example.java
```

## What Is an Enum Type?

An enum type creates an ordered list of constants as a type. It specifies constants in a specific order.

The constants defined in an enum type are instances of that enum type.

## Syntax

You define an enum type using the keyword enum with the following syntax:

```java title=Example.java

<access-modifier> enum <enum-type-name>  {
    // List of  comma  separated names of  enum constants
}
```

<access-modifiers> is the same as the access modifier for a class: public, private, protected, or package-level.

<enum-type-name> is a valid Java identifier.

The body of the enum type is placed within braces following its name, The body can have a list of comma-separated constants and other elements, for example, instance variables, methods, etc.

Most of the time, the enum body includes only constants.

## Example

The following code declares an enum type called Gender, which declares two constants, MALE and FEMALE:

```java title=Example.java
public enum Gender  {
    MALE,  FEMALE;  // The semi-colon is optional
}
```

It is a convention to name the enum constants in uppercase.

The following code declares a public enum type called Level with four enum constants: LOW, MEDIUM, HIGH, and URGENT.

```java title=Example.java
public enum Level {
    LOW,  MEDIUM,  HIGH, URGENT;
}
```

A public enum type can be accessed from anywhere in the application.

A public enum type stays in a file with enum type name. The Level enum would be saved in a file named Level.java.

We need to place an enum type in a package and we can use an import statement to import an enum type.

## enum variable

We can declare a variable of an enum type the same way we declare a variable of a class type.

The following code declare errorLevel variable of the Level enum type

```java title=Example.java

Level errorLevel;
```

You can assign null to an enum type variable, like so:

```java title=Example.java

Level defectLevel = null;
```

## Using Enum Types in switch Statements

You can use enum types in switch statements.

When the switch expression is of an enum type, all case labels must be unqualified enum constants of the same enum type.

```java title=Example.java
enum Direction {/*www.java2s.com*/
  East, South, West, North
}
publicclass Main {
  publicstaticvoid main(String args[]) {
    Direction dir = Direction.South;
    switch (dir) {
    case South:
      System.out.println("south");
      break;
    case East:
      System.out.println("East");
      break;
    case West:
      System.out.println("West");
      break;
    case North:
      System.out.println("North.");
      break;
    }
  }
}
```

The code above generates the following result.

## Nested Enum Types

We can have a nested enum type declaration inside a class, an interface, or another enum type.

Nested enum types are implicitly static. Since an enum type is always static, we cannot declare a local enum type inside a method's body.

We can use any of the access modifiers (public, private, protected, or package) level for a nested enum type.

The following code shows how to declare a nested public enum type named Gender inside a Person class.

```java title=Example.java
class Person {
  public enum Gender {
    MALE, FEMALE
  }
}
publicclass Main {
  publicstatic void main(String[] args) {
    Person.Gender m = Person.Gender.MALE;
    Person.Gender f = Person.Gender.FEMALE;
    System.out.println(m);
    System.out.println(f);
  }
}
```

The Person.Gender enum type can be accessed from anywhere in the application because it has been declared public.

We can also use the simple name of an enum constant by importing the enum constants using static imports.

```java title=Example.java

import static  com.java2s.enums.Person.Gender.*;
```

## Implementing an Interface to an Enum Type

An enum type may implement interfaces. The rules for an enum type implementing an interface are the same as the rules for a class implementing an interface.

The following code shows how to let enum type implement an interface.

```java title=Example.java
interface Command {
  void execute();
}/*fromwww.java2s.com*/enum Level implements Command {
  LOW {
    publicvoid execute() {
      System.out.println("Low...");
    }
  },
  HIGH {
    publicvoid execute() {
      System.out.println("HIGH...");
    }
  };
  publicabstractvoid execute();
}
publicclass Main {
  publicstaticvoid main(String... args) {
    for (Command cmd : Level.values()) {
      cmd.execute();
    }
  }
}
```

The code above generates the following result.

- « Previous
