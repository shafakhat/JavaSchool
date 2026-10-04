---
title: Java Object Oriented Design - Java Enum Compare
nav: Java Object Oriented Desig...
description: The compareTo() method of the Enum class compares two enum constants of the same enum type. It returns the difference in ordinal for the two enum constants. If both enum
section: Imported - java2s Archive
order: 50190
source: https://www.java2s.com/Tutorials/Java/Java_Object_Oriented_Design/0650__Java_Enum_Compare.html
---
You can compare two enum constants in three ways:

- Using the compareTo() method of the Enum class
- Using the equals() method of the Enum class
- Using the == operator

The compareTo() method of the Enum class compares two enum constants of the same enum type. It returns the difference in ordinal for the two enum constants. If both enum constants are the same, it returns zero.

## Example

The following code will print -3 because the difference of the ordinals for LOW(ordinal=0) and URGENT(ordinal=3) is -3.

A negative value means the constant being compared occurs before the one being compared against.

```java title=Example.java
enum Level {
  LOW, MEDIUM, HIGH, URGENT;
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    Level s1 = Level.LOW;
    Level s2 = Level.URGENT;
    // s1.compareTo(s2) returns s1.ordinal() - s2.ordinal()
int diff = s1.compareTo(s2);
    System.out.println(diff);
  }
}
```

The code above generates the following result.

## Example 2

The equals() method of the Enum class compares two enum constants for equality.

An enum constant is equal only to itself. The equals() method can be invoked on two enum constants of different types.

```java title=Example.java
enum Level {
  LOW, MEDIUM, HIGH, URGENT;
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    Level s1  = Level.LOW;
    Level s2  = Level.URGENT;
    System.out.println(s1.equals(s1));
  }
}
```

The code above generates the following result.

We can use the equality operator == to compare two enum constants for equality.

Both operands to the == operator must be of the same enum type.

- « Previous
