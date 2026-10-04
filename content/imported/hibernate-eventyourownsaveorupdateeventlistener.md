---
title: Event
nav: Event
description: Event: Your Own Save Or Update Event Listener : Java examples (example source code) » Hibernate » Event
section: Imported - java2s Archive
order: 1055
source: https://web.archive.org/web/20060513083729/http://www.java2s.com/Code/Java/Hibernate/EventYourOwnSaveOrUpdateEventListener.htm
---
Event: Your Own Save Or Update Event Listener : Java examples (example source code) » Hibernate » Event

Event: Your Own Save Or Update Event Listener

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
      config.setListener("save-update", new UseringSaveOrUpdateEventListener());
      SessionFactory factory = config.configure().buildSessionFactory();
      Session session = factory.openSession();
      Transaction tx = session.beginTransaction();
      session.saveOrUpdate(new User("R1"));
      session.saveOrUpdate(new User("R2"));
      tx.commit();
      session.close();
   }
}
class UseringSaveOrUpdateEventListener extends DefaultSaveOrUpdateEventListener
{
   public Serializable onSaveOrUpdate(SaveOrUpdateEvent event)
         throws HibernateException {
      if( event.getObject() instanceof User ) {
         User user = (User)event.getObject();
         System.out.println("Preparing to save or update user " + user.getUsername());
         if( user.getUsername().equalsIgnoreCase("R1")) {
            System.out.println("Conventional user not recorded.");
            // Here we prevent the invocation
            // of saveOrUpdate on the Session from having
            // any effect on the database!
            return null;
         }
      }
      return super.onSaveOrUpdate(event);
   }
}
/////////////////////////////////////////////////////////////////////////<?xml version='1.0' encoding='utf-8'?>
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

Download: HibernateEventYourOwnSaveOrUpdateEventListener.zip (4582 K)
---
Related examples in the same category
1. Event For Cancel Query
2. Event For Criteria List
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
