---
title: Catching multiple exception types to improve type checking
nav: Catching multiple exceptio...
description: 1. Catching Multiple Exception Types To Improve Type Handling
section: Imported - java2s Archive
order: 1005
source: https://web.archive.org/web/20130313051853/http://www.java2s.com:80/Code/Java/JDK-7/Catchingmultipleexceptiontypestoimprovetypechecking.htm
---
Catching multiple exception types to improve type checking

```java title=Example.java
import java.util.InputMismatchException;
import java.util.Scanner;
public class Test {
  public static void main(String[] args) {
    try {
      System.out.print("Enter a number: ");
      int number = new Scanner(System.in).nextInt();
      if (number < 0) {
        throw new InvalidParameter();
      }
      System.out.println("The number is: " + number);
    } catch (InputMismatchException | InvalidParameter e) {
      System.out.println("Invalid input, try again");
    }
  }
}
class InvalidParameter extends java.lang.Exception {
  public InvalidParameter() {
    super("Invalid Parameter");
  }
}
```

1.  Catching Multiple Exception Types To Improve Type Handling
