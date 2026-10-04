---
title: Redirecting input and output from operating systems processes
nav: Redirecting input and outp...
description: Redirecting input and output from operating systems processes
section: Imported - java2s Archive
order: 1118
source: https://web.archive.org/web/20130821113911/http://java2s.com/Code/Java/JDK-7/Redirectinginputandoutputfromoperatingsystemsprocesses.htm
---
```java title=Example.java
import java.io.File;
public class Test {
  public static void main(String[] args) throws Exception {
    File commands = new File("C:/Projects/ProcessCommands.txt");
    File output = new File("C:/Projects/ProcessLog.txt");
    File errors = new File("C:/Projects/ErrorLog.txt");
    ProcessBuilder pb = new ProcessBuilder("cmd");
    System.out.println(pb.redirectInput().toString());
    System.out.println(pb.redirectOutput().toString());
    System.out.println(pb.redirectError().toString());
    pb.redirectInput(commands);
    pb.redirectError(errors);
    pb.redirectOutput(output);
    System.out.println(pb.redirectInput().toString());
    System.out.println(pb.redirectOutput().toString());
    System.out.println(pb.redirectError().toString());
    pb.start();
  }
}
```

1.  Using the platform MXBeans for a JVM for system and process load monitoring
