---
title: The for Statement
nav: The for Statement
description: The for statement is like the while statement, i.e. you use it to create loop. The for statement has following syntax:
section: Imported - java2s Archive
order: 1011
source: https://web.archive.org/web/20070612233943/http://www.java2s.com:80/Tutorial/Java/0080__Statement-Control/TheforStatement.htm
---
The for statement is like the while statement, i.e. you use it to create loop. The for statement has following syntax:

```java title=Example.java
for ( init ; booleanExpression ; update ) {
    statement (s)
}
```

- init is an initialization that will be performed before the first iteration.
- booleanExpression is a boolean expression which will cause the execution of statement(s) if it evaluates to true.
- update is a statement that will be executed after the execution of the statement block.
- init, expression, and update are optional.

The for statement will stop only if one of the following conditions is met:

- booleanExpression evaluates to false
- A break or continue statement is executed
- A runtime error occurs.
