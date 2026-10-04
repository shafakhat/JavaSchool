---
title: Demonstrates the pitfalls of depending on the order of static initializers
nav: Demonstrates the pitfalls ...
description: * This software is granted under the terms of the Common Public License,
section: Imported - java2s Archive
order: 1262
source: https://web.archive.org/web/20140829084058/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Demonstratesthepitfallsofdependingontheorderofstaticinitializers.htm
---
```java title=Example.java
/*
 *     file: StaticOrderDemo.java
 *  package: oreilly.hcj.review
 *
 * This software is granted under the terms of the Common Public License,
 * CPL, which may be found at the following URL:
 * http://www-124.ibm.com/developerworks/oss/CPLv1.0.htm
 *
 * Copyright(c) 2003-2005 by the authors indicated in the @author tags.
 * All Rights are Reserved by the various authors.
 *
########## DO NOT EDIT ABOVE THIS LINE ########## */
import java.util.Arrays;
/**
 *
 * @author <a href=mailto:kraythe@arcor.de>Robert Simmons jr. (kraythe)</a>
 * @version $Revision: 1.3 $
 */
public class StaticOrderDemo {
  static {
    Class cl = Values.class;
    System.out.println("Class " + cl.getName() + " Loaded");
  }
  /**
   * Creates a new instance of StaticOrderDemo
   */
  public StaticOrderDemo() {
  }
  /**
   * The main demo method.  Used only to start the virtual machine.
   *
   * @param args Arguments passed.
   */
  public static final void main(final String[] args) {
  }
  // --- Inner Classes --
  /**
   * Holds ranges for the values.
   *
   * @author <a href=mailto:kraythe@arcor.de>Robert Simmons jr. (kraythe)</a>
   * @version $Revision: 1.3 $
   */
  public static class Ranges {
    /** Bluw range */
    public static final String[] RANGE_BLUE = { "Sky", "Navy" };
    /** Red range */
    public static final String[] RANGE_RED = { "Light", "Dark" };
    static {
      System.out.println("static{} method for Ranges");
      System.out.println(Arrays.asList(RANGE_BLUE));
      System.out.println(Values.VALUE_SPECIFIER);
      System.out.println(Arrays.asList(RANGE_RED));
    }
  }
  /**
   * Holds values.
   *
   * @author <a href=mailto:kraythe@arcor.de>Robert Simmons jr. (kraythe)</a>
   * @version $Revision: 1.3 $
   */
  public static class Values {
    /** A value holder */
    public static final String VALUE = "Blue";
    /** A specifier for the value */
    public static final String VALUE_SPECIFIER;
    static {
      System.out.println("static{} method for Values");
      System.out.println(VALUE);
      System.out.println(Ranges.RANGE_BLUE);
      VALUE_SPECIFIER = Ranges.RANGE_BLUE[1];
    }
  }
}
/* ########## End of File ########## */
```
