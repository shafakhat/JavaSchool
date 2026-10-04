---
title: ApplicationContext Aware
nav: ApplicationContext Aware
description: http://www.springframework.org/schema/beans/spring-beans.xsd">
section: Imported - java2s Archive
order: 1013
source: https://web.archive.org/web/20090310175330/http://www.java2s.com:80/Code/Java/Spring/ApplicationContextAware.htm
---
```java title=Example.java
File: context.xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="
                http://www.springframework.org/schema/beans
                http://www.springframework.org/schema/beans/spring-beans.xsd">
    <bean id="contextAware" class="ContextAwareDemo"/>
</beans>
File: Main.java
import org.springframework.beans.BeansException;
import org.springframework.context.ApplicationContext;
import org.springframework.context.ApplicationContextAware;
import org.springframework.context.support.ClassPathXmlApplicationContext;
public class Main {
  public static void main(String[] args) throws Exception {
    ApplicationContext ctx = new ClassPathXmlApplicationContext(
        "context.xml");
    ContextAwareDemo demo = (ContextAwareDemo) ctx.getBean("contextAware");
    demo.displayAppContext();
  }
}
class ContextAwareDemo implements ApplicationContextAware {
  private ApplicationContext ctx;
  public void setApplicationContext(ApplicationContext applicationContext) throws BeansException {
    ctx = applicationContext;
  }
  public static void main(String[] args) {
  }
  public void displayAppContext() {
    System.out.println(ctx);
  }
}
```

Spring-ApplicationContextAware.zip( 2,598 k)
1.  ResourceLoader Demo
2.  Create ApplicationContext with ClassPathXmlApplicationContext
3.  ContextApplication Event
