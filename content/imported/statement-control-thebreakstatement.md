---
title: The break Statement
nav: The break Statement
description: Imported from the java2s.com archive: The break Statement
section: Imported - java2s Archive
order: 1062
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0080__Statement-Control/ThebreakStatement.htm
---
- The break statement is used to break from an enclosing do, while, for, or switch statement.
- It is a compile error to use break anywhere else.
- 'break' breaks the loop without executing the rest of the statements in the block.

For example, consider the following code

```java title=Example.java
publicclass MainClass {
  publicstaticvoid main(String[] args) {
    int i = 0;
    while (true) {
        System.out.println(i);
        i++;
        if (i > 3) {
            break;
        }
    }
  }
}
```

The result is

```java title=Example.java
0
1
2
3
```
