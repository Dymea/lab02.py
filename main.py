# Author: Dymea Schippers dxs5940@psu.edu
# Collaborator: August Sanderson aes6218@psu.edu
# Collaborator: Johnathan Ahn jxa5570@psu.edu
# Collaborator: Ronit Ramnarayan rvr5507@psu.edu
# Collaborator: Nicholas Glaz nsg5204@psu.edu
# Section: 11
# Breakout: 2

def getLetterGrade(grade):
  if (grade >= 93.0):
    print("Your letter grade for CMPSC 131 is A.")
  elif (grade >= 90.0 and grade <93.0):
    print("Your letter grade for CMPSC 131 is A-.")
  elif (grade >= 87.0 and grade < 90.0):
    print("Your letter grade for CMPSC 131 is B+.")
  elif (grade >= 83.0 and grade < 87.0):
    print("Your letter grade for CMPSC 131 is B.")
  elif (grade >= 80.0 and grade < 83.0):
    print("Your letter grade for CMPSC 131 is B-.")
  elif (grade >= 77.0 and grade < 80.0):
    print("Your letter grade for CMPSC 131 is C+.")
  elif (grade >= 70.0 and grade < 77.0):
    print("Your letter grade for CMPSC 131 is C.")
  elif (grade >= 60.0 and grade < 70.0):
    print("Your letter grade for CMPSC 131 is D.")
  else:
    print("Your letter grade for CMPSC 131 is F.")

def run():
  grade = input("Enter your CMPSC 131 grade: ")
  grade = float(grade)
  getLetterGrade(grade)

if __name__ == "__main__":
  run()