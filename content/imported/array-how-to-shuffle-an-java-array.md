---
title: How to shuffle an Java array
nav: How to shuffle an Java array
description: public static void shuffle(final Object[] array, final long seed) {
section: Imported - java2s Archive
order: 1132
source: https://web.archive.org/web/2016/http://java2s.com/Tutorials/Java/Array/How_to_shuffle_an_Java_array.htm
---
In this chapter you will learn:

- Shuffle an array

### Shuffle an array

```java title=Example.java
import java.util.Random;
public class Main {
  public static void shuffle(final Object[] array) {
    final Random r = new Random();
    final int limit = array.length;
    for (int i = 0; i < limit; ++i) {
      swap(array, i, r.nextInt(limit));
    }
  }
  public static void shuffle(final int[] array) {
    final Random r = new Random();
    final int limit = array.length;
    for (int i = 0; i < limit; ++i) {
      swap(array, i, r.nextInt(limit));
    }
  }
  public static void shuffle(final Object[] array, final long seed) {
    final Random r = new Random(seed);
    final int limit = array.length;
    for (int i = 0; i < limit; ++i) {
      swap(array, i, r.nextInt(limit));
    }
  }
  public static void swap(final Object[] array, final int i, final int j) {
    Object o = array[i];
    array[i] = array[j];
    array[j] = o;
  }
  public static void swap(final int[] array, final int i, final int j) {
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
