---
title: Bean Name Aliasing
nav: Bean Name Aliasing
description: Bean Name Aliasing : Java examples (example source code) » Spring » IoC Bean Name
section: Imported - java2s Archive
order: 1032
source: https://web.archive.org/web/20060504200245/http://www.java2s.com:80/Code/Java/Spring/BeanNameAliasing.htm
---
Bean Name Aliasing : Java examples (example source code) » Spring » IoC Bean Name

Bean Name Aliasing

```java title=Example.java
/*
Pro Spring
By Rob Harrop
Jan Machacek
ISBN: 1-59059-461-4
Publisher: Apress
*/
///////////////////////////////////////////////////////////////////////////////
//File: beans.xml
<!DOCTYPE beans PUBLIC "-//SPRING//DTD BEAN//EN" "http://www.springframework.org/dtd/spring-beans.dtd">
<beans>
    <!-- aliasing examples -->
    <bean id="name1" name="name2,name3,name4" class="java.lang.String"/>
</beans>
//////////////////////////////////////////////////////////////////////////////
import org.springframework.beans.factory.BeanFactory;
import org.springframework.beans.factory.xml.XmlBeanFactory;
import org.springframework.core.io.FileSystemResource;
public class BeanNameAliasing {
    public static void main(String[] args) {
        BeanFactory factory = new XmlBeanFactory(new FileSystemResource("build/beans.xml"));
        String s1 = (String)factory.getBean("name1");
        String s2 = (String)factory.getBean("name2");
        String s3 = (String)factory.getBean("name3");
        String s4 = (String)factory.getBean("name4");
        System.out.println((s1 == s2));
        System.out.println((s2 == s3));
        System.out.println((s3 == s4));
        String[] x = factory.getAliases("name3");
        System.out.println("");
    }
}
```

Download: BeanNameAliasing.zip (1196 K)
---
Related examples in the same category
1. Define Bean Name
2. Bean Name Example
