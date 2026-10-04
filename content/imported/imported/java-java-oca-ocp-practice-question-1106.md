---
title: Java OCA OCP Practice Question 1106
nav: Java OCA OCP Practice Ques...
description: What does the output of the following contain? (Choose all that apply)
section: Imported - java2s Archive
order: 1087
source: https://web.archive.org/web/20210101014717/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1106.html
---
## Question

What does the output of the following contain? (Choose all that apply)

```java title=Example.java

12: publicstaticvoid main(String[] args) {
13:   System.out.print("a");
14:   try { //fromwww.java2s.com
15:     System.out.print("b");
16:     thrownewIllegalArgumentException();
17:   } catch (IllegalArgumentException e) {
18:     System.out.print("c");
19:     thrownewRuntimeException("1");
20:   } catch (RuntimeException e) {
21:     System.out.print("d");
22:     thrownewRuntimeException("2");
23:   } finally {
24:     System.out.print("e");
25:     thrownewRuntimeException("3");
26:   }
27: }
```

```java title=Example.java

A.   abce
B.   abde
C.   An exception with the message set to  "1"
D.   An exception with the message set to  "2"
E.   An exception with the message set to  "3"
F.   Nothing; the code does not compile.
```

```java title=Example.java
A, E.
```

## Note

The code begins normally and prints a on line 13, followed by b on line 15.

On line 16, it throws an exception that's caught on line 17.

Remember, only the most specific matching catch is run.

Line 18 prints c, and then line 19 throws another exception.

Regardless, the finally block runs, printing e.

Since the finally block also throws an exception, that's the one printed.

PreviousNext

## Related

- Java OCA OCP Practice Question 1103
- Java OCA OCP Practice Question 1104
- Java OCA OCP Practice Question 1105
- Java OCA OCP Practice Question 1107
- Java OCA OCP Practice Question 1108
