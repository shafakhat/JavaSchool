---
title: Compare Beans From FactoryBean
nav: Compare Beans From Factory...
description: http://www.springframework.org/schema/beans/spring-beans.xsd">
section: Imported - java2s Archive
order: 1043
source: https://web.archive.org/web/20090423061108/http://www.java2s.com:80/Code/Java/Spring/CompareBeansFromFactoryBean.htm
---
Compare Beans From FactoryBean

```java title=Example.java
File: context.xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="
                http://www.springframework.org/schema/beans
                http://www.springframework.org/schema/beans/spring-beans.xsd">
    <bean id="sha" class="MessageDigestFactoryBean">
        <property name="algorithm" value="SHA1"/>
    </bean>
    <bean id="md5" class="MessageDigestFactoryBean"/>
</beans>
File: Main.java
import java.security.MessageDigest;
import org.springframework.beans.factory.FactoryBean;
import org.springframework.beans.factory.InitializingBean;
import org.springframework.beans.factory.xml.XmlBeanFactory;
import org.springframework.core.io.ClassPathResource;
public class Main {
  public static void main(String[] args) throws Exception {
    XmlBeanFactory factory = new XmlBeanFactory(new ClassPathResource("context.xml"));
    MessageDigestFactoryBean factoryBean = (MessageDigestFactoryBean) factory.getBean("&sha");
    String d1 = (String) factory.getBean("sha");
    String d2 = (String) factoryBean.getObject();
    System.out.println("Equal created? " + (d1.equals(d2)));
  }
}
class MessageDigestFactoryBean implements FactoryBean, InitializingBean {
  private static final String DEFAULT_ALGORITHM = "MD5";
  private String algorithm = DEFAULT_ALGORITHM;
  public Object getObject() throws Exception {
    return this.algorithm;
  }
  public Class getObjectType() {
    return MessageDigest.class;
  }
  public boolean isSingleton() {
    return true;
  }
  public void setAlgorithm(String algorithm) {
    this.algorithm = algorithm;
  }
  public void afterPropertiesSet() throws Exception {
    this.algorithm += " after setting";
  }
}
```

Spring-CompareBeansFromFactoryBean.zip( 2,599 k)
1.  Spring FactoryBean Demo
