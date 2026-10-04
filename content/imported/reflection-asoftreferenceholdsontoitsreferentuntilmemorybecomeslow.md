---
title: A soft reference holds onto its referent until memory becomes low.
nav: A soft reference holds ont...
description: SoftReference<String> sr = new SoftReference<String>("object");
section: Imported - java2s Archive
order: 2207
source: https://web.archive.org/web/2014/http://www.java2s.com/Tutorial/Java/0125__Reflection/Asoftreferenceholdsontoitsreferentuntilmemorybecomeslow.htm
---
```java title=Example.java
import java.lang.ref.SoftReference;
public class Main {
  public static void main(String[] argv) throws Exception {
    SoftReference<String> sr = new SoftReference<String>("object");
    Object o = sr.get();
    if (o != null) {
      System.out.println(o);
    } else {
      System.out.println("collected or has been reclaimed");
    }
  }
}
```
