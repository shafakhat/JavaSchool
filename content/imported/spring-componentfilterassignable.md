---
title: Component Filter Assignable
nav: Component Filter Assignable
description: xmlns:context="http://www.springframework.org/schema/context"
section: Imported - java2s Archive
order: 1044
source: https://web.archive.org/web/20090307144316/http://www.java2s.com:80/Code/Java/Spring/ComponentFilterAssignable.htm
---
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
File: Magic.java
package bean;
public @interface Magic {
}
File: MarkedBean.java
package bean;
public class MarkedBean implements ComponentMarker {
    @Override
    public String toString() {
        final StringBuilder sb = new StringBuilder();
        sb.append("MarkedBean");
        sb.append("{}");
        return sb.toString();
    }
}
File: SimpleBean.java
package bean;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import org.springframework.util.ObjectUtils;
/**
 * @author janm
 */
@Magic
class SimpleBean {
    private Dependency dependency;
    @Autowired(required = true)
    public void setDependency(Dependency dependency) {
        this.dependency = dependency;
    }
    @Override
    public String toString() {
        final StringBuilder sb = new StringBuilder();
        sb.append("SimpleBean");
        sb.append(ObjectUtils.identityToString(this));
        sb.append("{dependency=").append(dependency);
        sb.append('}');
        return sb.toString();
    }
}
@Component
class Dependency {
    @Override
    public String toString() {
        final StringBuilder sb = new StringBuilder();
        sb.append("Dependency");
        sb.append(ObjectUtils.identityToString(this));
        sb.append("{}");
        return sb.toString();
    }
}
File: ComponentMarker.java
package bean;
public interface ComponentMarker {
}
```

Spring-ComponentFilterAssignable.zip( 4,454 k)
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
18.  implements BeanNameAware
19.  Bean Lifecycle Initializing
20.  Bean Lifecycle DisposableBean
21.  Autowiring
22.  Alias Bean Demo
