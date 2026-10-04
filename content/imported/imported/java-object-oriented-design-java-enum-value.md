---
title: Java Object Oriented Design - Java Enum Value
nav: Java Object Oriented Desig...
description: The following code declares a public enum type called Level with four enum constants: LOW, MEDIUM, HIGH, and URGENT.
section: Imported - java2s Archive
order: 50186
source: https://www.java2s.com/Tutorials/Java/Java_Object_Oriented_Design/0610__Java_Enum_Value.html
---
```java title=Example.java
« Previous
```

- Next »

An enum type defines two things:

- The enum constants
- The order for those constants

The following code declares a public enum type called Level with four enum constants: LOW, MEDIUM, HIGH, and URGENT.

```java title=Example.java
public enum Level {
    LOW,  MEDIUM,  HIGH, URGENT;
}
```

The Level enum type defines four enum constants.

A variable of the Level enum type can have only one of the four values-LOW, MEDIUM, HIGH, and URGENT-or null.

We can use dot notation to refer to the enum constants by using the enum type name as the qualifier.

The following code assigns values to a variable of Level enum type:

```java title=Example.java

Level low  = Level.LOW;
Level medium = Level.MEDIUM;
Level high  = Level.HIGH;
Level urgent = Level.URGENT;
```

We cannot instantiate an enum type. The following code results in a compile-time error:

```java title=Example.java

Level badAttempt   = new Level(); // A  compile-time error
```

## Enum order number

An enum type assigns an order number, called ordinal, to all of its constants.

The ordinal starts with zero and is incremented by one as moving from first to last in the list of constants.

The first enum constant is assigned the value of zero, the second of 1, the third of 2, and so on.

The ordinal values assigned to constants declared in Level enum type are 0 to LOW, 1 to MEDIUM, 2 to HIGH, and 3 to URGENT.

Each enum constant has a name which is the same as the identifier for the constant. For example, the name for the LOW constant in the Level enum type is "LOW".

We can get the name and the ordinal of an enum constant using the name() and ordinal() methods, respectively.

Each enum type has a static method named values() that returns an array of constants in the order they are declared in its body.

The following code prints the name and ordinal of all enum constants declared in the Level enum type.

```java title=Example.java
enum Level {//www.java2s.com
  LOW, MEDIUM, HIGH, URGENT;
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    for (Level s : Level.values()) {
      String name = s.name();
      int ordinal = s.ordinal();
      System.out.println(name + "(" + ordinal + ")");
    }
  }
}
```

The code above generates the following result.

## Reverse Lookup for Enum Constants

We can get the reference of an enum constant from its name or position. using valueOf() method.

The reverse lookup for enum constants is case-sensitive.

We can use the array returned by the values() method to perform reverse lookup by ordinal.

The order of the values in the array returned by values() method is the same as the order in which the enum constants are declared.

The ordinal of enum constants starts at zero.

The following code demonstrates how to reverse look up enum constants:

```java title=Example.java
enum Level {/*fromwww.java2s.com*/
  LOW, MEDIUM, HIGH, URGENT;
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    Level low1 = Level.valueOf("LOW");
    // A reverse lookup using a name
    Level low2 = Level.values()[0];
    // A reverse lookup using an ordinal
    System.out.println(low1);
    System.out.println(low2);
    System.out.println(low1 == low2);
  }
}
```

The code above generates the following result.

## Range of Enum Constants

java.util.EnumSet collection class works with lists of enum constants of an enum type.

The following code demonstrates how to use the EnumSet class to work with the range for enum constants.

```java title=Example.java
import java.util.EnumSet;
/*fromwww.java2s.com*/enum Level {
  LOW, MEDIUM, HIGH, URGENT;
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    EnumSet<Level> allLevels = EnumSet.allOf(Level.class);
    print(allLevels);
    EnumSet<Level> l = EnumSet.range(Level.LOW, Level.URGENT);
    print(l);
  }
  publicstaticvoid print(EnumSet<Level> levels) {
    for (Level d : levels) {
      System.out.println(d + "  ");
    }
  }
}
```

The code above generates the following result.

- Next »
- « Previous
