---
title: The switch Statement
nav: The switch Statement
description: An alternative to a series of else if is the switch statement. The switch statement allows you to choose a block of statements to run from a selection of code, based on t
section: Imported - java2s Archive
order: 1173
source: https://web.archive.org/web/20140829080809/http://www.java2s.com/Tutorial/Java/0080__Statement-Control/TheswitchStatement.htm
---
An alternative to a series of else if is the switch statement. The switch statement allows you to choose a block of statements to run from a selection of code, based on the return value of an expression. The expression used in the switch statement must return an int or an enumerated value.
The syntax of the switch statement is as follows.

```java title=Example.java
switch (expression) {
case value_1 :
     statement (s);
     break;
case value_2 :
     statement (s);
     break;
  .
  .
  .
case value_n :
     statement (s);
     break;
default:
     statement (s);
}
```

Failure to add a break statement after a case will not generate a compile error but may have more serious consequences because the statements on the next case will be executed.
Here is an example of the switch statement:

```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    int i = 1;
    switch (i) {
    case 1 :
        System.out.println("One.");
        break;
    case 2 :
        System.out.println("Two.");
        break;
    case 3 :
        System.out.println("Three.");
        break;
    default:
        System.out.println("You did not enter a valid value.");
    }
  }
}
```
