---
title: Using a Thread-Local Variable
nav: Using a Thread-Local Varia...
description: Imported from the java2s.com archive: Using a Thread-Local Variable
section: Imported - java2s Archive
order: 1023
source: https://web.archive.org/web/20111106223530/http://java2s.com/Tutorial/Java/0160__Thread/UsingaThreadLocalVariable.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] argv) throws Exception {
    ThreadLocal localThread = new ThreadLocal();
    Object o = localThread.get();
    localThread.set(o);
  }
}
```
