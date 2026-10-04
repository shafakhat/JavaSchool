---
title: Reading Output from a Command
nav: Reading Output from a Comm...
description: Imported from the java2s.com archive: Reading Output from a Command
section: Imported - java2s Archive
order: 1810
source: https://web.archive.org/web/20140829085658/http://www.java2s.com/Tutorial/Java/0120__Development/ReadingOutputfromaCommand.htm
---
```java title=Example.java
import java.io.InputStream;
public class Main {
  public static void main(String[] argv) throws Exception {
    String command = "ls";
    Process child = Runtime.getRuntime().exec(command);
    InputStream in = child.getInputStream();
    int c;
    while ((c = in.read()) != -1) {
      System.out.println(((char) c));
    }
    in.close();
  }
}
```

| 6.27.1. | Reading Output from a Command |
|---|---|
| 6.27.2. | Sending Input to a Command |
| 6.27.3. | Execute external command and obtain the result |
| 6.27.4. | Helper method to execute shell command |
