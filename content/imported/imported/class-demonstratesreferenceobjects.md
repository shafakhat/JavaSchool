---
title: Demonstrates Reference objects
nav: Demonstrates Reference obj...
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1007
source: https://web.archive.org/web/20090503021238/http://www.java2s.com:80/Code/Java/Class/DemonstratesReferenceobjects.htm
---
```java title=Example.java
// : c11:References.java
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
import java.lang.ref.PhantomReference;
import java.lang.ref.Reference;
import java.lang.ref.ReferenceQueue;
import java.lang.ref.SoftReference;
import java.lang.ref.WeakReference;
class VeryBig {
  private static final int SZ = 10000;
  private double[] d = new double[SZ];
  private String ident;
  public VeryBig(String id) {
    ident = id;
  }
  public String toString() {
    return ident;
  }
  public void finalize() {
    System.out.println("Finalizing " + ident);
  }
}
public class References {
  private static ReferenceQueue rq = new ReferenceQueue();
  public static void checkQueue() {
    Object inq = rq.poll();
    if (inq != null)
      System.out
          .println("In queue: " + (VeryBig) ((Reference) inq).get());
  }
  public static void main(String[] args) {
    int size = 10;
    // Or, choose size via the command line:
    if (args.length > 0)
      size = Integer.parseInt(args[0]);
    SoftReference[] sa = new SoftReference[size];
    for (int i = 0; i < sa.length; i++) {
      sa[i] = new SoftReference(new VeryBig("Soft " + i), rq);
      System.out.println("Just created: " + (VeryBig) sa[i].get());
      checkQueue();
    }
    WeakReference[] wa = new WeakReference[size];
    for (int i = 0; i < wa.length; i++) {
      wa[i] = new WeakReference(new VeryBig("Weak " + i), rq);
      System.out.println("Just created: " + (VeryBig) wa[i].get());
      checkQueue();
    }
    SoftReference s = new SoftReference(new VeryBig("Soft"));
    WeakReference w = new WeakReference(new VeryBig("Weak"));
    System.gc();
    PhantomReference[] pa = new PhantomReference[size];
    for (int i = 0; i < pa.length; i++) {
      pa[i] = new PhantomReference(new VeryBig("Phantom " + i), rq);
      System.out.println("Just created: " + (VeryBig) pa[i].get());
      checkQueue();
    }
  }
} ///:~
```

1.  Create Object Demo
---  ---
2.  Passing objects to methods may not be what you're used to.
3.  A companion class to modify immutable objects
4.  Objects that cannot be modified are immune to aliasing
5.  Examination of the way the class loader works
6.  A changeable wrapper class
