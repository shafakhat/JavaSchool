---
title: OCA Java SE 8 Mock Exam 2 - OCA Mock Question 1
nav: OCA Java SE 8 Mock Exam 2 ...
description: What will happen when you compile and run the following code?
section: Imported - java2s Archive
order: 50007
source: https://www.java2s.com/Tutorials/Java/OCA_Mock_Exam_Questions_2/index.html
---
- Next »

## Question

What will happen when you compile and run the following code?

```java title=Example.java
publicclass Main{
           private int i = 1;
           publicstatic void main(String argv[]){
              int i = 2;
              Main s = new Main ();
              s.someMethod();
           }
           publicstatic void someMethod(){
              System.out.println(i);
           }
         }
```

- 1 will be printed out
- 2 will be printed out
- A compile time error will be generated
- An exception will be thrown

## Answer

C

## Note

You cannot access an instance variable from a static method.

- Next »
