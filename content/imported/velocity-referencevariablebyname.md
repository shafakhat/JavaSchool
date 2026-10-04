---
title: Reference variable by name
nav: Reference variable by name
description: Imported from the java2s.com archive: Reference variable by name
section: Imported - java2s Archive
order: 1053
source: https://web.archive.org/web/20061018193125/http://www.java2s.com/Code/Java/Velocity/Referencevariablebyname.htm
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
#set ($a = "12.99")
#set ($b = "13.99")
$a = $a
$b = $b
```

Download: velocity-VariableName.zip ( 877 K )
Related examples in the same category
