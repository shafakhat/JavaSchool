---
title: Using java.util.concurrent.AtomicLong
nav: Using java.util.concurrent...
description: Imported from the java2s.com archive: Using java.util.concurrent.AtomicLong
section: Imported - java2s Archive
order: 1987
source: https://web.archive.org/web/20140829083707/http://www.java2s.com/Tutorial/Java/0120__Development/UsingjavautilconcurrentAtomicLongAnumericalidstartatzeroandincrementbyone.htm
---
```java title=Example.java
import java.util.concurrent.atomic.AtomicLong;
public class Main {
  public static void main(String[] argv) {
    AtomicLong nextId = new AtomicLong();
    System.out.println(nextId.getAndIncrement());
  }
}
```

| 6.54.1. | Get a unique identifier Using java.rmi.dgc.VMID |
|---|---|
| 6.54.2. | Using java.util.UUID |
| 6.54.3. | Using java.util.concurrent.AtomicLong: A numerical id, start at zero and increment by one. |
| 6.54.4. | Create your own basic UUID |
| 6.54.5. | Random GUID |
| 6.54.6. | Session ID generator |
| 6.54.7. | Generates a UUID |
| 6.54.8. | ID generator |
| 6.54.9. | Generator for Globally unique Strings |
| 6.54.10. | Generates random UUIDs |
| 6.54.11. | UUID generator |
