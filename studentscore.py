class Student:
    def __init__(self, name, num_scores):
        self.name = name
        # Initialize a list of scores to 0 based on the provided number
        self.test_scores = [0] * num_scores

    def getName(self):
        return self.name

    def getScore(self, position):
        # Assuming position is 0-indexed
        if 0 <= position < len(self.test_scores):
            return self.test_scores[position]
        return None

    def setScore(self, position, value):
        if 0 <= position < len(self.test_scores):
            self.test_scores[position] = value

    def getHighestScore(self):
        if not self.test_scores:
            return 0
        return max(self.test_scores)

    def getAverageScore(self):
        if not self.test_scores:
            return 0
        return sum(self.test_scores) / len(self.test_scores)

    def __str__(self):
        return f"Student: {self.name}\nScores: {self.test_scores}\nAverage: {self.getAverageScore():.2f}"

# --- User Input Implementation ---
if __name__ == "__main__":
    print("--- Student Record System ---")
    
    # 1. Input the student's name
    student_name = input("Enter the student's name: ")
    
    # 2. Input the number of scores (with validation)
    while True:
        try:
            num = int(input(f"How many test scores will you enter for {student_name}? "))
            if num > 0:
                break
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            
    # Initialize the student object
    current_student = Student(student_name, num)
    
    # 3. Input each individual score
    print(f"\nPlease enter the {num} scores for {student_name}:")
    for i in range(num):
        while True:
            try:
                # Prompting as i+1 so it reads "score #1, score #2", etc.
                score_val = float(input(f"Score #{i + 1}: "))
                current_student.setScore(i, score_val)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                
    # 4. Print the final results
    print("\n--- Final Record ---")
    print(current_student)
    print(f"Highest Score: {current_student.getHighestScore():.2f}")
