---
title: Java OCA OCP Practice Question 1161
nav: Java OCA OCP Practice Ques...
description: method1 () is overloading for three different argument types.
section: Imported - java2s Archive
order: 1128
source: https://web.archive.org/web/20210101014726/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1161.html
---
## Question

Given:

```java title=Example.java
class MyClass{ //fromwww.java2s.comvoid method1 (int x){
        System.out.println ("method1 int");
     }

    void method1 (double x){
        System.out.println ("method1 double");
     }

    void method1 (String x){
        System.out.println ("method1 String");
     }

}

publicclass Main  {
    publicstaticvoid main (String [] args) throwsException  {
        MyClass ot = new MyClass ();
        ot.method1 (1.0);
     }
}
```

What will be the output?

Select 1 option

- A. It will fail to compile.
- B. method1 int
- C. method1 double
- D. method1 String

```java title=Example.java
Correct Option is  : C
```

## Note

method1 () is overloading for three different argument types.

So when you call ot.method1 (1.0), the one with argument of type double will be invoked.

PreviousNext

## Related

- Java OCA OCP Practice Question 1158
- Java OCA OCP Practice Question 1159
- Java OCA OCP Practice Question 1160
- Java OCA OCP Practice Question 1162
- Java OCA OCP Practice Question 1163
