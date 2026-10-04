---
title: Use LinkedBlockingQueue
nav: Use LinkedBlockingQueue
description: LinkedBlockingQueue<String> queue = new LinkedBlockingQueue<String>();
section: Imported - java2s Archive
order: 1136
source: https://web.archive.org/web/20130820184538/http://java2s.com/Code/Java/JDK-7/UseLinkedBlockingQueue.htm
---
```java title=Example.java
import java.io.DataOutputStream;
import java.io.FileOutputStream;
import java.util.concurrent.LinkedBlockingQueue;
public class Test {
  public static void main(String[] args) throws Exception {
    LinkedBlockingQueue<String> queue = new LinkedBlockingQueue<String>();
    FileOutputStream fos = new FileOutputStream("out.log");
    DataOutputStream dos = new DataOutputStream(fos);
    while (!queue.isEmpty()) {
      dos.writeUTF(queue.take());
    }
  }
}
```
