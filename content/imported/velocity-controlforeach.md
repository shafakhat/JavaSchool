---
title: Control
nav: Control
description: Imported from the java2s.com archive: Control
section: Imported - java2s Archive
order: 1025
source: https://web.archive.org/web/20060716183812/http://www.java2s.com:80/Code/Java/Velocity/ControlForeach.htm
---
Control: For each

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
#set ($myArray = ["one", "two", "three"])
#foreach($item in $myArray)
  List Item: $item
#end
```

Download: velocity-Control-Foreach.zip ( 875 K )
---
Related examples in the same category
1. Demo loop: for each
