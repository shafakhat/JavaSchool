---
title: Thread Join Demo
nav: Thread Join Demo
description: public TryThread(String firstName, String secondName, long delay) {
section: Imported - java2s Archive
order: 1020
source: https://web.archive.org/web/20070608194946/http://www.java2s.com:80/Tutorial/Java/0160__Thread/ThreadJoinDemo.htm
---
```java title=Example.java
Thread Joinclass TryThread extends Thread {
  public TryThread(String firstName, String secondName, long delay) {
    this.firstName = firstName;
    this.secondName = secondName;
    aWhile = delay;
    setDaemon(true);
  }
  public void run() {
    try {
      while (total < 1000) {
        System.out.print(firstName);
        sleep(aWhile);
        total += aWhile;
        System.out.print(secondName + "\n");
      }
      System.out.print(secondName + " stoped.\n");
    } catch (InterruptedException e) {
      System.out.println(firstName + secondName + e);
    }
  }
  private String firstName;
  private String secondName;
  private long aWhile;
  private long total;
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
      first.join();
    } catch (InterruptedException e) {
      // TODO Auto-generated catch block
      e.printStackTrace();
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
c  stoped.
a
a  stoped.
```
