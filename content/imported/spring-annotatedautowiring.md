---
title: Annotated Autowiring
nav: Annotated Autowiring
description: http://www.springframework.org/schema/beans/spring-beans.xsd">
section: Imported - java2s Archive
order: 1008
source: https://web.archive.org/web/20081209070026/http://www.java2s.com:80/Code/Java/Spring/AnnotatedAutowiring.htm
---
```java title=Example.java
File: context.xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="
                http://www.springframework.org/schema/beans
                http://www.springframework.org/schema/beans/spring-beans.xsd">
    <bean id="a" class="A"/>
    <bean id="b" class="B"/>
    <bean id="annotatedTarget" class="AnnotatedClass"/>
    <bean class="org.springframework.beans.factory.annotation.AutowiredAnnotationBeanPostProcessor"/>
</beans>
File: Main.java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
public class Main {
  public static void main(String[] args) {
    ApplicationContext bf = new ClassPathXmlApplicationContext("context.xml");
    System.out.println("annotatedTarget:");
    System.out.println(bf.getBean("annotatedTarget"));
  }
}
class A {
  @Override
  public String toString() {
    return getClass().getName();
  }
}
class B {
  @Override
  public String toString() {
    return getClass().getName();
  }
}
class AnnotatedClass {
  @Autowired
  private A foo;
  @Autowired
  private A foo2;
  @Autowired
  private B bar;
  @Override
  public String toString() {
      final StringBuilder sb = new StringBuilder();
      sb.append("AnnotatedClass");
      sb.append("{foo=").append(foo);
      sb.append(", foo2=").append(foo2);
      sb.append(", bar=").append(bar);
      sb.append('}');
      return sb.toString();
  }
}
```

Spring-AnnotatedAutowiring.zip( 2,599 k)
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
16.  AOP Annotation
17.  Annotation Scope
18.  Annotation Component
