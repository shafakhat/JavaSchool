---
title: Execute system command
nav: Execute system command
description: Imported from the java2s.com archive: Execute system command
section: Imported - java2s Archive
order: 1010
source: https://web.archive.org/web/20101102173918/http://www.java2s.com:80/Tutorial/Java/0120__Development/Executesystemcommand.htm
---
```java title=Example.java
import java.io.IOException;
public class Main {
  public static void main(String[] args) throws IOException {
    String cmd = "cmd.exe /c start ";
    // String file = "c:\\version.txt";
    // String file = "http://www.google.com";
    // String file = "c:\\";
    // String file = "mailto:author@my.com";
    String file = "mailto:";
    Runtime.getRuntime().exec(cmd + file);
  }
}
```
