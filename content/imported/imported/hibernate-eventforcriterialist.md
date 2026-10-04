---
title: Event For Criteria List
nav: Event For Criteria List
description: Event For Criteria List : Java examples (example source code) » Hibernate » Event
section: Imported - java2s Archive
order: 1037
source: https://web.archive.org/web/20060513083806/http://www.java2s.com/Code/Java/Hibernate/EventForCriteriaList.htm
---
Event For Criteria List : Java examples (example source code) » Hibernate » Event

```java title=Example.java
/////////////////////////////////////////////////////////////////////////
import java.io.Serializable;
import java.util.*;
import java.sql.*;
import org.hibernate.*;
import org.hibernate.cfg.*;
import org.hibernate.criterion.*;
import org.hibernate.event.*;
import org.hibernate.event.def.*;
public class Main {
   public static void main(String[] args) throws Exception {
      HibernateUtil.setup("create table User ( id int, username VARCHAR);");
      Configuration config = new Configuration();
      // Apply this event listener (programmatically)
      config.setListener("auto-flush",new NoisyAutoFlushEventListener());
      config.setListener("delete",new NoisyDeleteEventListener());
      config.setListener("dirty-check",new NoisyDirtyCheckEventListener());
      config.setListener("evict",new NoisyEvictEventListener());
      config.setListener("flush-entity",new NoisyFlushEntityEventListener());
      config.setListener("flush",new NoisyFlushEventListener());
      config.setListener("load-collection",new NoisyInitializeCollectionEventListener());
      config.setListener("load",new NoisyLoadEventListener());
      config.setListener("lock",new NoisyLockEventListener());
      config.setListener("merge",new NoisyMergeEventListener());
      config.setListener("persist",new NoisyPersistEventListener());
      config.setListener("post-delete",new NoisyPostDeleteEventListener());
      config.setListener("post-insert",new NoisyPostInsertEventListener());
      config.setListener("post-load",new NoisyPostLoadEventListener());
      config.setListener("post-update",new NoisyPostUpdateEventListener());
      config.setListener("pre-delete",new NoisyPreDeleteEventListener());
      config.setListener("pre-insert",new NoisyPreInsertEventListener());
      config.setListener("pre-load",new NoisyPreLoadEventListener());
      config.setListener("pre-update",new NoisyPreUpdateEventListener());
      config.setListener("refresh",new NoisyRefreshEventListener());
      config.setListener("replicate",new NoisyReplicateEventListener());
      config.setListener("save-update",new NoisySaveOrUpdateEventListener());
      SessionFactory factory = config.configure().buildSessionFactory();
      Session session = factory.openSession();
      System.out.println("beginTransaction()");
      Transaction tx = session.beginTransaction();
      User t1 = new User("1");
      User t2 = new User("2");
      User t3 = new User("3");
      User t4 = new User("4");
      User t5 = new User("5");
      System.out.println("save(Object)");
      session.save(t1);
      session.flush();
      System.out.println("createCriteria(Class)");
      Criteria c1 = session.createCriteria(User.class);
      System.out.println("[Criteria.add]");
      c1.add(Restrictions.eq("username","1"));
      System.out.println("[Criteria.list]");
      System.out.println(c1.list().size());
      session.close();
   }
   private static class NoisyAutoFlushEventListener extends
         DefaultAutoFlushEventListener {
      public boolean onAutoFlush(AutoFlushEvent event)
            throws HibernateException {
         System.out.println("AutoFlushEventListener.onAutoFlush(AutoFlushEvent)");
         return super.onAutoFlush(event);
      }
   }
   private static class NoisyDeleteEventListener extends
         DefaultDeleteEventListener {
      public void onDelete(DeleteEvent event) throws HibernateException {
         System.out.println("DeleteEventListener.onDelete(DeleteEvent)");
         super.onDelete(event);
      }
   }
   private static class NoisyDirtyCheckEventListener extends
         DefaultDirtyCheckEventListener {
      public boolean onDirtyCheck(DirtyCheckEvent event)
            throws HibernateException {
         System.out.println("DirtyCheckEventListener.onDirtyCheck(DirtyCheckEvent)");
         return super.onDirtyCheck(event);
      }
   }
   private static class NoisyEvictEventListener extends
         DefaultEvictEventListener { public void onEvict(EvictEvent event) throws HibernateException {
         System.out.println("EvictEventListener.onEvict(EvictEvent)");
         super.onEvict(event);
      }
   }
   private static class NoisyFlushEntityEventListener extends
         DefaultFlushEntityEventListener {
      public void onFlushEntity(FlushEntityEvent event)
            throws HibernateException {
         System.out.println("FlushEntityEventListener.onFlushEntity(FlushEntityEvent)");
         super.onFlushEntity(event);
      }
   }
   private static class NoisyFlushEventListener extends
         DefaultFlushEventListener {
      public void onFlush(FlushEvent event) throws HibernateException {
         System.out.println("FlushEventListener.onFlush(FlushEvent)");
         super.onFlush(event);
      }
   }
   private static class NoisyInitializeCollectionEventListener extends
         DefaultInitializeCollectionEventListener {
      public void onInitializeCollection(InitializeCollectionEvent event)
            throws HibernateException {
         System.out.println("InitializeCollectionEventListener.onInitializeCollection(InitializeCollectionEvent)");
         super.onInitializeCollection(event);
      }
   }
   private static class NoisyLoadEventListener extends
         DefaultLoadEventListener {
      public Object onLoad(LoadEvent event, LoadType type)
            throws HibernateException {
         System.out.println("LoadEventListener.onLoad(LoadEvent,LoadType)");
         return super.onLoad(event, type);
      }
   }
   private static class NoisyLockEventListener extends
         DefaultLockEventListener {
      public void onLock(LockEvent event) throws HibernateException {
         System.out.println("LockEventListener.onLock(LockEvent)");
         super.onLock(event);
      }
   }
   private static class NoisyMergeEventListener extends
         DefaultMergeEventListener {
      public Object onMerge(MergeEvent event, Map copiedAlready)
            throws HibernateException {
         System.out.println("MergeEventListener.onMerge(MergeEvent,Map)");
         return super.onMerge(event, copiedAlready);
      }
      public Object onMerge(MergeEvent event) throws HibernateException {
         System.out.println("MergeEventListener.onMerge(MergeEvent)");
         return super.onMerge(event);
      }
   }
   private static class NoisyPersistEventListener extends
         DefaultPersistEventListener {
      public void onPersist(PersistEvent event, Map createdAlready)
            throws HibernateException {
         System.out.println("PersistEventListener.onPersist(PersistEvent,Map)");
         super.onPersist(event, createdAlready);
      }
      public void onPersist(PersistEvent event)
            throws HibernateException {
         System.out.println("PersistEventListener.onPersist(PersistEvent)");
         super.onPersist(event);
      }
   }
   private static class NoisyPostDeleteEventListener extends
         DefaultPostDeleteEventListener {
      public void onPostDelete(PostDeleteEvent event) {
         System.out.println("PostDeleteEventListener.onPostDelete(PostDeleteEvent)");
         super.onPostDelete(event);
      }
   }
   private static class NoisyPostInsertEventListener extends
         DefaultPostInsertEventListener {
      public void onPostInsert(PostInsertEvent event) {
         System.out.println("PostInsertEventListener.onPostInsert(PostInsertEvent)");
         super.onPostInsert(event);
      }
   }
   private static class NoisyPostLoadEventListener extends
         DefaultPostLoadEventListener {
      public void onPostLoad(PostLoadEvent event) {
         System.out.println("PostLoadEventListener.onPostLoad(onPostLoad)");
         super.onPostLoad(event);
      }
   }
   private static class NoisyPostUpdateEventListener extends
         DefaultPostUpdateEventListener {
      public void onPostUpdate(PostUpdateEvent event) {
         System.out.println("PostUpdateEventListener.onPostUpdate(PostUpdateEvent)");
         super.onPostUpdate(event);
      }
   }
   private static class NoisyPreDeleteEventListener extends
         DefaultPreDeleteEventListener {
      public boolean onPreDelete(PreDeleteEvent event) {
         System.out.println("PreDeleteEventListener.onPreDelete(PreDeleteEvent)");
         return super.onPreDelete(event);
      }
   }
   private static class NoisyPreInsertEventListener extends
         DefaultPreInsertEventListener {
      public boolean onPreInsert(PreInsertEvent event) {
         System.out.println("PreInsertEventListener.onPreInsert(PreInsertEvent)");
         return super.onPreInsert(event);
      }
   }
   private static class NoisyPreLoadEventListener extends
         DefaultPreLoadEventListener {
      public void onPreLoad(PreLoadEvent event) {
         System.out.println("PreLoadEventListener.onPreLoad(PreLoadEvent)");
         super.onPreLoad(event);
      }
   }
   private static class NoisyPreUpdateEventListener extends
         DefaultPreUpdateEventListener {
      public boolean onPreUpdate(PreUpdateEvent event) {
         System.out.println("PreUpdateEventListener.onPreUpdate(PreUpdateEvent)");
         return super.onPreUpdate(event);
      }
   }
   private static class NoisyRefreshEventListener extends
         DefaultRefreshEventListener {
      public void onRefresh(RefreshEvent event)
            throws HibernateException {
         System.out.println("RefreshEventListener.onRefresh(RefreshEvent)");
         super.onRefresh(event);
      }
   }
   private static class NoisyReplicateEventListener extends
         DefaultReplicateEventListener {
      public void onReplicate(ReplicateEvent event)
            throws HibernateException {
         System.out.println("ReplicateEventListener.onReplicate(ReplicateEvent)");
         super.onReplicate(event);
      }
   }
   private static class NoisySaveOrUpdateEventListener extends
         DefaultSaveOrUpdateEventListener {
      public Serializable onSaveOrUpdate(SaveOrUpdateEvent event)
            throws HibernateException {
         System.out.println("SaveOrUpdateEventListener.onSaveOrUpdate(SaveOrUpdateEvent)");
         return super.onSaveOrUpdate(event);
      }
   }
}
/////////////////////////////////////////////////////////////////////////
<?xml version='1.0' encoding='utf-8'?>
<!DOCTYPE hibernate-mapping
   PUBLIC "-//Hibernate/Hibernate Mapping DTD//EN"
   "http://hibernate.sourceforge.net/hibernate-mapping-3.0.dtd">
<hibernate-mapping>
  <class name="User">
    <id name="id" type="int">
      <generator class="increment"/>
    </id>
    <property name="username" type="string" length="32"/>
  </class>
</hibernate-mapping>
/////////////////////////////////////////////////////////////////////////
public class User
{
    private int id;
    private String username;
    public User(){
    }
    public User(String u){
        username = u;
    }
    public int getId()
    {
        return id;
    }
    public void setId(int id)
    {
        this.id = id;
    }
    public String getUsername()
    {
        return username;
    }
    public void setUsername(String username)
    {
        this.username = username;
    }
}
/////////////////////////////////////////////////////////////////////////
<?xml version='1.0' encoding='utf-8'?>
<!DOCTYPE hibernate-configuration PUBLIC
    "-//Hibernate/Hibernate Configuration DTD//EN"
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
        <!-- Mapping files -->
        <mapping resource="User.hbm.xml"/>
    </session-factory>
</hibernate-configuration>
```

Download: HibernateEventForCriteriaList.zip (4598 K)
---
Related examples in the same category
1. Event: Your Own Save Or Update Event Listener
2. Event For Cancel Query
3. Event For Flush
4. Event For Get Identifier
5. Event For Get Method
6. Event: Load Method
7. Event: Persist
8. Event: Unique Result
9. Event: On Commit
10. Event: On Delete
11. Event: On Dirty Check Event
12. Event: On Evict
13. Event: On Flush Event
14. Event: On Lock
15. Event: On Merge
16. Event: On PreLoad and On PostLoad
17. Event: On Refresh
18. Event: On Replicate
19. Event: On Save and On Update
