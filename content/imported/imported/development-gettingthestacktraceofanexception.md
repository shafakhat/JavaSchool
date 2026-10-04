---
title: Getting the Stack Trace of an Exception
nav: Getting the Stack Trace of...
description: Imported from java2s.com: Getting the Stack Trace of an Exception
section: Imported
order: 20041
source: http://www.java2s.com:80/Tutorial/Java/0120__Development/GettingtheStackTraceofanException.htm
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
