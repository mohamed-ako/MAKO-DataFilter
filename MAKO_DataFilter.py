import pandas as pd
import pyfiglet


# Define the welcome value
welcome_value = "M~AKO DataFilter"

# Generate and print a stylized banner
banner = pyfiglet.figlet_format(welcome_value)
print(banner)

data_file_path = "email_list.csv"
input_data_file_path=input("\n enter the CSV DATA FILE PATH (in default = email_list.csv)) : ")
if input_data_file_path != "":
    data_file_path = input_data_file_path

try:
    data = pd.read_csv(data_file_path)
except FileNotFoundError:
    print(f"Error: File '{data_file_path}' not found.")
    exit()

print(f"\n data COLUMNS : {data.columns.to_list()}")
column_finder = "dsnStatus"
input_column_finder=input("\n enter the COLUMN (in default = dsnStatus)) : ")
if input_column_finder != "":
    value_finder = input_column_finder

value_finder = "2.0.0 (success)"
input_finder=input("\n enter the VALUE (in default = 2.0.0 (success))) : ")
if input_finder != "":
    value_finder = input_finder

my_column = ["rcpt","dsnStatus"]
input_my_column=input("\n enter the COLUMN (in default = rcpt,dsnStatus)) : ")
while input_my_column != "":
    my_column=[]
    my_column.append(input_my_column.strip())
    input_my_column = input(f"\nYou entered {my_column}. Do you want to add another column? (press Enter to stop): ").strip()

try:
    my_email_list = data.loc[data[column_finder] == value_finder, my_column]
    if(my_column[0] == "rcpt"):
        my_email_list = my_email_list.rename(columns={"rcpt": "email"})

    my_email_list.to_csv("./my_filtred_data.csv")

    all_email_list = data.value_counts(column_finder)
    print(all_email_list.to_csv())
    print("\n data Recevid on <./my_filtred_data.csv> length : ",len(data))

except KeyError:
    print("Error: Column not found.")
    exit()
