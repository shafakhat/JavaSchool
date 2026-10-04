---
title: Velocity Variable Add
nav: Velocity Variable Add
description: Imported from the java2s.com archive: Velocity Variable Add
section: Imported - java2s Archive
order: 1097
source: https://web.archive.org/web/20061018193115/http://www.java2s.com/Code/Java/Velocity/VelocityVariableAdd.htm
---
Velocity Variable Add

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
#set ($c = $a + $b)
$c
```

Download: velocity-Variable-Add.zip ( 877 K )
Related examples in the same category
