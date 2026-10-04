---
title: AspectJ Expression Pointcut
nav: AspectJ Expression Pointcut
description: import org.springframework.aop.aspectj.AspectJExpressionPointcut;
section: Imported - java2s Archive
order: 1020
source: https://web.archive.org/web/20081208084510/http://www.java2s.com:80/Code/Java/Spring/AspectJExpressionPointcut.htm
---
```java title=Example.java
File: Main.java
import org.springframework.aop.Advisor;
import org.springframework.aop.aspectj.AspectJExpressionPointcut;
import org.springframework.aop.framework.ProxyFactory;
import org.springframework.aop.support.DefaultPointcutAdvisor;
import bean.MyClass;
import bean.SimpleAfterAdvice;
public class Main {
  public static void main(String[] args) {
    MyClass target = new MyClass();
    AspectJExpressionPointcut pc = new AspectJExpressionPointcut();
    pc.setExpression("execution(* bean..*.get*(..))");
    Advisor advisor = new DefaultPointcutAdvisor(pc, new SimpleAfterAdvice());
    ProxyFactory pf = new ProxyFactory();
    pf.setTarget(target);
    pf.addAdvisor(advisor);
    MyClass proxy = (MyClass) pf.getProxy();
    System.out.println(proxy.getName());
    proxy.setName("New Name");
    System.out.println(proxy.getHeight());
  }
}
File: MyClass.java
package bean;
public class MyClass {
    public String getName() {
        return "AAA";
    }
    public void setName(String name) {
    }
    public int getHeight() {
        return 201;
    }
}
File: SimpleAfterAdvice.java
package bean;
import org.springframework.aop.AfterReturningAdvice;
import java.lang.reflect.Method;
public class SimpleAfterAdvice implements AfterReturningAdvice{
    public void afterReturning(Object returnValue, Method method, Object[] args, Object target) throws Throwable {
        System.out.println("After method: " + method);
    }
}
```

Spring-AspectJExpressionPointcut.zip( 4,746 k)
1.  Spring Tracing Aspect
2.  Method Lookup
3.  Method Before Advice
4.  Matcher For Getter And Setter
5.  Spring AOP Examples
6.  Jdk Regexp Method Pointcut
7.  Customizable TraceInterceptor
8.  Concurrency Throttle Interceptor
9.  ComposablePointcut Union
10.  ComposablePointcut Intersection
11.  AspectJ AutoProxy
12.  Aspect Filter
13.  Aspect Annotation Pointcut AroundAfter
14.  Aspect Annotation
15.  AOP Annotation
16.  Annotation Scope
17.  Annotation Component
18.  Annotated Autowiring
