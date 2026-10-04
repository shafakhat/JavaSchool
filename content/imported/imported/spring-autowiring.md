---
title: Auto Wiring
nav: Auto Wiring
description: ///////////////////////////////////////////////////////////////////////////////////
section: Imported - java2s Archive
order: 1021
source: https://web.archive.org/web/20061026224421/http://www.java2s.com/Code/Java/Spring/AutoWiring.htm
---
```java title=Example.java
/*
Pro Spring
By Rob Harrop
Jan Machacek
ISBN: 1-59059-461-4
Publisher: Apress
*/
///////////////////////////////////////////////////////////////////////////////////
//File: autowiring.xml
<!DOCTYPE beans PUBLIC "-//SPRING//DTD BEAN//EN" "http://www.springframework.org/dtd/spring-beans.dtd">
<beans>
    <bean id="foo" class="Foo"/>
    <bean id="bar" class="Bar"/>
    <bean id="targetByName" autowire="byName" class="Target"/>
    <bean id="targetByType" autowire="byType" class="Target"/>
    <bean id="targetConstructor" autowire="constructor" class="Target"/>
    <bean id="targetAutodetect" autowire="autodetect" class="Target"/>
</beans>
///////////////////////////////////////////////////////////////////////////////////
public class Bar {
}
///////////////////////////////////////////////////////////////////////////////////
public class Foo {
}
///////////////////////////////////////////////////////////////////////////////////
import org.springframework.beans.factory.BeanFactory;
import org.springframework.beans.factory.xml.XmlBeanFactory;
import org.springframework.core.io.FileSystemResource;
public class Target {
    private Foo foo;
    private Foo foo2;
    private Bar bar;
    public Target() {
    }
    public Target(Foo foo) {
        System.out.println("Target(Foo) called");
    }
    public Target(Foo foo, Bar bar) {
        System.out.println("Target(Foo, Bar) called");
    }
    public void setFoo(Foo foo) {
        this.foo = foo;
        System.out.println("Property foo set");
    }
    public void setFoo2(Foo foo) {
        this.foo2 = foo;
        System.out.println("Property foo2 set");
    }
    public void setMyBarProperty(Bar bar) {
        this.bar = bar;
        System.out.println("Property myBarProperty set");
    }
    public static void main(String[] args) {
        BeanFactory factory = new XmlBeanFactory(new FileSystemResource(
                "build/autowiring.xml"));
        Target t = null;
        System.out.println("Using byName:\n");
        t = (Target) factory.getBean("targetByName");
        System.out.println("\nUsing byType:\n");
        t = (Target) factory.getBean("targetByType");
        System.out.println("\nUsing constructor:\n");
        t = (Target) factory.getBean("targetConstructor");
        System.out.println("\nUsing autodetect:\n");
        t = (Target) factory.getBean("targetAutodetect");
    }
}
```

Download: AutoWiring.zip ( 1,200 K )
Related examples in the same category
