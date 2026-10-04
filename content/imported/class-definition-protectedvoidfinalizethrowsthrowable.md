---
title: protected void finalize() throws Throwable
nav: protected void finalize() ...
description: Imported from the java2s.com archive: protected void finalize() throws Throwable
section: Imported - java2s Archive
order: 1152
source: https://web.archive.org/web/20140829080126/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/protectedvoidfinalizethrowsThrowable.htm
---
```java title=Example.java
public class Main {
  private static int id;
  private int myId;
  Main() {
    myId = id++;
    System.out.println("Created #" + myId);
  }
    System.out.println("Finalized #" + myId);
    super.finalize();
  }
  public static void main(String[] args) {
    Main fd;
    for (int i = 0; i < 10000; i++)
      fd = new Main();
  }
}
```

5.33.1.  protected void finalize() throws Throwable
