---
title: Cascade Save Or Update
nav: Cascade Save Or Update
description: /////////////////////////////////////////////////////////////////////////
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/20061027011522/http://www.java2s.com:80/Code/Java/Hibernate/CascadeSaveOrUpdate.htm
---
Cascade Save Or Update

```java title=Example.java
/////////////////////////////////////////////////////////////////////////
import java.util.*;
import org.hibernate.*;
import org.hibernate.criterion.*;
public class SimpleRetrieveTest {
  public static void main(String[] args) {
    HibernateUtil.setup("create table EVENTS ( uid int, name VARCHAR, start_Date date, duration int, location_id int);");
    HibernateUtil.setup("create table locations ( uid int, name VARCHAR, street_address VARCHAR, city VARCHAR, state VARCHAR, zip_Code VARCHAR);");
    // hibernate code start
    Session session = HibernateUtil.currentSession();
    Transaction tx = session.beginTransaction();
        Location location = new Location();
        location.setName("USA");
        location.getAddress().setStreetAddress("St.");
        location.getAddress().setCity("Regina");
        location.getAddress().setState("SK");
        location.getAddress().setZipCode("22204");
        Event event = new Event();
        event.setName("Annual Meeting");
        event.setDuration(60);
        event.setStartDate(createDate(2004, 11, 1));
        event.setLocation(location);
//        session.save(location);
        session.save(event);
        tx.commit();
    HibernateUtil.closeSession();
    HibernateUtil.sessionFactory.close();
        HibernateUtil.checkData("select * from events");
        HibernateUtil.checkData("select * from locations");
    // hibernate code end
  }
    private static Date createDate(int year, int month, int day) {
        Calendar calendar = Calendar.getInstance();
        calendar.set(year, month, day);
        return calendar.getTime();
    }
}
/////////////////////////////////////////////////////////////////////////
import java.io.Serializable;
public class Location implements Serializable{
    private Long id;
    private String name;
    private Address address = new Address();
    public Location(String name) { this.name = name;}
    public Location() { }
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public Address getAddress() { return address; }
    public void setAddress(Address address) { this.address = address;}
}
/////////////////////////////////////////////////////////////////////////
<?xml version="1.0"?>
<!DOCTYPE hibernate-mapping PUBLIC
        "-//Hibernate/Hibernate Mapping DTD 3.0//EN"
        "http://hibernate.sourceforge.net/hibernate-mapping-3.0.dtd">
<hibernate-mapping >
    <class name="Location" table="locations">
        <id name="id" column="uid" type="long">
            <generator class="increment"/>
        </id>
        <property name="name" type="string"/>
        <component name="address" class="Address" >
            <property name="streetAddress" column="street_address" type="string"/>
            <property name="city" type="string"/>
            <property name="state" type="string"/>
            <property name="zipCode" column="zip_code" type="string"/>
        </component>
    </class>
</hibernate-mapping>
/////////////////////////////////////////////////////////////////////////
<?xml version='1.0' encoding='utf-8'?>
<!DOCTYPE hibernate-configuration PUBLIC
        "-//Hibernate/Hibernate Configuration DTD 3.0//EN"
        "http://hibernate.sourceforge.net/hibernate-configuration-3.0.dtd">
<hibernate-configuration>
    <session-factory>
        <!-- Database connection settings -->
        <property name="connection.driver_class">org.hsqldb.jdbcDriver</property>
        <property name="connection.url">jdbc:hsqldb:data/tutorial</property>
        <property name="connection.username">sa</property>
        <property name="connection.password"></property>
        <!-- JDBC connection pool (use the built-in) -->
        <property name="connection.pool_size">1</property>
        <!-- SQL dialect -->
        <property name="dialect">org.hibernate.dialect.HSQLDialect</property>
        <!-- Echo all executed SQL to stdout -->
        <property name="show_sql">true</property>
        <mapping resource="Event.hbm.xml"/>
        <mapping resource="Location.hbm.xml"/>
    </session-factory>
</hibernate-configuration>
/////////////////////////////////////////////////////////////////////////
import java.io.Serializable;
import java.util.Date;
public class Event implements Serializable {
    private Long id;
    private int duration;
    private String name;
    private Date startDate;
    private Location location;
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name;   }
    public Date getStartDate() { return startDate; }
    public void setStartDate(Date startDate) {
        this.startDate = startDate;
    }
    public int getDuration() { return duration; }
    public void setDuration(int duration) {
        this.duration = duration;
    }
    public Location getLocation() { return location; }
    public void setLocation(Location location) {
        this.location = location;
    }
    public Event() { }
    public Event(String name) { this.name = name; }
}
/////////////////////////////////////////////////////////////////////////
<?xml version="1.0"?>
<!DOCTYPE hibernate-mapping PUBLIC
        "-//Hibernate/Hibernate Mapping DTD 3.0//EN"
        "http://hibernate.sourceforge.net/hibernate-mapping-3.0.dtd">
<hibernate-mapping >
    <class name="Event" table="events">
        <id name="id" column="uid" type="long">
            <generator class="increment"/>
        </id>
        <property name="name" type="string"/>
        <property name="startDate" column="start_date"
            type="date"/>
        <property name="duration" type="integer"/>
        <many-to-one name="location" column="location_id" class="Location" cascade="save-update" />
    </class>
</hibernate-mapping>
/////////////////////////////////////////////////////////////////////////
public class Address {
    private String streetAddress;
    private String city;
    private String state;
    private String zipCode;
    public String getStreetAddress() { return streetAddress; }
    public void setStreetAddress(String streetAddress) { this.streetAddress = streetAddress;}
    public String getCity() { return city; }
    public void setCity(String city) { this.city = city; }
    public String getState() { return state; }
    public void setState(String state) { this.state = state; }
    public String getZipCode() { return zipCode; }
    public void setZipCode(String zipCode) { this.zipCode = zipCode;    }
    public void parse(String address) {
        String[] parts = address.split("\\.");
        setStreetAddress(parts[0] + ".");
        String[] remainingPart = parts[1].split(" ");
        setCity(remainingPart[1].replaceAll(",", ""));
        setState(remainingPart[2]);
        setZipCode(remainingPart[3]);
    }
}
```

Download: HibernateCascadeSaveOrUpdate.zip ( 4,582 K )
Related examples in the same category
