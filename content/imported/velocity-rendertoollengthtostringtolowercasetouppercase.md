---
title: Render tool
nav: Render tool
description: Render tool: length(), toString(), toLowerCase(), toUpperCase()
section: Imported - java2s Archive
order: 1054
source: https://web.archive.org/web/20070428084225/http://www.java2s.com:80/Code/Java/Velocity/RendertoollengthtoStringtoLowerCasetoUpperCase.htm
---
Render tool: length(), toString(), toLowerCase(), toUpperCase()

```java title=Example.java
import java.io.StringWriter;
import java.io.Writer;
import org.apache.velocity.Template;
import org.apache.velocity.VelocityContext;
import org.apache.velocity.app.Velocity;
import org.apache.velocity.tools.generic.RenderTool;
public class RenderToolExample {
  public static void main(String[] args) throws Exception {
    Velocity.init();
    Template t = Velocity.getTemplate("./src/renderTool.vm");
    VelocityContext ctx = new VelocityContext();
    ctx.put("render", new RenderTool());
    ctx.put("str", new String("The One Ring"));
    ctx.put("ctx", ctx);
    Writer writer = new StringWriter();
    t.merge(ctx, writer);
    System.out.println(writer);
  }
}
-------------------------------------------------------------------------------------
#set($methods = ["length()", "toString()", "toLowerCase()", "toUpperCase()"])
#set($name = '$str')
#foreach($method in $methods)
   $render.eval($ctx, "${name}.$method")
#end
```

Download: velocity-RendererTool.zip ( 877 K )
Related examples in the same category
