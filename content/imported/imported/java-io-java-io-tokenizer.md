---
title: Java IO Tutorial - Java Tokenizer
nav: Java IO Tutorial - Java To...
description: Java has some utility classes that let we break a string into parts called tokens.
section: Imported - java2s Archive
order: 50216
source: https://www.java2s.com/Tutorials/Java/Java_io/0740__Java_io_Tokenizer.html
---
```java title=Example.java
« Previous
```

- Next »

Java has some utility classes that let we break a string into parts called tokens.

We define the sequence of characters that are considered tokens by defining delimiter characters.

The StringTokenizer class is in the java.util package. The StreamTokenizer class is in the java.io package.

A StringTokenizer breaks a string into tokens whereas a StreamTokenizer gives we access to the tokens in a character-based stream.

## StringTokenizer

A StringTokenizer object breaks a string into tokens based on your definition of delimiters. It returns one token at a time.

We also have the ability to change the delimiter anytime. We can create a StringTokenizer by specifying the string and accepting the default delimiters, which are a space, a tab, a new line, a carriage return, and a line-feed character (" \t\n\r\f") as follows:

```java title=Example.java

StringTokenizer st  = new StringTokenizer("here is my string");
```

We can specify your own delimiters when we create a StringTokenizer as follows: The following code uses a space, a comma and a semi-colon as delimiters.

```java title=Example.java

String delimiters = " ,;";
StringTokenizer st  = new StringTokenizer("my text...",  delimiters);
```

We can use the hasMoreTokens() method to check if we have more tokens and the nextToken() method to get the next token from the string.

We can also use the split() method of the String class to split a string into tokens based on delimiters.

The split() method accepts a regular expression as a delimiter.

The following code shows how to use the StringTokenizer and the split() method of the String class.

```java title=Example.java
import java.util.StringTokenizer;
//www.java2s.compublicclass Main {
  publicstaticvoid main(String[] args) {
    String str = "This is a  test, this is another test.";
    String delimiters = "  ,"; // a space and a comma
    StringTokenizer st = new StringTokenizer(str, delimiters);
    System.out.println("Tokens  using a  StringTokenizer:");
    String token = null;
    while (st.hasMoreTokens()) {
      token = st.nextToken();
      System.out.println(token);
    }
  }
}
```

The code above generates the following result.

## StreamTokenizer

To distinguish between tokens based on their types, use the StreamTokenizer class.

```java title=Example.java
importstatic java.io.StreamTokenizer.TT_EOF;
importstatic java.io.StreamTokenizer.TT_NUMBER;
importstatic java.io.StreamTokenizer.TT_WORD;
//fromwww.java2s.comimport java.io.IOException;
import java.io.StreamTokenizer;
import java.io.StringReader;
publicclass Main {
  publicstaticvoid main(String[] args) throws Exception {
    String str = "This is a  test, 200.89  which  is  simple 50";
    StringReader sr = new StringReader(str);
    StreamTokenizer st = new StreamTokenizer(sr);
    try {
      while (st.nextToken() != TT_EOF) {
        switch (st.ttype) {
        case TT_WORD: /* a word has been read */
          System.out.println("String value: " + st.sval);
          break;
        case TT_NUMBER: /* a number has been read */
          System.out.println("Number value:  " + st.nval);
          break;
        }
      }
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
```

The program uses a StringReader object as the data source. We can use a FileReader object or any other Reader object as the data source.

The nextToken() method of StreamTokenizer is called repeatedly. It populates three fields of the StreamTokenizer object: ttype, sval, and nval. The ttype field indicates the token type that was read.

The following are the four possible values for the ttype field:

Field  Meanings
---  ---
TT_EOF  End of the stream has been reached.
TT_EOL  End of line has been reached.
TT_WORD  A word (a string) has been read as a token from the stream.
TT_NUMBER  A number has been read as a token from the stream.

If the ttype has TT_WORD, the string value is stored in its field sval.

If it returns TT_NUBMER, its number value is stored in nval field.

The code above generates the following result.

- Next »
- « Previous
