---
title: an example of a simple anonymous class
nav: an example of a simple ano...
description: Imported from the java2s.com archive: an example of a simple anonymous class
section: Imported - java2s Archive
order: 1130
source: https://web.archive.org/web/20090530094024/http://www.java2s.com:80/Code/Java/Class/anexampleofasimpleanonymousclass.htm
---
an example of a simple anonymous class

```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    Ball b = new Ball() {
      public void hit() {
        System.out.println("You hit it!");
      }
    };
    b.hit();
  }
  interface Ball {
    void hit();
  }
}
```

1.  Tick Tock with an Anonymous Class
---  ---
2.  Access inner class from outside
3.  Anonymous inner class
