---
title: Constructor Confusion
nav: Constructor Confusion
description: ///////////////////////////////////////////////////////////////////////
section: Imported - java2s Archive
order: 1054
source: https://web.archive.org/web/20070508151507/http://www.java2s.com:80/Code/Java/Spring/ConstructorConfusion.htm
---
Constructor Confusion

```java title=Example.java
/*
Pro Spring
By Rob Harrop
Jan Machacek
ISBN: 1-59059-461-4
Publisher: Apress
*/
///////////////////////////////////////////////////////////////////////
//File: beans.xml
<!DOCTYPE beans PUBLIC "-//SPRING//DTD BEAN//EN" "http://www.springframework.org/dtd/spring-beans.dtd">
<beans>
    <!-- ctor confusion -->
    <bean id="constructorConfusion" class="ConstructorConfusion">
        <constructor-arg type="int">
            <value>90</value>
        </constructor-arg>
    </bean>
</beans>
///////////////////////////////////////////////////////////////////////
import org.springframework.beans.factory.BeanFactory;
import org.springframework.beans.factory.xml.XmlBeanFactory;
import org.springframework.core.io.FileSystemResource;
public class ConstructorConfusion {
    private String someValue;
    public ConstructorConfusion(String someValue) {
        System.out.println("ConstructorConfusion(String) called");
        this.someValue = someValue;
    }
    public ConstructorConfusion(int someValue) {
        System.out.println("ConstructorConfusion(int) called");
        this.someValue = "Number: " + Integer.toString(someValue);
    }
    public static void main(String[] args) {
        BeanFactory factory = new XmlBeanFactory(new FileSystemResource(
                "build/beans.xml"));
        ConstructorConfusion cc = (ConstructorConfusion) factory.getBean("constructorConfusion");
        System.out.println(cc);
    }
    public String toString() {
        return someValue;
    }
}
```

Download: ConstructorConfusion.zip ( 1,196 K )
Related examples in the same category
