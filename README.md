**MAKO-DataFilter** is a Python script or program designed to process and filter data from CSV files based on specific criteria, typically for email or status data. The tool provides a user-friendly command-line interface that allows users to define input data, specify filter criteria, and generate a customized output. Here’s a breakdown of its key features and functionality:

### **Features of MAKO-DataFilter:**

1. **Welcome Banner:**
   - Upon launching, the script displays a stylized welcome banner using the `pyfiglet` library to create a visually appealing text-based header, which reads **"M~AKO DataFilter"**.

2. **File Input:**
   - Users can specify the path of the CSV file they wish to filter, or they can accept the default file path (`email_list.csv`).

3. **Column and Value Filtering:**
   - The script prompts the user to enter:
     - A **column name** to filter on (e.g., `dsnStatus`).
     - A **value** to match in that column (e.g., `"2.0.0 (success)"`).
   - The program then filters the data, keeping only rows where the value in the specified column matches the given value.

4. **Dynamic Column Selection:**
   - Users are prompted to define which columns they want to extract and view (default is `rcpt` and `dsnStatus`).
   - The user can enter additional column names or change the default values to adjust the output based on their needs.

5. **Data Processing:**
   - The filtered data is processed and output into a new CSV file (`my_filtred_data.csv`), allowing users to easily download or share the results.

6. **Data Overview:**
   - The script also outputs a count of the total records, showing how many entries matched the filter criteria.

7. **Customizable Settings:**
   - Users have the flexibility to define custom file paths, column names, and filter values, which makes the script adaptable to a variety of use cases, from processing email lists to filtering status codes.

8. **Generated Output:**
   - The final output is a CSV file containing only the rows with the specified value, with columns renamed for clarity (e.g., `rcpt` becomes `email` and `dsnStatus` becomes `status`).

### **Use Case:**
- **Email List Filtering:** If you have a large list of email records with different statuses (e.g., delivery successes or failures), you can use this tool to extract only the records that meet specific criteria (e.g., delivery success).
- **Data Processing for Reports:** It can be used in scenarios where you need to clean up or process raw data, apply filters, and generate reports.

### **How It Works:**
1. The user runs the script and is greeted with the **"M~AKO DataFilter"** banner.
2. The user specifies the path to the CSV file to process.
3. The script asks for column names and values to filter the data.
4. The data is filtered and cleaned.
5. The output is saved to a new CSV file, ready for analysis or sharing.

### **Technologies Used:**
- **Python:** The script is written in Python, making it easy to run in any environment where Python is available.
- **Pandas:** The script utilizes `pandas` for data manipulation and filtering.
- **PyFiglet:** Used to create a nice text-based banner for the user interface.
- **CSV:** The input and output are handled using the CSV format for compatibility with spreadsheet software.

### **Summary:**
MAKO-DataFilter is a Python-based data processing tool that provides an easy way to filter, clean, and process large datasets, particularly in CSV format. It’s ideal for tasks such as filtering email lists or any scenario where data needs to be filtered based on specific criteria. With its customizable settings, it can be adapted for different use cases and is especially useful for quick, command-line-based data manipulation.
