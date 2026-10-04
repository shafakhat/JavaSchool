---
title: Java Regular Expression Tutorial - Java Pattern Matcher
nav: Java Regular Expression Tu...
description: The package java.util.regex contains three classes to support the full version of regular expressions.
section: Imported - java2s Archive
order: 50381
source: https://www.java2s.com/Tutorials/Java/Java_Regular_Expression/0030__Java_Regex_Pattern.html
---
```java title=Example.java
```

The package java.util.regex contains three classes to support the full version of regular expressions.

- Pattern
- Matcher
- PatternSyntaxException

A Pattern holds the compiled form of a regular expression.

A Matcher associates the string to be matched with a Pattern and it performs the actual match.

A PatternSyntaxException represents an error in a malformed regular expression.

## Compiling Regular Expressions

A Pattern which has no public constructor is immutable and can be shared.

Pattern class contains a static compile() method, which returns a Pattern object.

The compile() method is overloaded.

```java title=Example.java
static Pattern  compile(String regex)
static Pattern compile(String regex, int flags)
```

The following code compiles a regular expression into a Pattern object:

```java title=Example.java
import java.util.regex.Pattern;
publicclass Main {
  publicstatic void main(String[] args) {
    // Prepare a regular expression
    String regex = "[a-z]@.";
    // Compile the regular expression into a Pattern object
    Pattern p = Pattern.compile(regex);
  }
}
```

The second version of the compile() method sets flags that modify the way the pattern is matched.

The flags parameter is a bit mask and defines as int constants in the Pattern class.

Flag  Description
---  ---
Pattern.CANON_EQ  Enables canonical equivalence.
Pattern.CASE_INSENSITIVE  Enables case-insensitive matching.
Pattern.COMMENTS  Permits whitespace and comments in pattern. ignore whitespace and embedded comments starting with # until the end of a line.
Pattern.DOTALL  Enables dotall mode. By default, . does not match line terminators. When this flag is set, . matches a line terminator.
Pattern.LITERAL  Enables literal parsing of the pattern. This flag makes metacharacters and escape sequences as normal character.
Pattern.MULTILINE  Enables multiline mode. By default, ^ and $ match the beginning and the end of the input sequence. This flag makes pattern only match line by line or the end of the input sequence.
Pattern.UNICODE_CASE  Enables Unicode-aware case. Together with the CASE_INSENSITIVE flag, the case-insensitive matching can be performed according to the Unicode Standard.
Pattern.UNICODE_ CHARACTER_CLASS  Enables the Unicode version of predefined character classes and POSIX character classes. When this flag is set, the Predefined character classes and POSIX character classes are in conformance with Unicode Technical Standard.
Pattern.UNIX_LINES  Enables Unix lines mode. When this flag is set, only the \n character is recognized as a line terminator.

## Example

The following code compiles a regular expression setting the CASE_INSENSTIVE and DOTALL flags.

```java title=Example.java
import java.util.regex.Pattern;
publicclass Main {
  publicstatic void main(String[] args) {
    String regex   = "[a-z]@.";
    Pattern p  = Pattern.compile(regex,  Pattern.CASE_INSENSITIVE|Pattern.DOTALL);
  }
}
```

## Example 2

```java title=Example.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
publicclass Main {
  publicstaticvoid main(String args[]) {
    Pattern p = Pattern.compile("java", Pattern.CASE_INSENSITIVE);
    String candidateString = "Java. java JAVA jAVA";
    Matcher matcher = p.matcher(candidateString);
    // display the latter match
    System.out.println(candidateString);
    matcher.find(11);
    System.out.println(matcher.group());
    // display the earlier match
    System.out.println(candidateString);
    matcher.find(0);
    System.out.println(matcher.group());
  }
}
```

The code above generates the following result.

- « Previous
