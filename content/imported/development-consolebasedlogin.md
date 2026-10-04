---
title: Console based login
nav: Console based login
description: Imported from the java2s.com archive: Console based login
section: Imported - java2s Archive
order: 1022
source: https://web.archive.org/web/20110130081237/http://java2s.com:80/Tutorial/Java/0120__Development/Consolebasedlogin.htm
---
```java title=Example.java
import java.io.Console;
public class Login {
  public static void main(String[] args) throws Exception {
    Console console = System.console();
    String username = console.readLine("Username:");
    char[] pwd = console.readPassword("Password:");
    System.out.println("Username = " + username);
    System.out.println("Password = " + new String(pwd));
    username = "";
    for (int i = 0; i < pwd.length; i++)
      pwd[i] = 0;
  }
}
```
