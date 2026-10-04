---
title: Thansform an array of ASCII bytes to a string. the byte array should contains only values in [0, 127].
nav: Thansform an array of ASCI...
description: 2.7.41.Thansform an array of ASCII bytes to a string. the byte array should contains only values in [0, 127]. Previous / Next
section: Imported - java2s Archive
order: 1338
source: https://web.archive.org/web/20140309053613/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ThansformanarrayofASCIIbytestoastringthebytearrayshouldcontainsonlyvaluesin0127.htm
---
2.7.41.Thansform an array of ASCII bytes to a string. the byte array should contains only values in [0, 127]. Previous / Next

```java title=Example.java
import java.io.UnsupportedEncodingException;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
/*
 *  Licensed to the Apache Software Foundation (ASF) under one
 *  or more contributor license agreements.  See the NOTICE file
 *  distributed with this work for additional information
 *  regarding copyright ownership.  The ASF licenses this file
 *  to you under the Apache License, Version 2.0 (the
 *  "License"); you may not use this file except in compliance
 *  with the License.  You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing,
 *  software distributed under the License is distributed on an
 *  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 *  KIND, either express or implied.  See the License for the
 *  specific language governing permissions and limitations
 *  under the License.
 *
 */
/**
 * Various string manipulation methods that are more efficient then chaining
 * string operations: all is done in the same buffer without creating a bunch of
 * string objects.
 *
 * @author <a href="mailto:dev@labs.apache.org">Dungeon Project</a>
 */
public class Main {
  /**
   * Thansform an array of ASCII bytes to a string. the byte array should contains
   * only values in [0, 127].
   *
   * @param bytes The byte array to transform
   * @return The resulting string
   */
  public static String asciiBytesToString( byte[] bytes )
  {
      if ( (bytes == null) || (bytes.length == 0 ) )
      {
          return "";
      }
      char[] result = new char[bytes.length];
      for ( int i = 0; i < bytes.length; i++ )
      {
          result[i] = (char)bytes[i];
      }
      return new String( result );
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
