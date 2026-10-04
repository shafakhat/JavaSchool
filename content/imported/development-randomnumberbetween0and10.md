---
title: Random number between 0 AND 10
nav: Random number between 0 AN...
description: Imported from the java2s.com archive: Random number between 0 AND 10
section: Imported - java2s Archive
order: 1868
source: https://web.archive.org/web/20140829084301/http://www.java2s.com/Tutorial/Java/0120__Development/Randomnumberbetween0AND10.htm
---
```java title=Example.java
import java.util.Random;
public class Main {
  public static void main(String[] argv) {
    Random r = new Random();
    int randint = Math.abs(r.nextInt()) % 11;
    System.out.println(randint);
  }
}
```

| 6.37.1. | Generating Random integer Numbers |
|---|---|
| 6.37.2. | Roll a six-sided die 6000 times |
| 6.37.3. | Random integers that range from from 0 to n |
| 6.37.4. | Random bytes |
| 6.37.5. | Random boolean |
| 6.37.6. | Random long type number |
| 6.37.7. | Random float type number |
| 6.37.8. | Random double type number |
| 6.37.9. | Create two random number generators with the same seed |
| 6.37.10. | Random number between 0 AND 10 |
| 6.37.11. | Random numbers between 0.0 and 1.0 |
| 6.37.12. | Random.nextInt(n) returns a distributed int value between 0 (inclusive) and n (exclusive). |
| 6.37.13. | Generate a random array of numbers |
| 6.37.14. | Random Gaussian values. |
| 6.37.15. | Operations for random Strings |
