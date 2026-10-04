---
title: use Arrays.copyOf to copy array
nav: use Arrays.copyOf to copy ...
description: Imported from the java2s.com archive: use Arrays.copyOf to copy array
section: Imported - java2s Archive
order: 2486
source: https://web.archive.org/web/20140829082424/http://www.java2s.com/Tutorial/Java/0140__Collections/useArrayscopyOftocopyarray.htm
---
```java title=Example.java
import java.util.Arrays;
class MainClass
{
    public static void main(String args[])
    {
        int arrayOriginal[] = {42, 55, 21};
        int arrayNew[] =
            Arrays.copyOf(arrayOriginal, 3);
        printIntArray(arrayNew);
    }
    static void printIntArray(int arrayNew[])
    {
        for (int i : arrayNew)
        {
            System.out.print(i);
            System.out.print(' ');
        }
        System.out.println();
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
