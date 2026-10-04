---
title: Handle concurrent read/write
nav: Handle concurrent read/write
description: Imported from the java2s.com archive: Handle concurrent read/write
section: Imported - java2s Archive
order: 1010
source: https://web.archive.org/web/20100615010220/http://www.java2s.com:80/Tutorial/Java/0160__Thread/Handleconcurrentreadwriteusesynchronizedtolockthedata.htm
---
```java title=Example.java
import java.util.Iterator;
import java.util.Vector;
public class Main {
  public static void main(String[] args) throws Exception {
    Vector data = new Vector();
    new Producer(data).start();
    new Consumer(data).start();
  }
}
class Producer extends Thread {
  Vector data;
  Producer(Vector data) {
    super("Producer");
    this.data = data;
  }
  public void run() {
    while (true) {
      data.addElement(new Object());
      if (data.size() > 1000)
        data.removeAllElements();
    }
  }
}
class Consumer extends Thread {
  Vector data;
  Consumer(Vector data) {
    super("Consumer");
    this.data = data;
  }
  public void run() {
    while (true) {
      synchronized (data) {
        Iterator it = data.iterator();
        while (it.hasNext())
          it.next();
      }
    }
  }
}
```
