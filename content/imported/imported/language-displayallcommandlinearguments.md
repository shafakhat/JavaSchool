---
title: Display all command-line arguments.
nav: Display all command-line a...
description: Imported from the java2s.com archive: Display all command-line arguments.
section: Imported - java2s Archive
order: 1002
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0020__Language/Displayallcommandlinearguments.htm
---
```java title=Example.java
class CommandLine {
  publicstaticvoid main(String args[]) {
    for (int i = 0; i < args.length; i++)
      System.out.println("args[" + i + "]: " + args[i]);
  }
}
```
