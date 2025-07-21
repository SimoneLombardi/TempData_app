
def check_file_name(filename):
    print(f"Checking file name: {filename}")
    
    if filename.endswith('.csv'):
        print("File name is valid.")
        return True
    else:
        print("File name is invalid. It should end with '.csv'.")
        return False