---
title: ComposablePointcut Union
nav: ComposablePointcut Union
description: import org.springframework.aop.support.DefaultPointcutAdvisor;
section: Imported - java2s Archive
order: 1049
source: https://web.archive.org/web/20081209070111/http://www.java2s.com:80/Code/Java/Spring/ComposablePointcutUnion.htm
---
ComposablePointcut Union

```java title=Example.java
File: Main.java
import java.lang.reflect.Method;
import org.springframework.aop.Advisor;
import org.springframework.aop.ClassFilter;
import org.springframework.aop.MethodBeforeAdvice;
import org.springframework.aop.framework.ProxyFactory;
import org.springframework.aop.support.ComposablePointcut;
import org.springframework.aop.support.DefaultPointcutAdvisor;
import org.springframework.aop.support.StaticMethodMatcher;
public class Main {
  public static void main(String[] args) {
    SampleBean target = new SampleBean();
    ComposablePointcut pc = new ComposablePointcut(ClassFilter.TRUE, new GetterMethodMatcher());
    pc.union(new SetterMethodMatcher());
    SampleBean proxy = getProxy(pc, target);
    testInvoke(proxy);
  }
  private static SampleBean getProxy(ComposablePointcut pc, SampleBean target) {
    Advisor advisor = new DefaultPointcutAdvisor(pc, new SimpleBeforeAdvice());
    ProxyFactory pf = new ProxyFactory();
    pf.setTarget(target);
    pf.addAdvisor(advisor);
    return (SampleBean) pf.getProxy();
  }
  private static void testInvoke(SampleBean proxy) {
    proxy.getAge();
    proxy.getName();
    proxy.setName("QQQ");
  }
}
class GetterMethodMatcher extends StaticMethodMatcher {
  public boolean matches(Method method, Class cls) {
    return (method.getName().startsWith("get"));
  }
}
class SetterMethodMatcher extends StaticMethodMatcher {
  public boolean matches(Method method, Class cls) {
    return (method.getName().startsWith("set"));
  }
}
class SampleBean {
  public String getName() {
    return "AAA";
  }
  public void setName(String name) {
  }
  public int getAge() {
    return 100;
  }
}
class SimpleBeforeAdvice implements MethodBeforeAdvice {
  public void before(Method method, Object[] args, Object target) throws Throwable {
    System.out.println("Before method " + method);
  }
}
```

Spring-ComposablePointcutUnion.zip( 4,746 k)
1.  Spring Tracing Aspect
2.  Method Lookup
3.  Method Before Advice
4.  Matcher For Getter And Setter
5.  Spring AOP Examples
6.  Jdk Regexp Method Pointcut
7.  Customizable TraceInterceptor
8.  Concurrency Throttle Interceptor
9.  ComposablePointcut Intersection
10.  AspectJ Expression Pointcut
11.  AspectJ AutoProxy
12.  Aspect Filter
13.  Aspect Annotation Pointcut AroundAfter
14.  Aspect Annotation
15.  AOP Annotation
16.  Annotation Scope
17.  Annotation Component
18.  Annotated Autowiring
