---
title: Java Tutorial - Java Switch
nav: Java Tutorial - Java Switch
description: The switch statement is a multiway branch statement. It provides a better alternative than a large series of if-else-if statements.
section: Imported - java2s Archive
order: 50433
source: https://www.java2s.com/Tutorials/Java/Java_Language/4020__Java_switch.html
---
```java title=Example.java
```

The switch statement is a multiway branch statement. It provides a better alternative than a large series of if-else-if statements.

## Java switch Statement

Here is the general form of a switch statement:

```java title=Example.java
switch (expression) {
case value1:
    statement sequence
    break;
case value2:
    statement sequence
    break;
.
.
.
case valueN:
    statement sequence
    break;
default:
    default statement sequence
}
```

The value1 to valueN are the possible case values for expression. Duplicate case values are not allowed.

A break statement jumps out of switch statement to the first line that follows the entire switch statement.

Here is a simple example that uses a switch statement:

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String args[]) {
    for (int i = 0; i < 6; i++)
      switch (i) {
        case 0://fromwww.java2s.com
          System.out.println("i is zero.");
          break;
        case 1:
          System.out.println("i is one.");
          break;
        case 2:
          System.out.println("i is two.");
          break;
        case 3:
          System.out.println("i is three.");
          break;
        default:
          System.out.println("i is greater than 3.");
      }
  }
}
```

The output produced by this program is shown here:

## Example

The break statement is optional. If you omit the break, execution will continue on into the next case. For example, consider the following program:

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String args[]) {
    for (int i = 0; i < 12; i++)
      switch (i) {
        case 0:/*www.java2s.com*/case 1:
        case 2:
        case 3:
        case 4:
          System.out.println("i is less than 5");
          break;
        case 5:
        case 6:
        case 7:
        case 8:
        case 9:
          System.out.println("i is less than 10");
          break;
        default:
          System.out.println("i is 10 or more");
      }
  }
}
```

This program generates the following output:

## Example 2

Java supports the nested switch statements. For example, the following fragment is a valid nested switch statement.

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String args[]) {
    for (int i = 0; i < 6; i++)
      switch(i) {
        case 0: //www.java2s.comswitch(i+1) { // nested switch
case 0:
              System.out.println("target is zero");
              break;
            case 1:
              System.out.println("target is one");
              break;
          }
          break;
        case 2: // ...
     }
  }
}
```

The output:

## Example 3

The following code shows how to switch with char value.

```java title=Example.java
//fromwww.java2s.comimport java.util.Scanner;
publicclass Main {
  static Scanner sc = new Scanner(System.in);
  publicstaticvoid main(String[] args) {
    char p = 'a';
    String details = "";
    switch (p) {
    case'E':
    case'e':
      details += "\tE...\n";
    case'D':
    case'd':
      details += "\tD...\n";
    case'C':
    case'c':
      details += "\tC...\n";
    case'B':
    case'b':
      details += "\tB...\n";
    case'A':
    case'a':
      details += "\tA.\n";
      break;
    default:
      details = "That's";
      break;
    }
    System.out.println(details);
  }
}
```

The code above generates the following result.

## Example 4

The following code shows how to use string literals in switch statements.

```java title=Example.java
//fromwww.java2s.compublicclass Main {
  publicstaticvoid main(String[] args) {
    String[] data = new String[]{"a","b","java2s.com"};
    for (String argument : data) {
      switch (argument) {
      case"a":
      case"b":
        System.out.println("a or b");
        break;
      case"java2s.com":
        System.out.println("java2s.com");
        break;
      case"-help":
        System.out.println("displayHelp");
        break;
      default:
        System.out.println("Illegal command line argument");
      }
    }
  }
}
```

The code above generates the following result.

- « Previous
