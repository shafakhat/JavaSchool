---
title: Execute a command with more than one argument
nav: Execute a command with mor...
description: String[] commands = new String[] { "grep", "hello world", "/tmp/f.txt" };
section: Imported - java2s Archive
order: 1008
source: https://web.archive.org/web/20101102173143/http://www.java2s.com:80/Tutorial/Java/0120__Development/Executeacommandwithmorethanoneargument.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] argv) throws Exception {
    // Execute a command with an argument that contains a space
    String[] commands = new String[] { "grep", "hello world", "/tmp/f.txt" };
    commands = new String[] { "grep", "hello world", "c:\\f.txt" };
    Process child = Runtime.getRuntime().exec(commands);
  }
}
```
