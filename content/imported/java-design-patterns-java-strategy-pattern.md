---
title: Java Design Patterns Tutorial - Java Design Pattern - Strategy Pattern
nav: Java Design Patterns Tutor...
description: In Strategy pattern, an algorithm can be changed at run time.
section: Imported - java2s Archive
order: 50132
source: https://www.java2s.com/Tutorials/Java/Java_Design_Patterns/0240__Java_Strategy_Pattern.html
---
```java title=Example.java
```

In Strategy pattern, an algorithm can be changed at run time.

Strategy pattern is a behavior pattern.

In Strategy pattern, we create objects to represent various algorithms and a context object to run the algorithm.

The strategy object changes the algorithm on the context object.

## Example

```java title=Example.java
interface MathAlgorithm {
   publicint calculate(int num1, int num2);
}class MathAdd implements MathAlgorithm{
   @Override
   publicint calculate(int num1, int num2) {
      return num1 + num2;
   }
}
class MathSubstract implements MathAlgorithm{
   @Override
   publicint calculate(int num1, int num2) {
      return num1 - num2;
   }
}
class MathMultiply implements MathAlgorithm{
   @Override
   publicint calculate(int num1, int num2) {
      return num1 * num2;
   }
}
class MathContext {
   private MathAlgorithm algorithm;
   public MathContext(MathAlgorithm strategy){
      this.algorithm = strategy;
   }
   publicint execute(int num1, int num2){
      return algorithm.calculate(num1, num2);
   }
}
publicclass Main {
   publicstaticvoid main(String[] args) {
      MathContext context = new MathContext(new MathAdd());
      System.out.println("10 + 5 = " + context.execute(10, 5));
      context = new MathContext(new MathSubstract());
      System.out.println("10 - 5 = " + context.execute(10, 5));
      context = new MathContext(new MathMultiply());
      System.out.println("10 * 5 = " + context.execute(10, 5));
   }
}
```

The code above generates the following result.

- « Previous
