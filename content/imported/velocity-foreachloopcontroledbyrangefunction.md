---
title: For each loop controled by Range function
nav: For each loop controled by...
description: 3. Render tool: length(), toString(), toLowerCase(), toUpperCase()
section: Imported - java2s Archive
order: 1035
source: https://web.archive.org/web/20071106044858/http://www.java2s.com:80/Code/Java/Velocity/ForeachloopcontroledbyRangefunction.htm
---
For each loop controled by Range function

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
#foreach($number in [1..5])
          Current Index: $number
#end
```

velocity-Foreach-Range.zip( 875 k)
1.  Range with negative index
2.  Range set
3.  Render tool: length(), toString(), toLowerCase(), toUpperCase()
