---
title: Demonstrates Static nested Classes
nav: Demonstrates Static nested...
description: * This software is granted under the terms of the Common Public License,
section: Imported - java2s Archive
order: 1212
source: https://web.archive.org/web/20140829083734/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/DemonstratesStaticnestedClasses.htm
---
```java title=Example.java
/*
 *     file: StaticNestedClassDemo.java
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
public class StaticNestedClassDemo {
  /**
   * Main method.
   *
   * @param args
   *          Command line arguments.
   */
  public static void main(final String[] args) {
    OuterClass.SomeClass obj = new OuterClass.SomeClass();
    obj.someMethod();
    // OuterClass.SomeOtherClass prot = new OuterClass.SomeOtherClass(); // <=
    // Compiler error
    OuterClass.doPrivate();
  }
}
/* ########## End of File ########## */
/*
 * file: OuterClass.java package: oreilly.hcj.nested
 *
 * This software is granted under the terms of the Common Public License, CPL,
 * which may be found at the following URL:
 * http://www-124.ibm.com/developerworks/oss/CPLv1.0.htm
 *
 * Copyright(c) 2003-2005 by the authors indicated in the @author tags. All
 * Rights are Reserved by the various authors.
 *
 * ########## DO NOT EDIT ABOVE THIS LINE ##########
 */
/**
 * Demonstration of some static nested classes.
 *
 * @author <a href=mailto:kraythe@arcor.de>Robert Simmons jr. (kraythe)</a>
 * @version $Revision: 1.5 $
 */
class OuterClass {
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
   * Demo of instatiation of a private class.
   */
  public static void doPrivate() {
    SomeOtherClass cl = new SomeOtherClass();
    cl.someMethod();
  }
  /**
   * A demo nested static class.
   *
   * @author <a href=mailto:kraythe@arcor.de>Robert Simmons jr. (kraythe)</a>
   * @version $Revision: 1.5 $
   */
  public static class SomeClass {
    /**
     * a demo method.
     */
    public void someMethod() {
      System.out.println(company);
      System.out.println(name);
      // System.out.println(value); // <= Compiler error
    }
  }
  /**
   * A demo nested static class.
   *
   * @author <a href=mailto:kraythe@arcor.de>Robert Simmons jr. (kraythe)</a>
   * @version $Revision: 1.5 $
   */
  protected static class YetAnotherClass {
  }
  /**
   * A demo nested static class.
   *
   * @author <a href=mailto:kraythe@arcor.de>Robert Simmons jr. (kraythe)</a>
   * @version $Revision: 1.5 $
   */
  private static class SomeOtherClass {
    /**
     * a demo method.
     */
    public void someMethod() {
      System.out.println("Protect me!");
    }
  }
}
/* ########## End of File ########## */
```
