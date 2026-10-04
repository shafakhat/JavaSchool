---
title: Velocity Math Tool Round To Integer
nav: Velocity Math Tool Round T...
description: 4.45678 rounded to the nearest integer is $math.roundToInt("4.45678")
section: Imported - java2s Archive
order: 1087
source: https://web.archive.org/web/20071104045810/http://www.java2s.com:80/Code/Java/Velocity/VelocityMathToolRoundToInteger.htm
---
```java title=Example.java
import java.io.StringWriter;
import java.io.Writer;
import org.apache.velocity.Template;
import org.apache.velocity.VelocityContext;
import org.apache.velocity.app.Velocity;
import org.apache.velocity.tools.generic.MathTool;
public class MathToolExample {
  public static void main(String[] args) throws Exception {
    Velocity.init();
    Template t = Velocity.getTemplate("./src/mathTool.vm");
    VelocityContext ctx = new VelocityContext();
    ctx.put("math", new MathTool());
    ctx.put("aNumber", new Double(5.5));
    Writer writer = new StringWriter();
    t.merge(ctx, writer);
    System.out.println(writer);
  }
}
-------------------------------------------------------------------------------------
4.45678 rounded to the nearest integer is $math.roundToInt("4.45678")
```

velocity-MathTool-RoundToInteger.zip( 875 k)
1.  Velocity MathTool: Add
2.  Velocity MathTool Divide
3.  Velocity MathTool: Maximun
4.  Velocity MathTool Minimum
5.  Velocity MathTool: Multiply
6.  Reference Class method in Mathtool
7.  Velocity Math Tool: Power
8.  Velocity Math Tool Random
9.  Velocity MathTool Random Between
10.  Math tool: round to a given integer
11.  Velocity Math Tool: Subtract
