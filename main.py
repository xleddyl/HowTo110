def loadFile(fileName):
   grades = []
   thesisPoints = 0
   with open(fileName) as file:
      for line in file:
         if line[0] == '#':
            continue
         try:
            if line[0] == 'T':
               thesisPoints = int(line.strip().split(';')[1])
               continue
            grade = int(line.strip().split(';')[0])
            if grade < 18 or grade > 30: grade = 0
            CFU = int(line.strip().split(';')[1])
            grades.append((grade, CFU))
         except:
            print('Terminated with error (invalid <GRADE>;<CFU> or T;<MAXPOINTS>) :(')
            exit(0)
   return grades, thesisPoints

def computeAvg(grades):
   numerator = 0
   CFUs = 0
   avg = 0
   for exam in grades:
      numerator += exam[0] * exam[1]
      CFUs += exam[1]
   if CFUs != 0:
      avg = numerator / CFUs
   return avg, CFUs

def splitGrades(grades):
   finalGrades = []
   pendingGrades = []
   [(pendingGrades.append(grade) if grade[0] == 0 else finalGrades.append(grade)) for grade in grades]
   return finalGrades, pendingGrades

if __name__ == '__main__':
   grades, thesisPoints = loadFile('./grades.txt')
   finalGrades, pendingGrades = splitGrades(grades)
   GOAL = ((110 - thesisPoints) * 30) / 110
   CURRENT, CFU_CURRENT = computeAvg(finalGrades)
   _, pendingCFUs = computeAvg(pendingGrades)
   print(f"Exams avg: {round(CURRENT, 2)}")
   print(f"Goal: {round(GOAL, 2)} (assuming {thesisPoints} points for Thesis)")
   print(f"Obtained CFUs: {round(CFU_CURRENT, 2)} / Pending CFUs: {pendingCFUs}")
   PENDING_GOAL = round(((((CFU_CURRENT + pendingCFUs) * GOAL) - (CURRENT * CFU_CURRENT)) / pendingCFUs), 2) if pendingCFUs != 0 else 0
   print(f"Pending exams goal: {f'{CURRENT} (already reached goal, maintain or improve)' if CURRENT > GOAL else ('impossible, greater than 30 :(' if PENDING_GOAL >= 30 else ('impossible, no more pending CFUs :(' if pendingCFUs <= 0 else PENDING_GOAL))}")
   # TUTTO SU UNA LINEA PERCHÉ SI, FATTI GLI AFFARI TUOI