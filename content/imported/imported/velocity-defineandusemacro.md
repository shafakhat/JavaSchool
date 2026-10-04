---
title: Define and use Macro
nav: Define and use Macro
description: Imported from the java2s.com archive: Define and use Macro
section: Imported - java2s Archive
order: 1030
source: https://web.archive.org/web/20060928131959/http://www.java2s.com:80/Code/Java/Velocity/DefineanduseMacro.htm
---
Define and use Macro

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
#macro (writeTable $productList)
  #set ($rowCount = 1)
  #foreach($product in $productList)
  #if ($rowCount % 2 == 0)
    #set ($bgcolor = "#FFFFFF")
  #else
    #set ($bgcolor = "#CCCCCC")
  #end
    <tr>
      <td bgcolor="$bgcolor">$product</td>
      <td bgcolor="$bgcolor">$product</td>
    </tr>
    #set ($rowCount = $rowCount + 1)
  #end
#end
#set ($products = ["one", "two", "three"])
<html>
  <head>
    <title>Title</title>
  </head>
  <body>
    <table>
      #writeTable($products)
    </table>
  </body>
</html>
```

Download: velocity-Macro.zip ( 875 K )
---
Related examples in the same category
1. Use macro to wrap HTML tags
2. Velocity Macro With Parameters
