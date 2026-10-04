---
title: Concurrency Throttle Interceptor
nav: Concurrency Throttle Inter...
description: <bean id="afterBean" class="org.springframework.aop.framework.ProxyFactoryBean">
section: Imported - java2s Archive
order: 1050
source: https://web.archive.org/web/20081209070117/http://www.java2s.com:80/Code/Java/Spring/ConcurrencyThrottleInterceptor.htm
---
```java title=Example.java
File: context.xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE beans PUBLIC "-//SPRING//DTD BEAN//EN"
    "http://www.springframework.org/dtd/spring-beans.dtd">
<beans>
  <bean id="afterBean" class="org.springframework.aop.framework.ProxyFactoryBean">
    <property name="target">
      <bean class="MtBean">
        <property name="firstName" value="AAA"/>
      </bean>
    </property>
    <property name="interceptorNames">
      <list>
        <idref bean="endMatchPointcutAdvisor"/>
      </list>
    </property>
    <property name="proxyTargetClass" value="true"/>
  </bean>
  <bean id="endMatchPointcutAdvisor"
        class="org.springframework.aop.support.NameMatchMethodPointcutAdvisor"
        singleton="false">
    <property name="advice" ref="concurrencyThrottleInterceptor"/>
    <property name="mappedName" value="showValues"/>
  </bean>
  <bean id="concurrencyThrottleInterceptor"
        class="org.springframework.aop.interceptor.ConcurrencyThrottleInterceptor"
        singleton="false">
    <property name="concurrencyLimit" value="5"/>
  </bean>
</beans>
File: Main.java
import org.aopalliance.intercept.MethodInterceptor;
import org.aopalliance.intercept.MethodInvocation;
import org.springframework.beans.factory.BeanFactory;
import org.springframework.beans.factory.xml.XmlBeanFactory;
import org.springframework.core.io.ClassPathResource;
import org.springframework.util.StopWatch;
public class Main {
  public static void main(String[] args) throws Exception {
    BeanFactory beanFactory = new XmlBeanFactory(new ClassPathResource("context.xml"));
    MtBean testBean = (MtBean) beanFactory
        .getBean("afterBean");
    testBean.showValues();
  }
}
class MtBean {
  private String firstName;
  public String getFirstName() {
    return this.firstName;
  }
  public void setFirstName(String firstName) {
    this.firstName = firstName;
  }
  public void showValues() {
    System.out.println("First name: " + this.firstName);
  }
}
```

Spring-ConcurrencyThrottleInterceptor.zip( 2,894 k)
1.  Spring Tracing Aspect
2.  Method Lookup
3.  Method Before Advice
4.  Matcher For Getter And Setter
5.  Spring AOP Examples
6.  Jdk Regexp Method Pointcut
7.  Customizable TraceInterceptor
8.  ComposablePointcut Union
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
