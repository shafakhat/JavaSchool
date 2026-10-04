---
title: Password Prompting with java.io.Console
nav: Password Prompting with ja...
description: char[] passwordEntered = console.readPassword("Enter password: ");
section: Imported - java2s Archive
order: 1952
source: https://web.archive.org/web/2014/http://www.java2s.com/Tutorial/Java/0120__Development/PasswordPromptingwithjavaioConsole.htm
---
```java title=Example.java
import java.io.Console;
import java.util.Arrays;
public class PasswordPromptingDemo {
  public static void main(String[] args) {
    Console console = System.console();
    if (console == null) {
      System.out.println("Console is not available");
      System.exit(1);
    }
    char[] password = "mustang".toCharArray();
    char[] passwordEntered = console.readPassword("Enter password: ");
    if (Arrays.equals(password, passwordEntered)) {
      System.out.println("\n Access granted \n");
      Arrays.fill(password, ' ');
      Arrays.fill(passwordEntered, ' ');
      System.out.println("OK ...");
    } else {
      System.out.println("Access denied");
      System.exit(1);
    }
  }
}
```

| 6.40.1. | Java Console readLine |
|---|---|
| 6.40.2. | Console read Password |
| 6.40.3. | Console output with format |
| 6.40.4. | Password Prompting with java.io.Console |
