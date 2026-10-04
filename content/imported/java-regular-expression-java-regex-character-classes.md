---
title: Java Regular Expression Tutorial - Java Regex Metacharacters
nav: Java Regular Expression Tu...
description: Metacharacters are characters with special meanings in Java regular expression.
section: Imported - java2s Archive
order: 50380
source: https://www.java2s.com/Tutorials/Java/Java_Regular_Expression/0020__Java_Regex_Character_Classes.html
---
```java title=Example.java
```

Metacharacters are characters with special meanings in Java regular expression.

The metacharacters supported by the regular expressions in Java are as follows:

```java title=Example.java
( ) [ ] { { \ ^ $ | ? * + . < > - = !
```

## Character Classes

The metacharacters [ and ] specifies a character class inside a regular expression.

A character class is a set of characters. The regular expression engine will attempt to match one character from the set.

The character class "[ABC]" will match characters A, B, or C. For example, the strings "woman" or "women" will match the regular expression "wom[ae]n".

We can specify a range of characters using a character class.

The range is expressed using a hyphen - character.

For example, [A-Z] represents any uppercase English letters; "[0-9]" represents any digit between 0 and 9.

^ means not.

For example, [^ABC] means any character except A, B, and C.

The character class [^A-Z] represents any character except uppercase letters.

If ^ appears in a character class except in the beginning, it just matches a ^ character.

For example, "[ABC^]" will match A, B, C, or ^.

You can also include two or more ranges in one character class. For example, [a-zA-Z] matches any character a through z and A through Z.

[a-zA-Z0-9] matches any character a through z (uppercase and lowercase), and any digit 0 through 9.

The following table has examples of Character Classes

Character Classes  Meaning
[abc]  Character a, b, or c
[^xyz]  A character except x, y, and z
[a-z]
[a-cx-z]  Characters a through c, or x through z, which would include a, b, c, x, y, or z.
[0-9&&[4-8]]  Intersection of two ranges (4, 5, 6, 7, or 8)
[a-z&&[^aeiou]]  All lowercase letters minus vowels

## Predefined Character Classes

The following table lists some frequently used predefined character classes.

Meaning
.  Any character
\d  A digit. Same as [0-9]
\D  A non-digit. Same as [^0-9]
\s  A whitespace character. Same as [ \t\n\x0B\f\r] which include. a space a tab a new line a vertical tab a form feed a carriage return characters
\S  A non-whitespace character. Same as [^\s]
\w  A word character. Same as [a-zA-Z_0-9].
\W  A non-word character. Same as [^\w]

## Example

The following code uses \d to match all digits.

\\d is used in the string to escape the \.

```java title=Example.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
publicclass Main {
  publicstaticvoid main(String args[]) {
    Pattern p = Pattern.compile("Java \\d");
    String candidate = "Java 4";
    Matcher m = p.matcher(candidate);
    if (m != null)
      System.out.println(m.find());
  }
}
```

The code above generates the following result.

## Example 2

The following code \w+ to match any word.

Double slash is used to escape \.

```java title=Example.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
publicclass Main {
  publicstaticvoid main(String args[]) {
    String regex = "\\w+";
    Pattern pattern = Pattern.compile(regex);
    String candidate = "asdf JavaSchool";
    Matcher matcher = pattern.matcher(candidate);
    if (matcher.find()) {
      System.out.println("GROUP 0:" + matcher.group(0));
    }
  }
}
```

The code above generates the following result.

- « Previous
