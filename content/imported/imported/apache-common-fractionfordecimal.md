---
title: Fraction for decimal
nav: Fraction for decimal
description: System.err.println(fraction_whole.divideBy(fraction_double));
section: Imported - java2s Archive
order: 1032
source: https://web.archive.org/web/20061018210414/http://www.java2s.com/Code/Java/Apache-Common/Fractionfordecimal.htm
---
Fraction for decimal

```java title=Example.java
import org.apache.commons.lang.math.Fraction;
public class FractionExampleV1 {
  public static void main(String args[]) {
    Fraction twoThirds = Fraction.TWO_THIRDS;
    Fraction fraction_whole  = Fraction.getFraction(2, 2, 3);
    Fraction fraction  = Fraction.getFraction(27, 98);
    Fraction fraction_double = Fraction.getFraction(4.56);
    Fraction fraction_string = Fraction.getFraction("2 1/3");
    System.err.println(twoThirds.doubleValue());
    System.err.println(fraction_string.getNumerator());
    System.err.println(fraction_whole.divideBy(fraction_double));
    System.err.println(fraction.divideBy(fraction));
  }
}
```

Download: BeanUtilsFractionExampleV1.zip ( 1,004 K )
Related examples in the same category
