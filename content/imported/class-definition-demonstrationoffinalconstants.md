---
title: Demonstration of final constants
nav: Demonstration of final con...
description: * This software is granted under the terms of the Common Public License,
section: Imported - java2s Archive
order: 1143
source: https://web.archive.org/web/20140829085358/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Demonstrationoffinalconstants.htm
---
```java title=Example.java
/*
 *     file: FinalParameters.java
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
/**
 *
 * @author <a href=mailto:kraythe@arcor.de>Robert Simmons jr. (kraythe)</a>
 * @version $Revision: 1.3 $
 */
public class FinalParameters {
  /** Contains a constant for both equations. */
  private static final double M = 9.3;
  /**
   * Calculate the results of an equation.
   *
   * @param inputValue Input to the equation.
   *
   * @return result of the equation.
   */
  public double equation2(double inputValue) {
    final double K = 1.414;
    final double X = 45.0;
    double result = (((Math.pow(inputValue, 3.0d) * K) + X) * M);
    double powInputValue = 0;
    if (result > 360) {
      powInputValue = X * Math.sin(result);
    } else {
      inputValue = K * Math.sin(result);
    }
    result = Math.pow(result, powInputValue);
    if (result > 360) {
      result = result / inputValue;
    }
    return result;
  }
  /**
   * Calculate the results of an equation.
   *
   * @param inputValue Input to the equation.
   *
   * @return result of the equation.
   */
  public double equation2Better(final double inputValue) {
    final double K = 1.414;
    final double X = 45.0;
    double result = (((Math.pow(inputValue, 3.0d) * K) + X) * M);
    double powInputValue = 0;
    if (result > 360) {
      powInputValue = X * Math.sin(result);
    } else {
      // inputValue = K * Math.sin(result); // <= Compiler error
    }
    result = Math.pow(result, powInputValue);
    if (result > 360) {
      result = result / inputValue;
    }
    return result;
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
