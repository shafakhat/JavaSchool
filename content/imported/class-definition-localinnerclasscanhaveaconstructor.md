---
title: Local inner class can have a constructor
nav: Local inner class can have...
description: Imported from the java2s.com archive: Local inner class can have a constructor
section: Imported - java2s Archive
order: 1278
source: https://web.archive.org/web/20140829090834/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Localinnerclasscanhaveaconstructor.htm
---
```java title=Example.java
interface Counter {
  int next();
}
public class MainClass{
  private int count = 0;
  Counter getCounter(final String name) {
    // A local inner class:
    class LocalCounter implements Counter {
      public LocalCounter() {
        System.out.println("LocalCounter()");
      }
      public int next() {
        System.out.print(name); // Access local final
        return count++;
      }
    }
    return new LocalCounter();
  }
  public static void main(String[] args) {
    MainClass lic = new MainClass();
    Counter c1 = lic.getCounter("Local inner ");
  }
}
```
