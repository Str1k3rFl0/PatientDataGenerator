import pandas as pd
import random
import time

class Patient:
    file_name = 'patient_data.csv'
    first_names_file = 'first_names.txt'
    last_names_file = 'last_names.txt'
    ages_file = 'ages.txt'
    diseases_file = 'diseases.txt'

    # Constructor
    def __init__(self):
        pass 

    # ADD PATIENTS DATA TO CSV FILE
    def add_patient_data(self):
        with open(self.first_names_file, 'r') as file:
            first_names = [line.strip() for line in file]

        with open(self.last_names_file, 'r') as file:
            last_names = [line.strip() for line in file]
        
        with open(self.ages_file, 'r') as file:
            ages = [line.strip() for line in file]

        with open(self.diseases_file, 'r') as file:
            diseases = [line.strip() for line in file]

        try:
            num_patients = int(input('How many patients you want to introduce? :: '))
            if num_patients <= 0:
                print('Negative number! Try a positive number!')
        except ValueError:
            print('Wrong type! Type a number instead')
        
        new_data = []
        for i in range(num_patients):
            first_name = random.choice(first_names)
            last_name = random.choice(last_names)
            age = random.choice(ages)
            disease = random.choice(diseases)
            print(f'Patient {i+1} added with: Full Name: {first_name} {last_name}, Age: {age}, Disease: {disease}')

            new_data.append({
                'First Name': first_name,
                'Last Name': last_name,
                'Age': age,
                'Disease': disease
            })

            # JUST FOR TEST ( you cant delete these 3 rows below)
            wait_time = random.uniform(1, 3)
            print(f'Waiting for {wait_time} seconds before generating the next patient')
            time.sleep(wait_time)

        new_df = pd.DataFrame(new_data)
        try:
            existing_df = pd.read_csv(self.file_name)
            updated_df = pd.concat([existing_df, new_df], ignore_index = True)
        except FileNotFoundError:
            updated_df = new_df

        updated_df.to_csv(self.file_name, index = False)
        print(f'\n{num_patients} patient(s) added successfully to {self.file_name}.')    

    
    # MAIN MENU
    def menu(self):
        while True:
            print('\n----- MAIN MENU -----\n')
            print('[1]. ADD PATIENTS')
            print('[2]. EXIT')
            option = input('Choose an option: ')

            match (option):
                case "1": self.add_patient_data()
                case "2": exit(0)
                case _: print('Invalid Option! Try again!')


patient = Patient()
patient.menu()