---
title: Comments in general
nav: Comments in general
description: There are two types of comments in Java, both with syntax similar to comments in C and C++.
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0020__Language/Commentsingeneral.htm
---
It is good practice to write comments explaining your code.

There are two types of comments in Java, both with syntax similar to comments in C and C++.

- Traditional comments: Enclose a traditional comment in /* and */.
- End-of-line comments: Use double slashes (//) which causes the rest of the line ignored by the compiler.

Traditional comments do not nest, which means

```java title=Example.java
/*
  /* comment 1 */
  comment 2 */
```

- is invalid because the first */ after the first /* will terminate
- which will generate a compiler error

End-of-line comments can contain anything, including the sequences of characters /* and */, such as this:

```java title=Example.java
// /* this comment is okay */
```
