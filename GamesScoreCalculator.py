# Ang Hao Yi 10273989D

killcount = int(input("Enter the kill count score "))
objCompletion = int(input("Enter the objective completion score  "))
survivaltime = int(input("Enter the survival time score "))

finalperformance = killcount*0.3 + objCompletion*0.3 + survivaltime*0.4 
print("The final performance score is ",finalperformance)
