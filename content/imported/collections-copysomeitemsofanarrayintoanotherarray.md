---
title: Copy some items of an array into another array
nav: Copy some items of an arra...
description: Imported from the java2s.com archive: Copy some items of an array into another array
section: Imported - java2s Archive
order: 2482
source: https://web.archive.org/web/20140829082016/http://www.java2s.com/Tutorial/Java/0140__Collections/Copysomeitemsofanarrayintoanotherarray.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] args) {
    String[] letters = { "A", "I", "U", "E", "O" };
    String[] results = new String[3];
    System.arraycopy(letters, 2, results, 0, 3);
    for (int i = 0; i < results.length; i++) {
      System.out.println("result = " + results[i]);
    }
  }
}
```

| 9.5.1. | use Arrays.copyOf to copy array |
|---|---|
| 9.5.2. | Copying and Cloning Arrays |
| 9.5.3. | Doubling the size of an array |
| 9.5.4. | Array clone |
| 9.5.5. | Copy some items of an array into another array |
| 9.5.6. | Using Arrays.copyOf to copy an array |
| 9.5.7. | Copies the given array and adds the given element at the end of the new array. (long value type) |
