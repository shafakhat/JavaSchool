---
title: Using an Argument Index
nav: Using an Argument Index
description: Imported from the java2s.com archive: Using an Argument Index
section: Imported - java2s Archive
order: 1522
source: https://web.archive.org/web/20140829083116/http://www.java2s.com/Tutorial/Java/0120__Development/UsinganArgumentIndex.htm
---
| Normally, format specifiers and arguments are matched in order, from left to right. |
|---|
| However, by using an argument index you can explicitly control which argument a format specifier matches. |
| An argument index immediately follows the % in a format specifier: n$, where n is the index of the desired argument, beginning with 1. |

```java title=Example.java
import java.util.Formatter;
public class MainClass {
  public static void main(String args[]) {
    Formatter fmt = new Formatter();
    fmt.format("%3$d %1$d %2$d", 10, 20, 30);
    System.out.println(fmt);
  }
}
java title=Example.java
30 10 20
```

| 6.11.1. | Using an Argument Index |
|---|---|
| 6.11.2. | Argument indexes enable you to reuse an argument without having to specify it twice |
| 6.11.3. | Relative index enables you to reuse the argument matched by the preceding format specifier |
| 6.11.4. | Relative indexes are especially useful when creating custom time and date formats |
