---
title: Use Dollar Sign
nav: Use Dollar Sign
description: Imported from the java2s.com archive: Use Dollar Sign
section: Imported - java2s Archive
order: 1063
source: https://web.archive.org/web/20060513071036/http://www.java2s.com/Code/Java/Velocity/UseDollarSign.htm
---
```java title=Example.java
-------------------------------------------------------------------------------------
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
A ($) sign.
```

Download: velocity-DollarSign3.zip (875 K)
---
Related examples in the same category
1. Dollar sign: Double Dollar
2. Velocity Dollar Sign 2
3. Reference Dollar Sign in String
