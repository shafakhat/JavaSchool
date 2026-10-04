---
title: From Runtime.exec() to ProcessBuilder
nav: From Runtime.exec() to Pro...
description: System.out.printf("Output of running %s is:", Arrays.toString(args));
section: Imported
order: 20024
source: http://www.java2s.com:80/Tutorial/Java/0120__Development/FromRuntimeexectoProcessBuilder.htm
---
```java title=Example.java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.Arrays;
public class Main {
  public static void main(String args[]) throws IOException {
    Runtime runtime = Runtime.getRuntime();
    Process process = runtime.exec(args);
    InputStream is = process.getInputStream();
    InputStreamReader isr = new InputStreamReader(is);
    BufferedReader br = new BufferedReader(isr);
    String line;
    System.out.printf("Output of running %s is:", Arrays.toString(args));
    while ((line = br.readLine()) != null) {
      System.out.println(line);
    }
  }
}
```
