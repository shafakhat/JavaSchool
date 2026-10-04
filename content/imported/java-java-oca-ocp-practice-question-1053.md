---
title: Java OCA OCP Practice Question 1053
nav: Java OCA OCP Practice Ques...
description: Had it been k-->0, it would imply, first compare k with 0, and then decrement k.
section: Imported - java2s Archive
order: 1033
source: https://web.archive.org/web/20210101014708/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1053.html
---
## Question

What will the following code print when compiled and run:

```java title=Example.java
publicclass Main  {
    publicstaticvoid main (String [] args){
        int k = 2;
        do{
            System.out.println (k);
        }while (--k>0);
     }
}
```

Select 1 option

```java title=Example.java
A.  1
B.  1
    0
C.  2
    1
D.  2
    1
    0
E. It will keeping printing numbers in an infinite loop.
F. It will not compile.
java title=Example.java
Correct Option is  : C
```

## Note

--k>0 implies, decrement the value of k and then compare with 0.

The loop will only execute twice, printing 2 and 1.

Had it been k-->0, it would imply, first compare k with 0, and then decrement k.

The loop would execute thrice, printing 2, 1, and 0.

PreviousNext

## Related

- Java OCA OCP Practice Question 1050
- Java OCA OCP Practice Question 1051
- Java OCA OCP Practice Question 1052
- Java OCA OCP Practice Question 1054
- Java OCA OCP Practice Question 1055
