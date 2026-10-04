---
title: Masking a password with the Console class
nav: Masking a password with th...
description: char passwordArray[] = console.readPassword("Enter your secret password: ");
section: Imported
order: 20062
source: http://java2s.com:80/Tutorial/Java/0120__Development/MaskingapasswordwiththeConsoleclass.htm
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
