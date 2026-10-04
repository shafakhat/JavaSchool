---
title: Java OCA OCP Practice Question 1121
nav: Java OCA OCP Practice Ques...
description: The while condition uses post increment operator, which means count is first compared with 11 (and based on this comparison a decision is made whether to execute the loop
section: Imported - java2s Archive
order: 1098
source: https://web.archive.org/web/20210101014719/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1121.html
---
## Question

What will the following code code print?

```java title=Example.java
publicclass Main {
   publicstaticvoid main(String args[]) {
      int count = 0, sum = 0;
      do {/*fromwww.java2s.com*/if (count % 3 == 0)
            continue;
         sum += count;
      } while (count++ < 11);
      System.out.println(sum);
   }
}
```

Select 1 option

- A. 49
- B. 48
- C. 37
- D. 36
- E. 38

```java title=Example.java
Correct Option is  : B
```

## Note

The while condition uses post increment operator, which means count is first compared with 11 (and based on this comparison a decision is made whether to execute the loop again or not) and then incremented. So when count is 10, the condition 10< 11 is true (that means the loop needs to be executed again) and count is incremented to 11.

When count is completely divisible by 3, (i.e. when count is 0, 3, 6, 9) sum+=count; is not executed.

The result is the summation of: 1 2 4 5 7 8 10 11

PreviousNext

## Related

- Java OCA OCP Practice Question 1118
- Java OCA OCP Practice Question 1119
- Java OCA OCP Practice Question 1120
- Java OCA OCP Practice Question 1122
- Java OCA OCP Practice Question 1123
