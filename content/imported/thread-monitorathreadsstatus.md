---
title: Monitor a thread's status.
nav: Monitor a thread's status.
description: System.out.println(thrd.getName()+" Alive:"+thrd.isAlive()+" State:" + thrd.getState() );
section: Imported - java2s Archive
order: 1012
source: https://web.archive.org/web/20100309132320/http://www.java2s.com:80/Tutorial/Java/0160__Thread/Monitorathreadsstatus.htm
---
```java title=Example.java
class MyThread extends Thread{
  boolean waiting= true;
  boolean ready= false;
  public void run() {
    String thrdName = Thread.currentThread().getName();
    System.out.println(thrdName + " starting.");
    while(waiting)
      System.out.println("waiting:"+waiting);
    System.out.println("waiting...");
    startWait();
    try {
      Thread.sleep(10000);
    } catch(Exception exc) {
      System.out.println(thrdName + " interrupted.");
    }
    System.out.println(thrdName + " terminating.");
  }
  synchronized void startWait() {
    try {
      while(!ready){
        wait();
      }
    } catch(InterruptedException exc) {
      System.out.println("wait() interrupted");
    }
  }
  synchronized void startWork() {
    ready = true;
    notify();
  }
}
public class Main {
  public static void main(String args[]) throws Exception{
      MyThread thrd = new MyThread();
      thrd.setName("MyThread #1");
      System.out.println(thrd.getName()+" Alive:"+thrd.isAlive()+" State:" + thrd.getState() );
      thrd.start();
      Thread.sleep(50);
      System.out.println(thrd.getName()+" Alive:"+thrd.isAlive()+" State:" + thrd.getState() );
      thrd.waiting = false;
      Thread.sleep(50);
      System.out.println(thrd.getName()+" Alive:"+thrd.isAlive()+" State:" + thrd.getState() );
      thrd.startWork();
      Thread.sleep(50);
      System.out.println(thrd.getName()+" Alive:"+thrd.isAlive()+" State:" + thrd.getState() );
      if(thrd.isAlive())
        System.out.println("alive");
      System.out.println(thrd.getName()+" Alive:"+thrd.isAlive()+" State:" + thrd.getState() );
  }
}
```
