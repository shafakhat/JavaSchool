---
title: Java OCA OCP Practice Question 1057
nav: Java OCA OCP Practice Ques...
description: Consider the following two classes defined in two .java files.
section: Imported - java2s Archive
order: 1007
source: https://web.archive.org/web/2016/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1057.html
---
## Question

Consider the following two classes defined in two .java files.

```java title=Example.java
//in file /root/com/foo/X.java package com .foo;
public class X{
  public static int MyID = 10;
  public void apply (int i){
    System.out.println ("applied");
   }
}
//in file /root/com/bar/Y.java package com .bar;
//1  <== INSERT STATEMENT (s) HERE public class Y{
    public static void main (String [] args){
       System.out.println (X.MyID);
     }
}
```

What should be inserted at // 1 so that Y.java can compile without any error?

Select 1 option

```java title=Example.java
A. import static X;
B. import static com.foo.*;
C. import static com.foo.X .*;
D. import com .foo.*;
E. import com .foo.X .MyID;
java title=Example.java
Correct Option is  : D
```

## Note

A. and B. are wrong.

Bad syntax. Package import does not use static keyword.

C. is wrong.

This static import, although syntactically correct, will not help here because Y is accessing class X in X.MyID.

D. is correct. This is required because Y is accessing class X.

static import of MyID is NOT required because Y is accessing MyID through X ( X.MyID).

Had it been j ust System.out.println(MyID), only one import statement: import static com.foo.X.*; would have worked.

E. is wrong. Bad Syntax.

Syntax for importing static fields is: import static <package>.

<classname>.*; or import static <package>.<classname>.<fieldname>;

PreviousNext

## Related

- Java OCA OCP Practice Question 1054
- Java OCA OCP Practice Question 1055
- Java OCA OCP Practice Question 1056
- Java OCA OCP Practice Question 1058
- Java OCA OCP Practice Question 1059
