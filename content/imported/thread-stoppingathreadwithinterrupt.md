---
title: Stopping a Thread with interrupt()
nav: Stopping a Thread with int...
description: public TryThread(String firstName, String secondName, long delay) {
section: Imported - java2s Archive
order: 1018
source: https://web.archive.org/web/20070612195855/http://www.java2s.com:80/Tutorial/Java/0160__Thread/StoppingaThreadwithinterrupt.htm
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
      first.interrupt();
      second.interrupt();
      third.interrupt();
    } catch (Exception e) {
      System.out.println(e);
    }
  }
}
java title=Example.java
A B C a
A b
B a
A c
C a
A b
B a
A b
B c
a
C A a
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
B b java.lang.InterruptedException: sleep interrupted
C A a java.lang.InterruptedException: sleep interrupted
C c java.lang.InterruptedException: sleep interrupted
```
