---
title: Java Tutorial - Java Enum
nav: Java Tutorial - Java Enum
description: The identifiers East, South are called enumeration constants. Enumeration constants is implicitly declared as a public, static final member of Direction.
section: Imported - java2s Archive
order: 50463
source: https://www.java2s.com/Tutorials/Java/Java_Language/9000__Java_enum.html
---
An enumeration is a list of named constants.

## Syntax

An enumeration is created using the enum keyword.

For example, here is a simple enumeration:

```java title=Example.java
enum Direction {
   East, South, West, North
}
```

The identifiers East, South are called enumeration constants. Enumeration constants is implicitly declared as a public, static final member of Direction.

## Enum type variable

Once you have defined an enumeration, you can create a variable of that type.

Even though enumerations define a class type, you do not instantiate an enum using new.

The following code declares ap as a variable of enumeration type Direction:

```java title=Example.java
Direction ap;
```

Because ap is of type Direction, the only values that it can be assigned are those defined by the enumeration. For example, this assigns ap the value South:

```java title=Example.java
ap = Direction.South;
```

## Compare

Two enumeration constants can be compared for equality by using the == relational operator.

```java title=Example.java
// An enumeration of direction varieties.
enum Direction {
  East, South, West, North
}
publicclass Main {
  publicstaticvoid main(String args[]) {
    Direction dir = Direction.South;
    System.out.println("Value of dir: " + dir);
    dir = Direction.South;
    if (dir == Direction.South){
      System.out.println("ap contains GoldenDel.\n");
    }
  }
}
```

The code above generates the following result.

## Enum Switch

An enumeration value can also be used to control a switch statement.

```java title=Example.java
enum Direction {
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

## Java Enum values() / valueOf() Methods

All enumerations automatically contain two predefined methods: values() and valueOf().

Their general forms are:

```java title=Example.java
publicstatic enum-type[ ] values()
publicstatic enum-type valueOf(String str)
```

The values() method returns an array that contains a list of the enumeration constants. The valueOf() method returns the enumeration constant whose value corresponds to the string passed in str.

The following program demonstrates the values() and valueOf() methods:

```java title=Example.java
enum Direction {
  East, South, West, North
}
publicclass Main {
  publicstaticvoid main(String args[]) {
    Direction all[] = Direction.values();
    for (Direction a : all){
      System.out.println(a);
    }
    System.out.println();
    Direction dir = Direction.valueOf("South");
    System.out.println(dir);
  }
}
```

The code above generates the following result.

## Compare enum

The following code shows how to compare enum data type.

```java title=Example.java
enum Week {
  Monday, Tuesday, Wednesday, Thursday, Friday, Saturaday, Sunday
}
publicclass Main {
  publicstaticvoid main(String args[]) {
    Week day1, day2, day3;
    day1 = Week.Monday;
    day2 = Week.Tuesday;
    day3 = Week.Friday;
    //
if (day1.compareTo(day2) < 0)
      System.out.println(day1 + " comes before " + day2);
    if (day2.compareTo(day3) > 0)
      System.out.println(day2 + " comes before " + day3);
    if (day1.compareTo(day3) == 0)
      System.out.println(day1 + " equals " + day3);
  }
}
```

The code above generates the following result.

- « Previous
