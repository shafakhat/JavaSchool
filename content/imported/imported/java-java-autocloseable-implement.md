---
title: Java AutoCloseable implement
nav: Java AutoCloseable implement
description: Imported from java2s.com: Java AutoCloseable implement
section: Imported
order: 20049
source: http://www.java2s.com/ref/java/java-autocloseable-implement.html
---
- java.lang
- java.lang AutoCloseable Boolean Character Class Cloneable Comparable Double Exception Float Integer Iterable Long Math ModuleLayer Package Process ProcessBuilder ProcessHandle Runtime Runtime Version String StringBuffer StringBuilder System Thread ThreadGroup ThreadLocal

## Description

Java AutoCloseable implement

```java title=Example.java
class MyResource implementsAutoCloseable {
  publicvoid close() {
    System.out.println("In MyResource?s close()");
  }//fromwww.java2s.com
}

publicclass Main {
  publicstaticvoid main(String args[]) throwsException {
    try (MyResource mr = new MyResource()) {
      // ...
    } finally {
      System.out.println("In finally");
    }
  }
}
```

PreviousNext

## Related

- Java StringReader create from String
- Java Writer create from OutputStream using "US-ASCII" encoding
- Java Writer create from OutputStream using system default encoding
- Java AutoCloseable throw exception in close() method
- Java Boolean class
