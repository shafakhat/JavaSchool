---
title: Java Design Patterns Tutorial - Java Design Pattern - Interpreter Pattern
nav: Java Design Patterns Tutor...
description: We normally use Interpreter pattern to evaluate language grammar or expression.
section: Imported - java2s Archive
order: 50129
source: https://www.java2s.com/Tutorials/Java/Java_Design_Patterns/0200__Java_Interpreter_Pattern.html
---
```java title=Example.java
« Previous
```

- Next »

We normally use Interpreter pattern to evaluate language grammar or expression.

This type of pattern is one of the behavioral patterns.

## Example

```java title=Example.java
interface Expression {
  publicboolean evaluate(String context);
}//www.java2s.comclass IsInExpression implements Expression {
  private String data;
  public IsInExpression(String data) {
    this.data = data;
  }
  @Override
  publicboolean evaluate(String context) {
    if (context.contains(data)) {
      return true;
    }
    return false;
  }
}
class OrExpression implements Expression {
  private Expression expr1 = null;
  private Expression expr2 = null;
  public OrExpression(Expression expr1, Expression expr2) {
    this.expr1 = expr1;
    this.expr2 = expr2;
  }
  @Override
  publicboolean evaluate(String context) {
    return expr1.evaluate(context) || expr2.evaluate(context);
  }
}
class AndExpression implements Expression {
  private Expression expr1 = null;
  private Expression expr2 = null;
  public AndExpression(Expression expr1, Expression expr2) {
    this.expr1 = expr1;
    this.expr2 = expr2;
  }
  @Override
  publicboolean evaluate(String context) {
    return expr1.evaluate(context) && expr2.evaluate(context);
  }
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    Expression select = new IsInExpression("Select");
    Expression from = new IsInExpression("From");
    Expression isSelectFrom = new AndExpression(select, from);
    Expression insert = new IsInExpression("Insert");
    Expression update = new IsInExpression("Update");
    Expression isInsertOrUpdate = new OrExpression(insert, update);
    System.out.println(isSelectFrom.evaluate("Select"));
    System.out.println(isInsertOrUpdate.evaluate("Insert"));
    System.out.println(isSelectFrom.evaluate("Select From"));
    System.out.println(isInsertOrUpdate.evaluate("Update"));
  }
}
```

The code above generates the following result.

- Next »
- « Previous
