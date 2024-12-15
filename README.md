# Patient Management System

This project is a simple Patient Management System implemented in Python using the pandas library. It allows users to manage patient records by adding patient data and viewing stored information. The data is saved in a CSV file for easy persistence and manipulation.

## Features

- **Add Patient Records**: Randomly generates and stores patient information (first name, last name, age, and disease) into a CSV file.
- **View Patient Records**: Displays the stored patient data from the CSV file.
- **Persistence**: All patient data is stored in a file named `patient_data.csv` for future access.
- **Realistic Data Simulation**: Randomized waiting time between entries simulates real-world scenarios (optional).

## Prerequisites

To run this project, you need:

- Python 3.8 or higher
- Required Python libraries: `pandas`

## File Structure

```
.
├── patient_data.csv         # CSV file for storing patient data (generated automatically)
├── first_names.txt          # Text file containing a list of first names
├── last_names.txt           # Text file containing a list of last names
├── ages.txt                 # Text file containing a list of ages
├── diseases.txt             # Text file containing a list of diseases
├── main.py                  # Main Python file containing the program logic
```

## How to Run

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/patient-management-system.git
   ```

2. Navigate to the project directory:

   ```bash
   cd patient-management-system
   ```

3. Install the required Python libraries:

   ```bash
   pip install pandas
   ```

4. Ensure the following files exist in the project directory and contain appropriate data:

   - `first_names.txt`
   - `last_names.txt`
   - `ages.txt`
   - `diseases.txt`

5. Run the program:

   ```bash
   python main.py
   ```

## Usage

1. **Main Menu**:

   - `[1] Add Patients`: Randomly generates patient data and appends it to the CSV file.
   - `[2] View Patients`: Displays the contents of the `patient_data.csv` file.
   - `[3] Exit`: Exits the program.

2. Follow the on-screen prompts to interact with the application.

## Customization

- Modify the `.txt` files to include your own datasets for first names, last names, ages, and diseases.
- Update the `file_name` attribute in the `Patient` class to change the CSV file's name.

## Example Output

### Adding Patients

```
How many patients you want to introduce? :: 2
Patient 1: John Smith, Age: 45, Disease: Flu
Waiting for 2.15 seconds...
Patient 2: Alice Johnson, Age: 30, Disease: Cold
2 patient(s) added successfully to patient_data.csv.
```

### Viewing Patients

```
  First Name  Last Name Age Disease
0       John      Smith  45     Flu
1      Alice    Johnson  30    Cold
```

## Contribution

Feel free to contribute to this project by:

- Adding new features
- Optimizing the code
- Reporting issues or bugs

To contribute:

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Author

[Your Name](https://github.com/your-username)

## Acknowledgements

Special thanks to the Python community and pandas documentation for their guidance in building this project.

