---
title: Sending Input to a Command
nav: Sending Input to a Command
description: Imported from the java2s.com archive: Sending Input to a Command
section: Imported - java2s Archive
order: 1809
source: https://web.archive.org/web/20140829091731/http://www.java2s.com/Tutorial/Java/0120__Development/SendingInputtoaCommand.htm
---
```java title=Example.java
import java.io.OutputStream;
public class Main {
  public static void main(String[] argv) throws Exception {
    String command = "cat";
    Process child = Runtime.getRuntime().exec(command);
    OutputStream out = child.getOutputStream();
    out.write("some text".getBytes());
    out.close();
  }
}
```

| 6.27.1. | Reading Output from a Command |
|---|---|
| 6.27.2. | Sending Input to a Command |
| 6.27.3. | Execute external command and obtain the result |
| 6.27.4. | Helper method to execute shell command |
