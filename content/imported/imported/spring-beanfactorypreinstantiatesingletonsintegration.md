---
title: BeanFactory PreInstantiate Singletons Integration
nav: BeanFactory PreInstantiate...
description: import org.springframework.beans.factory.config.ConfigurableListableBeanFactory;
section: Imported - java2s Archive
order: 1024
source: https://web.archive.org/web/20090322131248/http://www.java2s.com:80/Code/Java/Spring/BeanFactoryPreInstantiateSingletonsIntegration.htm
---
BeanFactory PreInstantiate Singletons Integration

```java title=Example.java
File: context.xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE beans PUBLIC "-//SPRING//DTD BEAN//EN"
    "http://www.springframework.org/dtd/spring-beans.dtd">
<beans>
   <bean id="instantiationCounterClass"
      class="InstantiationCounterClass"/>
</beans>
File: Main.java
import java.util.concurrent.atomic.AtomicInteger;
import org.springframework.beans.factory.config.ConfigurableListableBeanFactory;
import org.springframework.beans.factory.xml.XmlBeanFactory;
import org.springframework.core.io.ClassPathResource;
public class Main {
  public static void main(String[] args) throws Exception {
    ConfigurableListableBeanFactory beanFactory = new XmlBeanFactory(new ClassPathResource(
        "context.xml"));
    System.out.println(InstantiationCounterClass.getNumberOfInstantiations());
    beanFactory.preInstantiateSingletons();
    System.out.println(InstantiationCounterClass.getNumberOfInstantiations());
  }
}
class InstantiationCounterClass {
  private static AtomicInteger instantiationCounter = new AtomicInteger(0);
  public static int getNumberOfInstantiations() {
    return instantiationCounter.get();
  }
  public InstantiationCounterClass() {
    instantiationCounter.incrementAndGet();
  }
}
```

Spring-BeanFactoryPreInstantiateSingletonsIntegration.zip( 2,599 k)
1.  Prototype Singleton
