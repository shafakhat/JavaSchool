---
title: Use ReentrantLock to coordinate
nav: Use ReentrantLock to coord...
description: final Map<String, Integer> inventoryMap = new LinkedHashMap<String, Integer>();
section: Imported - java2s Archive
order: 1138
source: https://web.archive.org/web/20130821082329/http://java2s.com/Code/Java/JDK-7/UseReentrantLocktocoordinate.htm
---
```java title=Example.java
import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.UUID;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;
public class Test {
  Set<Thread> orderingThreads = new HashSet<Thread>();
  Lock lock = new ReentrantLock();
  final Map<String, Integer> inventoryMap = new LinkedHashMap<String, Integer>();
  List<Task> customerOrders = new ArrayList<Task>();
  public static void main(String[] args) throws InterruptedException {
    Test t = new Test();
    t.start();
  }
  private void start() throws InterruptedException {
    for (int i = 0; i < 10; i++) {
      inventoryMap.put("Book #" + i, 100);
    }
    for (int i = 0; i < 20; i++) {
      createOrderingThread();
    }
    checkInventoryLevels();
    for (Thread thread : orderingThreads) {
      thread.interrupt();
    }
    displayOrders();
  }
  private void displayOrders() {
    try {
      lock.lock();
      for (Task order : customerOrders) {
        System.out.println(order.getCount() + " "
            + order.id() + " for " + order.getTaskName());
      }
    } finally {
      lock.unlock();
    }
  }
  private void createOrderingThread() {
    Thread orderingThread = new Thread(new Runnable() {
      public void run() {
        while (!Thread.interrupted()) {
          createRandomOrder();
        }
      }
    });
    orderingThread.start();
    orderingThreads.add(orderingThread);
  }
  private void createRandomOrder() {
    String itemOrdered = UUID.randomUUID().toString();
    String customerName = "Customer ";
    fulfillOrder(itemOrdered, 2, customerName);
  }
  private boolean fulfillOrder(String itemOrdered, int quantityOrdered,
      String customerName) {
    try {
      lock.lock();
      int currentInventory = inventoryMap.get(itemOrdered);
      if (currentInventory < quantityOrdered) {
        return false;
      }
      inventoryMap.put(itemOrdered, currentInventory - quantityOrdered);
      Task order = new Task(itemOrdered, quantityOrdered,
          customerName);
      customerOrders.add(order);
      return true;
    } finally {
      lock.unlock();
    }
  }
  private void checkInventoryLevels() {
    try {
      lock.lock();
      for (Map.Entry<String, Integer> inventoryEntry : inventoryMap.entrySet()) {
        System.out.println(inventoryEntry.getKey() + " "
            + inventoryEntry.getValue());
      }
    } finally {
      lock.unlock();
    }
  }
}
class Task {
  String id;
  int count;
  String taskName;
  Task(String id, int q, String c) {
    this.id = id;
    this.count = q;
    this.taskName = c;
  }
  public String id() {
    return id;
  }
  public int getCount() {
    return count;
  }
  public String getTaskName() {
    return taskName;
  }
}
```

1.  Use ReentrantLock
---  ---
2.  LinkedBlockingQueue and ThreadPoolExecutor
3.  Two ReentrantLock
