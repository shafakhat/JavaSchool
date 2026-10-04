---
title: Use a variable defined in Velocity
nav: Use a variable defined in ...
description: Imported from the java2s.com archive: Use a variable defined in Velocity
section: Imported - java2s Archive
order: 1062
source: https://web.archive.org/web/20061018193047/http://www.java2s.com/Code/Java/Velocity/UseavariabledefinedinVelocity.htm
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
#set($msg = "Hi!")
I have a message: $msg
```

Download: velocity-Data-Type-Refer.zip ( 875 K )
Related examples in the same category
