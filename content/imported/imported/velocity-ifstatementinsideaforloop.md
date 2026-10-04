---
title: If statement inside a for loop
nav: If statement inside a for ...
description: If statement inside a for loop : Java examples (example source code) » Velocity » If
section: Imported - java2s Archive
order: 1042
source: https://web.archive.org/web/20060513075047/http://www.java2s.com/Code/Java/Velocity/Ifstatementinsideaforloop.htm
---
If statement inside a for loop : Java examples (example source code) » Velocity » If

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
<html>
    <head>
        <title>Gimli's Widgetarium</title>
    </head>
    <body>
        <table>
            #set ($rowCount = 1)
            #set ($products = ["one", "two", "three"])
            #foreach($product in $products)
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
        </table>
    </body>
</html>
```

Download: velocity-ForLoop.zip (875 K)
---
Related examples in the same category
1. Use if in velocity
2. If Else and End
3. If and elseif
