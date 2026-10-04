---
title: Velocity MathTool Divide
nav: Velocity MathTool Divide
description: Imported from the java2s.com archive: Velocity MathTool Divide
section: Imported - java2s Archive
order: 1080
source: https://web.archive.org/web/20071105053931/http://www.java2s.com:80/Code/Java/Velocity/VelocityMathToolDivide.htm
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
$aNumber / 3.2 = $math.div($aNumber, "3.2")
```

velocity-MathTool-Divide.zip( 875 k)
1.  Velocity MathTool: Add
2.  Velocity MathTool: Maximun
3.  Velocity MathTool Minimum
4.  Velocity MathTool: Multiply
5.  Reference Class method in Mathtool
6.  Velocity Math Tool: Power
7.  Velocity Math Tool Random
8.  Velocity MathTool Random Between
9.  Math tool: round to a given integer
10.  Velocity Math Tool Round To Integer
11.  Velocity Math Tool: Subtract
