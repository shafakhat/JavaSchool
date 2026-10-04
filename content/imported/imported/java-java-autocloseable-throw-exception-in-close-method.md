---
title: Java AutoCloseable throw exception in close() method
nav: Java AutoCloseable throw e...
description: try {//www.java2s.comtry (MyResource mr = new MyResource()) {
section: Imported
order: 20044
source: http://www.java2s.com/ref/java/java-autocloseable-throw-exception-in-close-method.html
---
- java.lang
- java.lang AutoCloseable Boolean Character Class Cloneable Comparable Double Exception Float Integer Iterable Long Math ModuleLayer Package Process ProcessBuilder ProcessHandle Runtime Runtime Version String StringBuffer StringBuilder System Thread ThreadGroup ThreadLocal

## Description

Java AutoCloseable throw exception in close() method

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String args[]) throwsException {
    try {//www.java2s.comtry (MyResource mr = new MyResource()) {
        System.out.println("Throwing from try block");
        thrownewException("try block");
      }
    } catch (Exception e) {
      System.out.println(e);
      Throwable[] t = e.getSuppressed();
      System.out.println("Suppressed exception...");
      for (int i = 0; i < t.length; i++)
        System.out.println(t[i]);
    }
  }
}

class MyResource implementsAutoCloseable {
  publicvoid close() throwsException {
    System.out.println("Throwing from close()");
    thrownewException("close()");
  }
}
```

PreviousNext

## Related

- Java Writer create from OutputStream using "US-ASCII" encoding
- Java Writer create from OutputStream using system default encoding
- Java AutoCloseable implement
- Java Boolean class
- Java Character replace space with dot in String
