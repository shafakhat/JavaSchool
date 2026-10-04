---
title: Java OCA OCP Practice Question 1023
nav: Java OCA OCP Practice Ques...
description: This code compiles and runs without issue, outputting false, so option B is the correct answer.
section: Imported - java2s Archive
order: 1003
source: https://web.archive.org/web/20210101014703/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1023.html
---
## Question

What is the output of the following code?

```java title=Example.java
1: interface Checkable {
2:   defaultboolean check() { return true; }
3: }
4: publicclass Main implements Checkable {
5:   publicboolean check() { return false; }
6:     publicstaticvoid main(String[] args) {
7:     Checkable nocturnal = (Checkable)new Main();
8:     System.out.println(nocturnal.check());
9:     }
10: }
```

- A. true
- B. false
- C. The code will not compile because of line 2.
- D. The code will not compile because of line 5.
- E. The code will not compile because of line 7.
- F. The code will not compile because of line 8.

```java title=Example.java
B.
```

## Note

This code compiles and runs without issue, outputting false, so option B is the correct answer.

The first declaration of check() is as a default interface method, assumed public.

The second declaration of check() correctly overrides the default interface method.

Finally, the newly created Main instance may be automatically cast to a Checkable reference without an explicit cast, although adding it doesn't break the code.

PreviousNext

## Related

- Java OCA OCP Practice Question 1020
- Java OCA OCP Practice Question 1021
- Java OCA OCP Practice Question 1022
- Java OCA OCP Practice Question 1024
- Java OCA OCP Practice Question 1025
