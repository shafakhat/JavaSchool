---
title: Component Scan and scope
nav: Component Scan and scope
description: xmlns:context="http://www.springframework.org/schema/context"
section: Imported - java2s Archive
order: 1046
source: https://web.archive.org/web/20090426214739/http://www.java2s.com:80/Code/Java/Spring/ComponentScanandscope.htm
---
```java title=Example.java
File: context.xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:context="http://www.springframework.org/schema/context"
       xmlns:aop="http://www.springframework.org/schema/aop"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="
                http://www.springframework.org/schema/beans
                http://www.springframework.org/schema/beans/spring-beans.xsd
                http://www.springframework.org/schema/context
                http://www.springframework.org/schema/context/spring-context.xsd
                http://www.springframework.org/schema/aop
                http://www.springframework.org/schema/aop/spring-aop.xsd">
    <aop:aspectj-autoproxy />
    <context:component-scan base-package="bean">
        <context:include-filter type="annotation" expression="org.aspectj.lang.annotation.Aspect"/>
    </context:component-scan>
</beans>
File: Main.java
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
import bean.Helper;
import bean.HelperDemo;
public class Main {
  public static void main(String[] args) throws Exception {
    ApplicationContext ac = new ClassPathXmlApplicationContext(
        "context.xml");
    HelperDemo hd1 = (HelperDemo) ac.getBean("helperDemo");
    hd1.someOperation();
    System.out.println(hd1);
    HelperDemo hd2 = (HelperDemo) ac.getBean("helperDemo");
    hd2.someOperation();
    System.out.println(hd2);
    Helper helper = (Helper) ac.getBean("helper");
    System.out.println(helper);
  }
}
File: Helper.java
package bean;
import org.springframework.beans.factory.config.BeanDefinition;
import org.springframework.context.annotation.Scope;
import org.springframework.stereotype.Component;
@Component("helper")
@Scope(BeanDefinition.SCOPE_PROTOTYPE)
public class Helper {
    private int count;
    public void work() {
        this.count++;
    }
    @Override
    public String toString() {
        final StringBuilder sb = new StringBuilder();
        sb.append("Helper");
        sb.append("{count=").append(count);
        sb.append('}');
        return sb.toString();
    }
}
File: HelperDemo.java
package bean;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.config.BeanDefinition;
import org.springframework.context.annotation.Scope;
import org.springframework.stereotype.Component;
@Component
@Scope(BeanDefinition.SCOPE_PROTOTYPE)
public class HelperDemo {
    @Autowired
    private Helper helper;
    public void setHelper(Helper helper) {
        this.helper = helper;
    }
    public void someOperation() {
        this.helper.work();
    }
    @Override
    public String toString() {
        final StringBuilder sb = new StringBuilder();
        sb.append("HelperDemo");
        sb.append("{helper=").append(helper);
        sb.append('}');
        return sb.toString();
    }
}
```

Spring-ComponentScan.zip( 4,452 k)
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
17.  Component Filter Assignable
18.  implements BeanNameAware
19.  Bean Lifecycle Initializing
20.  Bean Lifecycle DisposableBean
21.  Autowiring
22.  Alias Bean Demo
