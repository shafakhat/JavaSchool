---
title: Generic
nav: Generic
description: Generic: Dao Delete : Java examples (example source code) » Hibernate » DAO Generic DAO
section: Imported - java2s Archive
order: 1004
source: https://web.archive.org/web/20060513081221/http://www.java2s.com/Code/Java/Hibernate/GenericDaoDelete.htm
---
Generic: Dao Delete : Java examples (example source code) » Hibernate » DAO Generic DAO

Generic: Dao Delete

```java title=Example.java
/////////////////////////////////////////////////////////////////////////
import java.util.*;
import java.sql.*;
import org.hibernate.*;
import org.hibernate.criterion.*;
public class Main {
  public static void main(String[] args) {
    HibernateUtil.setup("create table EVENTS ( uid int, name VARCHAR, start_Date date, duration int);");
    // hibernate code start
        EventDao eventDao = new EventDao();
        Event event = new Event();
        event.setName("Create");
        eventDao.create(event);
        eventDao.delete(event);
        HibernateUtil.checkData("select uid, name from events");
    // hibernate code end
  }
}
/////////////////////////////////////////////////////////////////////////
import org.hibernate.HibernateException;
import org.hibernate.Session;
import org.hibernate.Transaction;
import java.util.List;
public class EventDao extends AbstractDao {
    public EventDao() {
        super();
    }
    /**
     * Insert a new Event into the database.
     * @param event
     */
    public void create(Event event) throws DataAccessLayerException {
        super.saveOrUpdate(event);
    }
    /**
     * Delete a detached Event from the database.
     * @param event
     */
    public void delete(Event event) throws DataAccessLayerException {
        super.delete(event);
    }
    /**
     * Find an Event by its primary key.
     * @param id
     * @return
     */
    public Event find(Long id) throws DataAccessLayerException {
        return (Event) super.find(Event.class, id);
    }
    /**
     * Updates the state of a detached Event.
     *
     * @param event
     */
    public void update(Event event) throws DataAccessLayerException {
        super.saveOrUpdate(event);
    }
    /**
     * Finds all Events in the database.
     * @return
     */
    public List findAll() throws DataAccessLayerException{
        return super.findAll(Event.class);
    }
}
/////////////////////////////////////////////////////////////////////////
import org.hibernate.HibernateException;
import org.hibernate.Session;
import org.hibernate.Transaction;
import org.hibernate.Query;
import java.util.List;
public abstract class AbstractDao {
    private Session session;
    private Transaction tx;
    public AbstractDao() {
        HibernateFactory.buildIfNeeded();
    }
    protected void saveOrUpdate(Object obj) {
        try {
            startOperation();
            session.saveOrUpdate(obj);
            tx.commit();
        } catch (HibernateException e) {
            handleException(e);
        } finally {
            HibernateFactory.close(session);
        }
    }
    protected void delete(Object obj) {
        try {
            startOperation();
            session.delete(obj);
            tx.commit();
        } catch (HibernateException e) {
            handleException(e);
        } finally {
            HibernateFactory.close(session);
        }
    }
    protected Object find(Class clazz, Long id) {
        Object obj = null;
        try {
            startOperation();
            obj = session.load(clazz, id);
            tx.commit();
        } catch (HibernateException e) {
            handleException(e);
        } finally {
//            HibernateFactory.close(session); }
        return obj;
    }
    protected List findAll(Class clazz) {
        List objects = null;
        try {
            startOperation();
            Query query = session.createQuery("from " + clazz.getName());
            objects = query.list();
            tx.commit();
        } catch (HibernateException e) {
            handleException(e);
        } finally {
            HibernateFactory.close(session);
        }
        return objects;
    }
    protected void handleException(HibernateException e) throws DataAccessLayerException {
        HibernateFactory.rollback(tx);
        throw new DataAccessLayerException(e);
    }
    protected void startOperation() throws HibernateException {
        session = HibernateFactory.openSession();
        tx = session.beginTransaction();
    }
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
        <property name="startDate" column="start_date" type="date"/>
        <property name="duration" type="integer"/>
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
        <property name="connection.url">jdbc:hsqldb:data/tutorial</property>      <property name="connection.username">sa</property>
        <property name="connection.password"></property>
        <!-- JDBC connection pool (use the built-in) -->
        <property name="connection.pool_size">1</property>
        <!-- SQL dialect -->
        <property name="dialect">org.hibernate.dialect.HSQLDialect</property>
        <!-- Echo all executed SQL to stdout -->
        <property name="show_sql">true</property>
        <mapping resource="Event.hbm.xml"/>
    </session-factory>
</hibernate-configuration>
/////////////////////////////////////////////////////////////////////////
```

Download: HibernateGenericDaoDelete.zip (4583 K)
---
Related examples in the same category
1. Generic Dao: Create
2. Generic Dao: Find
3. Generic Dao Find All
4. Generic Dao Save Or Update
5. Generic Dao: Update
