---
title: A Map that stores the values in files within a directory.
nav: A Map that stores the valu...
description: /*********************************************************************
section: Imported - java2s Archive
order: 1056
source: https://web.archive.org/web/20111114172152/http://www.java2s.com:80/Code/Java/Collections-Data-Structure/AMapthatstoresthevaluesinfileswithinadirectory.htm
---
A Map that stores the values in files within a directory.

```java title=Example.java
//     package com.croftsoft.core.util.filemap;
import java.io.BufferedOutputStream;
import java.io.ByteArrayInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.AbstractMap;
import java.util.AbstractSet;
import java.util.Iterator;
import java.util.Set;
/*********************************************************************
 * A Map that stores the values in files within a directory.
 *
 * Uses filenames as the keys and InputStreams as the values.
 *
 * @see FilenameKeyGenerator
 * @see java.util.AbstractMap
 *
 * @version 1999-04-03
 * @author <a href="http://www.CroftSoft.com/">David Wallace Croft</a>
 *********************************************************************/
public class FileMap extends AbstractMap
// ////////////////////////////////////////////////////////////////////
// ////////////////////////////////////////////////////////////////////
{
  private File rootDirectory;
  // ////////////////////////////////////////////////////////////////////
  // ////////////////////////////////////////////////////////////////////
  public static void main(String[] args)
  // ////////////////////////////////////////////////////////////////////
  {
    System.out.println(test());
  }
  public static boolean test()
  // ////////////////////////////////////////////////////////////////////
  {
    try {
      String filename = "com.orbs.util.filemap.FileMap_test.tmp";
      FileMap fileMap = new FileMap(new File("."));
      fileMap.put(filename, new ByteArrayInputStream("Hello".getBytes()));
      InputStream in = (InputStream) fileMap.get(filename);
      int i;
      while ((i = in.read()) > -1)
        System.out.write(i);
      in.close();
      System.out.println("");
      fileMap.remove(filename);
    } catch (Exception ex) {
      ex.printStackTrace();
      return false;
    }
    return true;
  }
  // ////////////////////////////////////////////////////////////////////
  // ////////////////////////////////////////////////////////////////////
  public FileMap(File rootDirectory)
  // ////////////////////////////////////////////////////////////////////
  {
    this.rootDirectory = rootDirectory;
  }
  // ////////////////////////////////////////////////////////////////////
  // ////////////////////////////////////////////////////////////////////
  public Set entrySet()
  // ////////////////////////////////////////////////////////////////////
  {
    return new FileMapEntrySet(rootDirectory);
  }
  // synchronize?
  public synchronized Object put(Object key, Object value)
  // ////////////////////////////////////////////////////////////////////
  {
    File file = null;
    BufferedOutputStream out = null;
    InputStream in = null;
    try {
      String filename = (String) key;
      file = new File(rootDirectory, filename);
      out = new BufferedOutputStream(new FileOutputStream(file));
      in = (InputStream) value;
      int i;
      while ((i = in.read()) > -1)
        out.write(i);
    } catch (IOException ioex) {
      try {
        out.close();
      } catch (Exception ex) {
      }
      try {
        file.delete();
      } catch (Exception ex) {
      }
      throw new RuntimeException(ioex.getMessage());
    } finally {
      try {
        in.close();
      } catch (Exception ex) {
      }
      try {
        out.close();
      } catch (Exception ex) {
      }
    }
    return null;
  }
  public synchronized Object remove(Object key)
  // ////////////////////////////////////////////////////////////////////
  {
    String filename = (String) key;
    File file = new File(rootDirectory, filename);
    file.delete();
    return null;
  }
  // ////////////////////////////////////////////////////////////////////
  // ////////////////////////////////////////////////////////////////////
}
/*********************************************************************
 * This Set is required for the AbstractMap implementation of FileMap.
 *
 * @see FileMap
 * @see java.util.AbstractSet
 *
 * @version 1999-04-03
 * @author <a href="http://www.CroftSoft.com/">David Wallace Croft</a>
 *********************************************************************/
class FileMapEntrySet extends AbstractSet
// ////////////////////////////////////////////////////////////////////
// ////////////////////////////////////////////////////////////////////
{
  private File rootDirectory;
  // ////////////////////////////////////////////////////////////////////
  // ////////////////////////////////////////////////////////////////////
  public FileMapEntrySet(File rootDirectory)
  // ////////////////////////////////////////////////////////////////////
  {
    this.rootDirectory = rootDirectory;
  }
  // ////////////////////////////////////////////////////////////////////
  // ////////////////////////////////////////////////////////////////////
  public Iterator iterator()
  // ////////////////////////////////////////////////////////////////////
  {
    return new FileMapEntryIterator(rootDirectory);
  }
  public int size()
  // ////////////////////////////////////////////////////////////////////
  {
    String[] files = rootDirectory.list();
    if (files == null)
      return 0;
    return files.length;
  }
  // ////////////////////////////////////////////////////////////////////
  // ////////////////////////////////////////////////////////////////////
}
/*********************************************************************
 * This Iterator is required for the AbstractMap implementation of FileMap.
 *
 * @see FileMap
 * @see java.util.AbstractSet
 *
 * @version 1999-04-03
 * @author <a href="http://www.CroftSoft.com/">David Wallace Croft</a>
 *********************************************************************/
