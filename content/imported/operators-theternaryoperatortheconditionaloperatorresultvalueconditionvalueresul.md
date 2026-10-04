---
title: The ternary operator (The Conditional Operator)
nav: The ternary operator (The ...
description: Imported from the java2s.com archive: The ternary operator (The Conditional Operator)
section: Imported - java2s Archive
order: 1125
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0060__Operators/TheternaryoperatorTheConditionalOperatorresultvalueconditionValueresult1result2.htm
---
```java title=Example.java
if(value > conditionValue){
  result = result1;
}else{
  result = result2;
}
 logical_expression ? expression1 : expression2
java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    int v = 1;
    System.out.println(v == 1 ? "A" : "B");
    v++;
    System.out.println(v == 1 ? "A" : "B");
  }
}
java title=Example.java
A
B
```
