---
title: Aspect Filter
nav: Aspect Filter
description: xmlns:context="http://www.springframework.org/schema/context"
section: Imported - java2s Archive
order: 1016
source: https://web.archive.org/web/20081209070053/http://www.java2s.com:80/Code/Java/Spring/AspectFilter.htm
---
Aspect Filter

```java title=Example.java
File: context.xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:context="http://www.springframework.org/schema/context"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="
                http://www.springframework.org/schema/beans
                http://www.springframework.org/schema/beans/spring-beans.xsd
                http://www.springframework.org/schema/context
                http://www.springframework.org/schema/context/spring-context.xsd">
    <context:component-scan base-package="bean">
        <context:include-filter type="annotation" expression="bean.Magic"/>
        <context:include-filter type="assignable" expression="bean.ComponentMarker"/>
        <context:include-filter type="aspectj" expression="* void bean.*Service*(..)"/>
    </context:component-scan>
</beans>
File: Main.java
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
public class Main {
  public static void main(String[] args) throws Exception {
    ApplicationContext ac = new ClassPathXmlApplicationContext(
        "context.xml");
    String[] beanNames = ac.getBeanDefinitionNames();
    for (String beanName : beanNames) {
      System.out.println(beanName + ": " + ac.getBean(beanName));
    }
  }
}
```

Spring-AspectFilter.zip( 4,453 k)
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
13.  Aspect Annotation Pointcut AroundAfter
14.  Aspect Annotation
15.  AOP Annotation
16.  Annotation Scope
17.  Annotation Component
18.  Annotated Autowiring
