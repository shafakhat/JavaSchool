---
title: Java OCA OCP Practice Question 1025
nav: Java OCA OCP Practice Ques...
description: 2: publicvoid printName(double input) { System.out.print("Printable"); }
section: Imported - java2s Archive
order: 1005
source: https://web.archive.org/web/20210101014704/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1025.html
---
## Question

What is the output of the following code?

```java title=Example.java
1: classPrintable
2:   publicvoid printName(double input) { System.out.print("Printable"); }
3: }
4: publicclass Main extendsPrintable {
5:   publicvoid printName(int input) { System.out.print("Main"); }
6:   publicstaticvoid main(String[] args) {
7:     Main m = new Main();
8:     m.printName(4);
9:     m.printName(9.0);
10:   }
11: }
java title=Example.java
A.  MainPrintable
B.  PrintableMain
C.  MainMain
D.  PrintablePrintable
E.  The code will not compile because of line 5.
F.  The code will not compile because of line 9.
java title=Example.java
A.
```

## Note

The code compiles and runs without issue, so options E and F are incorrect.

The printName() method is an overload in Main, not an override, so both methods may be called.

The call on line 8 references the version that takes an int as input defined in the Main class, and the call on line 9 references the version in the Printable class that takes a double.

Therefore, MainPrintable is output and option A is the correct answer.

PreviousNext

## Related

- Java OCA OCP Practice Question 1022
- Java OCA OCP Practice Question 1023
- Java OCA OCP Practice Question 1024
- Java OCA OCP Practice Question 1026
- Java OCA OCP Practice Question 1027
