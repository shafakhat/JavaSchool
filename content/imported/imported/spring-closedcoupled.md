---
title: Closed Coupled
nav: Closed Coupled
description: Imported from the java2s.com archive: Closed Coupled
section: Imported - java2s Archive
order: 1039
source: https://web.archive.org/web/20100213131543/http://java2s.com/Code/Java/Spring/ClosedCoupled.htm
---
Closed Coupled

```java title=Example.java
File: Main.java
import java.io.PrintStream;
public class Main {
  public static void main(String[] a) {
    MessageData source = new MessageData("Hello, world");
    MessageReporter destination = new MessageReporter();
    destination.write(System.out, source.getMessage());
  }
}
final class MessageData {
  private final String message;
  public MessageData(String message) {
    this.message = message;
  }
  public String getMessage() {
    return message;
  }
}
class MessageReporter {
  public void write(PrintStream out, String message) {
    out.println(message);
  }
}
```

Spring-ClosedCoupled.zip( 2,562 k)
1.  Decouple With Interface
2.  Spring Style Decouple
3.  Spring Prototype
