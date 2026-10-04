---
title: Velocity MathTool Random Between
nav: Velocity MathTool Random B...
description: Imported from the java2s.com archive: Velocity MathTool Random Between
section: Imported - java2s Archive
order: 1086
source: https://web.archive.org/web/20071105053936/http://www.java2s.com:80/Code/Java/Velocity/VelocityMathToolRandomBetween.htm
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
$math.random(1, 20) is a random number between 1 and 20
```

velocity-MathTool-Random-Between.zip( 875 k)
1.  Velocity MathTool: Add
2.  Velocity MathTool Divide
3.  Velocity MathTool: Maximun
4.  Velocity MathTool Minimum
5.  Velocity MathTool: Multiply
6.  Reference Class method in Mathtool
7.  Velocity Math Tool: Power
8.  Velocity Math Tool Random
9.  Math tool: round to a given integer
10.  Velocity Math Tool Round To Integer
11.  Velocity Math Tool: Subtract
