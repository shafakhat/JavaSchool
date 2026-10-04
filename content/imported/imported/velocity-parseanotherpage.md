---
title: Parse Another page
nav: Parse Another page
description: Imported from the java2s.com archive: Parse Another page
section: Imported - java2s Archive
order: 1046
source: https://web.archive.org/web/20070504050912/http://www.java2s.com:80/Code/Java/Velocity/ParseAnotherpage.htm
---
Parse Another page

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
#set ($companyName = "Name")
<html>
  <head>
    <title>$companyName Homepage</title>
  </head>
  <body>
    <h1>Welcome!!</h1>
    #parse("./src/pageFooter.vm")
  </body>
</html>
-------------------------------------------------------------------------------------
<h3>Copyright &copy; 2004</h3>
```

Download: velocity-ReferenceAnotherVM.zip ( 878 K )
Related examples in the same category
