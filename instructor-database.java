import java.util.Scanner;
import javafx.application.Application;
import java.io.FileNotFoundException;
import java.io.*;
import java.util.ArrayList;
import java.util.logging.Level;
import java.util.logging.Logger;
import static javafx.application.Application.launch;
import javafx.stage.Stage;
import javafx.scene.layout.StackPane;
import javafx.scene.control.Button;
import javafx.scene.Scene;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Pos;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.GridPane;
import javafx.scene.text.Text;
public class JavaApplication1 extends Application {
Scene mainScreen;
Scene option1;
Scene option2;
Scene errorScreen;
GridPane option2layout;
StackPane mainLayout;
StackPane option1layout;
StackPane errorlayout;
Button button1;
Button button2;
Button button3;
Button submitButtonOption1;
Button submitButtonOption2;
Button returnButton;
Button returnButton2;
Label option1label;
Label option1InstructorName;
Label option1InstructorDepartment;
Label option1InstructorLocation;
Label option2InstructorName;
Label option2InstructorDepartment;
Label option2InstructorID;
TextField instructorIDField;
TextField ID2;
TextField Dept2;
TextField Name2;
Label error1;
public static void main(String[] args) {
launch(args);
}
@Override
public void start(Stage primaryStage) throws FileNotFoundException {
ArrayList<Integer> departmentFund = new ArrayList<>();
ArrayList<String> departmentName = new ArrayList<>();
ArrayList<String> departmentLocation = new ArrayList<>();
primaryStage.setTitle("Primary Project");
button1 = new Button();
button1.setText("1. Get instructor information");
button2 = new Button();
button2.setText("2. Insert a new instructor");
button3 = new Button();
button3.setText("3. Exit");
returnButton = new Button();
returnButton.setText("Go back to main menu");
returnButton2 = new Button();
returnButton2.setText("Go back to main menu");
submitButtonOption1 = new Button();
submitButtonOption1.setText("Submit");
submitButtonOption2 = new Button();
submitButtonOption2.setText("Submit");
mainLayout = new StackPane();
errorlayout = new StackPane();
option1layout = new StackPane();
option2layout = new GridPane();
option2layout.setPrefWidth(10);
option2layout.setPrefHeight(10);
button1.setTranslateX(0);
button1.setTranslateY(-50);
button2.setTranslateX(0);
button2.setTranslateY(0);
button3.setTranslateX(0);
button3.setTranslateY(50);
returnButton.setTranslateX(0);
returnButton.setTranslateY(100);
submitButtonOption1.setTranslateX(0);
submitButtonOption1.setTranslateY(30);
option1label = new Label("Enter instructor ID: ");
option1label.setTranslateX(0);
option1label.setTranslateY(-50);
ID2 = new TextField();
ID2.setPrefWidth(80);
ID2.setMaxWidth(80);
Dept2 = new TextField();
Dept2.setPrefWidth(80);
Dept2.setMaxWidth(80);
Name2 = new TextField();
Name2.setPrefWidth(80);
Name2.setMaxWidth(80);
instructorIDField = new TextField();
instructorIDField.setPrefWidth(80);
instructorIDField.setMaxWidth(80);
Dept2.setAlignment(Pos.BASELINE_CENTER);
Name2.setAlignment(Pos.BASELINE_CENTER);
mainScreen = new Scene(mainLayout, 600, 300);
option1 = new Scene(option1layout, 600, 300);
option2 = new Scene(option2layout, 600, 300);
errorScreen = new Scene(errorlayout, 600, 300);
primaryStage.setScene(mainScreen);
primaryStage.show();
mainLayout.getChildren().add(button1);
mainLayout.getChildren().add(button2);
mainLayout.getChildren().add(button3);
button1.setOnAction((ActionEvent event) -> {
primaryStage.setScene(option1);
option1layout.getChildren().add(returnButton);
option1layout.getChildren().add(submitButtonOption1);
option1layout.getChildren().add(instructorIDField);
option1layout.getChildren().add(option1label);
});
button2.setOnAction((ActionEvent event) -> {
primaryStage.setScene(option2);
Text empty = new Text(" ");
option2layout.add(empty, 0, 0);
option2layout.add(ID2, 3, 1);
option2layout.add(Name2, 3, 2);
option2layout.add(Dept2, 3, 3);
option2InstructorName = new Label("Enter the instructor name: ");
option2InstructorDepartment = new Label("Enter the affiliated department name: ");
option2InstructorID = new Label("Enter the instructor ID: ");
option2layout.add(option2InstructorID, 1, 1);
option2layout.add(option2InstructorName, 1, 2);
option2layout.add(option2InstructorDepartment, 1, 3);
option2layout.add(submitButtonOption2, 3, 6);
});
button3.setOnAction((ActionEvent event) -> {
System.exit(0);
});
returnButton.setOnAction((ActionEvent event) -> {
option1layout.getChildren().clear();
option2layout.getChildren().clear();
errorlayout.getChildren().clear();
clearTextField();
primaryStage.setScene(mainScreen);
primaryStage.show();
});
submitButtonOption1.setOnAction(new EventHandler<ActionEvent>() {
@Override
public void handle(ActionEvent event) {
String strID = instructorIDField.getText();
if (strID == null) {
error1 = new Label("Invalid input. Please press the go back button and try again.");
option1layout.getChildren().add(error1);
removeButtons();
} else {
if (strID.matches("\\d{4}")) {
try {
File instructorFile = new File("C:\\Users\\kdorji01\\Desktop\\instructor.txt");
Scanner instructorDatabase = new Scanner(instructorFile);
File instructorFileSize = new File("C:\\Users\\kdorji01\\Desktop\\instructor.txt");
Scanner instructorDatabaseSize = new Scanner(instructorFileSize);
File departmentFile = new File("C:\\Users\\kdorji01\\Desktop\\department.txt");
Scanner departmentDatabase = new Scanner(departmentFile);
File departmentFileSize = new
File("C:\\Users\\kdorji01\\Desktop\\department.txt");
Scanner departmentDatabaseSize = new Scanner(departmentFile);
int ID = Integer.parseInt(strID);
int arrOfDeptSize = 0;
while (departmentDatabaseSize.hasNextLine()) {
arrOfDeptSize++;
departmentDatabaseSize.nextLine();
}
for (int j = 0; j < arrOfDeptSize; j++) {
String line = departmentDatabase.nextLine();
String[] deptField = line.split(",");
departmentName.add(deptField[0]);
departmentLocation.add(deptField[1]);
departmentFund.add(Integer.parseInt(deptField[2].trim()));
}
ArrayList<Integer> instructorID = new ArrayList<>();
ArrayList<String> instructorName = new ArrayList<>();
ArrayList<String> instructorDepartment = new ArrayList<>();
ArrayList<String> instructorLocation = new ArrayList<>();
int arrOfInstSize = 0;
while (instructorDatabaseSize.hasNextLine()) {
arrOfInstSize++;
instructorDatabaseSize.nextLine();
}
for (int j = 0; j < arrOfInstSize; j++) {
String line = instructorDatabase.nextLine();
String[] instrucField = line.split(",");
instructorID.add(Integer.parseInt(instrucField[0].trim()));
instructorName.add(instrucField[1]);
instructorDepartment.add(instrucField[2]);
for (int a = 0; a < arrOfDeptSize; a++) {
if (instructorDepartment.get(j).equals(departmentName.get(a))) {
instructorLocation.add(j, departmentLocation.get(a));
}
}
}
boolean option1flag = false;
for (int i = 0; i < arrOfInstSize; i++) {
if (instructorID.get(i) == ID) {
option1InstructorName = new Label("Instructor Name: "
+ instructorName.get(i));
option1InstructorDepartment = new Label("Instructor Department: "
+ instructorDepartment.get(i));
option1InstructorLocation = new Label("Department Location: "
+ instructorLocation.get(i));
option1InstructorName.setTranslateX(0);
option1InstructorName.setTranslateY(-50);
option1InstructorDepartment.setTranslateX(0);
option1InstructorDepartment.setTranslateY(-25);
option1InstructorLocation.setTranslateX(0);
option1InstructorLocation.setTranslateY(0);
removeButtons();
option1layout.getChildren().add(option1InstructorName);
option1layout.getChildren().add(option1InstructorDepartment);
option1layout.getChildren().add(option1InstructorLocation);
option1flag = true;
}
}
if (option1flag == false) {
removeButtons();
error1 = new Label("The ID does not appear in the file.");
option1layout.getChildren().add(error1);
}
} catch (FileNotFoundException ex) {
Logger.getLogger(JavaApplication1.class.getName()).log(Level.SEVERE, null,
ex);
}
} else {
error1 = new Label(
"Invalid input. Please press the go back button and try again.");
option1layout.getChildren().add(error1);
removeButtons();
}
}
}
});
submitButtonOption2.setOnAction((ActionEvent event) -> {
try {
String strID = ID2.getText();
String strDept = Dept2.getText();
String strName = Name2.getText();
if ("".equals(strID)) {
error1 = new Label("ID field cannot be empty.");
errorlayout.getChildren().add(error1);
error1.setTranslateX(0);
error1.setTranslateY(-50);
errorlayout.getChildren().add(returnButton);
primaryStage.setScene(errorScreen);
primaryStage.show();
} else {
boolean continueFlag = true;
File instructorFile = new File("C:\\Users\\kdorji01\\Desktop\\instructor.txt");
Scanner instructorDatabase = new Scanner(instructorFile);
File instructorFileSize = new File("C:\\Users\\kdorji01\\Desktop\\instructor.txt");
Scanner instructorDatabaseSize = new Scanner(instructorFileSize);
File departmentFile = new File("C:\\Users\\kdorji01\\Desktop\\department.txt");
Scanner departmentDatabase = new Scanner(departmentFile);
File departmentFileSize = new File("C:\\Users\\kdorji01\\Desktop\\department.txt");
Scanner departmentDatabaseSize = new Scanner(departmentFile);
FileWriter fw = new FileWriter(instructorFile, true);
PrintWriter output = new PrintWriter(fw);
int arrOfDeptSize = 0;
while (departmentDatabaseSize.hasNextLine()) {
arrOfDeptSize++;
departmentDatabaseSize.nextLine();
}
for (int j = 0; j < arrOfDeptSize; j++) {
String line = departmentDatabase.nextLine();
String[] deptField = line.split(",");
departmentName.add(deptField[0]);
departmentLocation.add(deptField[1]);
departmentFund.add(Integer.parseInt(deptField[2].trim()));
}
ArrayList<Integer> instructorID = new ArrayList<>();
ArrayList<String> instructorName = new ArrayList<>();
ArrayList<String> instructorDepartment = new ArrayList<>();
ArrayList<String> instructorLocation = new ArrayList<>();
int arrOfInstSize = 0;
while (instructorDatabaseSize.hasNextLine()) {
arrOfInstSize++;
instructorDatabaseSize.nextLine();
}
departmentFile = new File("C:\\Users\\kdorji01\\Desktop\\department.txt");
departmentDatabase = new Scanner(departmentFile);
for (int j = 0; j < arrOfInstSize; j++) {
String line = instructorDatabase.nextLine();
String[] instrucField = line.split(",");
instructorID.add(Integer.parseInt(instrucField[0].trim()));
instructorName.add(instrucField[1]);
instructorDepartment.add(instrucField[2]);
for (int a = 0; a < arrOfDeptSize; a++) {
if (instructorDepartment.get(j).equals(departmentName.get(a))) {
instructorLocation.add(j, departmentLocation.get(a));
}
}
}
for (int i = 0; i < arrOfInstSize; i++) {
if (instructorID.get(i) == Integer.parseInt(strID)) {
continueFlag = false;
break;
}
}
if (continueFlag == false) {
error1 = new Label("ID entered already exists in the file.");
errorlayout.getChildren().add(error1);
error1.setTranslateX(0);
error1.setTranslateY(-50);
errorlayout.getChildren().add(returnButton);
primaryStage.setScene(errorScreen);
primaryStage.show();
} else {
if ("".equals(strName)) {
error1 = new Label("Name field cannot be empty.");
errorlayout.getChildren().add(error1);
error1.setTranslateX(0);
error1.setTranslateY(-50);
errorlayout.getChildren().add(returnButton);
primaryStage.setScene(errorScreen);
primaryStage.show();
} else {
if (strName.matches("^[\\p{L} .'-]+$")) {
if ("".equals(strDept)) {
error1 = new Label("Department field cannot be empty.");
errorlayout.getChildren().add(error1);
error1.setTranslateX(0);
error1.setTranslateY(-50);
errorlayout.getChildren().add(returnButton);
primaryStage.setScene(errorScreen);
primaryStage.show();
} else {
boolean option2DeptFlag = false;
if (strDept.toUpperCase().matches("CMPT")
|| strDept.toUpperCase().matches("BIO") ||
strDept.toUpperCase().matches("MATH")) {
option2DeptFlag = true;
} else {
error1 = new Label("Invalid department format.");
errorlayout.getChildren().add(error1);
error1.setTranslateX(0);
error1.setTranslateY(-50);
errorlayout.getChildren().add(returnButton);
primaryStage.setScene(errorScreen);
primaryStage.show();
}
strDept = strDept.toUpperCase();
if (option2DeptFlag == true) {
arrOfInstSize++;
for (int a = 0; a < arrOfDeptSize; a++) {
if (strDept.equals(departmentName.get(a))) {
instructorID.add(Integer.parseInt(strID));
instructorDepartment.add(strDept);
instructorName.add(strName);
switch (strDept) {
case "MATH":
instructorLocation.add("RLC");
break;
case "BIO":
instructorLocation.add("LEO");
break;
default:
instructorLocation.add("RLC");
break;
}
}
}
output.println();
output.print(Integer.parseInt(strID) + "," + strName + "," + strDept);
output.close();
Label alertWindow = new Label("The new instructor has been
added.");
errorlayout.getChildren().add(alertWindow);
alertWindow.setTranslateX(0);
alertWindow.setTranslateY(-50);
errorlayout.getChildren().add(returnButton);
primaryStage.setScene(errorScreen);
primaryStage.show();
}
}
} else {
error1 = new Label("Invalid name format. Please press the go back
button and try again.");
errorlayout.getChildren().add(error1);
error1.setTranslateX(0);
error1.setTranslateY(-50);
errorlayout.getChildren().add(returnButton);
primaryStage.setScene(errorScreen);
primaryStage.show();
}
}
}
}
}catch (FileNotFoundException ex) {
Logger.getLogger(JavaApplication1.class.getName()).log(Level.SEVERE, null, ex);
}catch (IOException ex) {
Logger.getLogger(JavaApplication1.class.getName()).log(Level.SEVERE, null, ex);
}
});
}
public void removeButtons() {
option1layout.getChildren().remove(submitButtonOption1);
option1layout.getChildren().remove(option1label);
option1layout.getChildren().remove(instructorIDField);
option2layout.getChildren().remove(option2InstructorDepartment);
option2layout.getChildren().remove(option2InstructorID);
option2layout.getChildren().remove(option2InstructorName);
option2layout.getChildren().remove(ID2);
option2layout.getChildren().remove(Dept2);
option2layout.getChildren().remove(Name2);
option2layout.getChildren().remove(submitButtonOption2);
}
public void clearTextField() {
instructorIDField.setText(null);
ID2.setText("");
Dept2.setText("");
Name2.setText("");
}
