---
title: Pass variable into Velocity
nav: Pass variable into Velocity
description: Imported from the java2s.com archive: Pass variable into Velocity
section: Imported - java2s Archive
order: 1047
source: https://web.archive.org/web/20061018193158/http://www.java2s.com/Code/Java/Velocity/PassvariableintoVelocity.htm
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
    ctx.put("myName","Joe");
    Writer writer = new StringWriter();
    t.merge(ctx, writer);
    System.out.println(writer);
  }
}
-------------------------------------------------------------------------------------
My name is $myName
```

Download: velocity-DefineAndPassVariables.zip ( 875 K )
Related examples in the same category
