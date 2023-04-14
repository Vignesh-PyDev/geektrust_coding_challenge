import os,sys
import math

Loan_List = []

def Calculate_Interest(P,N,I):
	return math.ceil((P * N * I)/100)+P

def Calculate_EMI(P,N,I)	:
	return math.ceil((((P*N*I)/100)+P)/(N*12))

def Ledger(Input):

	global Loan_List

	Input_Command = Input.split()

	if len(Input_Command) == 6:

	

		Loan,Bank_Name,Borrower_Name,Principal,No_Of_Years,Interest_Rate  =  Input_Command

		Loan_List.append([

			Loan,

			Bank_Name,

			Borrower_Name,

			int(Principal),

			int(No_Of_Years),

			int(Interest_Rate),

			Calculate_Interest(int(Principal),int(No_Of_Years),int(Interest_Rate)),

			0,

			Calculate_EMI(int(Principal),int(No_Of_Years),int(Interest_Rate)),

			int(No_Of_Years)*12,

			0,

			math.ceil(Calculate_Interest(int(Principal),int(No_Of_Years),int(Interest_Rate)) % Calculate_EMI(int(Principal),int(No_Of_Years),int(Interest_Rate)))


			])


	# Payment

	elif len(Input_Command) == 5:

		
		# print(Input_Command)

		for Iter_Var in Loan_List:

			

			if Input_Command[1] in Iter_Var:


				Iter_Var[7] = int(Input_Command[3]) + (Iter_Var[8] * int(Input_Command[4]))
				

				Iter_Var[10] = int(Input_Command[4])

	# Balance

	elif len(Input_Command) == 4:

		for Iter_Var in Loan_List:

			if Input_Command[1] in Iter_Var:

				if(int(Input_Command[3]) < Iter_Var[10]):

					print(

						Iter_Var[1],

						Iter_Var[2],

						int(Input_Command[3]) * Iter_Var[8],

						math.ceil((Iter_Var[6] - int(Input_Command[3]) * Iter_Var[8]) / Iter_Var[8])


						)

				elif(int(Input_Command[3]) > Iter_Var[10]):

					print(

						Iter_Var[1],


						Iter_Var[2],


						Iter_Var[7] + ((int(Input_Command[3]) - Iter_Var[10]) * Iter_Var[8]),


						math.ceil((Iter_Var[6] - (Iter_Var[7] + ((int(Input_Command[3]) - Iter_Var[10]) * Iter_Var[8]))) / Iter_Var[8])

						)

				elif(int(Input_Command[3])  == Iter_Var[10]):

					print(

						Iter_Var[1],


						Iter_Var[2],

						Iter_Var[7],

						math.ceil((Iter_Var[6] - (Iter_Var[7] + ((int(Input_Command[3]) - Iter_Var[10]) * Iter_Var[8]))) / Iter_Var[8])

						)
IO = ["LOAN IDIDI Dale 10000 5 4","LOAN MBI Harry 2000 2 2","BALANCE IDIDI Dale 5","BALANCE IDIDI Dale 40","BALANCE MBI Harry 12","BALANCE MBI Harry 0"]

IO2 =["LOAN IDIDI Dale 5000 1 6","LOAN MBI Harry 10000 3 7","LOAN UON Shelly 15000 2 9","PAYMENT IDIDI Dale 1000 5","PAYMENT MBI Harry 5000 10",
		
		"PAYMENT UON Shelly 7000 12","BALANCE IDIDI Dale 3","BALANCE IDIDI Dale 6","BALANCE UON Shelly 12","BALANCE MBI Harry 12"]

IO3 = ["LOAN IDIDI Dale 4000 3 4","LOAN MBI Dale 10000 3 7","PAYMENT MBI Dale 2000 0","BALANCE IDIDI Dale 3","BALANCE IDIDI Dale 0","BALANCE MBI Dale 0",
		"BALANCE IDIDI Dale 12","BALANCE MBI Dale 4","BALANCE MBI Dale 30"]		


IO4 = ["LOAN MBI Dale 5000 4 5","PAYMENT MBI Dale 1000 0","BALANCE MBI Dale 0","BALANCE MBI Dale 18"]



if __name__ == '__main__':

	def main():

	input_File = sys.argv[1]

	IO = [line.strip() for line in open(input_File,'r')]

	print(IO,"vi")

	for Iter in IO[0]:

		print(Ledger(Iter))

	


# for Iter in IO:

# 	Ledger(Iter)
