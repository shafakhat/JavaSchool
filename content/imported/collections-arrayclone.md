---
title: Array clone
nav: Array clone
description: Imported from the java2s.com archive: Array clone
section: Imported - java2s Archive
order: 2481
source: https://web.archive.org/web/20140829082143/http://www.java2s.com/Tutorial/Java/0140__Collections/Arrayclone.htm
---
```java title=Example.java
public class MainClass {
  public static void main (String args[]) {
    int array1[] = {1, 2, 3, 4, 5};
    int[] clone = (int[]) array1.clone();
    for(int i: clone){
      System.out.println(i);
    }
  }
}
java title=Example.java
1
2
3
4
5
```

| 9.5.1. | use Arrays.copyOf to copy array |
|---|---|
| 9.5.2. | Copying and Cloning Arrays |
| 9.5.3. | Doubling the size of an array |
| 9.5.4. | Array clone |
| 9.5.5. | Copy some items of an array into another array |
| 9.5.6. | Using Arrays.copyOf to copy an array |
| 9.5.7. | Copies the given array and adds the given element at the end of the new array. (long value type) |
