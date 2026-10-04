---
title: Execute a command from code
nav: Execute a command from code
description: Imported from the java2s.com archive: Execute a command from code
section: Imported - java2s Archive
order: 1007
source: https://web.archive.org/web/20101102173912/http://www.java2s.com:80/Tutorial/Java/0120__Development/Executeacommandfromcode.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] argv) throws Exception {
    // Execute a command without arguments
    String command = "ls";
    Process child = Runtime.getRuntime().exec(command);
    // Execute a command with an argument
    command = "ls /tmp";
    child = Runtime.getRuntime().exec(command);
  }
}
```
