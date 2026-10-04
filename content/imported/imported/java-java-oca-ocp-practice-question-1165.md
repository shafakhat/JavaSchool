---
title: Java OCA OCP Practice Question 1165
nav: Java OCA OCP Practice Ques...
description: String color; /*fromwww.java2s.com*/public MyClass (double length){
section: Imported - java2s Archive
order: 1132
source: https://web.archive.org/web/20210101014726/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1165.html
---
## Question

Given:

```java title=Example.java
class MyClass  {
    privatedouble side = 0;
    String color; /*fromwww.java2s.com*/public MyClass (double length){
        this.side = length;
     }
    publicdouble getSide ()  {  return side;     }

    publicvoid setSide (double side)  {  this.side = side;    }

}

publicclass Main  {
    publicstaticvoid main (String [] args) throwsException  {
        MyClass mysq = new MyClass (10);
        mysq.color = "red";

        //set mysq's side to 20
     }
}
```

Which of the following statements will set mysq's side to 20?

Select 1 option

```java title=Example.java

A. mysq.side = 20;
B. mysq = new MyClass (20);
C. mysq.setSide (20);
D. side = 20;
E. MyClass.mysql.side = 20;
```

```java title=Example.java
Correct Option is  : C
```

## Note

Since side is a private variable, you cannot access it from outside MyClass class.

PreviousNext

## Related

- Java OCA OCP Practice Question 1162
- Java OCA OCP Practice Question 1163
- Java OCA OCP Practice Question 1164
- Java OCA OCP Practice Question 1166
- Java OCA OCP Practice Question 1167
