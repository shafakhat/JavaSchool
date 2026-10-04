---
title: Velocity Comments Multiline
nav: Velocity Comments Multiline
description: Imported from the java2s.com archive: Velocity Comments Multiline
section: Imported - java2s Archive
order: 1072
source: https://web.archive.org/web/20061018194903/http://www.java2s.com/Code/Java/Velocity/VelocityCommentsMultiline.htm
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
#* This
is
the
start
of
a
multi-line
comment
and
it
finishes
on
this
line
*#
Hi
```

Download: velocity-Comments-Multiline.zip ( 875 K )
Related examples in the same category
