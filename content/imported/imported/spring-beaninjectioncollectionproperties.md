---
title: Bean Injection
nav: Bean Injection
description: BeanFactory factory = new XmlBeanFactory(new ClassPathResource("context.xml"));
section: Imported - java2s Archive
order: 1027
source: https://web.archive.org/web/20090227235425/http://www.java2s.com:80/Code/Java/Spring/BeanInjectionCollectionProperties.htm
---
Bean Injection: Collection Properties

```java title=Example.java
File: Main.java
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Properties;
import java.util.Set;
import org.springframework.beans.factory.BeanFactory;
import org.springframework.beans.factory.xml.XmlBeanFactory;
import org.springframework.core.io.ClassPathResource;
public class Main {
  public static void main(String[] args) {
    BeanFactory factory = new XmlBeanFactory(new ClassPathResource("context.xml"));
    CollectionsDemo instance = (CollectionsDemo) factory.getBean("collectionsDemo");
    instance.displayInfo();
  }
}
interface Encyclopedia {
  Long findLong(String entry);
}
interface Oracle {
  String defineMeaningOfLife();
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
class CollectionsDemo {
  private Map map;
  private Properties props;
  private Set set;
  private List list;
  public void setList(List list) {
    this.list = list;
  }
  public void setSet(Set set) {
    this.set = set;
  }
  public void setMap(Map map) {
    this.map = map;
  }
  public void setProps(Properties props) {
    this.props = props;
  }
  public void displayInfo() {
    // display the Map
    Iterator i = map.keySet().iterator();
    System.out.println("Map contents:\n");
    while (i.hasNext()) {
      Object key = i.next();
      System.out.println("Key: " + key + " - Value: " + map.get(key));
    }
    // display the properties
    i = props.keySet().iterator();
    System.out.println("\nProperties contents:\n");
    while (i.hasNext()) {
      String key = i.next().toString();
      System.out.println("Key: " + key + " - Value: " + props.getProperty(key));
    }
    // display the set
    i = set.iterator();
    System.out.println("\nSet contents:\n");
    while (i.hasNext()) {
      System.out.println("Value: " + i.next());
    }
    // display the list
    i = list.iterator();
    System.out.println("\nList contents:\n");
    while (i.hasNext()) {
      System.out.println("Value: " + i.next());
    }
  }
}
File: context.xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="
                http://www.springframework.org/schema/beans
                http://www.springframework.org/schema/beans/spring-beans.xsd">
    <bean id="collectionsDemo" class="CollectionsDemo">
        <property name="map">
            <map>
                <entry key="someValue">
                    <value>Hello World!</value>
                </entry>
                <entry key="someBean">
                    <ref local="oracle"/>
                </entry>
            </map>
        </property>
        <property name="props">
            <props>
                <prop key="firstName">
                    Jan
                </prop>
                <prop key="secondName">
                    Machacek
                </prop>
            </props>
        </property>
        <property name="set">
            <set>
                <value>Hello World!</value>
                <ref local="oracle"/>
            </set>
        </property>
        <property name="list">
            <list>
                <value>Hello World!</value>
                <ref local="oracle"/>
            </list>
        </property>
    </bean>
    <bean id="oracle" class="BookwormOracle"/>
</beans>
```

Spring-BeanInjectionCollectionProperties.zip( 2,601 k)
1.  Property Setting: URL
2.  PropertySetting: String Array
3.  Property Setting: Stream From URL
4.  Property Setting: Properties
5.  Property Setting: Integer
6.  Property Setting: File
7.  Property Setting: Class type
8.  Property Setting: Byte Array
9.  Property Setting: Boolean
10.  Property Setting: BigDecimal
11.  Properties Setting: Date
12.  Load property File In Context
13.  lazy init
14.  Fill Value To List
15.  Fill Map
16.  Fill Set
17.  Fill Properties
18.  Fill List To Another List
19.  Fill Calendar Object To List
20.  Create List Map In Context
21.  Bean Injection: Map
22.  Bean Injection Collection: Set
23.  Bean Injection Collection: Map
24.  Bean Injection Collection: List
