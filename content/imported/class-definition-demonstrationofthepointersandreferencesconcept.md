---
title: Demonstration of the Pointers and References Concept
nav: Demonstration of the Point...
description: * This software is granted under the terms of the Common Public License,
section: Imported - java2s Archive
order: 1229
source: https://web.archive.org/web/20140829092021/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/DemonstrationofthePointersandReferencesConcept.htm
---
```java title=Example.java
/*
 *     file: PointersAndReferences.java
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
import java.util.Vector;
/**
 *
 * @author <a href=mailto:kraythe@arcor.de>Robert Simmons jr. (kraythe)</a>
 * @version $Revision: 1.3 $
 */
public class PointersAndReferences {
  /**
   * Main method.
   *
   * @param args Command Line arguments.
   */
  public static final void main(final String[] args) {
    Vector source = new Vector();
    source.add("O'Reilly");
    source.add("XML");
    source.add("Java");
    System.out.println("Original Vector");
    System.out.println(source.toString());
    // -- Try the first method.
    someMethod(source);
    System.out.println("After first method.");
    System.out.println(source.toString());
    // -- Try the second method.
    someOtherMethod(source);
    System.out.println("After second method.");
    System.out.println(source.toString());
  }
  /**
   * Try using a vector without changing it.
   *
   * @param source The source Vector.
   */
  public static void someMethod(Vector source) {
    Vector target = source;
    target.add("Swing");
  }
  /**
   * Try using a vector without changing it with final parameter.
   *
   * @param source The source Vector.
   */
  public static void someOtherMethod(final Vector source) {
    Vector target = source;
    target.add("JFC");  // ouch, still changes v.
    // source = new Vector(); // compiler error.
  }
}
/* ########## End of File ########## */
```
