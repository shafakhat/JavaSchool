---
title: Velocity Math Tool
nav: Velocity Math Tool
description: Imported from the java2s.com archive: Velocity Math Tool
section: Imported - java2s Archive
order: 1084
source: https://web.archive.org/web/20071105012712/http://www.java2s.com:80/Code/Java/Velocity/VelocityMathToolPower.htm
---
Velocity Math Tool: Power

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
$aNumber ^ 3.2 = $math.pow($aNumber, "3.2")
```

velocity-MathTool-Power.zip( 875 k)
1.  Velocity MathTool: Add
2.  Velocity MathTool Divide
3.  Velocity MathTool: Maximun
4.  Velocity MathTool Minimum
5.  Velocity MathTool: Multiply
6.  Reference Class method in Mathtool
7.  Velocity Math Tool Random
8.  Velocity MathTool Random Between
9.  Math tool: round to a given integer
10.  Velocity Math Tool Round To Integer
11.  Velocity Math Tool: Subtract
