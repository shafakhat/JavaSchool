---
title: Argument indexes enable you to reuse an argument without having to specify it twice
nav: Argument indexes enable yo...
description: Imported from the java2s.com archive: Argument indexes enable you to reuse an argument without having to specify it twice
section: Imported - java2s Archive
order: 1524
source: https://web.archive.org/web/20140829083220/http://www.java2s.com/Tutorial/Java/0120__Development/Argumentindexesenableyoutoreuseanargumentwithouthavingtospecifyittwice.htm
---
```java title=Example.java
import java.util.Formatter;
public class MainClass {
  public static void main(String args[]) {
    Formatter fmt = new Formatter();
    fmt.format("%d in hex is %1$x", 255);
    System.out.println(fmt);
  }
}
java title=Example.java
255 in hex is ff
```

| 6.11.1. | Using an Argument Index |
|---|---|
| 6.11.2. | Argument indexes enable you to reuse an argument without having to specify it twice |
| 6.11.3. | Relative index enables you to reuse the argument matched by the preceding format specifier |
| 6.11.4. | Relative indexes are especially useful when creating custom time and date formats |
