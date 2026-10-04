---
title: Java Regular Expression Tutorial - Java Regex Boundaries
nav: Java Regular Expression Tu...
description: To the match the beginning of a line, or match whole word, not part of any word, we have to set the boundary for matchers.
section: Imported - java2s Archive
order: 50384
source: https://www.java2s.com/Tutorials/Java/Java_Regular_Expression/0060__Java_Regex_Boundaries.html
---
```java title=Example.java
« Previous
```

- Next »

To the match the beginning of a line, or match whole word, not part of any word, we have to set the boundary for matchers.

The following table lists Boundary Matchers Inside Regular Expressions

Boundary Matchers  Meaning
---  ---
^  The beginning of a line
$  The end of a line
\b  A word boundary
\B  A non-word boundary
\A  The beginning of the input
\G  The end of previous match
\Z  The end of the input but for the final terminator, if any
\z  The end of the input

## Example

The following code demonstrates how to match a word boundary using a regular expression.

```java title=Example.java
//fromwww.java2s.compublicclass Main {
  publicstaticvoid main(String[] args) {
    // \\b to get \b inside the string literal.
    String regex = "\\bJava\\b";
    String replacementStr = "XML";
    String inputStr = "Java and Javascript";
    String newStr = inputStr.replaceAll(regex, replacementStr);
    System.out.println("Regular  Expression: " + regex);
    System.out.println("Input String: " + inputStr);
    System.out.println("Replacement String:  " + replacementStr);
    System.out.println("New String:  " + newStr);
  }
}
```

The code above generates the following result.

- Next »
- « Previous
