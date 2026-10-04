---
title: To determine whether a thread has been interrupted
nav: To determine whether a thr...
description: public TryThread(String firstName, String secondName, long delay) {
section: Imported - java2s Archive
order: 1021
source: https://web.archive.org/web/20070613000835/http://www.java2s.com:80/Tutorial/Java/0160__Thread/Todeterminewhetherathreadhasbeeninterrupted.htm
---
```java title=Example.java
class TryThread extends Thread {
  public TryThread(String firstName, String secondName, long delay) {
    this.firstName = firstName;
    this.secondName = secondName;
    aWhile = delay;
    setDaemon(true);
  }
  public void run() {
    try {
      while (true) {
        System.out.print(firstName);
        sleep(aWhile);
        System.out.print(secondName + "\n");
      }
    } catch (InterruptedException e) {
      System.out.println(firstName + secondName + e);
    }
  }
  private String firstName;
  private String secondName;
  private long aWhile;
}
public class MainClass {
  public static void main(String[] args) {
    Thread first = new TryThread("A ", "a ", 200L);
    Thread second = new TryThread("B ", "b ", 300L);
    Thread third = new TryThread("C ", "c ", 500L);
    first.start();
    second.start();
    third.start();
    try {
      Thread.sleep(3000);
    } catch (Exception e) {
      System.out.println(e);
    }
      first.interrupt();
      second.interrupt();
      third.interrupt();
    if (first.isInterrupted()) {
      System.out.println("First thread has been interrupted.");
    }
  }
}
```

```java title=Example.java
A B C a
A b
B a
A c
C a
A b
B a
A b
B c
C a
A a
A b
B a
A c
C b
B a
A a
A b
B c
C a
A b
B a
A a
A b
B c
C a
A b
B a
A c
C C c java.lang.InterruptedException: sleep interrupted
First thread has been interrupted.
B b java.lang.InterruptedException: sleep interrupted
A a java.lang.InterruptedException: sleep interrupted
```
