---
title: Demo for java.util.concurrent.Future
nav: Demo for java.util.concurr...
description: This program is a part of the companion code for Core Java 8th ed.
section: Imported - java2s Archive
order: 1046
source: https://web.archive.org/web/20111125081728/http://java2s.com/Code/Java/Threads/DemoforjavautilconcurrentFuture.htm
---
Demo for java.util.concurrent.Future

```java title=Example.java
/*
   This program is a part of the companion code for Core Java 8th ed.
   (http://horstmann.com/corejava)
   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.Future;
import java.util.concurrent.FutureTask;
/**
 * @version 1.0 2004-08-01
 * @author Cay Horstmann
 */
public class FutureTest
{
   public static void main(String[] args)
   {
      Scanner in = new Scanner(System.in);
      System.out.print("Enter base directory (e.g. /usr/local/jdk5.0/src): ");
      String directory = in.nextLine();
      System.out.print("Enter keyword (e.g. volatile): ");
      String keyword = in.nextLine();
      MatchCounter counter = new MatchCounter(new File(directory), keyword);
      FutureTask<Integer> task = new FutureTask<Integer>(counter);
      Thread t = new Thread(task);
      t.start();
      try
      {
         System.out.println(task.get() + " matching files.");
      }
      catch (ExecutionException e)
      {
         e.printStackTrace();
      }
      catch (InterruptedException e)
      {
      }
   }
}
/**
 * This task counts the files in a directory and its subdirectories that contain a given keyword.
 */
class MatchCounter implements Callable<Integer>
{
   /**
    * Constructs a MatchCounter.
    * @param directory the directory in which to start the search
    * @param keyword the keyword to look for
    */
   public MatchCounter(File directory, String keyword)
   {
      this.directory = directory;
      this.keyword = keyword;
   }
   public Integer call()
   {
      count = 0;
      try
      {
         File[] files = directory.listFiles();
         ArrayList<Future<Integer>> results = new ArrayList<Future<Integer>>();
         for (File file : files)
            if (file.isDirectory())
            {
               MatchCounter counter = new MatchCounter(file, keyword);
               FutureTask<Integer> task = new FutureTask<Integer>(counter);
               results.add(task);
               Thread t = new Thread(task);
               t.start();
            }
            else
            {
               if (search(file)) count++;
            }
         for (Future<Integer> result : results)
            try
            {
               count += result.get();
            }
            catch (ExecutionException e)
            {
               e.printStackTrace();
            }
      }
      catch (InterruptedException e)
      {
      }
      return count;
   }
   /**
    * Searches a file for a given keyword.
    * @param file the file to search
    * @return true if the keyword is contained in the file
    */
   public boolean search(File file)
   {
      try
      {
         Scanner in = new Scanner(new FileInputStream(file));
         boolean found = false;
         while (!found && in.hasNextLine())
         {
            String line = in.nextLine();
            if (line.contains(keyword)) found = true;
         }
         in.close();
         return found;
      }
      catch (IOException e)
      {
         return false;
      }
   }
   private File directory;
   private String keyword;
   private int count;
}
```

1.  Using java.util.concurrent.locks.Lock to control the synchronized resource
---  ---
2.  This program shows how multiple threads can safely access a data structure
3.  java.util.concurrent.ThreadPoolExecutor and thread pool
4.  Single Thread Request Executor
