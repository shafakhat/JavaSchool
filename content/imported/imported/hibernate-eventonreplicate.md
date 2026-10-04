---
title: Event
nav: Event
description: /////////////////////////////////////////////////////////////////////////
section: Imported - java2s Archive
order: 1051
source: https://web.archive.org/web/20060513083653/http://www.java2s.com/Code/Java/Hibernate/EventOnReplicate.htm
---
Event: On Replicate

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
      t1.setUsername("REPLICATE1");
      System.out.println("replicate(Object,ReplicationMode)");
      session.replicate(t1, ReplicationMode.LATEST_VERSION);
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
         DefaultEvictEventListener {
      public void onEvict(EvictEvent event) throws HibernateException {
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
   }private static class NoisyLockEventListener extends
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
```

Download: HibernateEventOnReplicate.zip (4598 K)
---
Related examples in the same category
1. Event: Your Own Save Or Update Event Listener
2. Event For Cancel Query
3. Event For Criteria List
4. Event For Flush
5. Event For Get Identifier
6. Event For Get Method
7. Event: Load Method
8. Event: Persist
9. Event: Unique Result
10. Event: On Commit
11. Event: On Delete
12. Event: On Dirty Check Event
13. Event: On Evict
14. Event: On Flush Event
15. Event: On Lock
16. Event: On Merge
17. Event: On PreLoad and On PostLoad
18. Event: On Refresh
19. Event: On Save and On Update
