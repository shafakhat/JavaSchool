---
title: Create a new thread for the thread pool. The create thread will be a daemon thread.
nav: Create a new thread for th...
description: Create a new thread for the thread pool. The create thread will be a daemon thread. : Thread Pool « Threads « Java
section: Imported - java2s Archive
order: 1030
source: https://web.archive.org/web/20090914064440/http://www.java2s.com:80/Code/Java/Threads/CreateanewthreadforthethreadpoolThecreatethreadwillbeadaemonthread.htm
---
Create a new thread for the thread pool. The create thread will be a daemon thread. : Thread Pool « Threads « Java
Create a new thread for the thread pool. The create thread will be a daemon thread.

```java title=Example.java
import java.util.concurrent.Executors;
import java.util.concurrent.ThreadFactory;
/**
 * Simple implementation of a ThreadFactory that
 * marks all of the threads as daemon threads.
 */
public class DaemonThreadFactory implements ThreadFactory {
    private final ThreadFactory factory = Executors.defaultThreadFactory();
    /**
     * Create a new thread for the thread pool.  The create
     * thread will be a daemon thread.
     *
     * @param r      The runnable used by the thread pool.
     *
     * @return The newly created thread.
     */
    public Thread newThread(Runnable r) {
        Thread t = factory.newThread(r);
        if (!t.isDaemon()) {
            t.setDaemon(true);
        }
        return t;
    }
}
```

1.  Defining a thread for a thread pool
---  ---
2.  Thread pool demo
3.  Thread Pools 1
4.  Thread Pools 2
5.  Thread pool
6.  Thread Pool 2
7.  Thread Pool Test
8.  JDK1.5 provides a mechanism to create a pool a scheduled task
9.  Very basic implementation of a thread pool
10.  Thread Cache
11.  Simple pool of Threads
12.  Worker thread pool
13.  Simple thread pool. A task is executed by obtaining a thread from the pool
14.  Simple object pool. Based on ThreadPool and few other classes
