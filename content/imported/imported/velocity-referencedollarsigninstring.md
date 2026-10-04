---
title: Reference Dollar Sign in String
nav: Reference Dollar Sign in S...
description: Reference Dollar Sign in String : Java examples (example source code) » Velocity » Dollar Sign
section: Imported - java2s Archive
order: 1052
source: https://web.archive.org/web/20060513071016/http://www.java2s.com/Code/Java/Velocity/ReferenceDollarSigninString.htm
---
Reference Dollar Sign in String : Java examples (example source code) » Velocity » Dollar Sign

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
#set ($dollar = "$")
A $dollar
```

Download: velocity-DollarSign4.zip (875 K)
---
Related examples in the same category
1. Dollar sign: Double Dollar
2. Velocity Dollar Sign 2
3. Use Dollar Sign
