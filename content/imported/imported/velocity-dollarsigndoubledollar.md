---
title: Dollar sign
nav: Dollar sign
description: Dollar sign: Double Dollar : Java examples (example source code) » Velocity » Dollar Sign
section: Imported - java2s Archive
order: 1033
source: https://web.archive.org/web/20060513071048/http://www.java2s.com/Code/Java/Velocity/DollarsignDoubleDollar.htm
---
Dollar sign: Double Dollar : Java examples (example source code) » Velocity » Dollar Sign

Dollar sign: Double Dollar

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
#set ($c = $a / $b)
$$c
```

Download: velocity-Variable-DollarSign.zip (877 K)
---
Related examples in the same category
1. Velocity Dollar Sign 2
2. Use Dollar Sign
3. Reference Dollar Sign in String
