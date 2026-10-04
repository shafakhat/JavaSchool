---
title: Java Tutorial - How to use Java enum as Class
nav: Java Tutorial - How to use...
description: You can give constructors, add instance variables and methods, and implement interfaces for enum types.
section: Imported - java2s Archive
order: 50464
source: https://www.java2s.com/Tutorials/Java/Java_Language/9010__Java_enum_class.html
---
```java title=Example.java
```

You can give constructors, add instance variables and methods, and implement interfaces for enum types.

When you define a constructor for an enum, the constructor is called when each enumeration constant is created.

Each enumeration constant has its own copy of any instance variables defined by the enumeration.

## Restrictions

Two restrictions that apply to enumerations.

- an enumeration can't inherit another class.
- an enum cannot be a superclass.

Enum with constructor

```java title=Example.java
enum Direction {/*www.java2s.com*/
  South(10), East(9), North(12), West(8);
  privateint myValue;
  Direction(int p) {
    myValue = p;
  }
  int getMyValue() {
    return myValue;
  }
}
publicclass Main {
  publicstaticvoid main(String args[]) {
    System.out.println(Direction.East.getMyValue());
    for (Direction a : Direction.values())
      System.out.println(a + " costs " + a.getMyValue());
  }
}
```

The code above generates the following result.

## Example

You can add fields, constructors, and methods to an enum. You can have the enum implement interfaces.

```java title=Example.java
//fromwww.java2s.comenum Coin {
  PENNY(1), NICKEL(5), DIME(10), QUARTER(25);
  privatefinalint denomValue;
  Coin(int denomValue) {
    this.denomValue = denomValue;
  }
  int denomValue() {
    return denomValue;
  }
  int toDenomination(int numPennies) {
    return numPennies / denomValue;
  }
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    int numPennies = 1;
    int numQuarters = Coin.QUARTER.toDenomination(numPennies);
    System.out.println(numQuarters);
    for (Coin c:Coin.values()) {
      System.out.println(c.denomValue());
    }
  }
}
```

The code above generates the following result.

## Java Enum Inherit Enum

All enum inherit java.lang.Enum. java.lang.Enum's methods are available for use by all enumerations.

## Ordinal value

You can obtain a value that indicates an enumeration constant's position in the list of constants. This is called its ordinal value, and it is retrieved by calling the ordinal() method:

```java title=Example.java
final int ordinal()
```

It returns the ordinal value of the invoking constant. Ordinal values begin at zero.

Enum Ordinal value

```java title=Example.java
enum Direction {/*fromwww.java2s.com*/
  East, South, West, North
}
publicclass Main {
  publicstaticvoid main(String args[]) {
    for (Direction a : Direction.values()){
      System.out.println(a + " " + a.ordinal());
    }
  }
}
```

The code above generates the following result.

## Example 2

Overriding toString() to return a Token constant's value.

```java title=Example.java
enum Token {/*www.java2s.com*/
  IDENTIFIER("ID"), INTEGER("INT"), LPAREN("("), RPAREN(")"), COMMA(",");
  privatefinal String tokValue;
  Token(String tokValue) {
    this.tokValue = tokValue;
  }
  @Override
  public String toString() {
    return tokValue;
  }
}
publicclass Main{
  publicstaticvoid main(String[] args) {
    for (Token t:Token.values()){
      System.out.println(t);
    }
  }
}
```

The code above generates the following result.

## Java Enum compareTo

You can compare the ordinal value of two constants of the same enumeration by using the compareTo() method.

```java title=Example.java
final int compareTo(enum-type e)
```

enum-type is the type of the enumeration, and e is the constant being compared to the invoking constant.

If the two ordinal values are the same, then zero is returned. If the invoking constant has an ordinal value greater than e's, then a positive value is returned.

Compare the ordinal value of two constants of enum

```java title=Example.java
enum Direction {/*fromwww.java2s.com*/
  East, South, West, North
}
publicclass Main {
  publicstaticvoid main(String args[]) {
    Direction ap = Direction.West;
    Direction ap2 = Direction.South;
    Direction ap3 = Direction.West;
    if (ap.compareTo(ap2) < 0){
      System.out.println(ap + " comes before " + ap2);
    }
    if (ap.compareTo(ap2) > 0){
      System.out.println(ap2 + " comes before " + ap);
    }
    if (ap.compareTo(ap3) == 0){
      System.out.println(ap + " equals " + ap3);
    }
  }
}
```

The code above generates the following result.

## Java Enum equals

You can compare for equality an enumeration constant with any other object by using equals(). Those two objects will only be equal if they both refer to the same constant, within the same enumeration.

Compare for equality an enumeration constant with any other object.

```java title=Example.java
enum Direction {/*fromwww.java2s.com*/
  East, South, West, North
}
publicclass Main {
  publicstaticvoid main(String args[]) {
    Direction ap = Direction.West;
    Direction ap2 = Direction.South;
    Direction ap3 = Direction.West;
    if (ap.equals(ap2)){
      System.out.println("Error!");
    }
    if (ap.equals(ap3)){
      System.out.println(ap + " equals " + ap3);
    }
    if (ap == ap3){
      System.out.println(ap + " == " + ap3);
    }
  }
}
```

The code above generates the following result.

## Java Enum Behaviour

We can define enum value with different behaviours by implementing abstract method differently.

We can assign different value for each constant in an enum.

```java title=Example.java
enum Converter {//www.java2s.com
  DollarToEuro("Dollar to Euro") {
    @Override
    double convert(double value) {
      return value * 0.9;
    }
  },
  DollarToPound("Dollar to Pound") {
    @Override
    double convert(double value) {
      return value * .8;
    }
  };
  Converter(String desc) {
    this.desc = desc;
  }
  private String desc;
  @Override
  public String toString() {
    return desc;
  }
  abstractdouble convert(double value);
}
publicclass Main{
  publicstaticvoid main(String[] args) {
    System.out.println(Converter.DollarToEuro + " = " + Converter.DollarToEuro.convert(100.0));
    System.out.println(Converter.DollarToPound + " = " + Converter.DollarToPound.convert(98.6));
  }
}
```

The code above generates the following result.

## Implement interface for enum type

The following code shows how to implement interface for enum type.

```java title=Example.java
/*fromwww.java2s.com*/publicclass Main {
  publicstaticvoid main(String[] args) {
    Size[] sizes = Size.values();
    for (Size s : sizes) {
      System.out.println(s);
    }
  }
}
enum Size implements Countable {
  S, M, L, XL, XXL, XXXL;
  @Deprecated
  public Size increase() {
    Size sizes[] = this.values();
    int pos = this.ordinal();
    if (pos < sizes.length - 1)
      pos++;
    return sizes[pos];
  }
}
interface Countable {
  public Size increase();
}
```

The code above generates the following result.

- « Previous
