---
title: Java Regular Expression Tutorial - Java Regex Quantifiers
nav: Java Regular Expression Tu...
description: We can specify the number of times a character in a regular expression may match the sequence of characters.
section: Imported - java2s Archive
order: 50383
source: https://www.java2s.com/Tutorials/Java/Java_Regular_Expression/0050__Java_Regex_Quantifiers.html
---
We can specify the number of times a character in a regular expression may match the sequence of characters.

To express a pattern "one digit or more" using a regular expression, we can use the quantifiers.

Quantifiers and their meanings are listed in the following Table.

Quantifiers  Meaning
---  ---
*  Zero or more times
+  One or more times
?  Once or not at all
{m}  Exactly m times
{m,}  At least m times
{m, n}  At least m, but not more than n times

The quantifiers must follow a character or character class.

## Example

```java title=Example.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
publicclass Main {
  publicstaticvoid main(String[] args) {
    // A group of 3 digits followed by 7 digits.
    String regex = "\\b(\\d{3})\\d{7}\\b";
    // Compile the regular expression
    Pattern p = Pattern.compile(regex);
    String source = "12345678, 12345, and 9876543210";
    // Get the Matcher object
    Matcher m = p.matcher(source);
    // Start matching and display the found area codes
while (m.find()) {
      String phone = m.group();
      String areaCode = m.group(1);
      System.out.println("Phone: " + phone + ", Area  Code:  " + areaCode);
    }
  }
}
```

The code above generates the following result.

## Example 2

* matches zero or more d.

```java title=Example.java
import java.util.regex.Pattern;
publicclass Main {
  publicstaticvoid main(String args[]) {
    String regex = "ad*";
    String input = "add";
    boolean isMatch = Pattern.matches(regex, input);
    System.out.println(isMatch);
  }
}
```

The code above generates the following result.

- « Previous
