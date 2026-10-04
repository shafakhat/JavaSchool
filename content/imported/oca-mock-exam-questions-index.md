---
title: OCA Java SE 8 Mock Exam - OCA Mock Question 1
nav: OCA Java SE 8 Mock Exam - ...
description: The code compiles and runs without issue; therefore, E and F are incorrect.
section: Imported - java2s Archive
order: 50006
source: https://www.java2s.com/Tutorials/Java/OCA_Mock_Exam_Questions/index.html
---
## Question

What is the output of the following program?

```java title=Example.java
     1: publicclass Main {
     2:  publicstatic void main(String[] args) {
     3:    int x = 5, j = 0;
     4:    for(int i=0; i<3; )
     5:      INNER: do {
     6:        i++; x++;
     7:        if(x > 10) break INNER;
     8:        x += 4;
     9:        j++;
     10:      } while(j <= 2);
     11:    System.out.println(x);
     12: }
     13:}
```

- 10
- 12
- 13
- 17
- The code will not compile because of line 4.
- The code will not compile because of line 6.

## Answer

B.

## Note

The code compiles and runs without issue; therefore, E and F are incorrect.

The following code adds println to the statements and shows the result of code execution.

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    int x = 5, j = 0;
    for (int i = 0; i < 3;) {
      System.out.println("for x:"+x);
      System.out.println("for j:"+j);
      System.out.println("for i:"+i);
      INNER: do {
        System.out.println("while x:"+x);
        System.out.println("while j:"+j);
        System.out.println("while i:"+i);
        i++;
        x++;
        if (x > 10)
          break INNER;
        x += 4;
        j++;
      } while (j <= 2);
    }
    System.out.println(x);
  }
}
```

The code above generates the following result.
