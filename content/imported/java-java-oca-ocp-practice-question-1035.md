---
title: Java OCA OCP Practice Question 1035
nav: Java OCA OCP Practice Ques...
description: class Main{ /*www.java2s.com*/void m (int... x) { System.out.println ("In ..."); } //1 void m (Integer x) { System.out.println ("In Integer"); } //2 void m (long x)
section: Imported - java2s Archive
order: 1016
source: https://web.archive.org/web/20210101014705/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1035.html
---
## Question

Consider the following class...

```java title=Example.java
class Main{ void m (int... x)  { System.out.println ("In  ...");  }  //1 void m (Integer x)  { System.out.println ("In Integer");  } //2 void m (long x)  { System.out.println ("In long");  } //3  void m (Long x)  { System.out.println ("In LONG");  } //4 publicstaticvoid main (String [] args){
        Integer a = 4; new Main ().m (a); //5 int b = 4; new Main ().m (b); //6
     }
}
```

What will it print when compiled and run?

Select 2 options

- A. In Integer and In long
- B. In ... and In LONG, if //2 and //3 are commented out.
- C. In Integer and In ..., if //4 is commented out.
- D. It will not compile, if // 1, //2, and //3 are commented out.
- E. In LONG and In long, if // 1 and //2 are commented out.

```java title=Example.java
Correct Options are  : A D
```

## Note

The compiler always tries to choose the most specific method available with least number of modifications to the arguments.

Widening is preferred to boxing/unboxing, which in turn, is preferred over var-args.

PreviousNext

## Related

- Java OCA OCP Practice Question 1032
- Java OCA OCP Practice Question 1033
- Java OCA OCP Practice Question 1034
- Java OCA OCP Practice Question 1036
- Java OCA OCP Practice Question 1037
