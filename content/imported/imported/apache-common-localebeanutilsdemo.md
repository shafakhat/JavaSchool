---
title: Locale Bean Utils Demo
nav: Locale Bean Utils Demo
description: LocaleBeanUtils.getProperty(movie, "dateOfRelease", "dd-MMM-yyyy"));
section: Imported - java2s Archive
order: 1047
source: https://web.archive.org/web/20080908044842/http://www.java2s.com/Code/Java/Apache-Common/LocaleBeanUtilsDemo.htm
---
```java title=Example.java
import org.apache.commons.beanutils.locale.LocaleBeanUtils;
import java.util.Date;
import java.util.GregorianCalendar;
public class BeanUtilsExampleV5 {
  public static void main(String args[]) throws Exception {
    BeanUtilsExampleV5 diff = new BeanUtilsExampleV5();
    Movie movie = diff.prepareData();
    System.err.println(
      LocaleBeanUtils.getProperty(movie, "dateOfRelease", "dd-MMM-yyyy"));
  }
  private Movie prepareData() {
    Movie movie = new Movie();
    movie.setTitle("The Italian Job");
    movie.setDateOfRelease(new GregorianCalendar(2000, 0, 1).getTime());
    return movie;
  }
}
-------------------------------------------------------------------------
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
-------------------------------------------------------------------------
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
-------------------------------------------------------------------------
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

BeanUtilsExampleV5.zip( 881 k)
