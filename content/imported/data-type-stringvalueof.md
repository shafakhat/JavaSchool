---
title: String.ValueOf
nav: String.ValueOf
description: Object objectRef = "hello"; // assign string to an Object reference
section: Imported - java2s Archive
order: 1328
source: https://web.archive.org/web/20140829085956/http://www.java2s.com/Tutorial/Java/0040__Data-Type/StringValueOf.htm
---
```java title=Example.java
public class MainClass
{
   public static void main( String args[] )
   {
      char charArray[] = { 'a', 'b', 'c', 'd', 'e', 'f' };
      boolean booleanValue = true;
      char characterValue = 'Z';
      int integerValue = 7;
      long longValue = 10000000000L; // L suffix indicates long
      float floatValue = 2.5f; // f indicates that 2.5 is a float
      double doubleValue = 33.333; // no suffix, double is default
      Object objectRef = "hello"; // assign string to an Object reference
      System.out.printf("char array = %s\n", String.valueOf( charArray ) );
      System.out.printf("part of char array = %s\n",String.valueOf( charArray, 3, 3 ) );
      System.out.printf("boolean = %s\n", String.valueOf( booleanValue ) );
      System.out.printf("char = %s\n", String.valueOf( characterValue ) );
      System.out.printf("int = %s\n", String.valueOf( integerValue ) );
      System.out.printf("long = %s\n", String.valueOf( longValue ) );
      System.out.printf("float = %s\n", String.valueOf( floatValue ) );
      System.out.printf("double = %s\n", String.valueOf( doubleValue ) );
      System.out.printf("Object = %s\n", String.valueOf( objectRef ) );
   } // end main
}
java title=Example.java
char array = abcdef
part of char array = def
boolean = true
char = Z
int = 7
long = 10000000000
float = 2.5
double = 33.333
Object = hello
```

| 2.36.1. | Number Parsing |
|---|---|
| 2.36.2. | Integer.valueOf: Converting String to Integer |
| 2.36.3. | Integer.parseInt(): Converting String to int |
| 2.36.4. | String.ValueOf |
| 2.36.5. | sums a list of numbers entered by the user |
| 2.36.6. | Convert string of time to time object |
| 2.36.7. | Converting a String to a byte Number |
| 2.36.8. | Converting a String to a short Number |
| 2.36.9. | Converting a String to a int(integer) Number |
| 2.36.10. | Convert a String to Date |
| 2.36.11. | Convert String to character array |
| 2.36.12. | Convert base64 string to a byte array |
| 2.36.13. | Parse basic types |
