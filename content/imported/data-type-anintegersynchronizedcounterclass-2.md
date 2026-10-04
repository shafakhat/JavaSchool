---
title: An integer synchronized counter class.
nav: An integer synchronized co...
description: * Copyright 2005, JBoss Inc., and individual contributors as indicated
section: Imported - java2s Archive
order: 1002
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Anintegersynchronizedcounterclass.htm
---
```java title=Example.java
/*
  * JBoss, Home of Professional Open Source
  * Copyright 2005, JBoss Inc., and individual contributors as indicated
  * by the @authors tag. See the copyright.txt in the distribution for a
  * full listing of individual contributors.
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
  */package org.jboss.util;
import java.io.Serializable;
/**
 * An integer counter class.
 *
 * @version <tt>$Revision: 2800 $</tt>
 * @author  <a href="mailto:jason@planet57.com">Jason Dillon</a>
 */publicclass Counter
   implements Serializable, Cloneable
{
   /** The serialVersionUID */privatestaticfinallong serialVersionUID = 7736259185393081556L;
   /** The current count */privateint count;
   /**
    * Construct a Counter with a starting value.
    *
    * @param count   Starting value for counter.
    */public Counter(finalint count) {
      this.count = count;
   }
   /**
    * Construct a Counter.
    */public Counter() {}
   /**
    * Increment the counter. (Optional operation)
    *
    * @return  The incremented value of the counter.
    */publicint increment() {
      return ++count;
   }
   /**
    * Decrement the counter. (Optional operation)
    *
    * @return  The decremented value of the counter.
    */publicint decrement() {
      return --count;
   }
   /**
    * Return the current value of the counter.
    *
    * @return  The current value of the counter.
    */publicint getCount() {
      return count;
   }
   /**
    * Reset the counter to zero. (Optional operation)
    */publicvoid reset() {
      this.count = 0;
   }
   /**
    * Check if the given object is equal to this.
    *
    * @param obj  Object to test equality with.
    * @return     True if object is equal to this.
    */publicboolean equals(final Object obj) {
      if (obj == this) return true;
      if (obj != null && obj.getClass() == getClass()) {
         return ((Counter)obj).count == count;
      }
      return false;
   }
   /**
    * Return a string representation of this.
    *
    * @return  A string representation of this.
    */public String toString() {
      return String.valueOf(count);
   }
   /**
    * Return a cloned copy of this object.
    *
    * @return  A cloned copy of this object.
    */public Object clone() {
      try {
         return super.clone();
      }
      catch (CloneNotSupportedException e) {
         thrownew InternalError();
      }
   }
   /////////////////////////////////////////////////////////////////////////
//                                Wrappers                             //
/////////////////////////////////////////////////////////////////////////
/**
    * Base wrapper class for other wrappers.
    */privatestaticclass Wrapper
      extends Counter
   {
      /** The serialVersionUID */privatestaticfinallong serialVersionUID = -1803971437884946242L;
      /** The wrapped counter */protectedfinal Counter counter;
      public Wrapper(final Counter counter) {
         this.counter = counter;
      }
      publicint increment() {
         return counter.increment();
      }
      publicint decrement() {
         return counter.decrement();
      }
      publicint getCount() {
         return counter.getCount();
      }
      publicvoid reset() {
         counter.reset();
      }
      publicboolean equals(final Object obj) {
         return counter.equals(obj);
      }
      public String toString() {
         return counter.toString();
      }
      public Object clone() {
         return counter.clone();
      }
   }
   /**
    * Return a synchronized counter.
    *
    * @param counter    Counter to synchronize.
    * @return           Synchronized counter.
    */publicstatic Counter makeSynchronized(final Counter counter) {
      returnnew Wrapper(counter) {
            /** The serialVersionUID */privatestaticfinallong serialVersionUID = -6024309396861726945L;
            publicsynchronizedint increment() {
               return this.counter.increment();
            }
            publicsynchronizedint decrement() {
               return this.counter.decrement();
            }
            publicsynchronizedint getCount() {
               return this.counter.getCount();
            }
            publicsynchronizedvoid reset() {
               this.counter.reset();
            }
            publicsynchronizedint hashCode() {
               return this.counter.hashCode();
            }
            publicsynchronizedboolean equals(final Object obj) {
               return this.counter.equals(obj);
            }
            publicsynchronized String toString() {
               return this.counter.toString();
            }
            publicsynchronized Object clone() {
               return this.counter.clone();
            }
         };
   }
   /**
    * Returns a directional counter.
    *
    * @param counter       Counter to make directional.
    * @param increasing    True to create an increasing only
    *                      or false to create a decreasing only.
    * @return              A directional counter.
    */publicstatic Counter makeDirectional(final Counter counter,
                                         finalboolean increasing)
   {
      Counter temp;
      if (increasing) {
         temp = new Wrapper(counter) {
               /** The serialVersionUID */privatestaticfinallong serialVersionUID = 2161377898611431781L;
               publicint decrement() {
                  thrownew UnsupportedOperationException();
               }
               publicvoid reset() {
                  thrownew UnsupportedOperationException();
               }
            };
      }
      else {
         temp = new Wrapper(counter) {
            /** The serialVersionUID */privatestaticfinallong serialVersionUID = -4683457706354663230L;
               publicint increment() {
                  thrownew UnsupportedOperationException();
               }
            };
      }
      return temp;
   }
}
```
