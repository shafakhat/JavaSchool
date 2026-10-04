---
title: Call Constructor
nav: Call Constructor
description: XmlBeanFactory bf = new XmlBeanFactory(new ClassPathResource("context.xml"));
section: Imported - java2s Archive
order: 1035
source: https://web.archive.org/web/20090404102137/http://www.java2s.com:80/Code/Java/Spring/CallConstructor.htm
---
Call Constructor

```java title=Example.java
File: context.xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:util="http://www.springframework.org/schema/util"
       xsi:schemaLocation="
                http://www.springframework.org/schema/beans
                http://www.springframework.org/schema/beans/spring-beans.xsd
                http://www.springframework.org/schema/util
                http://www.springframework.org/schema/util/spring-util.xsd">
    <bean id="encyclopedia"
          name="knowitall"
          class="ConfigurableEncyclopedia">
        <constructor-arg>
            <util:map>
                <entry key="AgeOfUniverse" value="13700000000"/>
                <entry key="ConstantOfLife" value="326190476"/>
            </util:map>
        </constructor-arg>
    </bean>
    <bean id="oracle" class="BookwormOracle">
        <property name="encyclopedia" ref="knowitall"/>
    </bean>
</beans>
File: Main.java
import java.util.Map;
import org.springframework.beans.factory.xml.XmlBeanFactory;
import org.springframework.core.io.ClassPathResource;
import org.springframework.util.Assert;
public class Main {
  public static void main(String[] a) {
    XmlBeanFactory bf = new XmlBeanFactory(new ClassPathResource("context.xml"));
    Oracle oracle = (Oracle) bf.getBean("oracle");
    System.out.println("Meaning of life is " + oracle.defineMeaningOfLife());
  }
}
interface Oracle {
  String defineMeaningOfLife();
}
interface Encyclopedia {
  Long findLong(String entry);
}
class BookwormOracle implements Oracle {
  private Encyclopedia encyclopedia;
  public String defineMeaningOfLife() {
      Long ageOfUniverse = this.encyclopedia.findLong("AgeOfUniverse");
      Long constantOfLife = this.encyclopedia.findLong("ConstantOfLife");
      return String.valueOf(ageOfUniverse / constantOfLife);
  }
  public void setEncyclopedia(Encyclopedia encyclopedia) {
      this.encyclopedia = encyclopedia;
  }
}
class ConfigurableEncyclopedia implements Encyclopedia {
  private Map<String, Long> entries;
  public ConfigurableEncyclopedia(Map<String, Long> entries) {
      Assert.notNull(entries, "The 'entries' argument cannot be null.");
      this.entries = entries;
  }
  public Long findLong(String entry) {
      return this.entries.get(entry);
  }
}
```

Spring-XMLBasedBeanConfigurationFillConstructor.zip( 2,601 k)
1.  Constructor Confusion Demo
2.  ConstructorCaller In ContextConfig
3.  Constructor Argument And Local Reference
4.  SingletonScope And PrototypeScope
