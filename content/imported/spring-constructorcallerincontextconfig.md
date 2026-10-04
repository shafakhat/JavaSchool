---
title: ConstructorCaller In ContextConfig
nav: ConstructorCaller In Conte...
description: BeanFactory beanFactory = new XmlBeanFactory(new ClassPathResource("context.xml"));
section: Imported - java2s Archive
order: 1053
source: https://web.archive.org/web/20090406053255/http://www.java2s.com:80/Code/Java/Spring/ConstructorCallerInContextConfig.htm
---
```java title=Example.java
File: context.xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE beans PUBLIC "-//SPRING//DTD BEAN//EN"
    "http://www.springframework.org/dtd/spring-beans.dtd">
<beans>
   <bean id="testBean" class="ConstructorTestBean">
      <constructor-arg value="Steven Devijver"/>
<!--
      <constructor-arg value="1"/>
-->
      <constructor-arg value="1" type="java.lang.Integer"/>
   </bean>
</beans>
File: Main.java
import org.springframework.beans.factory.BeanFactory;
import org.springframework.beans.factory.xml.XmlBeanFactory;
import org.springframework.core.io.ClassPathResource;
public class Main {
  public static void main(String[] args) throws Exception {
    BeanFactory beanFactory = new XmlBeanFactory(new ClassPathResource("context.xml"));
    ConstructorTestBean testBean = (ConstructorTestBean) beanFactory.getBean("testBean");
    System.out.println(testBean.isConstructor1Used());
    System.out.println(testBean.isConstructor2Used());
  }
}
class ConstructorTestBean {
  private boolean constructor1Used = false;
  private boolean constructor2Used = false;
  public ConstructorTestBean(String name, Integer id) {
    this.constructor1Used = true;
  }
  public ConstructorTestBean(String firstName, String lastName) {
    this.constructor2Used = true;
  }
  public boolean isConstructor1Used() {
    return this.constructor1Used;
  }
  public boolean isConstructor2Used() {
    return this.constructor2Used;
  }
}
```

Spring-ConstructorCallerInContextConfig.zip( 2,599 k)
1.  Call Constructor
2.  Constructor Confusion Demo
3.  Constructor Argument And Local Reference
4.  SingletonScope And PrototypeScope
