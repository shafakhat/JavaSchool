---
title: Bean Name Example
nav: Bean Name Example
description: Bean Name Example : Java examples (example source code) » Spring » IoC Bean Name
section: Imported - java2s Archive
order: 1033
source: https://web.archive.org/web/20060504200341/http://www.java2s.com:80/Code/Java/Spring/BeanNameExample.htm
---
Bean Name Example : Java examples (example source code) » Spring » IoC Bean Name

Bean Name Example

```java title=Example.java
/*
Pro Spring
By Rob Harrop
Jan Machacek
ISBN: 1-59059-461-4
Publisher: Apress
*/
/////////////////////////////////////////////////////////////////////////////////////
<!DOCTYPE beans PUBLIC "-//SPRING//DTD BEAN//EN" "http://www.springframework.org/dtd/spring-beans.dtd">
<beans>
    <bean id="fooBean" class="AutoBean"/>
    <bean id="barBean" class="AutoBean"/>
</beans>
/////////////////////////////////////////////////////////////////////////////////////
public class AutoBean {
    public void foo() {
        System.out.println("foo()");
    }
}
/////////////////////////////////////////////////////////////////////////////////////
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.FileSystemXmlApplicationContext;
public class BeanNameExample {    public static void main(String[] args) {
        ApplicationContext ctx = new FileSystemXmlApplicationContext(
        "build/bnapc.xml");
        AutoBean fooBean = (AutoBean)ctx.getBean("fooBean");
        AutoBean barBean = (AutoBean)ctx.getBean("barBean");
        fooBean.foo();
        barBean.foo();
    }
}
```

Download: BeanNameExample.zip (1478 K)
---
Related examples in the same category
1. Define Bean Name
2. Bean Name Aliasing
