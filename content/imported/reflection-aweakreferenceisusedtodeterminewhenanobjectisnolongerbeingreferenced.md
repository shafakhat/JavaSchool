---
title: A weak reference is used to determine when an object is no longer being referenced.
nav: A weak reference is used t...
description: WeakReference<String> wr = new WeakReference<String>("string", rq);
section: Imported - java2s Archive
order: 2215
source: https://web.archive.org/web/20140829083201/http://www.java2s.com/Tutorial/Java/0125__Reflection/Aweakreferenceisusedtodeterminewhenanobjectisnolongerbeingreferenced.htm
---
```java title=Example.java
import java.lang.ref.Reference;
import java.lang.ref.ReferenceQueue;
import java.lang.ref.WeakReference;
public class Main {
  public static void main(String[] argv) throws Exception {
    ReferenceQueue rq = new ReferenceQueue();
    WeakReference<String> wr = new WeakReference<String>("string", rq);
    while (true) {
      Reference r = rq.remove();
      if (r == wr) {
        System.out.println("no longer referenced");
      }
    }
  }
}
```
