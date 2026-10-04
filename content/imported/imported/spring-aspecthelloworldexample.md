---
title: Aspect Hello World Example
nav: Aspect Hello World Example
description: ///////////////////////////////////////////////////////////////////////////////////////
section: Imported - java2s Archive
order: 1017
source: https://web.archive.org/web/20070503171642/http://www.java2s.com:80/Code/Java/Spring/AspectHelloWorldExample.htm
---
Aspect Hello World Example

```java title=Example.java
/*
Pro Spring
By Rob Harrop
Jan Machacek
ISBN: 1-59059-461-4
Publisher: Apress
*/
///////////////////////////////////////////////////////////////////////////////////////
public interface IMessageWriter {
    public void writeMessage();
}
///////////////////////////////////////////////////////////////////////////////////////
public class MessageWriter implements IMessageWriter{
    public void writeMessage() {
        System.out.print("World");
    }
}
///////////////////////////////////////////////////////////////////////////////////////
import org.aopalliance.intercept.MethodInterceptor;
import org.aopalliance.intercept.MethodInvocation;
public class MessageDecorator implements MethodInterceptor {
    public Object invoke(MethodInvocation invocation) throws Throwable {
        System.out.print("Hello ");
        Object retVal = invocation.proceed();
        System.out.println("!");
        return retVal;
    }
}
///////////////////////////////////////////////////////////////////////////////////////
import org.springframework.aop.framework.ProxyFactory;
public class HelloWorldAOPExample {
    public static void main(String[] args) {
        MessageWriter target = new MessageWriter();
        // create the proxy
        ProxyFactory pf = new ProxyFactory();
        pf.addAdvice(new MessageDecorator());
        pf.setTarget(target);
        MessageWriter proxy = (MessageWriter) pf.getProxy();
        // write the messages
        target.writeMessage();
        System.out.println("");
        proxy.writeMessage();
    }
}
```

Download: SpringHelloWorldExample.zip ( 1,479 K )
Related examples in the same category
