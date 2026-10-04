---
title: A phantom reference is used to determine when an object is just about to be reclaimed.
nav: A phantom reference is use...
description: PhantomReference<String> pr = new PhantomReference<String>("object", rq);
section: Imported - java2s Archive
order: 2212
source: https://web.archive.org/web/2014/http://www.java2s.com/Tutorial/Java/0125__Reflection/Aphantomreferenceisusedtodeterminewhenanobjectisjustabouttobereclaimed.htm
---
```java title=Example.java
import java.lang.ref.PhantomReference;
import java.lang.ref.Reference;
import java.lang.ref.ReferenceQueue;
public class Main {
  public static void main(String[] argv) throws Exception {
    ReferenceQueue rq = new ReferenceQueue();
    PhantomReference<String> pr = new PhantomReference<String>("object", rq);
    while (true) {
      Reference r = rq.remove();
      if (r == pr) {
        // about to be reclaimed.
        r.clear();
      }
    }
  }
}
```
