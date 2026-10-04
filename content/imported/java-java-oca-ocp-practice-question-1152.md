---
title: Java OCA OCP Practice Question 1152
nav: Java OCA OCP Practice Ques...
description: To understand how this loop works let us put some extra print statements in the innermost loop :
section: Imported - java2s Archive
order: 1121
source: https://web.archive.org/web/20210101014724/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1152.html
---
## Question

What will the following program print?

```java title=Example.java
publicclass Main{
    publicstaticvoid main (String args [])  {
        int counter = 0;
        outer: for  (int i = 0; i < 3; i++)  {
            middle:
            for  (int j = 0; j < 3; j++)  {
                inner:
                for  (int k = 0; k < 3; k++)  {
                    if  (k - j > 0)  {
                        break middle;
                     }
                    counter++;
                 }
             }
         }
        System.out.println (counter);
     }
}
```

Select 1 option

- A. 2
- B. 3
- C. 6
- D. 7
- E. 9

```java title=Example.java
Correct Option is  : B
```

## Note

To understand how this loop works let us put some extra print statements in the innermost loop :

```java title=Example.java
System.out.println ("i="+i+" j="+j+" k="+k);
if (k-j>0){
     System.out.println ("breaking middle "+j);
     break middle;
}
counter++;
```

This is what it prints:

```java title=Example.java
i=0 j=0 k=0
i=0 j=0 k=1
breaking middle 0
i=1 j=0 k=0
i=1 j=0 k=1
breaking middle 0
i=2 j=0 k=0
i=2 j=0 k=1
breaking middle 0
3
```

The key is that the middle loop is broken as soon as k-j becomes > 0.

This happens on every second iteration of inner loop when k is 1 and j is 0.

When middle is broken inner cannot continue. So the next iteration of outer starts.

PreviousNext

## Related

- Java OCA OCP Practice Question 1149
- Java OCA OCP Practice Question 1150
- Java OCA OCP Practice Question 1151
- Java OCA OCP Practice Question 1153
- Java OCA OCP Practice Question 1154
