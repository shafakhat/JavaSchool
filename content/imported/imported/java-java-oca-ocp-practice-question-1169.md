---
title: Java OCA OCP Practice Question 1169
nav: Java OCA OCP Practice Ques...
description: What will be the result of attempting to compile and run the following code?
section: Imported - java2s Archive
order: 1136
source: https://web.archive.org/web/20210101014727/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1169.html
---
## Question

What will be the result of attempting to compile and run the following code?

```java title=Example.java
publicclass Main {
   publicstaticvoid main(String args[]) {
      int i = 5;//fromwww.java2s.comfloat f = 5.5f;
      double d = 3.8;
      char c = 'a';
      if (i == f)
         c++;
      if (((int) (f + d)) == ((int) f + (int) d))
         c += 2;
      System.out.println(c);
   }
}
```

Select 1 option

- A. The code will fail to compile.
- B. It will print d.
- C. It will print c.
- D. It will print b
- E. It will print a.

```java title=Example.java
Correct Option is  : E
```

## Note

In the case of i == f, value of i will be promoted to a float i.e. 5.0, and so it returns false.

```java title=Example.java

(int)f+(int)d =  (int)5.5 + (int) 3.8 => 5 + 3 = 8

(int)(f + d) => (int) (5.5 + 3.8) => (int)(9.3) => 9,
```

so this also return false.

c is not incremented at all. Hence c remains 'a'.

PreviousNext

## Related

- Java OCA OCP Practice Question 1166
- Java OCA OCP Practice Question 1167
- Java OCA OCP Practice Question 1168
- Java OCA OCP Practice Question 1170
- Java OCA OCP Practice Question 1171
