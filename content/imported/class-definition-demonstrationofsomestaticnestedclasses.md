---
title: Demonstration of some static nested classes
nav: Demonstration of some stat...
description: * This software is granted under the terms of the Common Public License,
section: Imported - java2s Archive
order: 1109
source: https://web.archive.org/web/20140829083704/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Demonstrationofsomestaticnestedclasses.htm
---
```java title=Example.java
/*
 *     file: DoubleNestedClassDemo.java
 *  package: oreilly.hcj.nested
 *
 * This software is granted under the terms of the Common Public License,
 * CPL, which may be found at the following URL:
 * http://www-124.ibm.com/developerworks/oss/CPLv1.0.htm
 *
 * Copyright(c) 2003-2005 by the authors indicated in the @author tags.
 * All Rights are Reserved by the various authors.
 *
########## DO NOT EDIT ABOVE THIS LINE ########## */
/*
 *     file: DoubleNestedClass.java
 *  package: oreilly.hcj.nested
 *
 * This software is granted under the terms of the Common Public License,
 * CPL, which may be found at the following URL:
 * http://www-124.ibm.com/developerworks/oss/CPLv1.0.htm
 *
 * Copyright(c) 2003-2005 by the authors indicated in the @author tags.
 * All Rights are Reserved by the various authors.
 *
########## DO NOT EDIT ABOVE THIS LINE ########## */
/**
 *
 * @author <a href=mailto:kraythe@arcor.de>Robert Simmons jr. (kraythe)</a>
 * @version $Revision: 1.3 $
 */
 class DoubleNestedClass {
  /** Holds the name. */
  private static final String name = "Robert";
  /** Holds the company. */
  private static String company = "O'Reilly";
  /** Holds a value. */
  private int value = 5;
  /**
   * Getter for the property company.
   *
   * @return The current company.
   */
  public static String getCompany() {
    return company;
  }
  /**
   * Getter for the variable name.
   *
   * @return The current name.
   */
  public static String getName() {
    return name;
  }
  /**
   * Getter for the variable company.
   *
   * @return the current company.
   */
  public int getValue() {
    return value;
  }
  /**
   * A demo nested static class.
   *
   * @author <a href=mailto:kraythe@arcor.de>Robert Simmons jr. (kraythe)</a>
   * @version $Revision: 1.3 $
   */
  public static class SomeClass {
    /** Name of the book. */
    private static final String book = "Hardcore Java";
    /**
     * a demo method.
     */
    public void someMethod() {
      System.out.println("In SomeClass.someMethod()");
      System.out.println(company);
      System.out.println(name);
      // System.out.println(value); // <= Compiler error
    }
    /**
     * A demo nested static class.
     *
     * @author <a href=mailto:kraythe@arcor.de>Robert Simmons jr. (kraythe)</a>
     * @version $Revision: 1.3 $
     */
    public static class SomeOtherClass {
      /**
       * a demo method.
       */
      public void someMethod() {
        System.out.println("In SomeOtherClass.someMethod()");
        System.out.println(company);
        System.out.println(book);
      }
    }
  }
}
/* ########## End of File ########## */
/**
 * Demonstrates Static nested Classes.
 *
 * @author <a href=mailto:kraythe@arcor.de>Robert Simmons jr. (kraythe)</a>
 * @version $Revision: 1.3 $
 */
public class DoubleNestedClassDemo {
  /**
   * Main method.
   *
   * @param args Command line arguments.
   */
  public static void main(final String[] args) {
    DoubleNestedClass.SomeClass.SomeOtherClass obj =
      new DoubleNestedClass.SomeClass.SomeOtherClass();
    obj.someMethod();
  }
}
/* ########## End of File ########## */
```

| 5.15.1. | Demonstrate an inner class. |
|---|---|
| 5.15.2. | Define an inner class within a for loop. |
| 5.15.3. | Use anonymous inner classes |
| 5.15.4. | Building the anonymous inner class in-place |
| 5.15.5. | Anonymous inner class cannot have a named constructor, only an instance initializer |
| 5.15.6. | Creating a constructor for an anonymous inner class |
| 5.15.7. | Using 'instance initialization' to perform construction on an anonymous inner class |
| 5.15.8. | Argument must be final to use inside anonymous inner class |
| 5.15.9. | A method that returns an anonymous inner class |
| 5.15.10. | An anonymous inner class that calls the base-class constructor |
| 5.15.11. | An anonymous inner class that performs initialization |
| 5.15.12. | Demonstrates method-scoped inner classes |
| 5.15.13. | Demonstrates anonymous classes |
| 5.15.14. | Demonstration of some static nested classes |
| 5.15.15. | Access inner class from outside |
| 5.15.16. | Accessing its enclosing instance from an inner class |
