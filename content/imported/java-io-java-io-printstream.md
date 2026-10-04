---
title: Java IO Tutorial - Java PrintStream
nav: Java IO Tutorial - Java Pr...
description: The PrintStream class is a concrete decorator for the output stream.
section: Imported - java2s Archive
order: 1011
source: https://web.archive.org/web/2016/https://www.java2s.com/Tutorials/Java/Java_io/0240__Java_io_PrintStream.html
---
The PrintStream class is a concrete decorator for the output stream.

PrintStream can print any data type values, primitive or object, in a suitable format for printing.

PrintStream can write data to the output stream do not throw an IOException.

If a method throws an IOException, PrintStream sets an internal flag, rather than throwing the exception to the caller. The flag can be checked using its checkError() method, which returns true if an IOException occurs during the method execution.

PrintStream has an auto-flush capability. We can specify in its constructor that it should flush the contents written to it automatically.

If we set the auto-flush flag to true, PrintStream will flush its contents when a byte array is written, one of its overloaded println() methods is used to write data, a newline character is written, or a byte ('\n') is written.

```java title=Example.java
import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintStream;
public class Main {
  public static void main(String[] args) {
    String destFile = "luci3.txt";
    try (PrintStream ps = new PrintStream(destFile)) {
      ps.println("test");
      ps.println("test1");
      ps.println("test2");
      ps.print("test3");
      // flush the print stream
      ps.flush();
      System.out.println("Text has  been  written to "
          + (new File(destFile).getAbsolutePath()));
    } catch (FileNotFoundException e1) {
      e1.printStackTrace();
    }
  }
}
```

The code above generates the following result.

- « Previous
