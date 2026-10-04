---
title: Velocity Date tool
nav: Velocity Date tool
description: Calendar aDate = Calendar.getInstance(TimeZone.getTimeZone("PST"));
section: Imported - java2s Archive
order: 1074
source: https://web.archive.org/web/20070630065000/http://www.java2s.com:80/Code/Java/Velocity/VelocityDatetoolgetandformat.htm
---
Velocity Date tool: get and format

```java title=Example.java
-------------------------------------------------------------------------------------
import java.io.StringWriter;
import java.io.Writer;
import java.util.Calendar;
import java.util.TimeZone;
import org.apache.velocity.Template;
import org.apache.velocity.VelocityContext;
import org.apache.velocity.app.Velocity;
import org.apache.velocity.tools.generic.DateTool;
public class DateToolExample {
  public static void main(String[] args) throws Exception {
    Velocity.init();
    Template t = Velocity.getTemplate("./src/dateTool.vm");
    VelocityContext ctx = new VelocityContext();
    ctx.put("date", new DateTool());
    Calendar aDate = Calendar.getInstance(TimeZone.getTimeZone("PST"));
    aDate.set(200, 11, 25);
    ctx.put("aDate", aDate);
    Writer writer = new StringWriter();
    t.merge(ctx, writer);
    System.out.println(writer);
  }
}
-------------------------------------------------------------------------------------
Today's date is:       $date
Today's date is also:  $date.long           #* using property shortcut *#
Today's date is also:  $date.get('long')    #* using full syntax *#
The date and time is:  $date.default $date.short
Another date is:       $aDate
Another date is also:  $date.format('medium', $aDate)
```

Download: velocity-Date.zip ( 875 K )
Related examples in the same category
