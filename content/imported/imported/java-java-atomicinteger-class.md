---
title: Java AtomicInteger class
nav: Java AtomicInteger class
description: java.util.concurrent.atomic can get, set, or compare the value of a variable in one uninterruptible operation.
section: Imported
order: 20036
source: http://www.java2s.com/ref/java/java-atomicinteger-class.html
---
- java.util.concurrent.atomic
- java.util.concurrent.atomic AtomicInteger AtomicIntegerArray AtomicLong

## Introduction

java.util.concurrent.atomic can get, set, or compare the value of a variable in one uninterruptible operation.

No lock or other synchronization mechanism is required.

The following code shows how to access a shared integer via AtomicInteger :

```java title=Example.java
// A simple example of Atomic. import java.util.concurrent.atomic.AtomicInteger;

publicclass Main {

  publicstaticvoid main(String args[]) {
    new AtomThread("A");
    new AtomThread("B");
    new AtomThread("C");
  }//www.java2s.com
}

class Shared {
  staticAtomicInteger ai = newAtomicInteger(0);
}

// A thread of execution that increments count.class AtomThread implementsRunnable {
  String name;

  AtomThread(String n) {
    name = n;
    newThread(this).start();
  }

  publicvoid run() {

    System.out.println("Starting " + name);

    for (int i = 1; i <= 3; i++)
      System.out.println(name + " got: " + Shared.ai.getAndSet(i));
  }
}
```

PreviousNext

## Related

- Java ThreadPoolExecutor use LinkedBlockingQueue to control threads
- Java TimeUnit Enumeration
- Java TimeUnit convert milliseconds to hours
- Java AtomicInteger extend
- Java AtomicIntegerArray class
