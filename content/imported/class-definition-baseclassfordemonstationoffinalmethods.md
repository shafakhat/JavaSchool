---
title: Base class for demonstation of final methods
nav: Base class for demonstatio...
description: * This software is granted under the terms of the Common Public License,
section: Imported - java2s Archive
order: 1154
source: https://web.archive.org/web/2014/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Baseclassfordemonstationoffinalmethods.htm
---
```java title=Example.java
/*
 *     file: FinalMethod.java
 *  package: oreilly.hcj.finalstory
 *
 * This software is granted under the terms of the Common Public License,
 * CPL, which may be found at the following URL:
 * http://www-124.ibm.com/developerworks/oss/CPLv1.0.htm
 *
 * Copyright(c) 2003-2005 by the authors indicated in the @author tags.
 * All Rights are Reserved by the various authors.
 *
########## DO NOT EDIT ABOVE THIS LINE ########## *//**
 *
 * @author <a href=mailto:kraythe@arcor.de>Robert Simmons jr. (kraythe)</a>
 * @version $Revision: 1.3 $
 */public class FinalMethod {
  /** A demo property. */ private final String name;
  /**
   * Creates a new FinalMethodBase object.
   *
   * @param name The name to use.
   */ protected FinalMethod(final String name) {
    this.name = name;
  }
  /**
   * Gets the value of the property name.
   *
   * @return The current name.
   */ public final String getName() {
    return this.name;
  }
  /**
   * A demo method.
   */ public final void someMethod() {
  }
}
/* ########## End of File ########## */
```

| 5.27.1. | final Variables |
|---|---|
| 5.27.2. | 'Blank' final fields |
| 5.27.3. | Java Final variable: Once created and initialized, its value can not be changed |
| 5.27.4. | Using 'final' with method arguments |
| 5.27.5. | The effect of final on fields |
| 5.27.6. | You can override a private or private final method |
| 5.27.7. | Making an entire class final |
| 5.27.8. | Demonstrates how final variables are replaced at compilation time |
| 5.27.9. | Demonstration of final class members |
| 5.27.10. | Base class for demonstation of final methods |
| 5.27.11. | Demonstration of final constants |
| 5.27.12. | Demonstration of final variables |
