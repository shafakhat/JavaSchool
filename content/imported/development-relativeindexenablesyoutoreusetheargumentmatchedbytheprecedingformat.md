---
title: Relative index enables you to reuse the argument matched by the preceding format specifier
nav: Relative index enables you...
description: Imported from the java2s.com archive: Relative index enables you to reuse the argument matched by the preceding format specifier
section: Imported - java2s Archive
order: 1525
source: https://web.archive.org/web/20140829082814/http://www.java2s.com/Tutorial/Java/0120__Development/Relativeindexenablesyoutoreusetheargumentmatchedbytheprecedingformatspecifier.htm
---
Simply specify < for the argument index.

```java title=Example.java
import java.util.Formatter;
public class MainClass {
  public static void main(String args[]) {
    Formatter fmt = new Formatter();
    fmt.format("%d in hex is %<x", 255);
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
