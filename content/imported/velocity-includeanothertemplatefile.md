---
title: Include another template file
nav: Include another template f...
description: Imported from the java2s.com archive: Include another template file
section: Imported - java2s Archive
order: 1043
source: https://web.archive.org/web/20061027021035/http://www.java2s.com/Code/Java/Velocity/Includeanothertemplatefile.htm
---
Include another template file

```java title=Example.java
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
<html>
  <head>
    <title>Homepage</title>
  </head>
  <body>
    <h1>Welcome!!</h1>
    #include("./src/pageFooter.vm")
  </body>
</html>
-------------------------------------------------------------------------------------
<h3>Copyright &copy; 2004</h3>
```

Download: velocity-include.zip ( 875 K )
Related examples in the same category
