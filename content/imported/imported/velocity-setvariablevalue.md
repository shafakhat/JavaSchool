---
title: Set variable value
nav: Set variable value
description: Imported from the java2s.com archive: Set variable value
section: Imported - java2s Archive
order: 1056
source: https://web.archive.org/web/20061018193151/http://www.java2s.com/Code/Java/Velocity/Setvariablevalue.htm
---
```java title=Example.java
import java.io.StringWriter;
import java.io.Writer;
import org.apache.velocity.Template;
import org.apache.velocity.VelocityContext;
import org.apache.velocity.app.Velocity;
import org.apache.velocity.tools.generic.IteratorTool;
public class IteratorToolExample {
  public static void main(String[] args) throws Exception {
    Velocity.init();
    Template t = Velocity.getTemplate("./src/iteratorTool.vm");
    VelocityContext ctx = new VelocityContext();
    ctx.put("var", new IteratorTool());
    Writer writer = new StringWriter();
    t.merge(ctx, writer);
    System.out.println(writer);
  }
}
-------------------------------------------------------------------------------------
#set($list = ["A", "B", "C", "D", "E"])
$list
```

Download: velocity-Set.zip ( 877 K )
Related examples in the same category
