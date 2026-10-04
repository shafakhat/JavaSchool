---
title: Creating Thread Objects
nav: Creating Thread Objects
description: public TryThread(String firstName, String secondName, long delay) {
section: Imported - java2s Archive
order: 1008
source: https://web.archive.org/web/20070524233647/http://www.java2s.com:80/Tutorial/Java/0160__Thread/CreatingThreadObjectsImplementingtherunMethodinRunnableinterface.htm
---
```java title=Example.java
import java.io.IOException;
class TryThread implements Runnable {
  public TryThread(String firstName, String secondName, long delay) {
    this.firstName = firstName;
    this.secondName = secondName;
    aWhile = delay;
  }
  public void run() {
    try {
      while (true) {
        System.out.print(firstName);
        Thread.sleep(aWhile);
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
    Thread first = new Thread(new TryThread("A ", "a ", 200L));
    Thread second = new Thread(new TryThread("B ", "b ", 300L));
    Thread third = new Thread(new TryThread("C ", "c ", 500L));
    System.out.println("Press Enter when you have had enough...\n");
    first.start();
    second.start();
    third.start();
    try {
      System.in.read();
      System.out.println("Enter pressed...\n");
    } catch (IOException e) {
      System.out.println(e);
    }
    System.out.println("Ending main()");
    return;
  }
}
```
