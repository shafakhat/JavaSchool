---
title: Collection Buffer
nav: Collection Buffer
description: Imported from the java2s.com archive: Collection Buffer
section: Imported - java2s Archive
order: 1018
source: https://web.archive.org/web/20061018181027/http://www.java2s.com/Code/Java/Apache-Common/CollectionBuffer.htm
---
```java title=Example.java
import org.apache.commons.collections.Buffer;
import org.apache.commons.collections.buffer.BlockingBuffer;
import org.apache.commons.collections.buffer.PriorityBuffer;
public class BufferExample {
  public static void main(String args[]) {
    Buffer buffer = new PriorityBuffer();
    buffer.add("2");
    buffer.add("1");
    buffer = BlockingBuffer.decorate(buffer);
    buffer.remove();
    System.err.println(buffer);
    buffer.clear();
    AddElementThread runner = new AddElementThread(buffer);
    runner.start();
    buffer.remove();
    System.err.println(buffer);
  }
}
class AddElementThread extends Thread {
  private Buffer buffer;
  public AddElementThread(Buffer buffer) {
    this.buffer = buffer;
  }
  public void run() {
    try {
      sleep(2000);
    } catch (InterruptedException ie) {}
    buffer.add("3");
  }
}
```

Download: ApacheCollectionBufferExample.zip ( 514 K )
Related examples in the same category
