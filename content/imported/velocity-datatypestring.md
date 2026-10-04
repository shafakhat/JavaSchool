---
title: Data type
nav: Data type
description: Imported from the java2s.com archive: Data type
section: Imported - java2s Archive
order: 1029
source: https://web.archive.org/web/20071104100037/http://www.java2s.com:80/Code/Java/Velocity/DatatypeString.htm
---
Data type: String

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
#set($str = "A String")
$str
```

velocity-Data-Type-String.zip( 875 k)
1.  Data Type: bool
2.  Data Type: number
