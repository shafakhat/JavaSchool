---
title: Generic Dao
nav: Generic Dao
description: Generic Dao: Create : Java examples (example source code) » Hibernate » DAO Generic DAO
section: Imported - java2s Archive
order: 1003
source: https://web.archive.org/web/20060513081225/http://www.java2s.com/Code/Java/Hibernate/GenericDaoCreate.htm
---
Generic Dao: Create : Java examples (example source code) » Hibernate » DAO Generic DAO

Generic Dao: Create

```java title=Example.java
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
import java.io.Serializable;
import java.util.Date;
import java.util.Set;
import java.util.LinkedHashSet;
public class Event implements Serializable {
    private Long id;
    private int duration;
    private String name;
    private Date startDate;
    public Event() {
    }
    public Event(String name) {
        this.name = name;
    }
    /**
     * @hibernate.id generator-class="native" column="uid"
     * @return
     */
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    /**
     * @hibernate.property column="name"
     * @return
     */
    public String getName() { return name; }
    public void setName(String name) { this.name = name;   }
    /**
     * @hibernate.property column="start_date"
     * @return
     */
    public Date getStartDate() { return startDate; }
    public void setStartDate(Date startDate) { this.startDate = startDate; }
    /**
     * @hibernate.property column="duration"
     * @return
     */
    public int getDuration() { return duration; }
    public void setDuration(int duration) { this.duration = duration; }
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
    </session-factory>
</hibernate-configuration>
/////////////////////////////////////////////////////////////////////////
import org.hibernate.*;
import org.hibernate.cfg.Configuration;
import org.apache.commons.logging.*;
public class HibernateFactory {
    private static SessionFactory sessionFactory;
    private static Log log = LogFactory.getLog(HibernateFactory.class);
    /**
     * Constructs a new Singleton SessionFactory
     * @return
     * @throws HibernateException
     */
    public static SessionFactory buildSessionFactory() throws HibernateException {
        if (sessionFactory != null) {
            closeFactory();
        }
        return configureSessionFactory();
    }
    /**
     * Builds a SessionFactory, if it hasn't been already.
     */
    public static SessionFactory buildIfNeeded() throws DataAccessLayerException{
        if (sessionFactory != null) {
            return sessionFactory;
        }
        try {
            return configureSessionFactory();
        } catch (HibernateException e) {
            throw new DataAccessLayerException(e);
        }
    }
    public static SessionFactory getSessionFactory() {
        return sessionFactory;
    }
    public static Session openSession() throws HibernateException {
        buildIfNeeded();
        return sessionFactory.openSession();
    }
    public static void closeFactory() {
        if (sessionFactory != null) {
            try {
                sessionFactory.close();
            } catch (HibernateException ignored) {
                log.error("Couldn't close SessionFactory", ignored);
            }
        }
    }
    public static void close(Session session) {
        if (session != null) {
            try {
                session.close();
            } catch (HibernateException ignored) {
                log.error("Couldn't close Session", ignored);
            }
        }
    }
    public static void rollback(Transaction tx) {
        try {
            if (tx != null) {
                tx.rollback();
            }
        } catch (HibernateException ignored) {
            log.error("Couldn't rollback Transaction", ignored);
        }
    }
    /**
     *
     * @return
     * @throws HibernateException
     */
    private static SessionFactory configureSessionFactory() throws HibernateException {
        Configuration configuration = new Configuration();
        configuration.configure();
        sessionFactory = configuration.buildSessionFactory();
        return sessionFactory;
    }
}
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
        HibernateUtil.checkData("select uid, name from events");
    // hibernate code end
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
            HibernateFactory.close(session);
        }
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
/**
 * Represents Exceptions thrown by the Data Access Layer.
 */
public class DataAccessLayerException extends RuntimeException {
    public DataAccessLayerException() {
    }
    public DataAccessLayerException(String message) {
        super(message);
    }
    public DataAccessLayerException(Throwable cause) {
        super(cause);
    }
    public DataAccessLayerException(String message, Throwable cause) {
        super(message, cause);
    }
}
```

Download: HibernateGenericDaoCreate.zip (4583 K)
---
Related examples in the same category
1. Generic: Dao Delete
2. Generic Dao: Find
3. Generic Dao Find All
4. Generic Dao Save Or Update
5. Generic Dao: Update
