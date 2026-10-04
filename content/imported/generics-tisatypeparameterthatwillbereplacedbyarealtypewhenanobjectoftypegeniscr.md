---
title: T is a type parameter that will be replaced by a real type when an object of type Gen is created.
nav: T is a type parameter that...
description: T is a type parameter that will be replaced by a real type when an object of type Gen is created.
section: Imported - java2s Archive
order: 1052
source: https://web.archive.org/web/20081201185946/http://www.java2s.com:80/Code/Java/Generics/TisatypeparameterthatwillbereplacedbyarealtypewhenanobjectoftypeGeniscreated.htm
---
```java title=Example.java
class Gen<T> {
  T ob;
  Gen(T o) {
    ob = o;
  }
  T getob() {
    return ob;
  }
  void showType() {
    System.out.println("Type of T is " + ob.getClass().getName());
  }
}
class GenDemo {
  public static void main(String args[]) {
    Gen<Integer> iOb;
    iOb = new Gen<Integer>(88);
    iOb.showType();
    int v = iOb.getob();
    System.out.println("value: " + v);
    System.out.println();
    Gen<String> strOb = new Gen<String>("Generics Test");
    strOb.showType();
    String str = strOb.getob();
    System.out.println("value: " + str);
  }
}
```

1.  A simple generic class with two type parameters: T and V.
---  ---
2.  Java generic: Hierarchy argument
3.  Boxing Generic Example
4.  Demonstrate a raw generic type.
5.  Create a generic class that can compute the average of an array of numbers of any given type.
6.  the type argument for T must be either Number, or a class derived from Number.
7.  Demonstrate a raw type.
8.  A subclass can add its own type parameters.
