---
title: Java OCA OCP Practice Question 1039
nav: Java OCA OCP Practice Ques...
description: Given the following two declarations, which of the options will compile?
section: Imported - java2s Archive
order: 1005
source: https://web.archive.org/web/2016/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1039.html
---
## Question

Consider the following classes:

```java title=Example.java
class A  {
      public int getCode (){ return 2;}
}
class MySubClass extends A  {
  public void doStuff ()  {
   }
}
```

Given the following two declarations, which of the options will compile?

```java title=Example.java
A a = null;
MySubClass aa = null;
```

Select 4 options

```java title=Example.java
A. a =  (MySubClass)aa;
B. a = new MySubClass ();
C. aa = new A ();
D. aa =  (MySubClass) a;
E. aa = a;
F.  ((MySubClass)a).doStuff ();
java title=Example.java
Correct Options are  : A B D F
```

## Note

a is declared as a reference of class A and therefore, at run time, it is possible for a to point to an object of class MySubClass because A is a super class of MySubClass.

Hence, the compiler will not complain.

Although if a does not point to an object of class MySubClass at run time, a ClassCastException will be thrown.

A cast is required because the compiler needs to be assured that at run time a will point to an object of class MySubClass.

Once you cast a to MySubClass, you can call methods defined in MySubClass.

Of course, if a does not point to an object of class MySubClass at runtime, a ClassCastException will be thrown.

PreviousNext

## Related

- Java OCA OCP Practice Question 1036
- Java OCA OCP Practice Question 1037
- Java OCA OCP Practice Question 1038
- Java OCA OCP Practice Question 1040
- Java OCA OCP Practice Question 1041
