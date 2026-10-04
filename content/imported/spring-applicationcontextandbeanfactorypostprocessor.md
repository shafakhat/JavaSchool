---
title: ApplicationContext And BeanFactoryPostProcessor
nav: ApplicationContext And Bea...
description: import org.springframework.beans.factory.config.BeanFactoryPostProcessor;
section: Imported - java2s Archive
order: 1012
source: https://web.archive.org/web/20100210133337/http://java2s.com/Code/Java/Spring/ApplicationContextAndBeanFactoryPostProcessor.htm
---
ApplicationContext And BeanFactoryPostProcessor

```java title=Example.java
File: context.xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE beans PUBLIC "-//SPRING//DTD BEAN//EN"
    "http://www.springframework.org/dtd/spring-beans.dtd">
<beans>
  <bean id="w" class="java.lang.String">
  </bean>
  <bean id="allBeansLister" class="AllBeansLister"/>
</beans>
File: Main.java
import org.springframework.beans.BeansException;
import org.springframework.beans.factory.config.BeanFactoryPostProcessor;
import org.springframework.beans.factory.config.ConfigurableListableBeanFactory;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
class Main {
  public static void main(String args[]) throws Exception {
    ApplicationContext ctx = new ClassPathXmlApplicationContext("context.xml");
    ctx.getBean("w");
  }
}
class AllBeansLister implements BeanFactoryPostProcessor {
  public void postProcessBeanFactory(ConfigurableListableBeanFactory factory) throws BeansException {
    System.out.println("The factory contains the followig beans:");
    String[] beanNames = factory.getBeanDefinitionNames();
    for (int i = 0; i < beanNames.length; ++i)
      System.out.println(beanNames[i]);
  }
}
```

Spring-ApplicationContextAndBeanFactoryPostProcessor.zip( 2,894 k)
1.  Add BeanFactoryPostProcessor To XmlBeanFactory
