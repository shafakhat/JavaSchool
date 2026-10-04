---
title: Collection Injection
nav: Collection Injection
description: Collection Injection : Java examples (example source code) » Spring » IoC Collections
section: Imported - java2s Archive
order: 1040
source: https://web.archive.org/web/20060513091011/http://www.java2s.com/Code/Java/Spring/CollectionInjection.htm
---
Collection Injection : Java examples (example source code) » Spring » IoC Collections

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
    <!-- oracle bean used for a few examples -->
    <bean id="oracle" name="wiseworm" class="BookwormOracle"/>
    <!-- collection injection samples -->
    <bean id="injectCollection" class="CollectionInjection">
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
                <prop key="firstName"> Rob </prop>
                <prop key="secondName"> Harrop </prop>
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
</beans>
///////////////////////////////////////////////////////////////////////////////////////
public interface Oracle {
    public String defineMeaningOfLife();
}
///////////////////////////////////////////////////////////////////////////////////////
public class Encyclopedia {
}
///////////////////////////////////////////////////////////////////////////////////////
public class BookwormOracle implements Oracle {
    private Encyclopedia enc;
    public void setEncyclopedia(Encyclopedia enc) {
        this.enc = enc;
    }
    public String defineMeaningOfLife() {
        return "Encyclopedia's are a waste of money - use the Internet";
    }
}
///////////////////////////////////////////////////////////////////////////////////////
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Properties;
import java.util.Set;
import org.springframework.beans.factory.BeanFactory;
import org.springframework.beans.factory.xml.XmlBeanFactory;
import org.springframework.core.io.FileSystemResource;
public class CollectionInjection {
    private Map map;
    private Properties props;
    private Set set;
    private List list;
    public static void main(String[] args) {
        BeanFactory factory = new XmlBeanFactory(new FileSystemResource(
                "build/beans.xml"));
        CollectionInjection instance = (CollectionInjection) factory.getBean("injectCollection");
        instance.displayInfo();
    }
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
            System.out.println("Key: " + key + " - Value: "
                    + props.getProperty(key));
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
```

Download: CollectionInjection.zip (1199 K)
Related examples in the same category
