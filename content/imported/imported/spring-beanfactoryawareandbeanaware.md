---
title: BeanFactoryAware and BeanAware
nav: BeanFactoryAware and BeanA...
description: http://www.springframework.org/schema/beans/spring-beans.xsd">
section: Imported - java2s Archive
order: 1023
source: https://web.archive.org/web/20090802100248/http://www.java2s.com:80/Code/Java/Spring/BeanFactoryAwareandBeanAware.htm
---
```java title=Example.java
File: context.xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="
                http://www.springframework.org/schema/beans
                http://www.springframework.org/schema/beans/spring-beans.xsd">
    <bean id="logging" class="LoggingBean"/>
    <bean class="ShutdownHookBean"/>
</beans>
File: Main.java
import org.springframework.beans.BeansException;
import org.springframework.beans.factory.BeanFactory;
import org.springframework.beans.factory.BeanFactoryAware;
import org.springframework.beans.factory.BeanNameAware;
import org.springframework.beans.factory.config.ConfigurableListableBeanFactory;
import org.springframework.beans.factory.support.DefaultListableBeanFactory;
import org.springframework.beans.factory.xml.XmlBeanFactory;
import org.springframework.core.io.ClassPathResource;
public class Main {
  public static void main(String[] args) throws Exception {
    XmlBeanFactory factory = new XmlBeanFactory(new ClassPathResource(
        "context.xml"));
    factory.preInstantiateSingletons();
    LoggingBean lb = (LoggingBean) factory.getBean("logging");
    lb.run();
  }
}
class LoggingBean implements BeanNameAware {
  private String name;
  public void setBeanName(String name) {
    this.name = name;
  }
  public void run() {
    System.out.println("Bean name is'" + this.name + "'.");
  }
}
class ShutdownHookBean implements BeanFactoryAware, Runnable {
  private ConfigurableListableBeanFactory beanFactory;
  public void setBeanFactory(BeanFactory beanFactory) throws BeansException {
      if (beanFactory instanceof DefaultListableBeanFactory) {
          this.beanFactory = (ConfigurableListableBeanFactory)beanFactory;
          Runtime.getRuntime().addShutdownHook(new Thread(this));
      }
  }
  public void run() {
      if (this.beanFactory != null) {
          System.out.println("Destroying singletons.");
          this.beanFactory.destroySingletons();
      }
  }
}
```

Spring-BeanFactoryAware.zip( 2,599 k)
1.  Create XmlBeanFactory from ClassPathResource
2.  XmlBeanFactory Demo
3.  FactoryObject Integration
4.  Spring factory method
