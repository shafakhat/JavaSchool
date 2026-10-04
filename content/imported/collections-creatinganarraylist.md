---
title: Creating an ArrayList
nav: Creating an ArrayList
description: For the first two constructors, an empty array list is created. The initial capacity is ten unless explicitly specified by using the second constructor.
section: Imported - java2s Archive
order: 2399
source: https://web.archive.org/web/20140216225539/http://www.java2s.com/Tutorial/Java/0140__Collections/CreatinganArrayList.htm
---
For the first two constructors, an empty array list is created. The initial capacity is ten unless explicitly specified by using the second constructor.

```java title=Example.java
public ArrayList()
public ArrayList (int initialCapacity)
```

For Sun's reference implementation, the formula to increase capacity is newCapacity= (oldCapacity * 3)/2 + 1.
