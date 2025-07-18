def get_marks():
    marks=[]
    for i in range(5):
        mark=float(input("enter mark {i+1}: "))
        marks.append(mark)
        return marks
    
    def add_marks(marks):
        total=sum(marks)
        print("Total :",total)
        marks_list = get_marks()
        add_marks(marks_list)