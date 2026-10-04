---
title: Java Regular Expression Tutorial - Java Regex Matcher
nav: Java Regular Expression Tu...
description: Matcher class performs a match on a sequence of characters by interpreting the compiled pattern defined in a Pattern object.
section: Imported - java2s Archive
order: 50382
source: https://www.java2s.com/Tutorials/Java/Java_Regular_Expression/0040__Java_Regex_Matcher.html
---
```java title=Example.java
```

Matcher class performs a match on a sequence of characters by interpreting the compiled pattern defined in a Pattern object.

The matcher() method of the Pattern class creates an instance of the Matcher class.

```java title=Example.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
publicclass Main {
  publicstaticvoid main(String[] args) {
    String regex   = "[a-z]@.";
    Pattern p  = Pattern.compile(regex);
    String str = "abc@yahoo.com,123@cnn.com,abc@google.com";
    Matcher  m   = p.matcher(str);
  }
}
```

The following methods of the Matcher performs the match.

- find() method
- start() method
- end() method
- group() method

## find method

The find() method finds a match for the pattern in the input.

If the find succeeds, it returns true. Otherwise, it returns false.

The first call to find() starts the search at the beginning of the input. The next call would start the search after the previous match.

We can use while loop with find() method to find all the matches.

find() method is an overloaded method. Another version of the find() method takes an integer argument, which is the offset to start the find for a match.

## start() method

The start() method returns the start index of the previous match. It is used after a successful find() method call.

## end() method

The end() method returns the index of the last character in the matched string plus one.

After a match, str.substring(m.start(), m.end()) gives you the matched string.

```java title=Example.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
publicclass Main {
  publicstaticvoid main(String[] args) {
    String regex   = "[a-z]@.";
    Pattern p  = Pattern.compile(regex);
    String str = "abc@yahoo.com,123@cnn.com,abc@google.com";
    Matcher  m   = p.matcher(str);
    if (m.find())  {
      String  foundStr = str.substring(m.start(),  m.end());
      System.out.println("Found string  is:" + foundStr);
    }
  }
}
```

The code above generates the following result.

## group() method

The group() method returns the found string by the previous successful find() method call.

```java title=Example.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
publicclass Main {
  publicstaticvoid main(String[] args) {
    String regex = "[a-z]@.";
    Pattern p = Pattern.compile(regex);
    String str = "abc@yahoo.com,123@cnn.com,abc@google.com";
    Matcher m = p.matcher(str);
    if (m.find()) {
      String foundStr = m.group();
      System.out.println("Found text is:" + foundStr);
    }
  }
}
```

The code above generates the following result.

## Example

```java title=Example.java
import java.util.regex.Pattern;
import java.util.regex.Matcher;
publicclass Main {
  publicstaticvoid main(String[] args) {
    String regex = "[abc]@.";
    String source = "abc@example.com";
    findPattern(regex, source);
  }
  publicstaticvoid findPattern(String regex, String source) {
    Pattern p = Pattern.compile(regex);
    Matcher m = p.matcher(source);
    System.out.println("Regex:" + regex);
    System.out.println("Text:" + source);
    while (m.find()) {
      System.out.println("Matched  Text:" + m.group() + ", Start:" + m.start()
          + ", " + "End:" + m.end());
    }
  }
}
```

The code above generates the following result.

- « Previous
