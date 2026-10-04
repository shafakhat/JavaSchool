---
title: Implements a manager of lists that stores the lists by key
nav: Implements a manager of li...
description: * This software is granted under the terms of the Common Public License,
section: Imported - java2s Archive
order: 1227
source: https://web.archive.org/web/20140829092253/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Implementsamanagerofliststhatstoresthelistsbykey.htm
---
```java title=Example.java
/*
 *     file: Inference.java
 *  package: oreilly.hcj.tiger
 *
 * This software is granted under the terms of the Common Public License,
 * CPL, which may be found at the following URL:
 * http://www-124.ibm.com/developerworks/oss/CPLv1.0.htm
 *
 * Copyright(c) 2003-2005 by the authors indicated in the @author tags.
 * All Rights are Reserved by the various authors.
 *
 ########## DO NOT EDIT ABOVE THIS LINE ########## */
import java.util.ArrayList;
import java.util.List;
/**
 */
public class InferenceDemo {
  static int callCount = 0;
  /** Second. */
  public static <Type extends Number> Type someMethod(final Type num) {
    System.out.print("Second==> ");
    return num;
  }
  /** Third. */
  public static <Type> Type someMethod(final Type obj, List<Type> list) {
    System.out.print("Third==> ");
    return obj;
  }
  /** Fourth. */
  public static <Type> List<Type> someMethod() {
    System.out.print("Fourth==> ");
    return new ArrayList<Type>();
  }
  /** Fifth. */
  public static void someMethod(final Object obj) {
    System.out.print("Fifth==> ");
  }
  /** Sixth. */
  public static void someMethod(final String str) {
    System.out.print("Sixth==> ");
  }
  /** Seventh. */
  public static <Type> Type someOtherMethod(final Type obj, List<? extends Type> list) {
    System.out.print("Seventh==> ");
    return obj;
  }
  /** Demonstrate the rules. */
  public final static void main(final String[] args) {
    System.out.println();
    // Picks Sixth
    System.out.print("\n1) ");
    someMethod("Hello");
    // Ambiguous, wont compile.
    // System.out.print("\n2) ");
    // someMethod(new C());
    // Ambiguous, wont compile.
    // First and Fifth mask each other and can never be called.
    // System.out.print("\n3) ");
    // someMethod(new Object());
    // Picks Second
    System.out.print("\n5) ");
    someMethod(new Integer(5));
    // Picks Second
    System.out.print("\n6) ");
    someMethod(5);
    // Picks Fourth
    System.out.print("\n7) ");
    List<Integer> listOne = someMethod();
    listOne.add(new Integer(5));
    System.out.print("\n7a) ");
    List<String> listTwo = someMethod();
    listTwo.add(new String("Hello"));
    System.out.print("\n7b) ");
    Object listThree = someMethod();
    System.out.println(listThree.getClass());
    // listThree.add( ... ); // Cant put anything into this list
    // -- Make some lists --
    List<A> listOfA = new ArrayList<A>();
    listOfA.add(new A());
    List<B> listOfB = new ArrayList<B>();
    listOfB.add(new B());
    // Picks
    System.out.print("\n8) ");
    someMethod(5, new ArrayList<Integer>());
    // Wont compile: No such type. Since A can not necessarily be promoted to B.
    // System.out.print("9) ");
    // someMethod(new A(), listOfB);
    // Picks Three: Works because B can be demoted to A
    System.out.print("\n10) ");
    someMethod(new B(), listOfA);
    // Picks Seventh
    System.out.print("\n11) ");
    someOtherMethod(new A(), listOfB);
    // Picks Seventh
    // Works even though it probably shouldnt. The someOtherMethod() signature
    // implies
    // that the type of the component of the ist should be a subtype of the type
    // used
    // for obj. However, in this case first is a List<A> and A clearly isnt a
    // subtype
    // of B. Is this a bug?
    System.out.print("\n12) ");
    someOtherMethod(new B(), listOfA);
    // Really weird as the two types arent even remotely related. This should
    // probably
    // be rejected by the compiler but it doesnt seem to be enforcing its
    // bounds.
    System.out.print("\n13) ");
    List<String> listOfString = new ArrayList<String>();
    listOfString.add("Hello");
    someOtherMethod(new Integer(5), listOfString);
    // Doesnt work even though the spec says it should:
    // System.out.print(I"14)");
    // A value = <A>someMethod(new B(), new ArrayList<A>());
    // Picks Fourth: The type of the list returned by SomeMethod is
    // List<Integer>
    System.out.print("\n15) ");
    someMethod(5, someMethod());
    // Picks Fourth: The type of the list returned by SomeMethod is List<String>
    System.out.print("\n16) ");
    someMethod("Hello", someMethod());
  }
  private static class A {
  }
  private static class B extends A {
  }
  private static class C extends B {
  }
}
/* ########## End of File ########## */
```
