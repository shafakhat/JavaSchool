---
title: Data Type
nav: Data Type
description: Imported from the java2s.com archive: Data Type
section: Imported - java2s Archive
order: 1027
source: https://web.archive.org/web/20071105053916/http://www.java2s.com:80/Code/Java/Velocity/DataTypebool.htm
---
Data Type: bool

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
#set($bool = true)
$bool
```

velocity-Data-Type-Boolean.zip( 875 k)
1.  Data Type: number
2.  Data type: String
