---
title: Use Console class to read user input?
nav: Use Console class to read ...
description: if (username.equals("admin") && String.valueOf(password).equals("secret")) {
section: Imported - java2s Archive
order: 1949
source: https://web.archive.org/web/20140829074830/http://www.java2s.com/Tutorial/Java/0120__Development/UseConsoleclasstoreaduserinput.htm
---
```java title=Example.java
import java.io.Console;
import java.util.Arrays;
public class Main {
  public static void main(String[] args) {
    Console console = System.console();
    String username = console.readLine("Username: ");
    char[] password = console.readPassword("Password: ");
    if (username.equals("admin") && String.valueOf(password).equals("secret")) {
      console.printf("Welcome to Java Application %1$s.\n", username);
      Arrays.fill(password, ' ');
    } else {
      console.printf("Invalid username or password.\n");
    }
  }
}
```

| 6.45.1. | Console based login |
|---|---|
| 6.45.2. | Printing text with the Console class |
| 6.45.3. | Masking a password with the Console class |
| 6.45.4. | Use Console class to read user input? |
| 6.45.5. | Console.ReadLine |
