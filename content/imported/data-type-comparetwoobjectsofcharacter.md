---
title: compare two objects of Character
nav: compare two objects of Cha...
description: * Copyright (c) 1995 - 2008 Sun Microsystems, Inc. All rights reserved.
section: Imported - java2s Archive
order: 1079
source: https://web.archive.org/web/20140829083129/http://www.java2s.com/Tutorial/Java/0040__Data-Type/comparetwoobjectsofCharacter.htm
---
```java title=Example.java
/*
 * Copyright (c) 1995 - 2008 Sun Microsystems, Inc.  All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 *
 *   - Redistributions of source code must retain the above copyright
 *     notice, this list of conditions and the following disclaimer.
 *
 *   - Redistributions in binary form must reproduce the above copyright
 *     notice, this list of conditions and the following disclaimer in the
 *     documentation and/or other materials provided with the distribution.
 *
 *   - Neither the name of Sun Microsystems nor the names of its
 *     contributors may be used to endorse or promote products derived
 *     from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
 * IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
 * THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
 * PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR
 * CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
 * PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
 * PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
 * LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
 * NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 * SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */
public class CharacterDemo {
  public static void main(String args[]) {
    Character a = new Character('a');
    Character a2 = new Character('a');
    Character b = new Character('b');
    int difference = a.compareTo(b);
    if (difference == 0) {
      System.out.println("a is equal to b.");
    } else if (difference < 0) {
      System.out.println("a is less than b.");
    } else if (difference > 0) {
      System.out.println("a is greater than b.");
    }
    System.out.println("a is " + ((a.equals(a2)) ? "equal" : "not equal")
        + " to a2.");
    System.out.println("The character " + a.toString() + " is "
        + (Character.isUpperCase(a.charValue()) ? "upper" : "lower") + "case.");
  }
}
```

| 2.7.1. | Java char: char is 16 bit type and used to represent Unicode characters. Range of char is 0 to 65,536. |
|---|---|
| 2.7.2. | Escape Sequence Characters |
| 2.7.3. | Storing Characters |
| 2.7.4. | Assign int value to char variable |
| 2.7.5. | char variables behave like integers |
| 2.7.6. | Display printable Characters |
| 2.7.7. | Character: is Upper Case |
| 2.7.8. | Character: is Lower Case |
| 2.7.9. | isDigit(): true if the argument is a digit (0 to 9), and false otherwise. |
| 2.7.10. | Validate if a String contains only numbers |
| 2.7.11. | isLetter(): true if the argument is a letter, and false otherwise. |
| 2.7.12. | Count letters in a String |
| 2.7.13. | isLetterOrDigit(): true if the argument is a letter or a digit, and false otherwise. |
| 2.7.14. | is White space |
| 2.7.15. | Is character a digit, letter, white space, lower case or upper case character |
| 2.7.16. | Convert character to digit with Character.digit |
| 2.7.17. | Demonstrate several Is... methods. |
| 2.7.18. | Convert from ASCII code to String |
| 2.7.19. | Convert from integer to ASCII code (byte) |
| 2.7.20. | To extract Ascii codes from a String |
| 2.7.21. | Copy char array to string |
| 2.7.22. | Store unicode in a char variable |
| 2.7.23. | Determining a Character's Unicode Block |
| 2.7.24. | Plus one to char variable |
| 2.7.25. | Convert string to char array |
| 2.7.26. | Compare Two Java char Arrays |
| 2.7.27. | Max and Min values of datatype char |
| 2.7.28. | Determining If a String Is a Legal Java Identifier |
| 2.7.29. | compare two objects of Character |
| 2.7.30. | ASCII character handling functions |
| 2.7.31. | Checks if the string contains only ASCII printable characters. |
| 2.7.32. | Checks whether the character is ASCII 7 bit alphabetic lower case. |
| 2.7.33. | Checks whether the character is ASCII 7 bit alphabetic upper case. |
| 2.7.34. | Checks whether the character is ASCII 7 bit alphabetic. |
| 2.7.35. | Checks whether the character is ASCII 7 bit control. |
| 2.7.36. | Checks whether the character is ASCII 7 bit numeric and character. |
| 2.7.37. | Checks whether the character is ASCII 7 bit numeric. |
| 2.7.38. | Checks whether the character is ASCII 7 bit printable. |
| 2.7.39. | Checks whether the character is ASCII 7 bit. |
| 2.7.40. | Determines if the specified string is permissible as a Java identifier. |
| 2.7.41. | Thansform an array of ASCII bytes to a string. the byte array should contains only values in [0, 127]. |
| 2.7.42. | Utility methods for ASCII character checking. |
