---
title: Use CopyOnWriteArrayList
nav: Use CopyOnWriteArrayList
description: CopyOnWriteArrayList<String> list = new CopyOnWriteArrayList<String>();
section: Imported - java2s Archive
order: 1134
source: https://web.archive.org/web/20130501011225/http://java2s.com:80/Code/Java/JDK-7/UseCopyOnWriteArrayList.htm
---
Use CopyOnWriteArrayList

```java title=Example.java
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;
import java.util.concurrent.CopyOnWriteArrayList;
public class Test {
  public static void main(String[] args) {
    CopyOnWriteArrayList<String> list = new CopyOnWriteArrayList<String>();
    startUpdatingThread(list);
    for (String element : list) {
      System.out.println("Element :" + element);
    }
    updatingThread.interrupt();
    List<String> lista = Collections.synchronizedList(new ArrayList<String>());
    startUpdatingThread(lista);
    synchronized (lista) {
      for (String element : lista) {
        System.out.println("Element :" + element);
      }
    }
    updatingThread.interrupt();
  }
  static Thread updatingThread;
  private static void startUpdatingThread(final List<String> list) {
    updatingThread = new Thread(new Runnable() {
      long counter = 0;
      public void run() {
        while (!Thread.interrupted()) {
          int size = list.size();
          Random random = new Random();
          if (random.nextBoolean()) {
            if (size > 1) {
              list.remove(random.nextInt(size - 1));
            }
          } else {
            if (size < 20) {
              list.add("Random string " + counter);
            }
          }
          counter++;
        }
      }
    });
    updatingThread.start();
  }
}
```
