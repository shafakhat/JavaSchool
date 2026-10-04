---
title: Printing text with the Console class
nav: Printing text with the Con...
description: Imported from the java2s.com archive: Printing text with the Console class
section: Imported - java2s Archive
order: 1947
source: https://web.archive.org/web/20140829074645/http://www.java2s.com/Tutorial/Java/0120__Development/PrintingtextwiththeConsoleclass.htm
---
```java title=Example.java
import java.io.Console;
public class Main {
  public static void main(String[] args) {
    Console console = System.console();
    console.printf("%s%n", "this is a test");
  }
}
```

| 6.45.1. | Console based login |
|---|---|
| 6.45.2. | Printing text with the Console class |
| 6.45.3. | Masking a password with the Console class |
| 6.45.4. | Use Console class to read user input? |
| 6.45.5. | Console.ReadLine |
