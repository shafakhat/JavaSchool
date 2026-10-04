---
title: Velocity Comments
nav: Velocity Comments
description: Imported from the java2s.com archive: Velocity Comments
section: Imported - java2s Archive
order: 1071
source: https://web.archive.org/web/20061018194859/http://www.java2s.com/Code/Java/Velocity/VelocityCommentsHalfLine.htm
---
Velocity Comments: HalfLine

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
Hello World! #* this is a comment *#
```

Download: velocity-Comments-HalfLine.zip ( 875 K )
Related examples in the same category
