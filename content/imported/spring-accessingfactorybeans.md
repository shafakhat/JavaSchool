---
title: Accessing Factory Beans
nav: Accessing Factory Beans
description: <!DOCTYPE beans PUBLIC "-//SPRING//DTD BEAN//EN" "http://www.springframework.org/dtd/spring-beans.dtd">
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/20070329152011/http://www.java2s.com:80/Code/Java/Spring/AccessingFactoryBeans.htm
---
Accessing Factory Beans

```java title=Example.java
/*
Pro Spring
By Rob Harrop
Jan Machacek
ISBN: 1-59059-461-4
Publisher: Apress
*/
//spring.xml
<!DOCTYPE beans PUBLIC "-//SPRING//DTD BEAN//EN" "http://www.springframework.org/dtd/spring-beans.dtd">
<beans>
    <bean id="messageDigest" class="MessageDigestFactoryBean">
        <property name="algorithmName">
            <value>SHA1</value>
        </property>
    </bean>
</beans>
//////////////////////////////////////////////////////////////////////////////
import java.security.MessageDigest;
import org.springframework.beans.factory.FactoryBean;
import org.springframework.beans.factory.InitializingBean;
public class MessageDigestFactoryBean implements FactoryBean, InitializingBean {
    private String algorithmName = "MD5";
    private MessageDigest messageDigest = null;
    public Object getObject() throws Exception {
       return messageDigest;
    }
    public Class getObjectType() {
       return MessageDigest.class;
    }
    public boolean isSingleton() {
       return true;
    }
    public void afterPropertiesSet() throws Exception {
        messageDigest = MessageDigest.getInstance(algorithmName);
    }
    public void setAlgorithmName(String algorithmName) {
        this.algorithmName = algorithmName;
    }
}
//////////////////////////////////////////////////////////////////////////////
import java.security.MessageDigest;
import org.springframework.beans.factory.BeanFactory;
import org.springframework.beans.factory.xml.XmlBeanFactory;
import org.springframework.core.io.FileSystemResource;
public class AccessingFactoryBeans {
    public static void main(String[] args) {
        BeanFactory factory = new XmlBeanFactory(new FileSystemResource(
                "build/spring.xml"));
        MessageDigest digest = (MessageDigest) factory
                .getBean("messageDigest");
        MessageDigestFactoryBean factoryBean = (MessageDigestFactoryBean) factory
                .getBean("&messageDigest");
    }
}
```

Download: AccessingFactoryBeans.zip ( 1,197 K )
Related examples in the same category
