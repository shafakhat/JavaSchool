---
title: A generic interface example.
nav: A generic interface example.
description: class MyClass<T extends Comparable<T>> implements MinMax<T> {
section: Imported - java2s Archive
order: 1002
source: https://web.archive.org/web/20090429173537/http://www.java2s.com:80/Code/Java/Generics/Agenericinterfaceexample.htm
---
```java title=Example.java
interface MinMax<T extends Comparable<T>> {
  T min();
  T max();
}
class MyClass<T extends Comparable<T>> implements MinMax<T> {
  T[] vals;
  MyClass(T[] o) { vals = o; }
  public T min() {
    T v = vals[0];
    for(int i=1; i < vals.length; i++)
      if(vals[i].compareTo(v) < 0) v = vals[i];
    return v;
  }
  public T max() {
    T v = vals[0];
    for(int i=1; i < vals.length; i++)
      if(vals[i].compareTo(v) > 0) v = vals[i];
    return v;
  }
}
public class GenIFDemo {
  public static void main(String args[]) {
    Integer inums[] = {3, 6, 2, 8, 6 };
    Character chs[] = {'b', 'r', 'p', 'w' };
    MyClass<Integer> iob = new MyClass<Integer>(inums);
    MyClass<Character> cob = new MyClass<Character>(chs);
    System.out.println("Max value in inums: " + iob.max());
    System.out.println("Min value in inums: " + iob.min());
    System.out.println("Max value in chs: " + cob.max());
    System.out.println("Min value in chs: " + cob.min());
  }
}
```

1.  Interface Generic (Has compile error)
