---
title: Logical operators in action
nav: Logical operators in action
description: "Conditional AND (&&)", "false && false", ( false && false ),
section: Imported - java2s Archive
order: 1128
source: https://web.archive.org/web/20140829090524/http://www.java2s.com/Tutorial/Java/0060__Operators/Logicaloperatorsinaction.htm
---
```java title=Example.java
public class MainClass
{
   public static void main( String args[] )
   {
      // create truth table for && (conditional AND) operator
      System.out.printf( "%s\n%s: %b\n%s: %b\n%s: %b\n%s: %b\n\n",
         "Conditional AND (&&)", "false && false", ( false && false ),
         "false && true", ( false && true ),
         "true && false", ( true && false ),
         "true && true", ( true && true ) );
      // create truth table for || (conditional OR) operator
      System.out.printf( "%s\n%s: %b\n%s: %b\n%s: %b\n%s: %b\n\n",
         "Conditional OR (||)", "false || false", ( false || false ),
         "false || true", ( false || true ),
         "true || false", ( true || false ),
         "true || true", ( true || true ) );
      // create truth table for & (boolean logical AND) operator
      System.out.printf( "%s\n%s: %b\n%s: %b\n%s: %b\n%s: %b\n\n",
         "Boolean logical AND (&)", "false & false", ( false & false ),
         "false & true", ( false & true ),
         "true & false", ( true & false ),
         "true & true", ( true & true ) );
      // create truth table for | (boolean logical inclusive OR) operator
      System.out.printf( "%s\n%s: %b\n%s: %b\n%s: %b\n%s: %b\n\n",
         "Boolean logical inclusive OR (|)",
         "false | false", ( false | false ),
         "false | true", ( false | true ),
         "true | false", ( true | false ),
         "true | true", ( true | true ) );
      // create truth table for ^ (boolean logical exclusive OR) operator
      System.out.printf( "%s\n%s: %b\n%s: %b\n%s: %b\n%s: %b\n\n",
         "Boolean logical exclusive OR (^)",
         "false ^ false", ( false ^ false ),
         "false ^ true", ( false ^ true ),
         "true ^ false", ( true ^ false ),
         "true ^ true", ( true ^ true ) );
      // create truth table for ! (logical negation) operator
      System.out.printf( "%s\n%s: %b\n%s: %b\n", "Logical NOT (!)",
         "!false", ( !false ), "!true", ( !true ) );
   }
}
java title=Example.java
Conditional AND (&&)
false && false: false
false && true: false
true && false: false
true && true: true
Conditional OR (||)
false || false: false
false || true: true
true || false: true
true || true: true
Boolean logical AND (&)
false & false: false
false & true: false
true & false: false
true & true: true
Boolean logical inclusive OR (|)
false | false: false
false | true: true
true | false: true
true | true: true
Boolean logical exclusive OR (^)
false ^ false: false
false ^ true: true
true ^ false: true
true ^ true: false
Logical NOT (!)
!false: true
!true: false
```
