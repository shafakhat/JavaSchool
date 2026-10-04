---
title: Java OCA OCP Practice Question 1102
nav: Java OCA OCP Practice Ques...
description: Which of the following can be inserted in the blank to make the code compile?
section: Imported - java2s Archive
order: 1083
source: https://web.archive.org/web/20210101014716/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1102.html
---
## Question

Which of the following can be inserted in the blank to make the code compile?

Choose all that apply

```java title=Example.java
publicstaticvoid main(String[] args) {
 try {
   System.out.println("work real hard");
 } catch (                        e) {
 } catch (RuntimeException e) {
 }
}
```

- A. Exception
- B. IOException
- C. IllegalArgumentException
- D. RuntimeException
- E. StackOverflowError
- F. None of the above.

```java title=Example.java
C, E.
```

## Note

Option C is allowed because it is a more specific type than RuntimeException.

Option E is allowed because it isn't in the same inheritance tree as RuntimeException.

It's not a good idea to catch either of these.

Option B is not allowed because the method called inside the try block doesn't declare an IOException to be thrown.

The compiler realizes that IOException would be an unreachable catch block.

Option D is not allowed because the same exception can't be specified in two different catch blocks.

Finally, option A is not allowed because it's more general than RuntimeException and would make that block unreachable.

PreviousNext

## Related

- Java OCA OCP Practice Question 1099
- Java OCA OCP Practice Question 1100
- Java OCA OCP Practice Question 1101
- Java OCA OCP Practice Question 1103
- Java OCA OCP Practice Question 1104
