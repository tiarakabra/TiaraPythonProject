import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Quiz Game")
        
        self.welcome_frame = tk.Frame(root)
        self.welcome_frame.pack(pady=80)
        
        self.welcome_label = tk.Label(self.welcome_frame, text="Welcome to the Python Quiz Game!")
        self.welcome_label.pack(pady=90)
        
        self.start_button = tk.Button(self.welcome_frame, text="Start Quiz", command=self.start_quiz)
        self.start_button.pack()
        
        self.quiz_frame = tk.Frame(root)
        
        self.questions = [
            {"question": "What is the capital of France?", 
             "options": ["Paris", "Berlin", "Madrid", "Rome"],
               "correct": 0},
           {
        "question": "What is the largest planet in our solar system?",
        "options": ["a) Saturn", "b) Mars", "c) Jupiter", "d) Venus"],
        "correct": "2"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["a) H2O", "b) CO2", "c) O2", "d) NaCl"],
        "correct": "0"
    },
    {
        "question": "Where is eiffel tower situeted?",
        "options": ["a) Paris", "b) India", "c) Australia", "d) New York"],
        "correct": "0"
    },
    {
        "question": "Which of these is a primary colour?",
        "options": ["a) Black", "b) Brown", "c) Orange", "d) Blue"],
        "correct": "3"
    },
    {
        "question": "Sun rises from?",
        "options": ["a) West", "b) North", "c) East", "d) South"],
        "correct": "2"
    },
    #6
    {
        "question": "How many sides are there in a triangle?",
        "options": ["a) Three", "b) Two", "c) Six", "d) Four"],
        "correct": "0"
    },
     {
        "question": "Who invented electricity?",
        "options": ["a) Neil Armstrong", "b) Benjamin Franklin", 
                    "c) Thomas Edison", "d) George Washington"],
        "correct": "1"
    },
    {
        "question": "HWho wrote Merchant of Venice?",
        "options": ["a) Shakespeare", "b) R.K Narayan", 
                    "c) Chetan Bhagat", "d) RavindraNath Tagore"],
        "correct": "0"
    },
    {
        "question": " Name the largest 'Democracy' of the world?",
        "options": ["a)France ", "b) Germany", "c) India", "d) Dubai"],
        "correct": "2"
    },
    #10
    {
        "question": "What is the currency of Dubai",
        "options": ["a)Rupee", "b) Dirhams", "c) Euros", "d) Dollars"],
        "correct": "1"
    },
    {
        "question": "Which of this animal Hibernates?",
        "options": ["a)Bears ", "b)Lion", "c) Dogs", "d) Eagle"],
        "correct": "1"
    },
    {
        "question": "Wich of this is the Powerhouse of  human cell",
        "options": ["a)Nucleas ", "b) Chromosome", "c) Mitochondria", "d)Platelets"],
        "correct": "2"
    },
    {
        "question": "Which of these architecture belongs to Harappan civilasation",
        "options": ["a)Taj Mahal ", "b) The Great Bath", 
                    "c) Leaning tower of Pisa", "d) Burj Khalifa"],
        "correct": "1"
    },
    {
        "question": " Name the largest 'Democracy' of the world?",
        "options": ["a)France ", "b) Germany", "c) India", "d) Dubai"],
        "correct": "2"
    },
    {
        "question": " Which is the continent with the most number of countries?",
        "options": ["a)Australia ", "b) Africa", "c) Asia", "d) Europe"],
        "correct": "1"
    },
    {
        "question": "  Which is the hardest substance available on earth?",
        "options": ["a)Diamond ", "b) Charcoal", "c) Platinum", "d) Aluminium"],
        "correct": "1"
    },
        ]
        
        self.current_question = 0
        self.score = 0
        
        self.question_label = tk.Label(self.quiz_frame, text="")
        self.question_label.pack(pady=10)
        
        self.radio_var = tk.IntVar()
        
        self.radio_buttons = []
        for i in range(4):
            radio_button = tk.Radiobutton(self.quiz_frame, text="", variable=self.radio_var, value=i)
            self.radio_buttons.append(radio_button)
            radio_button.pack(pady=5)
        
        self.next_button = tk.Button(self.quiz_frame, text="Next", command=self.next_question)
        self.next_button.pack(pady=10)
        
        self.load_question(self.current_question)
    
    def start_quiz(self):
        self.welcome_frame.pack_forget()
        self.quiz_frame.pack(pady=20)
    
    def load_question(self, question_idx):
        if question_idx < len(self.questions):
            question_data = self.questions[question_idx]
            self.question_label.config(text=question_data["question"])
            
            for i, option in enumerate(question_data["options"]):
                self.radio_buttons[i].config(text=option)
            
            self.radio_var.set(-1)
        else:
            messagebox.showinfo("Quiz Finished", f"Your score: {self.score}/{len(self.questions)}")
            self.root.destroy()
    
    def next_question(self):
        selected_option = self.radio_var.get()
        
        if selected_option == -1:
            messagebox.showwarning("Warning", "Please select an option.")
            return
        
        correct_option = self.questions[self.current_question]["correct"]
        if selected_option == correct_option:
            self.score += 1
        
        self.current_question += 1
        self.load_question(self.current_question)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
