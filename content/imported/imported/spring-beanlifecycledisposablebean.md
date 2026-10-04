---
title: Bean Lifecycle DisposableBean
nav: Bean Lifecycle DisposableB...
description: import org.springframework.beans.factory.config.ConfigurableListableBeanFactory;
section: Imported - java2s Archive
order: 1030
source: https://web.archive.org/web/20090125220917/http://www.java2s.com:80/Code/Java/Spring/BeanLifecycleDisposableBean.htm
---
Bean Lifecycle DisposableBean

```java title=Example.java
File: Main.java
import org.springframework.beans.factory.DisposableBean;
import org.springframework.beans.factory.InitializingBean;
import org.springframework.beans.factory.config.ConfigurableListableBeanFactory;
import org.springframework.beans.factory.xml.XmlBeanFactory;
import org.springframework.core.io.ClassPathResource;
import org.springframework.util.Assert;
public class Main {
  public static void main(String[] args) throws Exception {
    XmlBeanFactory factory = new XmlBeanFactory(new ClassPathResource("context.xml"));
    Runtime.getRuntime().addShutdownHook(new Thread(new ShutdownHook(factory)));
  }
}
class ShutdownHook implements Runnable {
  private ConfigurableListableBeanFactory beanFactory;
  public ShutdownHook(ConfigurableListableBeanFactory beanFactory) {
      Assert.notNull(beanFactory, "The 'beanFactory' argument must not be null.");
      this.beanFactory = beanFactory;
  }
  public void run() {
      this.beanFactory.destroySingletons();
  }
}
class DestructiveBeanI implements InitializingBean, DisposableBean {
  public void afterPropertiesSet() throws Exception {
  }
  public void destroy() {
      System.out.println("Destroying Bean");
  }
  @Override
  public String toString() {
      final StringBuilder sb = new StringBuilder();
      sb.append("DestructiveBean");
      return sb.toString();
  }
}
File: context.xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="
                http://www.springframework.org/schema/beans
                http://www.springframework.org/schema/beans/spring-beans.xsd">
    <bean id="destructive" class="DestructiveBeanI">
        <property name="filePath" value="/tmp"/>
    </bean>
</beans>
```

Spring-BeanLiftCycleDisposableBean.zip( 2,600 k)
1.  XML Bean Injection
2.  Reference another bean and set property
3.  Static Factory
4.  Serach By Base Package
5.  throw RequiredPropertyNotSetException
6.  Properties File Based Spring Bean
7.  Non Static Factory
8.  Local Reference
9.  Link With DataSource
10.  Inheritance Demo
11.  HierarchicalBeanFactory Demo
12.  Filtered By Annotatoin
13.  destroy method
14.  dependency check Demo
15.  Custom InitializationMethod
16.  component scan
17.  Component Scan and scope
18.  Component Filter Assignable
19.  implements BeanNameAware
20.  Bean Lifecycle Initializing
21.  Autowiring
22.  Alias Bean Demo
