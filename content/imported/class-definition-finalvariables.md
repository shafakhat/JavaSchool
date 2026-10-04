---
title: final Variables
nav: final Variables
description: You can prefix a variable declaration with the keyword final to make its value unchangeable. You can make both local variables and class fields final.
section: Imported - java2s Archive
order: 1025
source: https://web.archive.org/web/20070505041946/http://www.java2s.com:80/Tutorial/Java/0100__Class-Definition/finalVariables.htm
---
You can prefix a variable declaration with the keyword final to make its value unchangeable. You can make both local variables and class fields final.

```java title=Example.java
final int numberOfMonths = 12;
```

- Once assigned a value, the final value cannot change.
- Attempting to change it will result in a compile error.

```java title=Example.java
final float pi = (float) 22 / 7;
```

The casting (float) after 22 / 7 is needed to convert the value of division to float. Otherwise, an int will be returned and the pi variable will have a value of 3.0, instead of 3.1428.
