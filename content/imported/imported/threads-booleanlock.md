---
title: Boolean lock : Java examples (example source code) » Threads » Lock Synchronize
nav: Boolean lock : Java exampl...
description: private void waitWhileSuspended() throws InterruptedException {
section: Imported - java2s Archive
order: 1022
source: https://web.archive.org/web/20060513092444/http://www.java2s.com/Code/Java/Threads/Booleanlock.htm
---
Boolean lock

```java title=Example.java
public class BestReplacement extends Object {
  private Thread internalThread;
  private volatile boolean stopRequested;
  private BooleanLock suspendRequested;
  private BooleanLock internalThreadSuspended;
  public BestReplacement() {
    stopRequested = false;
    suspendRequested = new BooleanLock(false);
    internalThreadSuspended = new BooleanLock(false);
    Runnable r = new Runnable() {
      public void run() {
        try {
          runWork();
        } catch (Exception x) {
          x.printStackTrace();
        }
      }
    };
    internalThread = new Thread(r);
    internalThread.start();
  }
  private void runWork() {
    int count = 0;
    while (!stopRequested) {
      try {
        waitWhileSuspended();
      } catch (InterruptedException x) {
        Thread.currentThread().interrupt();
        continue;
      }
      System.out.println("Part I - count=" + count);
      try {
        Thread.sleep(1000);
      } catch (InterruptedException x) {
        Thread.currentThread().interrupt();
      }
      System.out.println("Part II - count=" + count);
      try {
        Thread.sleep(1000);
      } catch (InterruptedException x) {
        Thread.currentThread().interrupt();
      }
      System.out.println("Part III - count=" + count);
      count++;
    }
  }
  private void waitWhileSuspended() throws InterruptedException {
    synchronized (suspendRequested) {
      if (suspendRequested.isTrue()) {
        try {
          internalThreadSuspended.setValue(true);
          suspendRequested.waitUntilFalse(0);
        } finally {
          internalThreadSuspended.setValue(false);
        }
      }
    }
  }
  public void suspendRequest() {
    suspendRequested.setValue(true);
  }
  public void resumeRequest() {
    suspendRequested.setValue(false);
  }
  public boolean waitForActualSuspension(long msTimeout)
      throws InterruptedException {
    return internalThreadSuspended.waitUntilTrue(msTimeout);
  }
  public void stopRequest() {
    stopRequested = true;
    internalThread.interrupt();
  }
  public boolean isAlive() {
    return internalThread.isAlive();
  }
  public static void main(String[] args) {
    try {
      BestReplacement br = new BestReplacement();
      System.out
          .println(" just created, br.isAlive()=" + br.isAlive());
      Thread.sleep(4200);
      long startTime = System.currentTimeMillis();
      br.suspendRequest();
      System.out.println(" just submitted a suspendRequest");
      boolean suspensionTookEffect = br.waitForActualSuspension(10000);
      long stopTime = System.currentTimeMillis();
      if (suspensionTookEffect) {
        System.out.println(" the internal thread took "
            + (stopTime - startTime) + " ms to notice "
            + "\n    the suspend request and is now "
            + "suspended.");
      } else {
        System.out.println(" the internal thread did not notice "
            + "the suspend request " + "\n    within 10 seconds.");
      }
      Thread.sleep(5000);
      br.resumeRequest();
      System.out.println("Submitted a resumeRequest");
      Thread.sleep(2200);
      br.stopRequest();
      System.out.println("Submitted a stopRequest");
    } catch (InterruptedException x) {
      // ignore
    }
  }
}
class BooleanLock extends Object {
  private boolean value;
  public BooleanLock(boolean initialValue) {
    value = initialValue;
  }
  public BooleanLock() {
    this(false);
  }
  public synchronized void setValue(boolean newValue) {
    if ( newValue != value ) {
      value = newValue;
      notifyAll();
    }
  }
  public synchronized boolean waitToSetTrue(long msTimeout)
      throws InterruptedException {
    boolean success = waitUntilFalse(msTimeout);
    if ( success ) {
      setValue(true);
    }
    return success;
  }
  public synchronized boolean waitToSetFalse(long msTimeout)
      throws InterruptedException {
    boolean success = waitUntilTrue(msTimeout);
    if ( success ) {
      setValue(false);
    }
    return success;
  }
  public synchronized boolean isTrue() {
    return value;
  }
  public synchronized boolean isFalse() {
    return !value;
  }
  public synchronized boolean waitUntilTrue(long msTimeout)
      throws InterruptedException {
    return waitUntilStateIs(true, msTimeout);
  }
  public synchronized boolean waitUntilFalse(long msTimeout)
      throws InterruptedException {
    return waitUntilStateIs(false, msTimeout);
  }
  public synchronized boolean waitUntilStateIs(
        boolean state,
        long msTimeout
      ) throws InterruptedException {
    if ( msTimeout == 0L ) {
      while ( value != state ) {
        wait();
      }
      return true;
    }
    long endTime = System.currentTimeMillis() + msTimeout;
    long msRemaining = msTimeout;
    while ( ( value != state ) && ( msRemaining > 0L ) ) {
      wait(msRemaining);
      msRemaining = endTime - System.currentTimeMillis();
    }
    return ( value == state );
  }
}
```

Related examples in the same category
---
1. Thread: Dining Philosophers
2. Synchronizing on another object
3. Operations that may seem safe are not, when threads are present
4. Synchronizing blocks instead of entire methods
5. Static synchronized block
6. Thread notify
7. Thread deadlock
8. Synchronize method
9. Threads join
10. Static synchronize
11. No synchronize
12. Thread syncronization
13. Synchronized Block demo
14. Interruptible Synchronized Block
15. Signaling
16. Simple Object FIFO
17. Object FIFO
18. Byte FIFO
19. Thread Synch
20. Daemon Lock
21. Lock for read and write
