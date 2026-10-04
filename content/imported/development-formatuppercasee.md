---
title: format
nav: format
description: Imported from the java2s.com archive: format
section: Imported - java2s Archive
order: 1508
source: https://web.archive.org/web/20140829081821/http://www.java2s.com/Tutorial/Java/0120__Development/formatuppercaseE.htm
---
```java title=Example.java
import java.util.Formatter;
public class MainClass {
  public static void main(String args[]) {
    Formatter fmt = new Formatter();
    fmt.format("%E", 123.1234);
    System.out.println(fmt);
  }
}
java title=Example.java
1.231234E+02
```

| 6.10.1. | The Uppercase Option |
|---|---|
| 6.10.2. | format: uppercase X |
| 6.10.3. | format: uppercase E |
