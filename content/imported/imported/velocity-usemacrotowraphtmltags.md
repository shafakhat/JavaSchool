---
title: Use macro to wrap HTML tags
nav: Use macro to wrap HTML tags
description: Imported from the java2s.com archive: Use macro to wrap HTML tags
section: Imported - java2s Archive
order: 1066
source: https://web.archive.org/web/20060927013140/http://www.java2s.com:80/Code/Java/Velocity/UsemacrotowrapHTMLtags.htm
---
Use macro to wrap HTML tags

```java title=Example.java
import java.io.StringWriter;
import java.io.Writer;
import org.apache.velocity.Template;
import org.apache.velocity.VelocityContext;
import org.apache.velocity.app.Velocity;
import org.apache.velocity.tools.generic.IteratorTool;
public class VMDemo {
  public static void main(String[] args) throws Exception {
    Velocity.init();
    Template t = Velocity.getTemplate("./src/demo.vm");
    VelocityContext ctx = new VelocityContext();
    ctx.put("var", new IteratorTool());
    Writer writer = new StringWriter();
    t.merge(ctx, writer);
    System.out.println(writer);
  }
}
-------------------------------------------------------------------------------------
#macro( d )
<tr><td></td></tr>
#end
#d()
```

Download: velocity-Macro-Simple.zip ( 1,873 K )
---
Related examples in the same category
1. Define and use Macro
2. Velocity Macro With Parameters
