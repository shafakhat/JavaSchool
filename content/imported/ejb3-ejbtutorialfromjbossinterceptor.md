---
title: EJB Tutorial from JBoss
nav: EJB Tutorial from JBoss
description: * Copyright 2006, Red Hat Middleware LLC, and individual contributors
section: Imported - java2s Archive
order: 1024
source: https://web.archive.org/web/20090202200403/http://www.java2s.com:80/Code/Java/EJB3/EJBTutorialfromJBossInterceptor.htm
---
EJB Tutorial from JBoss: Interceptor

```java title=Example.java
File: AccountsCancelInterceptor.java
/*
 * JBoss, Home of Professional Open Source.
 * Copyright 2006, Red Hat Middleware LLC, and individual contributors
 * as indicated by the @author tags. See the copyright.txt file in the
 * distribution for a full listing of individual contributors.
 *
 * This is free software; you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License as
 * published by the Free Software Foundation; either version 2.1 of
 * the License, or (at your option) any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this software; if not, write to the Free
 * Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
 * 02110-1301 USA, or see the FSF site: http://www.fsf.org.
 */
package org.jboss.tutorial.interceptor.bean;
import javax.interceptor.InvocationContext;
import javax.jms.JMSException;
import javax.jms.Message;
import javax.jms.Queue;
import javax.jms.QueueConnection;
import javax.jms.QueueConnectionFactory;
import javax.jms.QueueSender;
import javax.jms.QueueSession;
import javax.jms.Session;
/**
 *
 * @author <a href="kabir.khan@jboss.com">Kabir Khan</a>
 * @version $Revision: 57207 $
 */
public class AccountsCancelInterceptor extends AccountsInterceptor
{
   QueueConnectionFactory cf;
   Queue queue;
   QueueConnection conn;
   public Object sendCancelMessage(InvocationContext ctx) throws Exception
   {
      QueueSession session = null;
      try
      {
         System.out.println("*** AccountsCancelInterceptor intercepting " + ctx.getMethod().getName());
         System.out.println("*** AccountsConfirmInterceptor - notifying accounts dept");
         session = getConnection().createQueueSession(false, Session.AUTO_ACKNOWLEDGE);
         Message msg = session.createTextMessage("Cancelling order " + ctx.getParameters()[0]);
         QueueSender sender = session.createSender(queue);
         sender.send(msg);
         return ctx.proceed();
      }
      catch(Exception e)
      {
         throw new RuntimeException(e);
      }
      finally
      {
         try{session.close();}catch(Exception e) {}
         System.out.println("*** AccountsCancelInterceptor exiting");
      }
   }
   QueueConnection getConnection() throws JMSException
   {
      if (conn == null)
      {
         synchronized(cf)
         {
            if (conn == null)
            {
               conn = cf.createQueueConnection();
            }
         }
      }
      return conn;
   }
}
File: AccountsConfirmInterceptor.java
/*
 * JBoss, Home of Professional Open Source.
 * Copyright 2006, Red Hat Middleware LLC, and individual contributors
 * as indicated by the @author tags. See the copyright.txt file in the
 * distribution for a full listing of individual contributors.
 *
 * This is free software; you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License as
 * published by the Free Software Foundation; either version 2.1 of
 * the License, or (at your option) any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this software; if not, write to the Free
 * Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
 * 02110-1301 USA, or see the FSF site: http://www.fsf.org.
 */
package org.jboss.tutorial.interceptor.bean;
import java.util.Date;
import javax.annotation.Resource;
import javax.interceptor.AroundInvoke;
import javax.interceptor.InvocationContext;
import javax.jms.JMSException;
import javax.jms.Message;
import javax.jms.Queue;
import javax.jms.QueueConnection;
import javax.jms.QueueConnectionFactory;
import javax.jms.QueueSender;
import javax.jms.QueueSession;
import javax.jms.Session;
import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
/**
 *
 * @author <a href="kabir.khan@jboss.com">Kabir Khan</a>
 * @version $Revision: 57207 $
 */
public class AccountsConfirmInterceptor extends AccountsInterceptor
{
   @Resource(mappedName="java:ConnectionFactory")
   QueueConnectionFactory cf;
   @Resource(mappedName="queue/tutorial/accounts")
   Queue queue;
   @PersistenceContext
   EntityManager em;
   QueueConnection conn;
   public Object intercept(InvocationContext ctx) throws Exception
   {
      //overrides AccountsInterceptor.intercept() so that will not be invoked
      return null;
   }
   @AroundInvoke
   public Object sendConfirmMessage(InvocationContext ctx) throws Exception
   {
      QueueSession session = null;
      try
      {
         System.out.println("*** AccountsConfirmInterceptor intercepting");
         long orderId = (Long)ctx.getParameters()[0];
         if (em.find(Confirmation.class, orderId) == null)
         {
            System.out.println("*** AccountsConfirmInterceptor - recording confirmation");
            Confirmation confirmation = new Confirmation(orderId, new Date());
            em.persist(confirmation);
         }
         else
         {
            System.out.println("*** AccountsConfirmInterceptor - order has already been confirmed aborting");
            return null;
         }
         System.out.println("*** AccountsConfirmInterceptor - notifying accounts dept " + ctx.getMethod().getName());
         session = getConnection().createQueueSession(false, Session.AUTO_ACKNOWLEDGE);
         Message msg = session.createTextMessage("Confirming order " + orderId);
         QueueSender sender = session.createSender(queue);
         sender.send(msg);
         return ctx.proceed();
      }
      catch(Exception e)
      {
         throw new RuntimeException(e);
      }
      finally
      {
         try{session.close();}catch(Exception e) {}
         System.out.println("*** AccountsConfirmInterceptor exiting");
      }
   }
   QueueConnection getConnection() throws JMSException
   {
      if (conn == null)
      {
         synchronized(cf)
         {
            if (conn == null)
            {
               conn = cf.createQueueConnection();
            }
         }
      }
      return conn;
   }
}
File: AccountsInterceptor.java
/*
 * JBoss, Home of Professional Open Source.
 * Copyright 2006, Red Hat Middleware LLC, and individual contributors
 * as indicated by the @author tags. See the copyright.txt file in the
 * distribution for a full listing of individual contributors.
 *
 * This is free software; you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License as
 * published by the Free Software Foundation; either version 2.1 of
 * the License, or (at your option) any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this software; if not, write to the Free
 * Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
 * 02110-1301 USA, or see the FSF site: http://www.fsf.org.
 */
package org.jboss.tutorial.interceptor.bean;
import javax.interceptor.AroundInvoke;
import javax.interceptor.InvocationContext;
/**
 *
 * @author <a href="kabir.khan@jboss.com">Kabir Khan</a>
 * @version $Revision: 57207 $
 */
public class AccountsInterceptor
{
   @AroundInvoke
   public Object intercept(InvocationContext ctx) throws Exception
   {
      System.out.println("*** AccountsInterceptor intercepting " + ctx.getMethod().getName());
      try
      {
         return ctx.proceed();
      }
      finally
      {
         System.out.println("*** AccountsInterceptor exiting");
      }
   }
}
File: AccountsMDB.java
/*
 * JBoss, Home of Professional Open Source.
 * Copyright 2006, Red Hat Middleware LLC, and individual contributors
 * as indicated by the @author tags. See the copyright.txt file in the
 * distribution for a full listing of individual contributors.
 *
 * This is free software; you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License as
 * published by the Free Software Foundation; either version 2.1 of
 * the License, or (at your option) any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this software; if not, write to the Free
 * Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
 * 02110-1301 USA, or see the FSF site: http://www.fsf.org.
 */
package org.jboss.tutorial.interceptor.bean;
import javax.ejb.ActivationConfigProperty;
import javax.ejb.MessageDriven;
import javax.jms.JMSException;
import javax.jms.Message;
import javax.jms.TextMessage;
import javax.jms.MessageListener;
/**
 *
 * @author <a href="kabir.khan@jboss.com">Kabir Khan</a>
 * @version $Revision: 57207 $
 */
@MessageDriven(activationConfig =
{
@ActivationConfigProperty(propertyName="destinationType", propertyValue="javax.jms.Queue"),
@ActivationConfigProperty(propertyName="destination", propertyValue="queue/tutorial/accounts")
})
public class AccountsMDB implements MessageListener
{
   public void onMessage(Message recvMsg)
   {
      try
      {
         System.out.println(
               "\n----------------\n" +
               "AccountsMDB - Got message " + ((TextMessage)recvMsg).getText() + "\n" +
               "----------------");
         //Do necessary bookkeeping
      }
      catch (JMSException e)
      {
         throw new RuntimeException(e);
      }
   }
}
File: Confirmation.java
/*
 * JBoss, Home of Professional Open Source.
 * Copyright 2006, Red Hat Middleware LLC, and individual contributors
 * as indicated by the @author tags. See the copyright.txt file in the
 * distribution for a full listing of individual contributors.
 *
 * This is free software; you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License as
 * published by the Free Software Foundation; either version 2.1 of
 * the License, or (at your option) any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this software; if not, write to the Free
 * Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
 * 02110-1301 USA, or see the FSF site: http://www.fsf.org.
 */
package org.jboss.tutorial.interceptor.bean;
import java.util.Date;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue; import javax.persistence.GenerationType;
import javax.persistence.Id;
/**
 *
 * @author <a href="kabir.khan@jboss.com">Kabir Khan</a>
 * @version $Revision: 57207 $
 */
@Entity
public class Confirmation
{
   long orderId;
   Date date;
   public Confirmation()
   {
   }
   public Confirmation(long orderId, Date date)
   {
      this.orderId = orderId;
      this.date = date;
   }
   @Id
   public long getOrderId()
   {
      return orderId;
   }
   public void setOrderId(long orderId)
   {
      this.orderId = orderId;
   }
   public Date getDate()
   {
      return date;
   }
   public void setDate(Date date)
   {
      this.date = date;
   }
}
File: DefaultInterceptor.java
/*
 * JBoss, Home of Professional Open Source.
 * Copyright 2006, Red Hat Middleware LLC, and individual contributors
 * as indicated by the @author tags. See the copyright.txt file in the
 * distribution for a full listing of individual contributors.
 *
 * This is free software; you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License as
 * published by the Free Software Foundation; either version 2.1 of
 * the License, or (at your option) any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this software; if not, write to the Free
 * Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
 * 02110-1301 USA, or see the FSF site: http://www.fsf.org.
 */
package org.jboss.tutorial.interceptor.bean;
import javax.interceptor.AroundInvoke;
import javax.interceptor.InvocationContext;
/**
 *
 * @author <a href="kabir.khan@jboss.com">Kabir Khan</a>
 * @version $Revision: 57207 $
 */
public class DefaultInterceptor
{
   @AroundInvoke
   public Object intercept(InvocationContext ctx) throws Exception
   {
      System.out.println("*** DefaultInterceptor intercepting " + ctx.getMethod().getName());
      try
      {
         return ctx.proceed();
      }
      finally
      {
         System.out.println("*** DefaultInterceptor exiting");
      }
   }
}
File: EmailMDB.java
/*
 * JBoss, Home of Professional Open Source.
 * Copyright 2006, Red Hat Middleware LLC, and individual contributors
 * as indicated by the @author tags. See the copyright.txt file in the
 * distribution for a full listing of individual contributors.
 *
 * This is free software; you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License as
 * published by the Free Software Foundation; either version 2.1 of
 * the License, or (at your option) any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this software; if not, write to the Free
 * Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
 * 02110-1301 USA, or see the FSF site: http://www.fsf.org.
 */
package org.jboss.tutorial.interceptor.bean;
import javax.interceptor.ExcludeDefaultInterceptors;
import javax.interceptor.InvocationContext;
import javax.ejb.MessageDriven;
import javax.interceptor.AroundInvoke;
import javax.ejb.ActivationConfigProperty;
import javax.jms.Message;
import javax.jms.MessageListener;
@MessageDriven(activationConfig =
        {
        @ActivationConfigProperty(propertyName="destinationType", propertyValue="javax.jms.Queue"),
        @ActivationConfigProperty(propertyName="destination", propertyValue="queue/tutorial/email")
        })
@ExcludeDefaultInterceptors
public class EmailMDB implements MessageListener
{
   public void onMessage(Message recvMsg)
   {
      System.out.println(
            "\n----------------\n" +
            "EMailMDB - Got message, sending email\n" +
            "----------------");
      //Generate and save email
   }
   @AroundInvoke
   public Object mdbInterceptor(InvocationContext ctx) throws Exception
   {
      System.out.println("*** EmailMDB.mdbInterceptor intercepting");
      return ctx.proceed();
   }
}
File: EmailSystem.java
/*
 * JBoss, Home of Professional Open Source.
 * Copyright 2006, Red Hat Middleware LLC, and individual contributors
 * as indicated by the @author tags. See the copyright.txt file in the
 * distribution for a full listing of individual contributors.
 *
 * This is free software; you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License as
 * published by the Free Software Foundation; either version 2.1 of
 * the License, or (at your option) any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this software; if not, write to the Free
 * Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
 * 02110-1301 USA, or see the FSF site: http://www.fsf.org.
 */
package org.jboss.tutorial.interceptor.bean;
public interface EmailSystem
{
   void emailLostPassword(String username);
   void sendBookingConfirmationMessage(long orderId);
   void sendBookingCancellationMessage(long orderId);
   void noop();
   void noop2();
}
File: EmailSystemBean.java
/*
 * JBoss, Home of Professional Open Source.
 * Copyright 2006, Red Hat Middleware LLC, and individual contributors
 * as indicated by the @author tags. See the copyright.txt file in the
 * distribution for a full listing of individual contributors.
 *
 * This is free software; you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License as
 * published by the Free Software Foundation; either version 2.1 of
 * the License, or (at your option) any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this software; if not, write to the Free
 * Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
 * 02110-1301 USA, or see the FSF site: http://www.fsf.org.
 */
package org.jboss.tutorial.interceptor.bean;
import javax.interceptor.AroundInvoke;
import javax.interceptor.ExcludeClassInterceptors;
import javax.interceptor.ExcludeDefaultInterceptors;
import javax.interceptor.Interceptors;
import javax.interceptor.InvocationContext;
import javax.ejb.Stateless;
import javax.ejb.Remote;
import javax.jms.JMSException;
import javax.jms.Queue;
import javax.jms.QueueConnection;
import javax.jms.QueueConnectionFactory;
import javax.jms.QueueSender;
import javax.jms.QueueSession;
import javax.jms.TextMessage;
import javax.naming.InitialContext;
@Stateless
@Interceptors ({TracingInterceptor.class})
@Remote(EmailSystem.class)
public class EmailSystemBean implements EmailSystem
{
   public void emailLostPassword(String username)
   {
      System.out.println("<In EmailSystemBean.emailLostPassword business method");
      //Pretend we are looking up password and email, and place a message on the queue
      String password = "xyz";
      String email = "xyz@lalala.com";
      sendMessage(email, "Password Reminder", "Your password is " + password);
      System.out.println("Exiting EmailSystemBean.emailLostPassword business method>");
   }
   @Interceptors({AccountsConfirmInterceptor.class})
   public void sendBookingConfirmationMessage(long orderId)
   {
      System.out.println("<In EmailSystemBean.sendBookingConfirmationMessage business method");
      //Pretend we are looking email, and place a message on the queue
      String email = "xyz@lalala.com";
      sendMessage(email, "Booking Confirmed!", "Your order " + orderId + "is confirmed!");
      System.out.println("Exiting EmailSystemBean.sendBookingConfirmationMessage business method>");
   }
   public void sendBookingCancellationMessage(long orderId)
   {
      System.out.println("<In EmailSystemBean.sendBookingCancellationMessage business method");
      //Pretend we are looking email, and place a message on the queue
      String email = "xyz@lalala.com";
      sendMessage(email, "Booking Confirmed!", "Your order " + orderId + "is confirmed!");
      System.out.println("Exiting EmailSystemBean.sendBookingCancellationMessage business method>");
   }
   @ExcludeClassInterceptors
   @ExcludeDefaultInterceptors
   public void noop()
   {
      System.out.println("<In EmailSystemBean.noop business method");
      System.out.println("Exiting EmailSystemBean.noop business method>");
   }
   public void noop2()
   {
      System.out.println("<In EmailSystemBean.noop2 business method");
      System.out.println("Exiting EmailSystemBean.noop2 business method>");
   }
   @AroundInvoke
   public Object myBeanInterceptor(InvocationContext ctx) throws Exception
   {
      if (ctx.getMethod().getName().equals("emailLostPassword"))
      {
         System.out.println("*** EmailSystemBean.myBeanInterceptor - username: " + ctx.getParameters()[0]);
      }
      return ctx.proceed();
   }
   private void sendMessage(String email, String subject, String body)
   {
      QueueConnection cnn = null;
      QueueSession session = null;
      try
      {
         QueueSender sender = null;
         InitialContext ctx = new InitialContext();
         Queue queue = (Queue) ctx.lookup("queue/tutorial/email");
         QueueConnectionFactory factory = (QueueConnectionFactory) ctx.lookup("ConnectionFactory");
         cnn = factory.createQueueConnection();
         session = cnn.createQueueSession(false, QueueSession.AUTO_ACKNOWLEDGE);
         TextMessage msg = session.createTextMessage(
               "<mail>" +
               "<to>" + email + "</to>" +
               "<to>" + subject + "</to>" +
               "<msg>" + body +"</msg>" +
               "</mail>");
         sender = session.createSender(queue);
         sender.send(msg);
         System.out.println("Message sent successfully to remote queue.");
      }
      catch(Exception e)
      {
         throw new RuntimeException(e);
      }
      finally
      {
         try
         {
            session.close();
            cnn.close();
         }
         catch (JMSException e)
         {
            throw new RuntimeException(e);
         }
      }
   }
}
File: OtherInterceptor.java
/*
 * JBoss, Home of Professional Open Source.
 * Copyright 2006, Red Hat Middleware LLC, and individual contributors
 * as indicated by the @author tags. See the copyright.txt file in the
 * distribution for a full listing of individual contributors.
 *
 * This is free software; you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License as
 * published by the Free Software Foundation; either version 2.1 of
 * the License, or (at your option) any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this software; if not, write to the Free
 * Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
 * 02110-1301 USA, or see the FSF site: http://www.fsf.org.
 */
package org.jboss.tutorial.interceptor.bean;
import javax.interceptor.AroundInvoke;
import javax.interceptor.InvocationContext;
public class OtherInterceptor
{
   @AroundInvoke
   public Object intercept(InvocationContext ctx) throws Exception
   {
      System.out.println("*** OtherInterceptor intercepting " + ctx.getMethod().getName());
      try
      {
         return ctx.proceed();
      }
      finally
      {
         System.out.println("*** OtherInterceptor exiting");
      }
   }
}
File: TracingInterceptor.java
/*
 * JBoss, Home of Professional Open Source.
 * Copyright 2006, Red Hat Middleware LLC, and individual contributors
 * as indicated by the @author tags. See the copyright.txt file in the
 * distribution for a full listing of individual contributors.
 *
 * This is free software; you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License as
 * published by the Free Software Foundation; either version 2.1 of
 * the License, or (at your option) any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this software; if not, write to the Free
 * Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
 * 02110-1301 USA, or see the FSF site: http://www.fsf.org.
 */
package org.jboss.tutorial.interceptor.bean;
import javax.interceptor.AroundInvoke;
import javax.interceptor.InvocationContext;
public class TracingInterceptor {
   @AroundInvoke
   public Object log(InvocationContext ctx) throws Exception
   {
      System.out.println("*** TracingInterceptor intercepting " + ctx.getMethod().getName());
      long start = System.currentTimeMillis();
      try
      {
         return ctx.proceed();
      }
      catch(Exception e)
      {
         throw e;
      }
      finally
      {
         long time = System.currentTimeMillis() - start;
         String method = ctx.getTarget().getClass().getName() + "." + ctx.getMethod().getName() + "()";
         System.out.println("*** TracingInterceptor invocation of " + method + " took " + time + "ms");
      }
   }
}
File: Client.java
/*
 * JBoss, Home of Professional Open Source.
 * Copyright 2006, Red Hat Middleware LLC, and individual contributors
 * as indicated by the @author tags. See the copyright.txt file in the
 * distribution for a full listing of individual contributors.
 *
 * This is free software; you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License as
 * published by the Free Software Foundation; either version 2.1 of
 * the License, or (at your option) any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this software; if not, write to the Free
 * Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
 * 02110-1301 USA, or see the FSF site: http://www.fsf.org.
 */
package org.jboss.tutorial.interceptor.client;
import org.jboss.tutorial.interceptor.bean.EmailSystem;
import javax.naming.InitialContext;
public class Client
{
   public static void main(String[] args) throws Exception
   {
      System.out.println("Starting");
      InitialContext ctx = new InitialContext();
      EmailSystem emailSystem = (EmailSystem)ctx.lookup("EmailSystemBean/remote");
      System.out.println("\nCalling emailLostPassword");
      emailSystem.emailLostPassword("whatever");
      System.out.println("Waiting 2 seconds");
      Thread.sleep(2000);
      System.out.println("\nCalling sendBookingConfirmationMessage");
      emailSystem.sendBookingConfirmationMessage(100);
      System.out.println("Waiting 2 seconds");
      Thread.sleep(2000);
      System.out.println("\nCalling sendBookingConfirmationMessage");
      emailSystem.sendBookingConfirmationMessage(100);
      System.out.println("Waiting 2 seconds");
      Thread.sleep(2000);
      System.out.println("\nCalling sendBookingCancellationMessage");
      emailSystem.sendBookingCancellationMessage(100);
      System.out.println("Waiting 2 seconds");
      Thread.sleep(2000);
      System.out.println("\nCalling noop");
      emailSystem.noop();
      System.out.println("Waiting 2 seconds");
      Thread.sleep(2000);
      System.out.println("\nCalling noop2");
      emailSystem.noop2();
      System.out.println("Waiting 2 seconds");
      Thread.sleep(2000);
      System.out.println("Done");
   }
}
```

jboss-EJB-3.0_RC9_Patch_1.zip( 10,289 k)
1.  Around InvokeMethod
2.  Get Ejb Info From InvocationContext
3.  Get Set Parameters In InvocationContext
4.  Use Interceptors To Check Permission
5.  EJB Tutorial from JBoss: Callback Listener
6.  Mark Interceptors For A Remote Method
7.  annotation override interceptor
8.  interceptor stateless
