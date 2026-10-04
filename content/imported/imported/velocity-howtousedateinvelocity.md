---
title: How to use Date in Velocity
nav: How to use Date in Velocity
description: Today's date is also: $date.long #* using property shortcut *#
section: Imported - java2s Archive
order: 1039
source: https://web.archive.org/web/20061026233600/http://www.java2s.com/Code/Java/Velocity/HowtouseDateinVelocity.htm
---
How to use Date in Velocity

```java title=Example.java
-------------------------------------------------------------------------------------
Today's date is:       $date
Today's date is also:  $date.long           #* using property shortcut *#
Today's date is also:  $date.get('long')    #* using full syntax *#
The date and time is:  $date.default $date.short
Another date is:       $aDate
Another date is also:  $date.format('medium', $aDate)
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
```

Download: velocity-DateTool.zip ( 875 K )
Related examples in the same category
