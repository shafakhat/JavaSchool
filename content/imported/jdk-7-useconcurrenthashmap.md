---
title: Use ConcurrentHashMap
nav: Use ConcurrentHashMap
description: ConcurrentMap<Integer, String> concurrentMap = new ConcurrentHashMap<Integer, String>();
section: Imported - java2s Archive
order: 1133
source: https://web.archive.org/web/20130721145603/http://www.java2s.com:80/Code/Java/JDK-7/UseConcurrentHashMap.htm
---
Use ConcurrentHashMap

```java title=Example.java
import java.util.HashSet;
import java.util.Map;
import java.util.Random;
import java.util.Set;
import java.util.UUID;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.ConcurrentMap;
public class Test {
  static Set<Thread> updateThreads = new HashSet<Thread>();
  public static void main(String[] args) {
    ConcurrentMap<Integer, String> concurrentMap = new ConcurrentHashMap<Integer, String>();
    for (int i = 0; i < 1000; i++) {
      startUpdateThread(i, concurrentMap);
    }
    for (Map.Entry<Integer, String> entry : concurrentMap.entrySet()) {
      System.out.println("Key :" + entry.getKey() + " Value:" + entry.getValue());
    }
    for (Thread thread : updateThreads) {
      thread.interrupt();
    }
  }
  private static void startUpdateThread(int i,
      final ConcurrentMap<Integer, String> concurrentMap) {
    Thread thread = new Thread(new Runnable() {
      public void run() {
        while (!Thread.interrupted()) {
          Random random = new Random();
          int randomInt = random.nextInt(20);
          concurrentMap.put(randomInt, UUID.randomUUID().toString());
        }
      }
    });
    thread.setName("Update Thread " + i);
    updateThreads.add(thread);
    thread.start();
  }
}
```
