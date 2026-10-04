---
title: Catching Multiple Exception Types To Improve Type Handling
nav: Catching Multiple Exceptio...
description: throw new AssertionError("Number was too big", new Throwable(
section: Imported - java2s Archive
order: 1006
source: https://web.archive.org/web/20130313054651/http://www.java2s.com:80/Code/Java/JDK-7/CatchingMultipleExceptionTypesToImproveTypeHandling.htm
---
Catching Multiple Exception Types To Improve Type Handling

```java title=Example.java
import java.util.InputMismatchException;
public class Test {
  public static void main(String[] args) {
    try {
      System.out.print("Enter a number: ");
      int number = 100;
      if (number < 0) {
        throw new InvalidParameter();
      }
      if (number > 10) {
        throw new AssertionError("Number was too big", new Throwable(
            "Throwable assertion message"));
      }
    } catch (InputMismatchException | InvalidParameter e) {
      e.addSuppressed(new Throwable());
      System.out.println("Invalid input, try again");
    } catch (final Exception e) {
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

1.  Catching multiple exception types to improve type checking
