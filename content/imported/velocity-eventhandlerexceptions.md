---
title: Event Handler
nav: Event Handler
description: import org.apache.velocity.app.event.MethodExceptionEventHandler;
section: Imported - java2s Archive
order: 1034
source: https://web.archive.org/web/20061018192901/http://www.java2s.com/Code/Java/Velocity/EventHandlerExceptions.htm
---
Event Handler: Exceptions

```java title=Example.java
import java.io.StringWriter;
import java.io.Writer;
import org.apache.velocity.Template;
import org.apache.velocity.VelocityContext;
import org.apache.velocity.app.Velocity;
import org.apache.velocity.app.event.EventCartridge;
import org.apache.velocity.app.event.MethodExceptionEventHandler;
import org.apache.velocity.app.event.NullSetEventHandler;
import org.apache.velocity.app.event.ReferenceInsertionEventHandler;
import org.apache.velocity.context.Context;
public class EventHandler implements ReferenceInsertionEventHandler,
    NullSetEventHandler, MethodExceptionEventHandler {
  public EventHandler(Context ctx) {
    EventCartridge ec = new EventCartridge();
    ec.addEventHandler(this);
    ec.attachToContext(ctx);
  }
  public Object referenceInsert(String reference, Object data) {
    System.out.println("referenceInsert: " + reference + " data: " + data);
    return data;
  }
  public boolean shouldLogOnNullSet(String lhs, String rhs) {
    System.out.println("shouldLogOnNullSet");
    System.out.println("lhs:" + lhs + " rhs:" + rhs);
      return true;
  }
  public Object methodException(Class cls, String method, Exception e)
      throws Exception {
    return "An " + e.getClass().getName() + " was thrown by the " + method
        + " method of the " + cls.getName() + " class [" + e.getMessage() + "]";
  }
  public static void main(String[] args) throws Exception {
    Velocity.init();
    Template t = Velocity.getTemplate("./src/eventHandler.vm");
    Context ctx = new VelocityContext();
    ctx.put("person", "Joe");
    ctx.put("exception", new ExceptionGenerator());
    EventHandler hdl = new EventHandler(ctx);
    Writer writer = new StringWriter();
    t.merge(ctx, writer);
    System.out.println(writer);
  }
}
import java.util.Random;
public class ExceptionGenerator {
  public String generate() throws Exception {
    Random rnd = new Random();
    int x = rnd.nextInt(5);
    if (x == 2) {
      throw new Exception("Unlucky!");
    } else {
      return "No Exception";
    }
  }
}
-------------------------------------------------------------------------------------
#set($myNull1 = $validNull)
#set($myNull2 = $invalidNull)
This is $person
$exception.generate()
$exception.generate()
$exception.generate()
$exception.generate()
```

Download: velocity-Processing-Exception-Handling.zip ( 2,195 K )
Related examples in the same category
