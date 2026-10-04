---
title: The 'in' field represents the standard input stream
nav: The 'in' field represents ...
description: Imported from the java2s.com archive: The 'in' field represents the standard input stream
section: Imported - java2s Archive
order: 1161
source: https://web.archive.org/web/20140829091702/http://www.java2s.com/Tutorial/Java/0120__Development/Theinfieldrepresentsthestandardinputstream.htm
---
You can use it to accept user keyboard input.

```java title=Example.java
import java.io.IOException;
public class MainClass {
  public static void main(String[] args) {
    try {
      char c = (char) System.in.read();
      while (c != '\r') {
        System.out.println(c);
        c = (char) System.in.read();
      }
    } catch (IOException e) {
    }
  }
}
```

| 6.1.1. | java.lang.System |
|---|---|
| 6.1.2. | PrintStream has many print method overloads that accept different types |
| 6.1.3. | println adds a line terminator at the end of the argument |
| 6.1.4. | The err field represents a PrintStream object |
| 6.1.5. | The 'in' field represents the standard input stream |
| 6.1.6. | Array copy method |
| 6.1.7. | Terminates the running program and the current JVM |
| 6.1.8. | Returns the computer time in milliseconds |
| 6.1.9. | public static long nanoTime(): provide more precision, i.e. in nanoseconds |
| 6.1.10. | Using System.getProperty(String key) to retrieve system properties |
| 6.1.11. | Get Name of User Currently Logged In to the Computer |
| 6.1.12. | Create a user-defined property or change the value of the current property |
| 6.1.13. | Returns a default value if the specified property does not exist |
| 6.1.14. | Returns all system properties |
| 6.1.15. | Exiting a Java program |
| 6.1.16. | Terminate virtual machine using System class |
| 6.1.17. | Redirect the output of System.out to a file. |
| 6.1.18. | Calculate process elapsed time |
