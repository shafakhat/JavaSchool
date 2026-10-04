---
title: Use if in velocity
nav: Use if in velocity
description: Imported from the java2s.com archive: Use if in velocity
section: Imported - java2s Archive
order: 1064
source: https://web.archive.org/web/20060513075051/http://www.java2s.com/Code/Java/Velocity/Useifinvelocity.htm
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
#foreach($item in $list)
    #if($velocityCount <= 3)
        $item
    #end
#end
```

Download: velocity-if.zip (875 K)
---
Related examples in the same category
1. If Else and End
2. If and elseif
3. If statement inside a for loop
