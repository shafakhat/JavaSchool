---
title: How to read from standard input
nav: How to read from standard ...
description: BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
section: Imported - java2s Archive
order: 1202
source: https://web.archive.org/web/20140829084840/http://www.java2s.com/Tutorial/Java/0120__Development/Howtoreadfromstandardinput.htm
---
```java title=Example.java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class MainClass {
  public static void main(String[] args) throws IOException {
    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    String s;
    while ((s = in.readLine()) != null && s.length() != 0)
      System.out.println(s);
    // An empty line or Ctrl-Z terminates the program
  }
}
```

| 6.3.1. | How to read from standard input |
|---|---|
| 6.3.2. | Read from keyboard |
| 6.3.3. | Getting Data From the Keyboard |
| 6.3.4. | Tokenizing a Stream from console input |
| 6.3.5. | Read password from console |
