---
title: Java OCA OCP Practice Question 1082
nav: Java OCA OCP Practice Ques...
description: Both String variables are assigned the same string, "test string".
section: Imported - java2s Archive
order: 1063
source: https://web.archive.org/web/20210101014713/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1082.html
---
## Question

What will be the output of the following code?

```java title=Example.java
publicclass StringTest {
      publicstaticvoid main(String [] a) {
         String s1 = "test string";
         String s2 = "test string";
         if (s1 == s2) {
            System.out.println("same");
         } else {
            System.out.println("different");
         } //fromwww.java2s.com
      }
}
```

- A. The code will compile but not run.
- B. The code will not compile.
- C. "different" will be printed out to the console.
- D. "same" will be printed out to the console.
- E. None of the above.

```java title=Example.java
D.
```

## Note

Both String variables are assigned the same string, "test string".

Because these strings are not created using the new String() method.

The strings are placed in the string pool, and a reference to those strings is stored in the String variables.

Because the reference to the string pool is the same, the == comparison will return true.

If the strings were created using the new String() method, the references would be different and the == comparison would return false.

PreviousNext

## Related

- Java OCA OCP Practice Question 1079
- Java OCA OCP Practice Question 1080
- Java OCA OCP Practice Question 1081
- Java OCA OCP Practice Question 1083
- Java OCA OCP Practice Question 1084
