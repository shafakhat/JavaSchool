---
title: Velocity Dollar Sign 2
nav: Velocity Dollar Sign 2
description: Velocity Dollar Sign 2 : Java examples (example source code) » Velocity » Dollar Sign
section: Imported - java2s Archive
order: 1075
source: https://web.archive.org/web/20060513071043/http://www.java2s.com/Code/Java/Velocity/VelocityDollarSign2.htm
---
Velocity Dollar Sign 2 : Java examples (example source code) » Velocity » Dollar Sign

Velocity Dollar Sign 2

```java title=Example.java
import java.io.StringWriter;
import java.io.Writer;
import org.apache.velocity.Template;
import org.apache.velocity.VelocityContext;
import org.apache.velocity.app.Velocity;
import org.apache.velocity.tools.generic.RenderTool;
public class VMDemo {
  public static void main(String[] args) throws Exception {
    Velocity.init();
    Template t = Velocity.getTemplate("./src/VMDemo.vm");
    VelocityContext ctx = new VelocityContext();
    Writer writer = new StringWriter();
    t.merge(ctx, writer);
    System.out.println(writer);
  }
}
-------------------------------------------------------------------------------------
#set ($a = 13)
#set ($b = 14)
#set ($e = 2)
#set ($c = $a + $e)
#set ($d = $b + $e)
Price List
----------
\$a = $$a $$c
\$b = $$b $$d
All prices in USD ($).
```

Download: velocity-Variable-DollarSign2.zip (877 K)
---
Related examples in the same category
1. Dollar sign: Double Dollar
2. Use Dollar Sign
3. Reference Dollar Sign in String
