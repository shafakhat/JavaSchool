---
title: Creating a resource that can be used with the try-with-resources technique
nav: Creating a resource that c...
description: Creating a resource that can be used with the try-with-resources technique
section: Imported - java2s Archive
order: 1037
source: https://web.archive.org/web/20130821074932/http://java2s.com/Code/Java/JDK-7/Creatingaresourcethatcanbeusedwiththetrywithresourcestechnique.htm
---
Creating a resource that can be used with the try-with-resources technique

```java title=Example.java
public class Test {
  public static void main(String[] args) {
    try (MyResource resource1 = new MyResource();
        OtherResource resource2 = new OtherResource()) {
      resource1.do1();
      resource2.do2();
    } catch (Exception e) {
      e.printStackTrace();
      for (Throwable throwable : e.getSuppressed()) {
        System.out.println(throwable);
      }
    }
  }
}
class MyResource implements AutoCloseable {
  @Override
  public void close() throws Exception {
    System.out.println("close method executed");
    throw new UnsupportedOperationException("A problem has occurred");
  }
  public void do1() {
    System.out.println("method executed");
  }
}
class OtherResource implements AutoCloseable {
  @Override
  public void close() throws Exception {
    System.out.println("A");
    throw new UnsupportedOperationException("A problem has occurred");
  }
  public void do2() {
    System.out.println("executed");
  }
}
```

1.  Using the try-with-resource block to improve exception handling code