class FileMapEntryIterator implements Iterator
// ////////////////////////////////////////////////////////////////////
// ////////////////////////////////////////////////////////////////////
{
  private File rootDirectory;
  private String[] files;
  private int index = 0;
  // ////////////////////////////////////////////////////////////////////
  // ////////////////////////////////////////////////////////////////////
  public FileMapEntryIterator(File rootDirectory)
  // ////////////////////////////////////////////////////////////////////
  {
    this.rootDirectory = rootDirectory;
  }
  // ////////////////////////////////////////////////////////////////////
  // ////////////////////////////////////////////////////////////////////
  public synchronized boolean hasNext()
  // ////////////////////////////////////////////////////////////////////
  {
    if (files == null)
      files = rootDirectory.list();
    if (files == null)
      return false;
    return (index < files.length);
  }
  public synchronized Object next()
  // ////////////////////////////////////////////////////////////////////
  {
    if (files == null)
      files = rootDirectory.list();
    if (files == null)
      return null;
    if (index >= files.length)
      return null;
    return new FileMapEntry(rootDirectory, files[index++]);
  }
  public synchronized void remove()
  // ////////////////////////////////////////////////////////////////////
  {
    if (files == null)
      files = rootDirectory.list();
    if (files == null)
      return;
    if (index >= files.length)
      return;
    new File(files[index]).delete();
  }
  // ////////////////////////////////////////////////////////////////////
  // ////////////////////////////////////////////////////////////////////
}
/*********************************************************************
 * This Map.Entry is required for the AbstractMap implementation of FileMap.
 *
 * @see FileMapEntryIterator
 * @see FileMapEntrySet
 * @see java.util.Map.Entry
 *
 * @version 1999-04-03
 * @author <a href="http://www.CroftSoft.com/">David Wallace Croft</a>
 *********************************************************************/
class FileMapEntry implements Map.Entry
// ////////////////////////////////////////////////////////////////////
// ////////////////////////////////////////////////////////////////////
{
  private File rootDirectory;
  private String filename;
  // ////////////////////////////////////////////////////////////////////
  // ////////////////////////////////////////////////////////////////////
  public FileMapEntry(File rootDirectory, String filename)
  // ////////////////////////////////////////////////////////////////////
  {
    this.rootDirectory = rootDirectory;
    this.filename = filename;
  }
  // ////////////////////////////////////////////////////////////////////
  // ////////////////////////////////////////////////////////////////////
  public boolean equals(Object o)
  // ////////////////////////////////////////////////////////////////////
  {
    if (o == null)
      return false;
    if (!o.getClass().equals(this.getClass()))
      return false;
    FileMapEntry other = (FileMapEntry) o;
    if (!filename.equals(other.filename))
      return false;
    if (!rootDirectory.equals(other.rootDirectory))
      return false;
    if (hashCode() != other.hashCode())
      return false;
    return true;
  }
  public Object getKey()
  // ////////////////////////////////////////////////////////////////////
  {
    return filename;
  }
  public Object getValue()
  // ////////////////////////////////////////////////////////////////////
  {
    try {
      return new FileInputStream(new File(rootDirectory, filename));
    } catch (FileNotFoundException ex) {
      return null;
    }
  }
  public int hashCode()
  // ////////////////////////////////////////////////////////////////////
  {
    return filename.hashCode();
  }
  public Object setValue(Object value)
  // ////////////////////////////////////////////////////////////////////
  {
    throw new UnsupportedOperationException();
  }
  // ////////////////////////////////////////////////////////////////////
  // ////////////////////////////////////////////////////////////////////
}
```

1.  Creating and storing arrays in a map
---  ---
2.  Sort based on the values
3.  Get a key from value with an HashMap
4.  Retrieve environment variables (JDK1.5)
5.  Creating a Type-Specific Map: creates a map whose keys are Integer objects and values are String objects.
6.  A map declared to hold objects of a type T can also hold objects that extend from T
7.  A value retrieved from a type-specific collection does not need to be casted
8.  Map techniques.
9.  Create an array containing the keys in a map
10.  Create an array containing the values in a map
11.  Creating a Hash Table
12.  Creating a Map That Retains Order-of-Insertion
13.  Automatically Removing an Unreferenced Element from a Hash Table
14.  Creating a Type-Specific Map [5.0]
15.  Use Iterator to loop through the HashMap class
16.  Create type specific collections
17.  Convert Properties into Map
18.  A java.util.Map implementation using reference values
19.  Utility method that return a String representation of a map. The elements will be represented as "key = value"
20.  Utility method that return a String representation of a map. The elements will be represented as "key = value" (tab)
21.  This program demonstrates the use of a map with key type String and value type Employee
22.  Format a Map
23.  A Map implementation that dumps its content when memory runs low.
24.  Map List
25.  Multi Value Map Array List
26.  Multi Value Map Linked HashSet
27.  An object that maps keys to values, and values back to keys.
28.  LRU Map
29.  A map acts like array.
30.  Order Retaining Map
31.  BinaryMap class implements a map from objects to integer objects where the only value is the integer with value 1.
32.  A space-optimized map for associating char keys with values.
33.  A Map implementation that grows to a fixed size and then retains only a fixed number of the highest (largest) keys.
34.  Class which creates mapping between keys and a list of values.
35.  A map of values by class.
36.  History Map
37.  Sorts map by values in ascending order.
38.  Map from a given key to a list of values
39.  Map from a given key to a set of values
40.  Class which keeps a set of values and assigns each value a unique positive index.
41.  Array Map
42.  Array map
43.  An ArrayMap is a very inefficient map type that is more robust in dealing with changes to its keys than other maps.
44.  This Map stores it's keys as strings in upper case, null and duplicate keys are not allowed
45.  Map to string
46.  A simple class that stores key Strings as char[]'s in a hash table.
