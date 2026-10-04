---
title: From Runtime.exec() to ProcessBuilder
nav: From Runtime.exec() to Pro...
description: System.out.printf("Output of running %s is:", Arrays.toString(args));
section: Imported - java2s Archive
order: 1964
source: https://web.archive.org/web/20140829091259/http://www.java2s.com/Tutorial/Java/0120__Development/FromRuntimeexectoProcessBuilder.htm
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

| 6.47.1. | Milliseconds elapsed since January 1, 1970 |
|---|---|
| 6.47.2. | Demonstrate totalMemory(), freeMemory() and gc(). |
| 6.47.3. | Demonstrate exec(). |
| 6.47.4. | Wait until notepad is terminated. |
| 6.47.5. | Timing program execution. |
| 6.47.6. | Using arraycopy(). |
| 6.47.7. | Display the total amount of memory in the Java virtual machine. |
| 6.47.8. | Display the maximum amount of memory |
| 6.47.9. | Display the amount of free memory in the Java Virtual Machine. |
| 6.47.10. | Get Number of Available Processors |
| 6.47.11. | System.getProperty |
| 6.47.12. | Execute system command |
| 6.47.13. | Determine when the application is about to exit |
| 6.47.14. | Execute a command from code |
| 6.47.15. | Execute a command with more than one argument |
| 6.47.16. | Launch a Unix script with Java |
| 6.47.17. | Read output from a Command execution |
| 6.47.18. | Send an Input to a Command |
| 6.47.19. | From Runtime.exec() to ProcessBuilder |
| 6.47.20. | Registering Shutdown Hooks for Virtual Machine |
