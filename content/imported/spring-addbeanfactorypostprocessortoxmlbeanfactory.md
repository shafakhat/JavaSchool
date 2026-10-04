---
title: Add BeanFactoryPostProcessor To XmlBeanFactory
nav: Add BeanFactoryPostProcess...
description: import org.springframework.beans.factory.config.BeanFactoryPostProcessor;
section: Imported - java2s Archive
order: 1002
source: https://web.archive.org/web/20100210133306/http://java2s.com/Code/Java/Spring/AddBeanFactoryPostProcessorToXmlBeanFactory.htm
---
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
import org.springframework.beans.factory.xml.XmlBeanFactory;
import org.springframework.core.io.ClassPathResource;
class Main {
  public static void main(String args[]) throws Exception {
    XmlBeanFactory factory = new XmlBeanFactory(new ClassPathResource("context.xml"));
    factory.getBean("w");
    AllBeansLister lister = new AllBeansLister();
    lister.postProcessBeanFactory(factory);
  }
}
class AllBeansLister implements BeanFactoryPostProcessor {
  public void postProcessBeanFactory(ConfigurableListableBeanFactory factory)
      throws BeansException {
    System.out.println("The factory contains the followig beans:");
    String[] beanNames = factory.getBeanDefinitionNames();
    for (int i = 0; i < beanNames.length; ++i)
      System.out.println(beanNames[i]);
  }
}
```

Spring-AddBeanFactoryPostProcessorToXmlBeanFactory.zip( 2,894 k)
1.  ApplicationContext And BeanFactoryPostProcessor
