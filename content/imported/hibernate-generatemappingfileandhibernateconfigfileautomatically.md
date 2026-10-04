---
title: Generate Mapping File And Hibernate Config File Automatically
nav: Generate Mapping File And ...
description: Generate Mapping File And Hibernate Config File Automatically
section: Imported - java2s Archive
order: 1002
source: https://web.archive.org/web/20061018180654/http://www.java2s.com/Code/Java/Hibernate/GenerateMappingFileAndHibernateConfigFileAutomatically.htm
---
```java title=Example.java
/////////////////////////////////////////////////////////////////////////
import java.io.Serializable;
/**
 * An Address component, it's not have its own identity.
 *
 */
public class Address implements Serializable {
    private String streetAddress;
    private String city;
    private String state;
    private String zipCode;
    /**
     * @hibernate.property
     * @hibernate.column name="street_address"
     * @return
     */
    public String getStreetAddress() { return streetAddress; }
    public void setStreetAddress(String streetAddress) { this.streetAddress = streetAddress;}
    /**
     * @hibernate.property
     * @hibernate.column name="city"
     * @return
     */
    public String getCity() { return city; }
    public void setCity(String city) { this.city = city; }
    /**
     * @hibernate.property
     * @hibernate.column name="state"
     * @return
     */
    public String getState() { return state; }
    public void setState(String state) { this.state = state; }
    /**
     * @hibernate.property
     * @hibernate.column name="zip_code"
     * @return
     */
    public String getZipCode() { return zipCode; }
    public void setZipCode(String zipCode) { this.zipCode = zipCode;    }
}
/////////////////////////////////////////////////////////////////////////
import java.io.Serializable;
import java.util.Date;
import java.util.Set;
import java.util.LinkedHashSet;
/**
 * A persistant Hibernate object.
 *
 * @hibernate.class table="events"
 */
public class Event implements Serializable {
    private Long id;
    private int duration;
    private String name;
    private Date startDate;
    private Location location;
    private Set speakers = new LinkedHashSet();
    /**
     * @hibernate.id generator-class="native" column="uid"
     * @return
     */
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    /**
     * @hibernate.property column="name"
     * @return
     */
    public String getName() { return name; }
    public void setName(String name) { this.name = name;   }
    /**
     * @hibernate.property column="start_date"
     * @return
     */
    public Date getStartDate() { return startDate; }
    public void setStartDate(Date startDate) { this.startDate = startDate; }
    /**
     * @hibernate.property column="duration"
     * @return
     */
    public int getDuration() { return duration; }
    public void setDuration(int duration) { this.duration = duration; }
    /**
     * @hibernate.many-to-one column="location_id" cascade="save-update"
     * @return
     */
    public Location getLocation() { return location; }
    public void setLocation(Location location) { this.location = location; }
    /**
     * @hibernate.set cascade="save-update"
     * @hibernate.collection-key column="event_id"
     * @hibernate.collection-one-to-many class="Speaker"
     * @return
     */
    public Set getSpeakers() { return speakers; }
    public void setSpeakers(Set speakers) { this.speakers = speakers; }
}
/////////////////////////////////////////////////////////////////////////
<component
        name="address"
        class="Address"
    >
    <property
        name="streetAddress"
        type="java.lang.String"
        update="true"
        insert="true"
        access="property"
        column="street_address"
    />
    <property
        name="city"
        type="java.lang.String"
        update="true"
        insert="true"
        access="property"
        column="city"
    />
    <property
        name="state"
        type="java.lang.String"
        update="true"
        insert="true"
        access="property"
        column="state"
    />
    <property
        name="zipCode"
        type="java.lang.String"
        update="true"
        insert="true"
        access="property"
        column="zip_code"
    />
    </component>
/////////////////////////////////////////////////////////////////////////
import java.io.Serializable;
/**
 * @hibernate.class table="locations"
 */
public class Location implements Serializable{
    private Long id;
    private String name;
    private Address address = new Address();
    /**
     * @hibernate.id generator-class="native" column="uid"
     * @return
     */
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    /**
     * @hibernate.component
     * @return
     */
    public Address getAddress() { return address; }
    public void setAddress(Address address) { this.address = address;}
}
/////////////////////////////////////////////////////////////////////////
<project name="hibernate-tutorial" default="compile">
    <property name="sourcedir" value="${basedir}/src"/>
    <property name="targetdir" value="${basedir}/build"/>
    <property name="librarydir" value="${basedir}/lib"/>
    <path id="libraries">
        <fileset dir="${librarydir}">
            <include name="*.jar"/>
        </fileset>
    </path>
    <target name="clean">
        <delete dir="${targetdir}"/>
        <mkdir dir="${targetdir}"/>
    </target>
    <target name="compile" depends="clean, copy-resources">
      <javac srcdir="${sourcedir}"
             destdir="${targetdir}"
             classpathref="libraries"
             debug="on"/>
    </target>
    <target name="copy-resources">
        <copy todir="${targetdir}">
            <fileset dir="${sourcedir}">
                <exclude name="**/*.java"/>
            </fileset>
        </copy>
    </target>
    <target name="run" depends="compile">
    <java classname="Main" fork="true" classpathref="libraries">
        <classpath path="${targetdir}"/>
        <arg value="${action}"/>
    </java>
   </target>
    <target name="hbm" depends="compile">
        <taskdef
            name="hibernatedoclet"
            classname="xdoclet.modules.hibernate.HibernateDocletTask"
            classpathref="libraries"
            />
        <hibernatedoclet
            destdir="${targetdir}"
            verbose="true">
            <fileset dir="${sourcedir}">
                <include name="**/*.java"/>
            </fileset>
            <hibernate version="3.0"/>
            <hibernatecfg
                dialect="${hibernate.dialect}"
                jdbcUrl="${hibernate.connection.url}"
                driver="${hibernate.connection.driver_class}"
                userName="${hibernate.connection.username}"
                password="${hibernate.connection.password}"
                showSql="false"
                version="3.0"
                />
        </hibernatedoclet>
    </target>
</project>
/////////////////////////////////////////////////////////////////////////
```

Download: HibernateGenerateMappingFileAndHibernateConfigFileAutomatically.zip ( 5,040 K )
Related examples in the same category
