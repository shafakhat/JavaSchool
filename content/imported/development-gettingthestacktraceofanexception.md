---
title: Getting the Stack Trace of an Exception
nav: Getting the Stack Trace of...
description: Imported from the java2s.com archive: Getting the Stack Trace of an Exception
section: Imported - java2s Archive
order: 1783
source: https://web.archive.org/web/20140829075842/http://www.java2s.com/Tutorial/Java/0120__Development/GettingtheStackTraceofanException.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] argv) throws Exception {
    try {
      int x = 1, y = 0;
      System.out.println(x / y);
    } catch (Throwable e) {
      StackTraceElement stack[] = e.getStackTrace();
      for (int i = 0; i < stack.length; i++) {
        String filename = stack[i].getFileName();
        if (filename == null) {
          System.out.println("filename is not available");
        }
        String className = stack[i].getClassName();
        System.out.println(className);
        String methodName = stack[i].getMethodName();
        System.out.println(methodName);
        boolean isNativeMethod = stack[i].isNativeMethod();
        System.out.println(isNativeMethod);
        int line = stack[i].getLineNumber();
        System.out.println(line);
      }
    }
  }
}
```

| 6.23.1. | Error Handling |
|---|---|
| 6.23.2. | Types of Exceptions |
| 6.23.3. | Java's Unchecked RuntimeException Subclasses |
| 6.23.4. | Java's Checked Exceptions Defined in java.lang |
| 6.23.5. | Throwing an Exception from a Method |
| 6.23.6. | Write a catch block that handles java.lang.Exception |
| 6.23.7. | Handling Exceptions |
| 6.23.8. | Multiple catch Blocks |
| 6.23.9. | The finally Block |
| 6.23.10. | Exception Objects: stack trace |
| 6.23.11. | Defining Your Own Exceptions, Throwing Your Own Exception |
| 6.23.12. | Demonstrate exception chaining. |
| 6.23.13. | Getting the Stack Trace of an Exception |
| 6.23.14. | Put printStackTrace() into a String: redirect the StackTrace to a String with a StringWriter/PrintWriter |
| 6.23.15. | Check whether given exception is compatible with the exceptions declared in a throws clause |
| 6.23.16. | Convert an exception to a String with full stack trace |
| 6.23.17. | Get Deepest Throwable |
| 6.23.18. | Get the stack trace of the supplied exception. |
| 6.23.19. | Is Checked Exception |
| 6.23.20. | Locates a particular type of exception |
| 6.23.21. | Make a string representation of the exception |
| 6.23.22. | Print all of the thread's information and stack traces |
| 6.23.23. | Return stack trace from the passed exception as a string |
| 6.23.24. | Returns the root cause of an exception |
| 6.23.25. | Create a new Exception, setting the cause if possible. |
| 6.23.26. | Returns the output of printStackTrace as a String. |
| 6.23.27. | This program creates a custom exception type. |
| 6.23.28. | Utility methods for dealing with stack traces |
