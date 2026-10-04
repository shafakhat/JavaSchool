---
title: Achieving Singleton in IoC
nav: Achieving Singleton in IoC
description: Achieving Singleton in IoC : Java examples (example source code) » Spring » IoC Singleton
section: Imported - java2s Archive
order: 1001
source: https://web.archive.org/web/20060513074544/http://www.java2s.com/Code/Java/Spring/AchievingSingletoninIoC.htm
---
Achieving Singleton in IoC : Java examples (example source code) » Spring » IoC Singleton

```java title=Example.java
/*
Pro Spring
By Rob Harrop
Jan Machacek
ISBN: 1-59059-461-4
Publisher: Apress
*/
///////////////////////////////////////////////////////////////////////////////////////
//File: beans.xml
<!DOCTYPE beans PUBLIC "-//SPRING//DTD BEAN//EN" "http://www.springframework.org/dtd/spring-beans.dtd">
<beans>
    <!-- non-singleton examples -->
    <bean id="nonSingleton" class="java.lang.String" singleton="true">
        <constructor-arg>
            <value>Value</value>
        </constructor-arg>
    </bean>
</beans>
///////////////////////////////////////////////////////////////////////////////////////
import org.springframework.beans.factory.BeanFactory;
import org.springframework.beans.factory.xml.XmlBeanFactory;
import org.springframework.core.io.FileSystemResource;
public class NonSingleton {
    public static void main(String[] args) {
        BeanFactory factory = new XmlBeanFactory(new FileSystemResource(
                "build/beans.xml"));
        String s1 = (String)factory.getBean("nonSingleton");
        String s2 = (String)factory.getBean("nonSingleton");
        System.out.println("Identity Equal?: " + (s1 ==s2));
        System.out.println("Value Equal:? " + s1.equals(s2));
        System.out.println(s1);
        System.out.println(s2);
    }
}
```

Download: Singleton.zip (1196 K)
---
Related examples in the same category
1. Non Singleton
