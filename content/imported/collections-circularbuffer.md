---
title: Circular Buffer
nav: Circular Buffer
description: Imported from the java2s.com archive: Circular Buffer
section: Imported - java2s Archive
order: 2304
source: https://web.archive.org/web/20140829091547/http://www.java2s.com/Tutorial/Java/0140__Collections/CircularBuffer.htm
---
```java title=Example.java
public class TestCircularBuffer {
  public static void main(String args[]) {
    TestCircularBuffer t = new TestCircularBuffer();
  }
  public TestCircularBuffer() {
    CircularBuffer c = new CircularBuffer(8);
    System.out.println("Storing: 1");
    c.store(1);
    System.out.println("Reading: " + c.read());
    System.out.println("Storing: 2");
    c.store(2);
    System.out.println("Storing: 3");
    c.store(3);
    System.out.println("Storing: 4");
    c.store(4);
    System.out.println("Reading: " + c.read());
    System.out.println("Reading: " + c.read());
    System.out.println("Storing: 8");
    c.store(8);
    System.out.println("Storing: 9");
    c.store(9);
    System.out.println("Storing: 10");
    c.store(10);
    System.out.println("Storing: 11");
    c.store(11);
    System.out.println("Storing: 12");
    c.store(12);
    System.out.println("Reading: " + c.read());
    System.out.println("Reading: " + c.read());
    System.out.println("Reading: " + c.read());
    System.out.println("Reading: " + c.read());
    System.out.println("Reading: " + c.read());
    System.out.println("Reading: " + c.read());
    System.out.println("Reading: " + c.read());
    System.out.println("Reading: " + c.read());
  }
}
class CircularBuffer {
  private Integer data[];
  private int head;
  private int tail;
  public CircularBuffer(Integer number) {
    data = new Integer[number];
    head = 0;
    tail = 0;
  }
  public boolean store(Integer value) {
    if (!bufferFull()) {
      data[tail++] = value;
      if (tail == data.length) {
        tail = 0;
      }
      return true;
    } else {
      return false;
    }
  }
  public Integer read() {
    if (head != tail) {
      int value = data[head++];
      if (head == data.length) {
        head = 0;
      }
      return value;
    } else {
      return null;
    }
  }
  private boolean bufferFull() {
    if (tail + 1 == head) {
      return true;
    }
    if (tail == (data.length - 1) && head == 0) {
      return true;
    }
    return false;
  }
}
```

| 9.3.1. | How to define an Array |
|---|---|
| 9.3.2. | Initializing array elements by index |
| 9.3.3. | Alternative Array Declaration Syntax |
| 9.3.4. | Anonymous arrays are declared similarly to regular arrays |
| 9.3.5. | An array is a Java object |
| 9.3.6. | To reference the components of an array |
| 9.3.7. | The Length of an Array |
| 9.3.8. | Initializing Arrays |
| 9.3.9. | Using a for loop to iterate over all the elements and set the values |
| 9.3.10. | Arrays of Characters |
| 9.3.11. | Using the Collection-Based for Loop with an Array |
| 9.3.12. | Changing Array Size |
| 9.3.13. | Array Reallocation |
| 9.3.14. | Use System.arraycopy to duplicate array |
| 9.3.15. | Minimum and maximum number in array |
| 9.3.16. | Shuffle elements of an array |
| 9.3.17. | Merge (or add) two arrays into one |
| 9.3.18. | Circular Buffer |
