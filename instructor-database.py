Kalden Dorji
Final Project

import tkinter
import tkinter.messagebox


class UniIndex:
   def __init__(self):
       self.main_window=tkinter.Tk()
       self.main_window.title("University Information System")
       self.main_window.geometry('400x150')
      
       #Radio creation/packing
       self.radio_frame = tkinter.Frame(self.main_window)
       self.radio_var = tkinter.IntVar()
       self.radio_var.set(0)
       self.rb1 = tkinter.Radiobutton(self.radio_frame,text='Get Instructor Info',variable=self.radio_var,value=1,command=self.option1)
       self.rb2 = tkinter.Radiobutton(self.radio_frame,text='Get Department Info',variable=self.radio_var,value=2,command=self.option2)
       self.rb3 = tkinter.Radiobutton(self.radio_frame,text='Clear',variable=self.radio_var,value=3,command=self.option3)
       self.rb4 = tkinter.Radiobutton(self.radio_frame,text='Quit',variable=self.radio_var,value=4,command=self.quit_function)
       self.rb1.pack(side='left')
       self.rb2.pack(side='left')
       self.rb3.pack(side='left')
       self.rb4.pack(side='left')
       self.radio_frame.pack()
      
       self.option_frame=tkinter.Frame(self.main_window)


       self.id_label1 = tkinter.Label(self.option_frame,text='Enter instructor ID: ')
       self.id_box = tkinter.Entry(self.option_frame)
       self.id_box.bind('<Return>',self.get_value)
       self.submit_btn =tkinter.Button(self.option_frame,text='Submit',command=self.get_value)
      
       self.name_frame=tkinter.Frame(self.main_window)
       self.name = tkinter.StringVar(self.name_frame)
       self.dept_frame=tkinter.Frame(self.main_window)
       self.dept=tkinter.StringVar(self.dept_frame)
       self.building_frame=tkinter.Frame(self.main_window)
       self.building=tkinter.StringVar(self.building_frame)
       self.pname_label=tkinter.Label(self.name_frame,text="Name: ")
       self.name_label=tkinter.Label(self.name_frame,textvariable=self.name)
       self.pdepartment_label=tkinter.Label(self.dept_frame,text="Department: ")
       self.dept_label = tkinter.Label(self.dept_frame, textvariable=self.dept)
       self.pbuilding_label=tkinter.Label(self.building_frame,text="Building: ")
       self.building_label = tkinter.Label(self.building_frame,textvariable=self.building)
       self.error_frame = tkinter.Frame(self.main_window)
       self.error_label=tkinter.Label(self.error_frame,text='Information not found.')
      


       self.name2 =tkinter.StringVar(self.option_frame)
       self.name2_label = tkinter.Label(self.option_frame,text="Enter department name: ")
       self.pname2 = tkinter.Label(self.option_frame,textvariable=self.name2)


       self.id_box2 = tkinter.Entry(self.option_frame)
       self.id_box2.bind('<Return>',self.get_value2)
       self.submit_btn2 =tkinter.Button(self.option_frame,text='Submit',command=self.get_value2)




       self.budget_frame = tkinter.Frame(self.main_window)
       self.budget=tkinter.StringVar(self.budget_frame)
       self.budget_label = tkinter.Label(self.budget_frame,text="Budget: ")
       self.pbudget_label = tkinter.Label(self.budget_frame, textvariable=self.budget)


       self.main_window.mainloop()
   def option1(self):
       self.option3()
       #Widgets for new frame
       self.id_label1.pack(side='left')
       self.id_box.pack(side='left')
       self.submit_btn.pack(side='left')
       self.option_frame.pack(anchor='w')
   def option2(self):
       self.option3()
       #adding widgets
       self.name2_label.pack(side='left')
       self.id_box2.pack(side='left')
       self.submit_btn2.pack(side='left')
       self.option_frame.pack(anchor='w')
   def option3(self):
       if(self.option_frame.winfo_ismapped()):
           self.id_label1.forget()
           self.name2_label.forget()
           self.id_box.delete(0,tkinter.END)
           self.id_box.forget()
           self.id_box2.delete(0,tkinter.END)
           self.id_box2.forget()


           self.option_frame.forget()
           self.name_frame.forget()
           self.building_frame.forget()
           self.dept_frame.forget()
           self.error_frame.forget()
           self.budget_frame.forget()
           self.submit_btn.forget()
           self.submit_btn2.forget()
   def get_value(self,event=None):
       flag1 = False
       flag2 = False
       with open('instructor.txt','r') as instructor:
           for line in instructor:
               temp = line.strip().split(',')
               ID = temp[0]
               temp_name = temp[1]
               temp_dept = temp[2]
               if ID == self.id_box.get():
                   flag1 = True
                   break
       with open('department.txt','r') as department:
           for line in department:
               temp = line.strip().split(',')
               temp_dept2 = temp[0]
               temp_building = temp[1]
               if temp_dept == temp_dept2:
                   flag2 = True
                   break
       if(flag1 and flag2):
           if self.error_frame is not None:
               self.error_frame.forget()
           self.name.set(temp_name)
           self.pname_label.pack(side='left')
           self.name_label.pack(side='left')
           self.dept.set(temp_dept)
           self.pdepartment_label.pack(side='left')
           self.dept_label.pack(side='left')
           self.building.set(temp_building)
           self.pbuilding_label.pack(side='left')
           self.building_label.pack(side='left')
           self.name_frame.pack(anchor='w')
           self.dept_frame.pack(anchor='w')
           self.building_frame.pack(anchor='w')
       else:
           if self.name_frame.winfo_ismapped():
               self.name_frame.forget()
               self.name.set('')
           if self.dept_frame.winfo_ismapped():
               self.dept_frame.forget()
               self.dept.set('')
           if self.building_frame.winfo_ismapped():
               self.building_frame.forget()
           self.error_label.pack()
           self.error_frame.pack(anchor='w')   
   def get_value2(self,event=None):
       flag1 = False
       with open('department.txt','r') as department:
           for line in department:
               temp = line.strip().split(',')
               temp_dept = temp[0]
               temp_building = temp[1]
               temp_fund = temp[2]
               if temp_dept == self.id_box2.get():
                   flag1 = True
                   break
       if(flag1):
           if self.error_frame is not None:
               self.error_frame.forget()
           self.building.set(temp_building)
           self.pbuilding_label.pack(side='left')
           self.building_label.pack()
           self.building_frame.pack(anchor='w')
           self.budget.set(temp_fund)
           self.budget_label.pack(side='left')
           self.pbudget_label.pack()
           self.budget_frame.pack(anchor='w')


       else:
           if self.building_frame.winfo_ismapped():
               self.building_frame.forget()
           if self.budget_frame.winfo_ismapped():
               self.budget_frame.forget()


           self.error_label.pack()
           self.error_frame.pack(anchor='w')
 


   def quit_function(self):
       self.main_window.destroy()


def main():
   gui = UniIndex()
main()
