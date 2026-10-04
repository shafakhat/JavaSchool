---
title: Testing PhantomReference
nav: Testing PhantomReference
description: Imported from the java2s.com archive: Testing PhantomReference
section: Imported - java2s Archive
order: 2199
source: https://web.archive.org/web/20140829091008/http://www.java2s.com/Tutorial/Java/0125__Reflection/TestingPhantomReference.htm
---
```java title=Example.java
import java.lang.ref.PhantomReference;
import java.lang.ref.Reference;
import java.lang.ref.ReferenceQueue;
import java.lang.ref.SoftReference;
import java.lang.ref.WeakReference;
import java.util.HashMap;
public class Main {
  public static void main(String[] args) {
    ReferenceQueue referenceQueue = new ReferenceQueue();
    Object object = new Object() {
      public String toString() {
        return "Referenced Object";
      }
    };
    Object data = new Object() {
      public String toString() {
        return "Data";
      }
    };
    HashMap map = new HashMap();
    Reference reference = null;
    System.out.println("Testing PhantomReference.");
    reference = new PhantomReference(object, referenceQueue);
    map.put(reference, data);
    System.out.println(reference.get());
    System.out.println(map.get(reference));
    System.out.println(reference.isEnqueued());
    System.gc();
    System.out.println(reference.get());
    System.out.println(map.get(reference));
    System.out.println(reference.isEnqueued());
    object = null;
    data = null;
    System.gc();
    System.out.println(reference.get());
    System.out.println(map.get(reference));
    System.out.println(reference.isEnqueued());
  }
}
```
