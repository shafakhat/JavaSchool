---
title: All bitwise operators in action
nav: All bitwise operators in a...
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1154
source: https://web.archive.org/web/20140312143353/http://www.java2s.com/Tutorial/Java/0060__Operators/Allbitwiseoperatorsinaction.htm
---
```java title=Example.java
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
import java.util.Random;
public class MainClass {
  public static void main(String[] args) {
    Random rand = new Random();
    int i = rand.nextInt();
    int j = rand.nextInt();
    printBinaryInt("-1", -1);
    printBinaryInt("+1", +1);
    int maxpos = 2147483647;
    printBinaryInt("maxpos", maxpos);
    int maxneg = -2147483648;
    printBinaryInt("maxneg", maxneg);
    printBinaryInt("i", i);
    printBinaryInt("~i", ~i);
    printBinaryInt("-i", -i);
    printBinaryInt("j", j);
    printBinaryInt("i & j", i & j);
    printBinaryInt("i | j", i | j);
    printBinaryInt("i ^ j", i ^ j);
    printBinaryInt("i << 5", i << 5);
    printBinaryInt("i >> 5", i >> 5);
    printBinaryInt("(~i) >> 5", (~i) >> 5);
    printBinaryInt("i >>> 5", i >>> 5);
    printBinaryInt("(~i) >>> 5", (~i) >>> 5);
    long l = rand.nextLong();
    long m = rand.nextLong();
    printBinaryLong("-1L", -1L);
    printBinaryLong("+1L", +1L);
    long ll = 9223372036854775807L;
    printBinaryLong("maxpos", ll);
    long lln = -9223372036854775808L;
    printBinaryLong("maxneg", lln);
    printBinaryLong("l", l);
    printBinaryLong("~l", ~l);
    printBinaryLong("-l", -l);
    printBinaryLong("m", m);
    printBinaryLong("l & m", l & m);
    printBinaryLong("l | m", l | m);
    printBinaryLong("l ^ m", l ^ m);
    printBinaryLong("l << 5", l << 5);
    printBinaryLong("l >> 5", l >> 5);
    printBinaryLong("(~l) >> 5", (~l) >> 5);
    printBinaryLong("l >>> 5", l >>> 5);
    printBinaryLong("(~l) >>> 5", (~l) >>> 5);
  }
  static void printBinaryInt(String s, int i) {
    System.out.println(s + ", int: " + i + ", binary: ");
    System.out.print("   ");
    for (int j = 31; j >= 0; j--)
      if (((1 << j) & i) != 0)
        System.out.print("1");
      else
        System.out.print("0");
    System.out.println();
  }
  static void printBinaryLong(String s, long l) {
    System.out.println(s + ", long: " + l + ", binary: ");
    System.out.print("   ");
    for (int i = 63; i >= 0; i--)
      if (((1L << i) & l) != 0)
        System.out.print("1");
      else
        System.out.print("0");
    System.out.println();
  }
}
java title=Example.java
-1, int: -1, binary:
   11111111111111111111111111111111
+1, int: 1, binary:
   00000000000000000000000000000001
maxpos, int: 2147483647, binary:
   01111111111111111111111111111111
maxneg, int: -2147483648, binary:
   10000000000000000000000000000000
i, int: 907739811, binary:
   00110110000110110000001010100011
~i, int: -907739812, binary:
   11001001111001001111110101011100
-i, int: -907739811, binary:
   11001001111001001111110101011101
j, int: -1527787021, binary:
   10100100111011111101000111110011
i & j, int: 604700835, binary:
   00100100000010110000000010100011
i | j, int: -1224748045, binary:
   10110110111111111101001111110011
i ^ j, int: -1829448880, binary:
   10010010111101001101001101010000
i << 5, int: -1017097120, binary:
   11000011011000000101010001100000
i >> 5, int: 28366869, binary:
   00000001101100001101100000010101
(~i) >> 5, int: -28366870, binary:
   11111110010011110010011111101010
i >>> 5, int: 28366869, binary:
   00000001101100001101100000010101
(~i) >>> 5, int: 105850858, binary:
   00000110010011110010011111101010
-1L, long: -1, binary:
   1111111111111111111111111111111111111111111111111111111111111111
+1L, long: 1, binary:
   0000000000000000000000000000000000000000000000000000000000000001
maxpos, long: 9223372036854775807, binary:
   0111111111111111111111111111111111111111111111111111111111111111
maxneg, long: -9223372036854775808, binary:
   1000000000000000000000000000000000000000000000000000000000000000
l, long: 6929873296403828491, binary:
   0110000000101011110110110000110000001010100111011000111100001011
~l, long: -6929873296403828492, binary:
   1001111111010100001001001111001111110101011000100111000011110100
-l, long: -6929873296403828491, binary:
   1001111111010100001001001111001111110101011000100111000011110101
m, long: -352541115944271612, binary:
   1111101100011011100001011011100100001111011011000000000100000100
l & m, long: 6920767123913179392, binary:
   0110000000001011100000010000100000001010000011000000000100000000
l | m, long: -343434943453622513, binary:
   1111101100111011110111111011110100001111111111011000111100001111
l ^ m, long: -7264202067366801905, binary:
   1001101100110000010111101011010100000101111100011000111000001111
l << 5, long: 395016600407892320, binary:
   0000010101111011011000011000000101010011101100011110000101100000
l >> 5, long: 216558540512619640, binary:
   0000001100000001010111101101100001100000010101001110110001111000
(~l) >> 5, long: -216558540512619641, binary:
   1111110011111110101000010010011110011111101010110001001110000111
l >>> 5, long: 216558540512619640, binary:
   0000001100000001010111101101100001100000010101001110110001111000
(~l) >>> 5, long: 359902211790803847, binary:
   0000010011111110101000010010011110011111101010110001001110000111
```
