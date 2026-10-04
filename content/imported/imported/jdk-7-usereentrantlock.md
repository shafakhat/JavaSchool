---
title: Use ReentrantLock
nav: Use ReentrantLock
description: Imported from the java2s.com archive: Use ReentrantLock
section: Imported - java2s Archive
order: 1137
source: https://web.archive.org/web/20130821043250/http://java2s.com/Code/Java/JDK-7/UseReentrantLock.htm
---
```java title=Example.java
import java.io.FileOutputStream;
import java.util.Random;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;
public class Test {
  public static void main(String[] args) throws Exception {
    Lock myLock = new ReentrantLock();
    Random random = new Random();
    myLock.lock();
    int number = random.nextInt(5);
    int result = 100 / number;
    System.out.println("A result is " + result);
    FileOutputStream file = new FileOutputStream("file.out");
    file.write(result);
    file.close();
  }
}
```

1.  Use ReentrantLock to coordinate
---  ---
2.  LinkedBlockingQueue and ThreadPoolExecutor
3.  Two ReentrantLock
