---
title: Java OCA OCP Practice Question 1177
nav: Java OCA OCP Practice Ques...
description: Which statements are true about comparing two instances of the same class,
section: Imported - java2s Archive
order: 1142
source: https://web.archive.org/web/20210101014728/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1177.html
---
## Question

Which statements are true about comparing two instances of the same class,

given that the equals() and hashCode() methods have been properly overridden?

Choose all that apply.

- A. If the equals() method returns true, the hashCode() comparison == might return false
- B. If the equals() method returns false, the hashCode() comparison == might return true
- C. If the hashCode() comparison == returns true, the equals() method must return true
- D. If the hashCode() comparison == returns true, the equals() method might return true
- E. If the hashCode() comparison != returns true, the equals() method might return true

```java title=Example.java
B and D.
```

## Note

B is true because often two dissimilar objects can return the same hash code value.

D is true because if the hashCode() comparison returns ==, the two objects might or might not be equal.

A, C, and E are incorrect.

C is incorrect because the hashCode() method is very flexible in its return values, and often two dissimilar objects can return the same hash code value.

A and E are a negation of the hashCode() and equals() contract.

PreviousNext

## Related

- Java OCA OCP Practice Question 1174
- Java OCA OCP Practice Question 1175
- Java OCA OCP Practice Question 1176
- Java OCA OCP Practice Question 1178
- Java OCA OCP Practice Question 1179
