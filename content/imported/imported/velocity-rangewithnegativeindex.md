---
title: Range with negative index
nav: Range with negative index
description: 2. Render tool: length(), toString(), toLowerCase(), toUpperCase()
section: Imported - java2s Archive
order: 1049
source: https://web.archive.org/web/20071105210548/http://www.java2s.com:80/Code/Java/Velocity/Rangewithnegativeindex.htm
---
Range with negative index

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
    Writer writer = new StringWriter();
    t.merge(ctx, writer);
    System.out.println(writer);
  }
}
-------------------------------------------------------------------------------------
#foreach( $bar in [2..-2] )
  $bar
#end
```

velocity-WithnegativeIndex.zip( 1,876 k)
1.  Range set
2.  Render tool: length(), toString(), toLowerCase(), toUpperCase()
3.  For each loop controled by Range function
