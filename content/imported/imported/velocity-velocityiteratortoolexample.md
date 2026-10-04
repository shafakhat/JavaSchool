---
title: Velocity Iterator Tool Example
nav: Velocity Iterator Tool Exa...
description: Velocity Iterator Tool Example : Java examples (example source code) » Velocity » Iterator Tool
section: Imported - java2s Archive
order: 1077
source: https://web.archive.org/web/20060513091101/http://www.java2s.com/Code/Java/Velocity/VelocityIteratorToolExample.htm
---
Velocity Iterator Tool Example : Java examples (example source code) » Velocity » Iterator Tool

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
#set($items = $var.wrap($list))
#foreach($item in $items)
    #if($velocityCount <= 3)
        $items.more()
    #end
#end
```

Download: velocity-IteratorToolExample.zip (875 K)
Related examples in the same category
