---
title: Add thread to thread group
nav: Add thread to thread group
description: Imported from the java2s.com archive: Add thread to thread group
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/20101021063713/http://java2s.com:80/Tutorial/Java/0160__Thread/Addthreadtothreadgroup.htm
---
```java title=Example.java
class ThreadGroupDemo1 {
  public static void main(String[] args) {
    ThreadGroup tg = new ThreadGroup("My ThreadGroup");
    MyThread mt = new MyThread(tg, "My Thread");
    mt.start();
  }
}
class MyThread extends Thread {
  MyThread(ThreadGroup tg, String name) {
    super(tg, name);
  }
  public void run() {
    ThreadGroup tg = getThreadGroup();
    System.out.println(tg.getName());
  }
}
```
