---
title: Getting Data From the Keyboard
nav: Getting Data From the Keyb...
description: StreamTokenizer tf = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
section: Imported - java2s Archive
order: 1201
source: https://web.archive.org/web/20140829084401/http://www.java2s.com/Tutorial/Java/0120__Development/GettingDataFromtheKeyboard.htm
---
```java title=Example.java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
public class MainClass {
  public static void main(String[] av) throws IOException {
    StreamTokenizer tf = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
    String s = null;
    int i;
    while ((i = tf.nextToken()) != StreamTokenizer.TT_EOF) {
      switch (i) {
      case StreamTokenizer.TT_EOF:
        System.out.println("End of file");
        break;
      case StreamTokenizer.TT_EOL:
        System.out.println("End of line");
        break;
      case StreamTokenizer.TT_NUMBER:
        System.out.println("Number " + tf.nval);
        break;
      case StreamTokenizer.TT_WORD:
        System.out.println("Word, length " + tf.sval.length() + "->" + tf.sval);
        break;
      default:
        System.out.println("What is it? i = " + i);
      }
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
