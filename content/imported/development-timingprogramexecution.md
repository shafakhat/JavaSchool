---
title: Timing program execution.
nav: Timing program execution.
description: Imported from the java2s.com archive: Timing program execution.
section: Imported - java2s Archive
order: 1955
source: https://web.archive.org/web/20140829091124/http://www.java2s.com/Tutorial/Java/0120__Development/Timingprogramexecution.htm
---
```java title=Example.java
class Elapsed {
  public static void main(String args[]) {
    long start, end;
    System.out.println("Timing a for loop from 0 to 1,000,000");
    start = System.currentTimeMillis(); // get starting time
    for (int i = 0; i < 1000000; i++)
      ;
    end = System.currentTimeMillis(); // get ending time
    System.out.println("Elapsed time: " + (end - start));
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
