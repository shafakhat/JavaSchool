---
title: AspectJ AutoProxy
nav: AspectJ AutoProxy
description: import org.springframework.context.support.ClassPathXmlApplicationContext;
section: Imported - java2s Archive
order: 1018
source: https://web.archive.org/web/20081209070059/http://www.java2s.com:80/Code/Java/Spring/AspectJAutoProxy.htm
---
AspectJ AutoProxy

```java title=Example.java
File: context.xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:aop="http://www.springframework.org/schema/aop"
       xsi:schemaLocation="
            http://www.springframework.org/schema/beans
            http://www.springframework.org/schema/beans/spring-beans.xsd
            http://www.springframework.org/schema/aop
            http://www.springframework.org/schema/aop/spring-aop.xsd">
    <bean id="test" class="TestBean2">
        <property name="simpleBean" ref="simple"/>
    </bean>
    <bean id="simple" class="SimpleBean"/>
    <bean class="Main"/>
    <aop:aspectj-autoproxy/>
</beans>
File: Main.java
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
public class Main {
  public static void main(String[] args) {
    ApplicationContext ac = new ClassPathXmlApplicationContext("context.xml");
    TestBean2 testBean = (TestBean2) ac.getBean("test");
    SimpleBean simpleBean = (SimpleBean) ac.getBean("simple");
    testBean.work();
    testBean.stop();
    simpleBean.sayHello();
    simpleBean.x("a", "b");
  }
}
class TestBean2 {
  private SimpleBean simpleBean;
  public void work() {
    this.simpleBean.sayHello();
    System.out.println("work");
  }
  public void stop() {
    this.simpleBean.sayHello();
    System.out.println("stop");
  }
  public void setSimpleBean(SimpleBean simpleBean) {
    this.simpleBean = simpleBean;
  }
}
class SimpleBean {
  public void sayHello() {
    System.out.println("Hello");
  }
  public void x(CharSequence a, String b) {
  }
}
```

Spring-AspectJAutoProxy.zip( 4,649 k)
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
12.  Aspect Filter
13.  Aspect Annotation Pointcut AroundAfter
14.  Aspect Annotation
15.  AOP Annotation
16.  Annotation Scope
17.  Annotation Component
18.  Annotated Autowiring
