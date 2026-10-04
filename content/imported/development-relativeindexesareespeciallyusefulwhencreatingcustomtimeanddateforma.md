---
title: Relative indexes are especially useful when creating custom time and date formats
nav: Relative indexes are espec...
description: Because of relative indexing, the argument cal need only be passed once, rather than three times.
section: Imported - java2s Archive
order: 1534
source: https://web.archive.org/web/20140829085113/http://www.java2s.com/Tutorial/Java/0120__Development/Relativeindexesareespeciallyusefulwhencreatingcustomtimeanddateformats.htm
---
Because of relative indexing, the argument cal need only be passed once, rather than three times.

```java title=Example.java
import java.util.Calendar;
import java.util.Formatter;
public class MainClass {
  public static void main(String args[]) {
    Formatter fmt = new Formatter();
    Calendar cal = Calendar.getInstance();
    fmt.format("Today is day %te of %<tB, %<tY", cal);
    System.out.println(fmt);
  }
}
java title=Example.java
Today is day 1 of December, 2006
```

| 6.11.1. | Using an Argument Index |
|---|---|
| 6.11.2. | Argument indexes enable you to reuse an argument without having to specify it twice |
| 6.11.3. | Relative index enables you to reuse the argument matched by the preceding format specifier |
| 6.11.4. | Relative indexes are especially useful when creating custom time and date formats |
