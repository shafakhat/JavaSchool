---
title: Java Tutorial - How to create Generic Method in Java
nav: Java Tutorial - How to cre...
description: It is possible to create a generic method that is enclosed within a non-generic class.
section: Imported - java2s Archive
order: 50458
source: https://www.java2s.com/Tutorials/Java/Java_Language/8010__Java_generic_method.html
---
```java title=Example.java
```

It is possible to create a generic method that is enclosed within a non-generic class.

```java title=Example.java
publicclass Main {
  static <T, V extends T> boolean isIn(T x, V[] y) {
    for (int i = 0; i < y.length; i++) {
      if (x.equals(y[i])) {
        return true;
      }//www.java2s.com
    }
    return false;
  }
  publicstaticvoid main(String args[]) {
    Integer nums[] = { 1, 2, 3, 4, 5 };
    if (isIn(2, nums)){
      System.out.println("2 is in nums");
    }
    String strs[] = { "one", "two", "three", "four", "five" };
    if (isIn("two", strs)){
      System.out.println("two is in strs");
    }
  }
}
```

The code above generates the following result.

## Example

The following code declares a copyList() generic method.

```java title=Example.java
/*www.java2s.com*/import java.util.ArrayList;
import java.util.List;
publicclass Main {
  publicstaticvoid main(String[] args) {
    List<String> ls = new ArrayList<String>();
    ls.add("A");
    ls.add("B");
    ls.add("C");
    List<String> lsCopy = new ArrayList<String>();
    copyList(ls, lsCopy);
    List<Integer> lc = new ArrayList<Integer>();
    lc.add(0);
    lc.add(5);
    List<Integer> lcCopy = new ArrayList<Integer>();
    copyList(lc, lcCopy);
  }
  static <T> void copyList(List<T> src, List<T> dest) {
    for (int i = 0; i < src.size(); i++)
      dest.add(src.get(i));
  }
}
```

## Java Generic Constructors

It is possible for constructors to be generic, even if their class is not. For example, consider the following short program:

```java title=Example.java
class MyClass {/*fromwww.java2s.com*/privatedouble val;
  <T extends Number> MyClass(T arg) {
    val = arg.doubleValue();
  }
  void showval() {
    System.out.println("val: " + val);
  }
}
publicclass Main {
  publicstaticvoid main(String args[]) {
    MyClass test = new MyClass(100);
    MyClass test2 = new MyClass(123.5F);
    test.showval();
    test2.showval();
  }
}
```

The code above generates the following result.

- « Previous
