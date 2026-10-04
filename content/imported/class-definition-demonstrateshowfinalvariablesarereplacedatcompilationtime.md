---
title: Demonstrates how final variables are replaced at compilation time
nav: Demonstrates how final var...
description: * This software is granted under the terms of the Common Public License,
section: Imported - java2s Archive
order: 1139
source: https://web.archive.org/web/20140829091548/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Demonstrateshowfinalvariablesarereplacedatcompilationtime.htm
---
```java title=Example.java
/*
 *     file: ExternalUser.java
 *  package: oreilly.hcj.finalstory
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
 *     file: FinalReplacement.java
 *  package: oreilly.hcj.finalstory
 *
 * This software is granted under the terms of the Common Public License,
 * CPL, which may be found at the following URL:
 * http://www-124.ibm.com/developerworks/oss/CPLv1.0.htm
 *
 * Copyright(c) 2003-2005 by the authors indicated in the @author tags.
 * All Rights are Reserved by the various authors.
 *
########## DO NOT EDIT ABOVE THIS LINE ########## */
import java.awt.Color;
/**
 *
 * @author <a href=mailto:kraythe@arcor.de>Robert Simmons jr. (kraythe)</a>
 * @version $Revision: 1.3 $
 */
 class FinalReplacement {
  /** A string constant */
  public static final String A_STRING = "Java Hardcore";
  /** An int constant. */
  public static final int AN_INT = 5;
  /** A double constant. */
  public static final double A_DOUBLE = 102.55d;
  /** An array constant. */
  public static final int[] AN_ARRAY = new int[] { 1, 2, 3, 6, 9, 18, 36 };
  /** A color constant. */
  public static final Color A_COLOR = new Color(45, 0, 155);
  /**
   * A demonstration method.
   */
  public void someMethod() {
    System.out.println(A_STRING);
    System.out.println(AN_INT);
    System.out.println(A_DOUBLE);
    System.out.println(AN_ARRAY);
    System.out.println(A_COLOR);
  }
}
/* ########## End of File ########## */
/**
 * Demonstrates what happens with final replacement.
 *
 * @author <a href=mailto:kraythe@arcor.de>Robert Simmons jr. (kraythe)</a>
 * @version $Revision: 1.3 $
 */
public class ExternalUser {
  /**
   * Demo method.
   *
   * @param args Command line arguments.
   */
  public static void main(String[] args) {
    System.out.println("The title of the book is: " + FinalReplacement.A_STRING + ".");
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
