---
title: Change Thread Priority
nav: Change Thread Priority
description: Imported from the java2s.com archive: Change Thread Priority
section: Imported - java2s Archive
order: 1005
source: https://web.archive.org/web/20070703183945/http://www.java2s.com:80/Tutorial/Java/0160__Thread/ChangeThreadPriority.htm
---
- A priority tells the operating system how much resource should be given to each thread.
- A high-priority thread is scheduled to receive more time on the CPU than a low-priority thread. A method called Thread.setPriority() sets the priority of a thread. Thread class constants can be used to set these.

```java title=Example.java
class CounterThread extends Thread {
  String name;
  public CounterThread(String name) {
    super();
    this.name = name;
  }
  public void run() {
    int count = 0;
    while (true) {
      try {
        sleep(100);
      } catch (InterruptedException e) {
      }
      if (count == 50000)
        count = 0;
      System.out.println(name+":" + count++);
    }
  }
}
public class MainClass{
    public static void main(String[] args) {
      CounterThread thread1 = new CounterThread("thread1");
      thread1.setPriority(10);
      CounterThread thread2 = new CounterThread("thread2");
      thread2.setPriority(1);
      thread2.start();
      thread1.start();
    }
}
```
