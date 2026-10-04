---
title: Define and use variable in Velocity
nav: Define and use variable in...
description: Imported from the java2s.com archive: Define and use variable in Velocity
section: Imported - java2s Archive
order: 1031
source: https://web.archive.org/web/20061018193146/http://www.java2s.com/Code/Java/Velocity/DefineandusevariableinVelocity.htm
---
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
#set ($c = $a * $b)
$c
```

Download: velocity-Varaible-Multiply.zip ( 877 K )
Related examples in the same category
