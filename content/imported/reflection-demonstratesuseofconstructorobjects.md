---
title: Demonstrates use of Constructor objects
nav: Demonstrates use of Constr...
description: * This software is granted under the terms of the Common Public License,
section: Imported - java2s Archive
order: 2069
source: https://web.archive.org/web/20140829083237/http://www.java2s.com/Tutorial/Java/0125__Reflection/DemonstratesuseofConstructorobjects.htm
---
```java title=Example.java
/*
 *     file: ConstructorDemo.java
 *  package: oreilly.hcj.reflection
 *
 * This software is granted under the terms of the Common Public License,
 * CPL, which may be found at the following URL:
 * http://www-124.ibm.com/developerworks/oss/CPLv1.0.htm
 *
 * Copyright(c) 2003-2005 by the authors indicated in the @author tags.
 * All Rights are Reserved by the various authors.
 *
########## DO NOT EDIT ABOVE THIS LINE ########## */
import java.lang.reflect.Constructor;
/**
 *
 * @author <a href=mailto:kraythe@arcor.de>Robert Simmons jr. (kraythe)</a>
 * @version $Revision$
 */
public class ConstructorDemo {
  /**
   * Run the demo.
   *
   * @param args Command line arguments.
   */
  public static void main(final String[] args) {
    try {
      final Class[] ARG_TYPES = new Class[] { String.class };
      Constructor cst = Integer.class.getConstructor(ARG_TYPES);
      System.out.println(cst.newInstance(new Object[] { "45" }));
    } catch (final Exception ex) {
      ex.printStackTrace();
    }
  }
}
/* ########## End of File ########## */
```
