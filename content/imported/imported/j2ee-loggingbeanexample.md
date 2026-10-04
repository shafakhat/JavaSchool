---
title: Logging Bean Example
nav: Logging Bean Example
description: Logging Bean Example : Java examples (example source code) » J2EE » Spring IoC Factory Beans
section: Imported - java2s Archive
order: 1035
source: https://web.archive.org/web/20060307045037/http://www.java2s.com:80/Code/Java/J2EE/LoggingBeanExample.htm
---
Logging Bean Example : Java examples (example source code) » J2EE » Spring IoC Factory Beans

Logging Bean Example

```java title=Example.java
/*
Pro Spring
By Rob Harrop
Jan Machacek
ISBN: 1-59059-461-4
Publisher: Apress
*/
///////////////////////////////////////////////////////////////////////////////////////
//File: logging.xml
<!DOCTYPE beans PUBLIC "-//SPRING//DTD BEAN//EN" "http://www.springframework.org/dtd/spring-beans.dtd">
<beans>
    <bean id="loggingBean" class="LoggingBean"/>
</beans>
///////////////////////////////////////////////////////////////////////////////////////
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.springframework.beans.factory.BeanNameAware;
public class LoggingBean implements BeanNameAware {
    private static final Log log = LogFactory.getLog(LoggingBean.class);
    private String beanName = null;
    public void setBeanName(String beanName) {
        this.beanName = beanName;
    }
    public void someOperation() {
        if(log.isInfoEnabled()) {
            log.info("Bean [" + beanName + "] - someOperation()");
        }
    }
}
///////////////////////////////////////////////////////////////////////////////////////
import org.springframework.beans.factory.BeanFactory;
import org.springframework.beans.factory.xml.XmlBeanFactory;
import org.springframework.core.io.FileSystemResource;
public class LoggingBeanExample {
    public static void main(String[] args) {
        BeanFactory factory = new XmlBeanFactory(new FileSystemResource(
                "build/logging.xml"));
        LoggingBean bean = (LoggingBean)factory.getBean("loggingBean");
        bean.someOperation();
    }
}
```

Download: LoggingBeanExample.zip (1197 K)
---
Related examples in the same category
1. Hierarchical Bean Factory Usage
2. Message Digest Example
3. Method Replacement Example
4. Property Editor Bean
5. Custom Editor Example
6. Accessing Factory Beans
