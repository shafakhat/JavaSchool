---
title: How to shuffle an Java array
nav: How to shuffle an Java array
description: publicstaticvoid shuffle(final Object[] array, finallong seed) {
section: Imported - java2s Archive
order: 1032
source: https://web.archive.org/web/20130905081700/http://java2s.com/Tutorials/Java/Array/How_to_shuffle_an_Java_array.htm
---
In this chapter you will learn:

- Shuffle an array

### Shuffle an array

```java title=Example.java
import java.util.Random;
publicclass Main {
  publicstaticvoid shuffle(final Object[] array) {
    final Random r = new Random();
    finalint limit = array.length;
    for (int i = 0; i < limit; ++i) {
      swap(array, i, r.nextInt(limit));
    }
  }
  publicstaticvoid shuffle(finalint[] array) {
    final Random r = new Random();
    finalint limit = array.length;
    for (int i = 0; i < limit; ++i) {
      swap(array, i, r.nextInt(limit));
    }
  }
  publicstaticvoid shuffle(final Object[] array, finallong seed) {
    final Random r = new Random(seed);
    finalint limit = array.length;
    for (int i = 0; i < limit; ++i) {
      swap(array, i, r.nextInt(limit));
    }
  }
  publicstaticvoid swap(final Object[] array, finalint i, finalint j) {
    Object o = array[i];
    array[i] = array[j];
    array[j] = o;
  }
  publicstaticvoid swap(finalint[] array, finalint i, finalint j) {
    int o = array[i];
    array[i] = array[j];
    array[j] = o;
  }
}
```

#### Next chapter...

What you will learn in the next chapter:

- Append an object to an array.
- Append one array to another
