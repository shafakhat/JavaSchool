---
title: Demonstrates that all classes descend from the type java.lang.Object
nav: Demonstrates that all clas...
description: * This software is granted under the terms of the Common Public License,
section: Imported - java2s Archive
order: 1226
source: https://web.archive.org/web/20140829090501/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/DemonstratesthatallclassesdescendfromthetypejavalangObject.htm
---
```java title=Example.java
/*
 *     file: ObjectIsGod.java
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
/**
 * Demonstrates that all classes descend from the type <tt>java.lang.Object</tt>.
 *
 * @author <a href=mailto:kraythe@arcor.de>Robert Simmons jr. (kraythe)</a>
 * @version $Revision: 1.3 $
 */
public class ObjectIsGod {
  /**
   * Main Method.
   *
   * @param args Command line arguments.
   */
  public static final void main(final String[] args) {
    System.out.println(SomeClass.class + " --|> " + SomeClass.class.getSuperclass());
    System.out.println(SomeOtherClass.class + " --|> "
                       + SomeOtherClass.class.getSuperclass());
  }
  /**
   * Class with implicit java.lang.Object inheritance.
   */
  public class SomeClass {
  }
  /**
   * Class with explicit java.lang.Object inheritance.
   */
  public class SomeOtherClass extends Object {
  }
}
/* ########## End of File ########## */
```
