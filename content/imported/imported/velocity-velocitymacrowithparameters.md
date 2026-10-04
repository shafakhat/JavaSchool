---
title: Velocity Macro With Parameters
nav: Velocity Macro With Parame...
description: Imported from the java2s.com archive: Velocity Macro With Parameters
section: Imported - java2s Archive
order: 1078
source: https://web.archive.org/web/20060923034756/http://www.java2s.com:80/Code/Java/Velocity/VelocityMacroWithParameters.htm
---
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
#macro( tablerows $color $somelist )
  #foreach( $something in $somelist )
      <tr><td bgcolor=$color>$something</td></tr>
  #end
#end
#set( $greatlakes = ["Superior","Michigan","Huron","Erie","Ontario"] )
#set( $color = "blue" )
<table>
    #tablerows( $color $greatlakes )
</table>
```

Download: velocity-Macro-WithParameters.zip ( 1,874 K )
---
Related examples in the same category
1. Define and use Macro
2. Use macro to wrap HTML tags
