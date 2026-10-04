---
title: Variable Scope
nav: Variable Scope
description: The scope of a variable is the part of the program over which the variable name can be referenced. (from Ivor Horton's Beginning Java 2, JDK 5 Edition by Ivor Horton)
section: Imported - java2s Archive
order: 1005
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0020__Language/VariableScope.htm
---
The scope of a variable is the part of the program over which the variable name can be referenced. (from Ivor Horton's Beginning Java 2, JDK 5 Edition by Ivor Horton)

You cannot refer to a variable before its declaration.

You can declare variables in several different places:

- In a class body as class fields. Variables declared here are referred to as class-level variables.
- As parameters of a method or constructor.
- In a method's body or a constructor's body.
- Within a statement block, such as inside a while or for block.

Variable scope refers to the accessibility of a variable.

The rule 1 is that variables defined in a block are only accessible from within the block. The scope of the variable is the block in which it is defined. For example, consider the following for statement.

```java title=Example.java
publicclass MainClass {
  publicstaticvoid main(String[] args) {
    for (int x = 0; x < 5; x++) {
        System.out.println(x);
    }
  }
}
```

Rule number 2 is a nested block can access variables declared in the outer block. Consider this code.

```java title=Example.java
publicclass MainClass {
  publicstaticvoid main(String[] args) {
    for (int x = 0; x < 5; x++) {
        for (int y = 0; y < 3; y++) {
            System.out.println(x);
            System.out.println(y);
        }
    }
  }
}
```

Variables declared as method parameters can be accessed from within the method body. Class-level variables are accessible from anywhere in the class.

If a method declares a local variable that has the same name as a class-level variable, the former will 'shadow' the latter. To access the class-level variable from inside the method body, use the this keyword.
