---
title: Using the ConcurrentLinkedDeque class safely with multiple threads
nav: Using the ConcurrentLinked...
description: Using the ConcurrentLinkedDeque class safely with multiple threads
section: Imported - java2s Archive
order: 1148
source: https://web.archive.org/web/20130821064049/http://java2s.com/Code/Java/JDK-7/UsingtheConcurrentLinkedDequeclasssafelywithmultiplethreads.htm
---
Using the ConcurrentLinkedDeque class safely with multiple threads

```java title=Example.java
import java.util.concurrent.ConcurrentLinkedDeque;
public class Test {
public static ConcurrentLinkedDeque<Item> deque = new ConcurrentLinkedDeque<>();
  public static void main(String[] args) {
    Thread producerThread = new Thread(new ItemProducer());
    Thread consumerThread = new Thread(new ItemConsumer());
    producerThread.start();
    consumerThread.start();
  }
}
class Item {
  private String description;
  private int itemId;
  public String getDescription() {
    return description;
  }
  public int getItemId() {
    return itemId;
  }
  public Item() {
    this.description = "Default Item";
    this.itemId = 0;
  }
  public Item(String description, int itemId) {
    this.description = description;
    this.itemId = itemId;
  }
}
class ItemProducer implements Runnable {
  @Override
  public void run() {
    String itemName = "";
    int itemId = 0;
    try {
      for (int i = 1; i < 8; i++) {
        itemName = "Item" + i;
        itemId = i;
        Test.deque.add(new Item(itemName, itemId));
        System.out.println("New Item Added:" + itemName + " " + itemId);
        Thread.currentThread().sleep(250);
      }
    } catch (InterruptedException ex) {
      ex.printStackTrace();
    }
  }
}
class ItemConsumer implements Runnable {
  @Override
  public void run() {
    try {
      Thread.currentThread().sleep(1000);
    } catch (InterruptedException ex) {
      ex.printStackTrace();
    }
    Item item;
    while ((item = Test.deque.pollFirst()) != null) {
      if (item == null) {
      } else {
        generateOrder(item);
      }
    }
  }
  private void generateOrder(Item item) {
    System.out.println(item.getDescription());
    System.out.println(item.getItemId());
    try {
      Thread.currentThread().sleep(1000);
    } catch (InterruptedException ex) {
      ex.printStackTrace();
    }
  }
}
```
