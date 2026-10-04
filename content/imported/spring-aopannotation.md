---
title: AOP Annotation
nav: AOP Annotation
description: import org.springframework.aop.support.DefaultPointcutAdvisor;
section: Imported - java2s Archive
order: 1011
source: https://web.archive.org/web/20081209070018/http://www.java2s.com:80/Code/Java/Spring/AOPAnnotation.htm
---
```java title=Example.java
File: Main.java
import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;
import java.lang.reflect.Method;
import org.springframework.aop.Advisor;
import org.springframework.aop.AfterReturningAdvice;
import org.springframework.aop.MethodBeforeAdvice;
import org.springframework.aop.framework.ProxyFactory;
import org.springframework.aop.support.DefaultPointcutAdvisor;
import org.springframework.aop.support.annotation.AnnotationMatchingPointcut;
public class Main {
  public static void main(String[] args) {
    SampleBean target = new SampleBean();
    AnnotationMatchingPointcut pc = new AnnotationMatchingPointcut(null, SimpleAnnotation.class);
    Advisor advisor = new DefaultPointcutAdvisor(pc, new SimpleBeforeAdvice());
    ProxyFactory pf = new ProxyFactory();
    pf.setTarget(target);
    pf.addAdvisor(advisor);
    SampleBean proxy = (SampleBean) pf.getProxy();
    proxy.getName();
    proxy.getHeight();
  }
}
class SimpleBeforeAdvice implements MethodBeforeAdvice {
  public void before(Method method, Object[] args, Object target) throws Throwable {
    System.out.println("Before method " + method);
  }
}
@SimpleAnnotation
class SampleBean {
  @SimpleAnnotation
  public String getName() {
    return "AAA";
  }
  public void setName(String name) {
  }
  public int getHeight() {
    return 201;
  }
}
@Target( { ElementType.METHOD, ElementType.TYPE })
@Retention(RetentionPolicy.RUNTIME)
@interface SimpleAnnotation {
}
class AnnotationAfterAdvice implements AfterReturningAdvice {
  public void afterReturning(Object returnValue, Method method, Object[] args, Object target)
      throws Throwable {
    System.out.print("After annotated method: " + method);
  }
}
```

Spring-AOPAnnotation.zip( 4,746 k)
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
11.  AspectJ Expression Pointcut
12.  AspectJ AutoProxy
13.  Aspect Filter
14.  Aspect Annotation Pointcut AroundAfter
15.  Aspect Annotation
16.  Annotation Scope
17.  Annotation Component
18.  Annotated Autowiring
