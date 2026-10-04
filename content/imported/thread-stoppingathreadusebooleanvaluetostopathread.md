---
title: Stopping a Thread
nav: Stopping a Thread
description: Imported from the java2s.com archive: Stopping a Thread
section: Imported - java2s Archive
order: 1017
source: https://web.archive.org/web/20070612233745/http://www.java2s.com:80/Tutorial/Java/0160__Thread/StoppingaThreadUsebooleanvaluetostopathread.htm
---
```java title=Example.java
class CounterThread extends Thread {
  public boolean stopped = false;
  int count = 0;
  public void run() {
    while (!stopped) {
      try {
        sleep(1000);
      } catch (InterruptedException e) {
      }
      System.out.println(count++);
      ;
    }
  }
}
public class MainClass {
  public static void main(String[] args) {
    CounterThread thread = new CounterThread();
    thread.start();
    try {
      Thread.sleep(10000);
    } catch (InterruptedException e) {
    }
    thread.stopped = true;
    System.out.println("exit");
  }
}
```

```java title=Example.java
0
1
2
3
4
5
6
7
8
9
exit
```
