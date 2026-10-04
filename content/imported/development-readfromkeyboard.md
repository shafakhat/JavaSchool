---
title: Read from keyboard
nav: Read from keyboard
description: Imported from the java2s.com archive: Read from keyboard
section: Imported - java2s Archive
order: 1200
source: https://web.archive.org/web/20140829084149/http://www.java2s.com/Tutorial/Java/0120__Development/Readfromkeyboard.htm
---
```java title=Example.java
import java.io.IOException;
public class MainClass {
  public static void main(String[] args) {
    try {
      while (true) {
        int datum = System.in.read();
        if (datum == -1)
          break;
        System.out.println(datum);
      }
    } catch (IOException ex) {
      System.err.println("Couldn't read from System.in!");
    }
  }
}
```

| 6.3.1. | How to read from standard input |
|---|---|
| 6.3.2. | Read from keyboard |
| 6.3.3. | Getting Data From the Keyboard |
| 6.3.4. | Tokenizing a Stream from console input |
| 6.3.5. | Read password from console |
