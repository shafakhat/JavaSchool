---
title: Your own auto-growth Array
nav: Your own auto-growth Array
description: * Copyright (c) 1999-2003 The Apache Software Foundation. All rights
section: Imported - java2s Archive
order: 2386
source: https://web.archive.org/web/20140216115613/http://www.java2s.com/Tutorial/Java/0140__Collections/YourownautogrowthArray.htm
---
```java title=Example.java
/*
 *
 * The Apache Software License, Version 1.1
 *
 * Copyright (c) 1999-2003 The Apache Software Foundation.  All rights
 * reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 *
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 *
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in
 *    the documentation and/or other materials provided with the
 *    distribution.
 *
 * 3. The end-user documentation included with the redistribution, if
 *    any, must include the following acknowlegement:
 *       "This product includes software developed by the
 *        Apache Software Foundation (http://www.apache.org/)."
 *    Alternately, this acknowlegement may appear in the software itself,
 *    if and wherever such third-party acknowlegements normally appear.
 *
 * 4. The names "The Jakarta Project", "Jakarta Element Construction Set",
 *    "Jakarta ECS" , and "Apache Software Foundation" must not be used
 *    to endorse or promote products derived
 *    from this software without prior written permission. For written
 *    permission, please contact apache@apache.org.
 *
 * 5. Products derived from this software may not be called "Apache",
 *    "Jakarta Element Construction Set" nor "Jakarta ECS" nor may "Apache"
 *    appear in their names without prior written permission of the Apache Group.
 *
 * THIS SOFTWARE IS PROVIDED ``AS IS'' AND ANY EXPRESSED OR IMPLIED
 * WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
 * OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 * DISCLAIMED.  IN NO EVENT SHALL THE APACHE SOFTWARE FOUNDATION OR
 * ITS CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
 * SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
 * LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF
 * USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
 * ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
 * OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
 * OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
 * SUCH DAMAGE.
 *
 */
public class Array implements java.util.Enumeration,java.io.Serializable
{
    private int current = 0;
    private int size = 10;
    private int grow = 2;
    private int place = 0;
    private Object[] elements = null;
    private Object[] tmpElements = null;
    public Array()
    {
        init();
    }
    public Array(int size)
    {
        setSize(size);
        init();
    }
    public Array(int size,int grow)
    {
        setSize(size);
        setGrow(grow);
        init();
    }
    private void init()
    {
        elements = new Object[size];
    }
    public Object nextElement() throws java.util.NoSuchElementException
    {
        if ( elements[place] != null && place != current)
        {
            place++;
            return elements[place - 1];
        }
        else
        {
            place = 0;
            throw new java.util.NoSuchElementException();
        }
    }
    public boolean hasMoreElements()
    {
        if( place < elements.length && current != place )
            return true;
        return false;
    }
    public void setSize(int size)
    {
        this.size = size;
    }
    public int getCurrentSize()
    {
        return current;
    }
    public void rehash()
    {
        tmpElements = new Object[size];
        int count = 0;
        for ( int x = 0; x < elements.length; x++ )
        {
            if( elements[x] != null )
            {
                tmpElements[count] = elements[x];
                count++;
            }
        }
        elements = (Object[])tmpElements.clone();
        tmpElements = null;
        current = count;
    }
    public void setGrow(int grow)
    {
        this.grow = grow;
    }
    public void grow()
    {
        size = size+=(size/grow);
        rehash();
    }
    public void add(Object o)
    {
        if( current == elements.length )
            grow();
        try
        {
            elements[current] = o;
            current++;
        }
        catch(java.lang.ArrayStoreException ase)
        {
        }
    }
    public void add(int location,Object o)
    {
        try
        {
            elements[location] = o;
        }
        catch(java.lang.ArrayStoreException ase)
        {
        }
    }
    public void remove(int location)
    {
        elements[location] = null;
    }
    public int location(Object o) throws NoSuchObjectException
    {
        int loc = -1;
        for ( int x = 0; x < elements.length; x++ )
        {
            if((elements[x] != null && elements[x] == o )||
               (elements[x] != null && elements[x].equals(o)))
            {
                loc = x;
                break;
            }
        }
        if( loc == -1 )
            throw new NoSuchObjectException();
        return(loc);
    }
    public Object get(int location)
    {
        return elements[location];
    }
    public java.util.Enumeration elements()
    {
        return this;
    }
}
class NoSuchObjectException extends Exception
{
    public NoSuchObjectException()
    {
        super("No such object found.");
    }
}
```

| 9.10.1. | A variable length Double Array: expanding and contracting its internal storage array as elements are added and removed. |
|---|---|
| 9.10.2. | Simple object pool. Based on ThreadPool and few other classes |
| 9.10.3. | Your own auto-growth Array |
| 9.10.4. | The character array based string |
| 9.10.5. | ByteArray wraps java byte arrays (byte[]) to allow byte arrays to be used as keys in hashtables. |
| 9.10.6. | Adds all the elements of the given arrays into a new double-type array. |
| 9.10.7. | A writer for char strings |
| 9.10.8. | Array-List for integer objects. |
| 9.10.9. | Simple object pool |
| 9.10.10. | Concatenates two arrays of strings |
| 9.10.11. | Puts the entire source array in the target array at offset offset. |
| 9.10.12. | Lazy List creation |
| 9.10.13. | Stores a list of int |
