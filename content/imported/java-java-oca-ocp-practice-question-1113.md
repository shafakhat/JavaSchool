---
title: Java OCA OCP Practice Question 1113
nav: Java OCA OCP Practice Ques...
description: On the first iteration through the outer loop, chars becomes 1 element.
section: Imported - java2s Archive
order: 1092
source: https://web.archive.org/web/20210101014718/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1113.html
---
## Question

What is the result of the following?

```java title=Example.java
int count = 10;
List<Character> chars = newArrayList<>();
do {
   chars.add('a');
   for (Character x : chars)
      count -=1;
} while (count > 0);
System.out.println(chars.size());
```

- A. 3
- B. 4
- C. The code does not compile.
- D. None of the above

```java title=Example.java
B.
```

## Note

On the first iteration through the outer loop, chars becomes 1 element.

The inner loop is run once and count becomes 9.

On the second iteration through the outer loop, chars becomes 2 elements.

The inner loop runs twice so count becomes 7.

On the third iteration through the outer loop, chars becomes 3 elements.

The inner loop runs three times so count becomes 4.

On the fourth iteration through the outer loop, chars becomes 4 elements.

The inner loop runs four times so count becomes 0.

Then both loops end.

Option B is correct.

PreviousNext

## Related

- Java OCA OCP Practice Question 1110
- Java OCA OCP Practice Question 1111
- Java OCA OCP Practice Question 1112
- Java OCA OCP Practice Question 1114
- Java OCA OCP Practice Question 1115
