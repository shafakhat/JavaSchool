---
title: The op= Operators
nav: The op= Operators
description: count += 5 has the same effect as the statement: count = count + 5;
section: Imported - java2s Archive
order: 1049
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0060__Operators/TheopOperators.htm
---
count += 5 has the same effect as the statement: count = count + 5;

```java title=Example.java
publicclass MainClass {
  publicstaticvoid main(String[] arg) {
    int count = 1;
    count += 5;
    System.out.println(count);
    count = count + 5;
    System.out.println(count);
  }
}
```

```java title=Example.java
6
11
```

The complete set of op= operators:

- +=
- -=
- *=
- /=
- %=
- < < =
- >>=
- >>>=
- &=
- |=
- ^=
