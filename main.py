from tkinter import *
from tkinter import ttk
import random
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()

        self.title("""Nikita's probability counter""")
        self.minsize(720, 480)
        self.label_frame = Frame(self, height=300, width=250)
        self.label_frame.grid(column=1, row=0, padx=30, sticky=W)
        self.x_axis = [x for x in range(101)]
        self.y_axis = [0 for x in range(101)]
        self.label_frame

        style = ttk.Style(self)
        style.theme_use('classic')
        style.configure('TButton', background='#eeeeee', relief=GROOVE, bd=0)

        self.label_total_num = ttk.Label(self.label_frame, text='Сколько частей в тесте')
        self.label_total_num.grid(column=0, row=0, sticky=W, columnspan=3)
        self.label_total_num.configure(background='#ffffff', font=("Arial", 20))
        style.configure('TRadiobutton', background='#eeeeee', relief=GROOVE, bd=0)

        self.rb_choice = IntVar()
        self.rb1 = ttk.Radiobutton(self.label_frame, text='1', variable=self.rb_choice, value=1, command=self.pick_rb)
        self.rb2 = ttk.Radiobutton(self.label_frame, text='2', variable=self.rb_choice, value=2, command=self.pick_rb)
        self.rb1.grid(column=0, row=1, sticky=W)
        self.rb2.grid(column=1, row=1, sticky=W)
        self.rb_choice.set('1')

        self.button = ttk.Button(self.label_frame, text='Посчитать', command=self.count_button)
        self.button.grid(column=0, row=8, pady=15, columnspan=3)

        self.init_ui()
        self.draw_plot()


    def pick_rb(self):
        self.init_ui()


    def count_button(self):
        try:
            self.concrete_answer.destroy()
        except:
            pass
        current_state = self.rb_choice.get()
        if current_state == 1:
            total_num = int(self.total_num.get())
            num_to_take = int(self.num_to_take.get())
            num_to_know = int(self.num_to_know.get())
            questions = list(x for x in range(0, total_num+1))
            success = 0
            all_runs = 100000
            chances = []

            for i_know in questions:
                for i in range(all_runs):
                    for question_sample in  sorted(random.sample(questions, num_to_take))[0:num_to_know]:
                        if question_sample > i_know:
                            break
                    else:
                        success += 1
                chances.append((success / all_runs) * 100)
                success = 0
            self.x_axis = questions
            self.y_axis = chances
        elif current_state == 2:
            total_num_p1 = int(self.total_num_p1.get())
            num_to_take_p1 = int(self.num_to_take_p1.get())
            num_to_know_p1 = int(self.num_to_know_p1.get())
            questions1 = list(x for x in range(0, total_num_p1 + 1))
            success = 0
            all_runs = 100000
            chances1 = []

            for i_know in questions1:
                for i in range(all_runs):
                    for question_sample in sorted(random.sample(questions1, num_to_take_p1))[0:num_to_know_p1]:
                        if question_sample > i_know:
                            break
                    else:
                        success += 1
                chances1.append(success / all_runs)
                success = 0

            total_num_p2 = int(self.total_num_p2.get())
            num_to_take_p2 = int(self.num_to_take_p2.get())
            num_to_know_p2 = int(self.num_to_know_p2.get())
            questions2 = list(x for x in range(0, total_num_p2 + 1))
            success = 0
            chances2 = []

            for i_know in questions2:
                for i in range(all_runs):
                    for question_sample in sorted(random.sample(questions2, num_to_take_p2))[0:num_to_know_p2]:
                        if question_sample > i_know:
                            break
                    else:
                        success += 1
                chances2.append(success / all_runs)
                success = 0

            self.x_axis = compare_p2_lists(questions1, questions2)
            self.y_axis = count_probabilities(chances1, chances2)
        self.draw_plot()

        try:
            concrete1 = int(self.concrete_p1.get())
            concrete2 = int(self.concrete_p2.get())
        except:
            concrete1 = False
            concrete2 = False

        if concrete1 and concrete2:
            for i in range(all_runs):
                for question_sample in sorted(random.sample(questions1, num_to_take_p1))[0:num_to_know_p1]:
                    if question_sample > concrete1:
                        break
                else:
                    success += 1
            answer_concrete_1 = (success / all_runs)
            success = 0

            for i in range(all_runs):
                for question_sample in sorted(random.sample(questions2, num_to_take_p2))[0:num_to_know_p2]:
                    if question_sample > concrete2:
                        break
                else:
                    success += 1
            answer_concrete_2 = (success / all_runs)
            success = 0
            self.concrete_answer = ttk.Label(self.label_frame, text='Вероятность сдать  {}%'.format(
                int(answer_concrete_1 * answer_concrete_2*100)))
            self.concrete_answer.grid(column=0, row=15, sticky=W, columnspan=3)
            self.concrete_answer.configure(background='#ffffff', font=("Arial", 20))



    def init_ui(self):
        current_state = self.rb_choice.get()
        if current_state == 1:
            try:
                self.label_num_to_take.destroy()
                self.label_num_to_know.destroy()
                self.textbox_total_num_p1.destroy()
                self.textbox_num_to_take_p1.destroy()
                self.textbox_num_to_know_p1.destroy()
                self.textbox_total_num_p2.destroy()
                self.textbox_num_to_take_p2.destroy()
                self.textbox_num_to_know_p2.destroy()
                self.label_part_1_1.destroy()
                self.label_part_2_1.destroy()
                self.label_part_1_2.destroy()
                self.label_part_2_2.destroy()
                self.label_part_1_3.destroy()
                self.label_part_2_3.destroy()
                self.label_part_1_4.destroy()
                self.label_part_2_4.destroy()
                self.textbox_concrete_p1.destroy()
                self.textbox_concrete_p2.destroy()
                self.label_concrete.destroy()
                self.button.grid(row=8)
                self.concrete_answer.destroy()
                self.concrete_p1.destroy()
                self.concrete_p2.destroy()
            except:
                pass


            self.label_total_num = ttk.Label(self.label_frame, text='Количество билетов')
            self.label_total_num.grid(column=0, row=2, sticky=W, columnspan=3)
            self.label_total_num.configure(background='#ffffff', font=("Arial", 20))

            self.label_num_to_take = ttk.Label(self.label_frame, text='Сколько билетов тянешь')
            self.label_num_to_take.grid(column=0, row=4, sticky=W, columnspan=3)
            self.label_num_to_take.configure(background='#ffffff', font=("Arial", 20))

            self.label_num_to_know = ttk.Label(self.label_frame, text='Сколько из них нужно знать')
            self.label_num_to_know.grid(column=0, row=6, sticky=W, columnspan=3)
            self.label_num_to_know.configure(background='#ffffff', font=("Arial", 20))

            self.draw_plot()

            self.total_num = StringVar()
            self.num_to_take = StringVar()
            self.num_to_know = StringVar()

            self.textbox_total_num = ttk.Entry(self.label_frame, width=20, textvariable=self.total_num)
            self.textbox_total_num.grid(column=0, row=3, sticky=W, pady=5, columnspan=3)
            self.textbox_total_num.configure(font=("Arial", 16))

            self.textbox_num_to_take = ttk.Entry(self.label_frame, width=20, textvariable=self.num_to_take)
            self.textbox_num_to_take.grid(column=0, row=5, sticky=W, pady=5, columnspan=3)
            self.textbox_num_to_take.configure(font=("Arial", 16))

            self.textbox_num_to_know = ttk.Entry(self.label_frame, width=20, textvariable=self.num_to_know)
            self.textbox_num_to_know.grid(column=0, row=7, sticky=W, pady=5, columnspan=3)
            self.textbox_num_to_know.configure(font=("Arial", 16))

        elif current_state == 2:
            self.label_total_num.destroy()
            self.label_num_to_take.destroy()
            self.label_num_to_know.destroy()
            self.textbox_total_num.destroy()
            self.textbox_num_to_take.destroy()
            self.textbox_num_to_know.destroy()
            self.button.grid(row=14)
            try:
                self.concrete_answer.destroy()
            except:
                pass

            self.label_total_num = ttk.Label(self.label_frame, text='Количество билетов')
            self.label_total_num.grid(column=0, row=2, sticky=W, columnspan=2)
            self.label_total_num.configure(background='#ffffff', font=("Arial", 20))

            self.label_num_to_take = ttk.Label(self.label_frame, text='Сколько билетов тянешь')
            self.label_num_to_take.grid(column=0, row=5, sticky=W, columnspan=2)
            self.label_num_to_take.configure(background='#ffffff', font=("Arial", 20))

            self.label_num_to_know = ttk.Label(self.label_frame, text='Сколько из них нужно знать')
            self.label_num_to_know.grid(column=0, row=8, sticky=W, columnspan=2)
            self.label_num_to_know.configure(background='#ffffff', font=("Arial", 20))

            self.label_concrete = ttk.Label(self.label_frame, text='Вероятность для конкретного случая')
            self.label_concrete.grid(column=0, row=11, sticky=W, columnspan=2)
            self.label_concrete.configure(background='#ffffff', font=("Arial", 20))

            self.label_part_1_1 = ttk.Label(self.label_frame, text='Часть 1')
            self.label_part_1_1.grid(column=0, row=3, sticky=W)
            self.label_part_1_1.configure(background='#ffffff', font=("Arial", 12))

            self.label_part_2_1 = ttk.Label(self.label_frame, text='Часть 2')
            self.label_part_2_1.grid(column=1, row=3, sticky=W)
            self.label_part_2_1.configure(background='#ffffff', font=("Arial", 12))

            self.label_part_1_2 = ttk.Label(self.label_frame, text='Часть 1')
            self.label_part_1_2.grid(column=0, row=6, sticky=W)
            self.label_part_1_2.configure(background='#ffffff', font=("Arial", 12))

            self.label_part_2_2 = ttk.Label(self.label_frame, text='Часть 2')
            self.label_part_2_2.grid(column=1, row=6, sticky=W)
            self.label_part_2_2.configure(background='#ffffff', font=("Arial", 12))

            self.label_part_1_3 = ttk.Label(self.label_frame, text='Часть 1')
            self.label_part_1_3.grid(column=0, row=9, sticky=W)
            self.label_part_1_3.configure(background='#ffffff', font=("Arial", 12))

            self.label_part_2_3 = ttk.Label(self.label_frame, text='Часть 2')
            self.label_part_2_3.grid(column=1, row=9, sticky=W)
            self.label_part_2_3.configure(background='#ffffff', font=("Arial", 12))

            self.label_part_1_4 = ttk.Label(self.label_frame, text='Часть 1')
            self.label_part_1_4.grid(column=0, row=12, sticky=W)
            self.label_part_1_4.configure(background='#ffffff', font=("Arial", 12))

            self.label_part_2_4 = ttk.Label(self.label_frame, text='Часть 2')
            self.label_part_2_4.grid(column=1, row=12, sticky=W)
            self.label_part_2_4.configure(background='#ffffff', font=("Arial", 12))

            self.total_num_p1 = StringVar()
            self.num_to_take_p1 = StringVar()
            self.num_to_know_p1 = StringVar()
            self.concrete_p1 = StringVar()

            self.total_num_p2 = StringVar()
            self.num_to_take_p2 = StringVar()
            self.num_to_know_p2 = StringVar()
            self.concrete_p2 = StringVar()

            self.textbox_total_num_p1 = ttk.Entry(self.label_frame, width=10, textvariable=self.total_num_p1)
            self.textbox_total_num_p1.grid(column=0, row=4, sticky=W, pady=5)
            self.textbox_total_num_p1.configure(font=("Arial", 16))

            self.textbox_num_to_take_p1 = ttk.Entry(self.label_frame, width=10, textvariable=self.num_to_take_p1)
            self.textbox_num_to_take_p1.grid(column=0, row=7, sticky=W, pady=5)
            self.textbox_num_to_take_p1.configure(font=("Arial", 16))

            self.textbox_num_to_know_p1 = ttk.Entry(self.label_frame, width=10, textvariable=self.num_to_know_p1)
            self.textbox_num_to_know_p1.grid(column=0, row=10, sticky=W, pady=5)
            self.textbox_num_to_know_p1.configure(font=("Arial", 16))

            self.textbox_concrete_p1 = ttk.Entry(self.label_frame, width=10, textvariable=self.concrete_p1)
            self.textbox_concrete_p1.grid(column=0, row=13, sticky=W, pady=5)
            self.textbox_concrete_p1.configure(font=("Arial", 16))

            self.textbox_total_num_p2 = ttk.Entry(self.label_frame, width=10, textvariable=self.total_num_p2)
            self.textbox_total_num_p2.grid(column=1, row=4, sticky=W, pady=5)
            self.textbox_total_num_p2.configure(font=("Arial", 16))

            self.textbox_num_to_take_p2 = ttk.Entry(self.label_frame, width=10, textvariable=self.num_to_take_p2)
            self.textbox_num_to_take_p2.grid(column=1, row=7, sticky=W, pady=5)
            self.textbox_num_to_take_p2.configure(font=("Arial", 16))

            self.textbox_num_to_know_p2 = ttk.Entry(self.label_frame, width=10, textvariable=self.num_to_know_p2)
            self.textbox_num_to_know_p2.grid(column=1, row=10, sticky=W, pady=5)
            self.textbox_num_to_know_p2.configure(font=("Arial", 16))

            self.textbox_concrete_p2 = ttk.Entry(self.label_frame, width=10, textvariable=self.concrete_p2)
            self.textbox_concrete_p2.grid(column=1, row=13, sticky=W, pady=5)
            self.textbox_concrete_p2.configure(font=("Arial", 16))

    def draw_plot(self):
        try:
            self.canvas.destroy()
            self.toolbar_frame.destroy()
        except:
            pass
        f = Figure(figsize=(7,5), dpi=100)
        a = f.add_subplot(111)
        a.plot(self.x_axis, self.y_axis)
        a.grid(color='#dddddd', linestyle='--', linewidth=1)
        a.set_xlabel('Число выученных билетов')
        a.set_ylabel('Вероятность сдать экзамен')

        self.canvas = FigureCanvasTkAgg(f, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(column = 0, row =0)

        self.toolbar_frame = Frame(self)
        self.toolbar_frame.grid(column=0, row=1)
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.toolbar_frame)


def compare_p2_lists(list1, list2):
    if len(list1) >= len(list2):
        return list1
    else:
        return list2

def count_probabilities(list1, list2):
    if len(list1) > len(list2):
        for _ in range(len(list1)-len(list2)):
            list2.append(list2[-1])
    elif len(list1) < len(list2):
        for _ in range(len(list2) - len(list1)):
            list1.append(list1[-1])
    return [a*b*100 for a,b in zip(list1,list2)]


root = Root()
root.mainloop()