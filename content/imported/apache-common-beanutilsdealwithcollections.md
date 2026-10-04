---
title: Bean Utils
nav: Bean Utils
description: public Date getDateOfRelease() { return this.dateOfRelease; }
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/20070119101737/http://www.java2s.com:80/Code/Java/Apache-Common/BeanUtilsdealwithcollections.htm
---
Bean Utils: deal with collections

```java title=Example.java
import org.apache.commons.beanutils.BeanUtils;
import java.util.Map;
import java.util.Date;
import java.util.List;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.GregorianCalendar;
public class BeanUtilsExampleV3 {
  public static void main(String args[]) throws Exception {
    BeanUtilsExampleV3 diff = new BeanUtilsExampleV3();
    Actor actor = diff.prepareData();
    Map describedData = BeanUtils.describe(actor);
    // check the map
    System.err.println(describedData.get("name"));
    // change this value
    describedData.put("name", "Robert Redford");
    // create a new Actor Bean
    Actor newActor = new Actor();
    BeanUtils.populate(newActor, describedData);
    System.err.println(BeanUtils.getProperty(newActor, "name"));
  }
  private Actor prepareData() {
    Actor actor = new Actor();
    actor.setName("Michael Caine");
    actor.setGender(1);
    actor.setWorth(10000000);
    return actor;
  }
}
----------------------------------------------------------------------------
import java.util.Map;
import java.util.List;
import java.util.Date;
public class Movie {
  public Movie() {
  }
  public Date getDateOfRelease() { return this.dateOfRelease; }
  public void setDateOfRelease(Date dateOfRelease) {
    this.dateOfRelease = dateOfRelease;
  }
  public String getTitle() { return this.title; }
  public void setTitle(String title) {this.title = title; }
  public Person getDirector() { return this.director; }
  public void setDirector(Person director) { this.director = director; }
  public List getActors() { return this.actors; }
  public void setActors(List actors) { this.actors= actors; }
  public String[] getKeywords() { return this.keywords; }
  public void setKeyWords(String[] keywords) { this.keywords = keywords; }
  public Map getGenre() { return this.genre; }
  public void setGenre(Map genre) { this.genre = genre; }
  private Date dateOfRelease;
  private String title;
  private Person director;
  private List actors;
  private String[] keywords;
  private Map genre;
}
----------------------------------------------------------------------------
import java.util.Map;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;
public class Person {
  public Person() {
  }
  public String getName() {
    return this.name == null ? "NoName" : this.name; }
  public void setName(String name) { this.name = name; }
  public int getGender() { return this.gender; }
  public void setGender(int gender) {  // 0 - Indeterminate, 1 - Male, 2 - Female
    this.gender = (gender > 2 || gender < 0) ? 0 : gender; }
  public Map getContactNumber() { return this.contactNumber; }
  public void setContactNumber(Map contactNumber) {
    this.contactNumber = contactNumber;
  }
  /**public boolean equals(Object o) {
    if(o == this) return true;
    if(!(o instanceof Person)) return false;
    Person otherPerson = (Person)o;
    if(otherPerson.getName().equals(this.name) &&
       otherPerson.getGender() == this.gender) return true;
    return false;
  }*/
  public boolean equals(Object o) {
    if(!(o instanceof Person)) return false;
    Person otherPerson = (Person)o;
    return new EqualsBuilder()
               .append(name, otherPerson.getName())
               .append(gender, otherPerson.getGender())
               .isEquals();
  }
  public int hashCode() {
    return new HashCodeBuilder(7, 51)
               .append(name)
               .append(gender)
               .append(contactNumber)
               .toHashCode();
  }
  public String toString() {
    return new ToStringBuilder(this)
               .append("Name", name)
               .append("Gender", gender)
               .append("Contact Details", contactNumber)
               .toString();
  }
  private String name;
  private int gender;
  private Map contactNumber;
}
----------------------------------------------------------------------------
import java.util.List;
public class Actor extends Person {
  public Actor() {
  }
  public List getMovieCredits() { return this.movieCredits; }
  public void setMovieCredits(List movieCredits) {
    this.movieCredits = movieCredits;
  }
  public long getWorth() { return this.worth; }
  public void setWorth(long worth) { this.worth = worth; }
  private List movieCredits;
  private long worth;
}
```

Download: BeanUtilsExampleV3.zip ( 879 K )
Related examples in the same category
