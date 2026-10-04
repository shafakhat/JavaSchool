---
title: A synchronized collection with Collections.synchronizedCollection
nav: A synchronized collection ...
description: Collection<String> syncCol = Collections.synchronizedCollection(tsStr);
section: Imported - java2s Archive
order: 1004
source: https://web.archive.org/web/20100615010215/http://www.java2s.com:80/Tutorial/Java/0160__Thread/AsynchronizedcollectionwithCollectionssynchronizedCollection.htm
---
```java title=Example.java
import java.util.Collection;
import java.util.Collections;
import java.util.Set;
import java.util.TreeSet;
class MyThread implements Runnable {
  Thread t;
  Collection<String> col;
  MyThread(Collection<String> c) {
    col = c;
    t = new Thread(this, "MyThread");
    t.start();
  }
  public void run() {
    try {
      Thread.sleep(100);
      col.add("D");
      synchronized (col) {
        for (String str : col) {
          System.out.println("MyThread: " + str);
          Thread.sleep(50);
        }
      }
    } catch (Exception exc) {
      exc.printStackTrace();
    }
  }
}
public class Main {
  public static void main(String args[]) throws Exception {
    Set<String> tsStr = new TreeSet<String>();
    Collection<String> syncCol = Collections.synchronizedCollection(tsStr);
    syncCol.add("A");
    syncCol.add("B");
    syncCol.add("C");
    new MyThread(syncCol);
    synchronized (syncCol) {
      for (String str : syncCol) {
        System.out.println("Main thread: " + str);
        Thread.sleep(500);
      }
    }
  }
}
```
