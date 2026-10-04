---
title: Add BeanPostProcessor To XmlBeanFactory
nav: Add BeanPostProcessor To X...
description: import org.springframework.beans.factory.config.BeanPostProcessor;
section: Imported - java2s Archive
order: 1003
source: https://web.archive.org/web/20100212113803/http://java2s.com/Code/Java/Spring/AddBeanPostProcessorToXmlBeanFactory.htm
---
Add BeanPostProcessor To XmlBeanFactory

```java title=Example.java
File: context.xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE beans PUBLIC "-//SPRING//DTD BEAN//EN"
    "http://www.springframework.org/dtd/spring-beans.dtd">
<beans>
  <bean id="w" class="java.lang.String">
  </bean>
  <bean id="beanInitLogger" class="BeanInitializationLogger"/>
</beans>
File: Main.java
import org.springframework.beans.BeansException;
import org.springframework.beans.factory.config.BeanPostProcessor;
import org.springframework.beans.factory.xml.XmlBeanFactory;
import org.springframework.core.io.ClassPathResource;
class Main {
  public static void main(String args[]) throws Exception {
    XmlBeanFactory factory = new XmlBeanFactory(new ClassPathResource("context.xml"));
    BeanInitializationLogger logger = new BeanInitializationLogger();
    factory.addBeanPostProcessor(logger);
    factory.preInstantiateSingletons();
  }
}
class BeanInitializationLogger implements BeanPostProcessor {
  public Object postProcessBeforeInitialization(Object bean, String beanName)
      throws BeansException {
    return bean;
  }
  public Object postProcessAfterInitialization(Object bean, String beanName)
      throws BeansException {
    System.out.println("Bean '" + beanName + "' initialized");
    return bean;
  }
}
```

Spring-AddaddBeanPostProcessorToXmlBeanFactory.zip( 2,894 k)
1.  Implements BeanPostProcessor
