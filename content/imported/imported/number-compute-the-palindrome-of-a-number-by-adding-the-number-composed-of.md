---
title: Java Algorithms How to - Compute the Palindrome of a number by adding the number composed of
nav: Java Algorithms How to - C...
description: We would like to know how to compute the Palindrome of a number by adding the number composed of.
section: Imported - java2s Archive
order: 1019
source: https://web.archive.org/web/20150331235509/http://www.java2s.com:80/Tutorials/Java/Algorithms_How_to/Number/Compute_the_Palindrome_of_a_number_by_adding_the_number_composed_of.htm
---
```java title=Example.java
Back to Number  ↑
```

## Question

We would like to know how to compute the Palindrome of a number by adding the number composed of.

## Answer

```java title=Example.java
//www.java2s.comimport java.math.BigInteger;

/** Compute the Palindrome of a number by adding the number composed of
 * its digits in reverse order, until a Palindrome occurs.
 * e.g., 42->66 (42+24); 1951->5995 (1951+1591=3542; 3542+2453=5995).
 * <P>TODO: Do we need to handle negative numbers?
 * @author Ian Darwin, http://www.darwinsys.com/
 * @version $Id: PalindromeBig.java,v 1.3 2004/02/09 03:33:57 ian Exp $.
 */
publicclass Main {

  publicstaticboolean verbose = true;

  publicstaticvoid main(String[] argv) {
       BigInteger l = new BigInteger("9999999");
     System.out.println(findPalindrome(l));

  }

  /** find a palindromic number given a starting point, by
   * calling ourself until we get a number that is palindromic.
   */
  publicstatic BigInteger findPalindrome(BigInteger num) {
    if (num.compareTo(BigInteger.ZERO) < 0)
      thrownew IllegalStateException("negative");
    if (isPalindrome(num))
      return num;
    if (verbose)
      System.out.println("Trying " + num);
    return findPalindrome(num.add(reverseNumber(num)));
  }

  /** A ridiculously large number  */
  protectedstaticfinalint MAX_DIGITS = 255;

  /** Check if a number is palindromic. */
  publicstaticboolean isPalindrome(BigInteger num) {
    String digits = num.toString();
    int numDigits = digits.length();
    if (numDigits >= MAX_DIGITS) {
      thrownew IllegalStateException("too big");
    }
    // Consider any single digit to be as palindromic as can be
if (numDigits == 1)
      return true;
    for (int i=0; i<numDigits/2; i++) {
      // System.out.println(
//   digits.charAt(i) + " ? " + digits.charAt(numDigits - i - 1));
if (digits.charAt(i) != digits.charAt(numDigits - i - 1))
        return false;
    }
    return true;
  }

  static BigInteger reverseNumber(BigInteger num) {
    String digits = num.toString();
      int numDigits = digits.length();
    char[] sb = newchar[numDigits];
    for (int i=0; i<digits.length(); i++) {
      sb[i] = digits.charAt(numDigits - i - 1);
    }
    // Debug.println("rev",
//   "reverseNumber(" + digits + ") -> " + "\"" + sb + "\"");
returnnew BigInteger(new String(sb));
  }
}
```

```java title=Example.java
Back to Number  ↑
```
