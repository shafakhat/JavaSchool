---
title: BufferedWriter and threads : Java examples (example source code) » Threads » File IO Threads
nav: BufferedWriter and threads...
description: BufferedWriter and threads : Java examples (example source code) » Threads » File IO Threads
section: Imported - java2s Archive
order: 1023
source: https://web.archive.org/web/20060513074749/http://www.java2s.com/Code/Java/Threads/BufferedWriterandthreads.htm
---
BufferedWriter and threads

```java title=Example.java
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.PipedReader;
import java.io.PipedWriter;
import java.io.Reader;
import java.io.Writer;
public class PipedCharacters extends Object {
  public static void writeStuff(Writer rawOut) {
    try {
      BufferedWriter out = new BufferedWriter(rawOut);
      String[][] line = { { "Java", "Source", "and", "Support." }};
      for (int i = 0; i < line.length; i++) {
        String[] word = line[i];
        for (int j = 0; j < word.length; j++) {
          out.write(word[j]);
        }
        out.newLine();
      }
      out.flush();
      out.close();
    } catch (IOException x) {
      x.printStackTrace();
    }
  }
  public static void readStuff(Reader rawIn) {
    try {
      BufferedReader in = new BufferedReader(rawIn);
      String line;
      while ((line = in.readLine()) != null) {
        System.out.println("read line: " + line);
      }
      System.out.println("Read all data from the pipe");
    } catch (IOException x) {
      x.printStackTrace();
    }
  }
  public static void main(String[] args) {
    try {
      final PipedWriter out = new PipedWriter();
      final PipedReader in = new PipedReader(out);
      Runnable runA = new Runnable() {
        public void run() {
          writeStuff(out);
        }
      };
      Thread threadA = new Thread(runA, "threadA");
      threadA.start();
      Runnable runB = new Runnable() {
        public void run() {
          readStuff(in);
        }
      };
      Thread threadB = new Thread(runB, "threadB");
      threadB.start();
    } catch (IOException x) {
      x.printStackTrace();
    }
  }
}
```

Related examples in the same category
---
1. Using pipes for inter-thread I/O
2. Output stream and threads
