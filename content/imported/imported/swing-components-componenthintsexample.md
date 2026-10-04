---
title: Component Hints Example
nav: Component Hints Example
description: Component Hints Example : Java examples (example source code) » Swing Components » Data Validation
section: Imported - java2s Archive
order: 1048
source: https://web.archive.org/web/20060506060108/http://www.java2s.com:80/Code/Java/Swing-Components/ComponentHintsExample.htm
---
Component Hints Example : Java examples (example source code) » Swing Components » Data Validation

```java title=Example.java
/*
Code revised from Desktop Java Live:
http://www.sourcebeat.com/downloads/
*/
import java.beans.PropertyChangeEvent;
import java.beans.PropertyChangeListener;
import javax.swing.JComponent;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JTextField;
import com.jgoodies.binding.PresentationModel;
import com.jgoodies.binding.adapter.BasicComponentFactory;
import com.jgoodies.binding.value.ValueModel;
import com.jgoodies.forms.builder.DefaultFormBuilder;
import com.jgoodies.forms.builder.PanelBuilder;
import com.jgoodies.forms.layout.FormLayout;
import com.jgoodies.validation.ValidationCapable;
import com.jgoodies.validation.ValidationResult;
import com.jgoodies.validation.util.DefaultValidationResultModel;
import com.jgoodies.validation.util.PropertyValidationSupport;
import com.jgoodies.validation.util.ValidationResultModel;
import com.jgoodies.validation.util.ValidationUtils;
import com.jgoodies.validation.view.ValidationComponentUtils;
import com.jgoodies.validation.view.ValidationResultViewFactory;
public class ComponentHintsExample extends JPanel {
    private Feed feed;
    private FeedPresentationModel feedPresentationModel;
    private JPanel panel1;
    private JPanel panel2;
    private JPanel panel3;
    private JComponent iconPanel;
    private ValidationResultModel validationModel;
    public ComponentHintsExample() {
        this.validationModel = new DefaultValidationResultModel();
        createFeed();
        this.feedPresentationModel = new FeedPresentationModel(this.feed);
        ValueModel nameModel = this.feedPresentationModel.getModel("name");
        DefaultFormBuilder formBuilder1 = new DefaultFormBuilder(new FormLayout("right:pref, 3dlu, p:g"));
        JTextField nameField1 = BasicComponentFactory.createTextField(nameModel, false);
        ValidationComponentUtils.setMandatory(nameField1, true);
        ValidationComponentUtils.setMessageKey(nameField1, "form.name_key");
        formBuilder1.append("Name:", nameField1);
        DefaultFormBuilder formBuilder2 = new DefaultFormBuilder(new FormLayout("right:pref, 3dlu, p:g"));
        JTextField nameField2 = BasicComponentFactory.createTextField(nameModel, false);
        ValidationComponentUtils.setMandatory(nameField2, true);
        ValidationComponentUtils.setMessageKey(nameField2, "form.name_key");
        formBuilder2.append("Name:", nameField2);
        DefaultFormBuilder formBuilder3 = new DefaultFormBuilder(new FormLayout("right:pref, 3dlu, p:g"));
        JTextField nameField3 = BasicComponentFactory.createTextField(nameModel, false);
        ValidationComponentUtils.setMandatory(nameField3, true);
        ValidationComponentUtils.setMessageKey(nameField3, "form.name_key");
        formBuilder3.append("Name:", nameField3);
        DefaultFormBuilder formBuilder4 = new DefaultFormBuilder(new FormLayout("right:pref, 4dlu, p:g"));
        JTextField nameField4 = BasicComponentFactory.createTextField(nameModel, false);
        ValidationComponentUtils.setMandatory(nameField4, true);
        ValidationComponentUtils.setMessageKey(nameField4, "form.name_key");
        formBuilder4.append("Name:", nameField4);
        //Padding for overlay icon
        formBuilder4.appendRow("5dlu");
        this.panel1 = formBuilder1.getPanel();
        this.panel2 = formBuilder2.getPanel();
        this.panel3 = formBuilder3.getPanel();
        this.iconPanel = new IconFeedbackPanel(this.validationModel, formBuilder4.getPanel());
        PanelBuilder builder = new PanelBuilder(new FormLayout("p:g"));
        builder.setDefaultDialogBorder();
        builder.appendRow("p");
        builder.add(this.panel1);
        builder.nextLine();
        builder.appendRow("p");
        builder.add(this.panel2);
        builder.nextLine(); builder.appendRow("p");
        builder.add(this.panel3);
        builder.nextLine();
        builder.appendRow("4dlu");
        builder.nextLine();
        builder.appendRow("p");
        builder.add(this.iconPanel);
        builder.nextLine();
        builder.appendRow("4dlu");
        builder.nextLine();
        builder.appendRow("p:g");
        builder.nextLine();
        builder.appendRow("p");
        builder.addLabel("Results");
        builder.nextLine();
        builder.appendRow("50dlu");
        builder.add(ValidationResultViewFactory.createReportList(this.validationModel));
        add(builder.getPanel());
    }
    private void createFeed() {
        this.feed = new Feed();
        this.feed.setName("ClientJava.com");
        this.feed.setSiteUrl("http://www.clientjava.com/blog");
        this.feed.setFeedUrl("http://www.clientjava.com/blog/rss.xml");
    }
    public class FeedPresentationModel extends PresentationModel implements ValidationCapable {
        private ValidationResultModel validationResultModel;
        public FeedPresentationModel(Object bean) {
            super(bean);
            this.validationResultModel = new DefaultValidationResultModel();
            initEventHandling();
        }
        public ValidationResultModel getValidationModel() {
            return this.validationResultModel;
        }
        public ValidationResult validate() {
            PropertyValidationSupport support = new PropertyValidationSupport(feed, "form");
            String name = (String) getModel("name").getValue();
            if (!ValidationUtils.isEmpty(name)) {
                if (!"ClientJava.com".equals(name)) {
                    support.addWarning("name_key", "is not ClientJava.com");
                }
                if (name.length() < 5) {
                    support.addError("name_key", "must be more than 4 characters long.");
                }
            }
            return support.getResult();
        }        private void initEventHandling() {
            PropertyChangeListener handler = new ValueUpdateHandler();
            addBeanPropertyChangeListener(handler);
            getBeanChannel().addValueChangeListener(handler);
        }
        public class ValueUpdateHandler implements PropertyChangeListener {
            public void propertyChange(PropertyChangeEvent evt) {
                updateComponents();
            }
            private void updateComponents() {
                ValidationResult result = validate();
                validationModel.setResult(result);
                ValidationComponentUtils.updateComponentTreeMandatoryAndBlankBackground(panel1);
                ValidationComponentUtils.updateComponentTreeMandatoryBackground(panel2);
                ValidationComponentUtils.updateComponentTreeMandatoryBorder(panel3);
                ValidationComponentUtils.updateComponentTreeValidationBackground(panel1, result);
            }
        }
    }
    public static void main(String[] a){
      JFrame f = new JFrame("Component Hints Example");
      f.setDefaultCloseOperation(2);
      f.add(new ComponentHintsExample());
      f.pack();
      f.setVisible(true);
    }
}
```

Download: jgoodiesValidation.zip (277 K)
---
Related examples in the same category
1. Error Dialog Example
2. Field List Validator Example
3. Info Assist Example
4. Input Verifier Example
5. Validating Domain Object Example
6. Validating On Focus Lost Example
7. Validating On Key Typed Example
8. Validating Presentation Model Example
9. Validation How to Example
10. Validation Icons Example
11. Validation Results View Example
12. Different styles how to indicate that a component contains invalid data
13. how to provide input hints
14. Different validation result views
15. different validation times: key-typed, focus lost, commit (OK pressed)
16. Different configurations of JFormattedTextField
17. different configurations of JFormattedTextField: Number
18. Different styles to mark mandatory fields
