---
title: Masking a password with the Console class
nav: Masking a password with th...
description: char passwordArray[] = console.readPassword("Enter your secret password: ");
section: Imported - java2s Archive
order: 1948
source: https://web.archive.org/web/20140829075038/http://www.java2s.com/Tutorial/Java/0120__Development/MaskingapasswordwiththeConsoleclass.htm
---
```java title=Example.java
import java.io.Console;
public class Main {
  public static void main(String[] args) {
    Console console = System.console();
    char passwordArray[] = console.readPassword("Enter your secret password: ");
    console.printf("Password entered was: %s%n", new String(passwordArray));
  }
}
```

| 6.45.1. | Console based login |
|---|---|
| 6.45.2. | Printing text with the Console class |
| 6.45.3. | Masking a password with the Console class |
| 6.45.4. | Use Console class to read user input? |
| 6.45.5. | Console.ReadLine |
