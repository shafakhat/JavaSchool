---
title: Aspect Annotation Pointcut AroundAfter
nav: Aspect Annotation Pointcut...
description: import org.springframework.context.support.ClassPathXmlApplicationContext;
section: Imported - java2s Archive
order: 1015
source: https://web.archive.org/web/20081209070047/http://www.java2s.com:80/Code/Java/Spring/AspectAnnotationPointcutAroundAfter.htm
---
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
    <bean id="test" class="TestBean"/>
    <bean class="LoggingAspectPC">
        <property name="beforeMessage" value="Before %s %s"/>
        <property name="afterMessage" value="After %s %s"/>
    </bean>
    <aop:aspectj-autoproxy />
</beans>
File: Main.java
import java.util.Arrays;
import javax.annotation.PostConstruct;
import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.After;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Pointcut;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
public class Main {
  public static void main(String[] args) {
    ApplicationContext ac = new ClassPathXmlApplicationContext("context.xml");
    TestBean testBean = (TestBean) ac.getBean("test");
    testBean.work();
    testBean.stop();
  }
}
class TestBean {
  public void work() {
    System.out.println("work");
  }
  public void stop() {
    System.out.println("stop");
  }
}
@Aspect
 class LoggingAspectPC {
    private String beforeMessage;
    private String afterMessage;
    @Pointcut("execution(* TestBean.*(..))")
    private void testBeanExecution() { }
    @Around("testBeanExecution()")
    public Object log(ProceedingJoinPoint pjp) throws Throwable {
      System.out.println(this.beforeMessage);
      System.out.println(pjp.getSignature().getName());
      System.out.println(Arrays.toString(pjp.getArgs()));
      Object ret = pjp.proceed();
      System.out.println(this.afterMessage);
      System.out.println(pjp.getSignature().getName());
      System.out.println(Arrays.toString(pjp.getArgs()));
        return ret;
    }
    @After("testBeanExecution()")
    public void afterCall(JoinPoint jp) {
        System.out.println("After");
    }
    @PostConstruct
    public void initialize() {
        System.out.println("initialize:"+this.beforeMessage);
        System.out.println("initialize:"+this.afterMessage);
    }
    public void setBeforeMessage(String beforeMessage) {
        this.beforeMessage = beforeMessage;
    }
    public void setAfterMessage(String afterMessage) {
        this.afterMessage = afterMessage;
    }
}
```

Spring-AspectAnnotationPointcutAroundAfter.zip( 4,650 k)
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
14.  Aspect Annotation
15.  AOP Annotation
16.  Annotation Scope
17.  Annotation Component
18.  Annotated Autowiring
