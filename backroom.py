import os
from glob import glob
import nbformat as nbf
from nbformat import read, write
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell

def analyze_notebooks_for_readability():


    files = glob("*.ipynb")
    success_files = []
    failure_files = []

    for file in files:
        with open(file, 'r') as f:
            notebook = read(f, nbf.NO_CONVERT)
        cells = [x for x in notebook['cells'] if x['cell_type'] == 'code']
        if len(cells) <= 1 or (len(cells) == 2 and cells[-1].source.strip() == ''):
            success_files.append(file)
        else:
            failure_files.append(file)
    action_needed_message = "Looks perfect." if len(failure_files) == 0 else """Action Needed\n==============\nFix the failures by combining the cells together.  The shortcut to do this is esc->shift+m.""" 
    failure_files_title = "" if len(failure_files) == 0 else """\n\nFailures\n========\n"""
    success_files = "\n".join(success_files)
    failure_files = "\n".join(failure_files)
    message = f"""Successes\n==========\n{success_files}{failure_files_title}{failure_files}\n\n{action_needed_message}
"""
    return message

def create_notebook(filename, code):
    if os.path.exists(filename):
        return "File already exists"
    notebook = new_notebook()
    cell = new_code_cell(code)
    notebook['cells'].append(cell)
    cell = new_code_cell("")
    notebook['cells'].append(cell)
    nbf.write(notebook, filename)
    return "Notebook created successfully"
    
def create_etl_notebook():
    code = '''# Query a database or read a CSV file here...
    # Minimize Memory Requirement: Thin the data using the following: filtering, aggregation, or converting strings to other datatypes
    # Faster Speed: Use the database's index or partition to speed up extraction
    # CSV/Database: Use Pandas 99% of the time.  Parquet: Use Pandas 80% of the time and Spark 20% of the time.



# Minor cleanup changes in Python




# Save to a CSV file

'''
    return create_notebook(filename='1.1_etl.ipynb', code=code)

def create_split_notebook():
    code = '''# Read in CSV



# Have a key column, De-dupe rows ensuring one row per key, and finalize clean up



# Split the data into train1-5, validation1-5, and test (11 datasets)



'''
    return create_notebook(filename='1.2_split_data.ipynb', code=code)

def create_feature_engineering_notebook():
    for i in range(1, 101):
        filename = f"2.{str(i).zfill(2)}_feature_engineering.ipynb"
        if os.path.exists(filename):
            pass
        else:
            break
    if i == 100:
        return "Files already exist"
    code = '''for cv_split in range(1,6):
    # Read in the train_{cv_split}, validation_{cv_split}, and test
    
    # Create the new features
    
    break # Remove this break when this is tested
    
    # Select the key column and all new features
    
    # Save to a new CV file called 2.1_feature_engineering_cv_{cv_split}
    # Append the validation and test set to this same CSV file
    
'''
    return create_notebook(filename=filename, code=code)
   
def create_model_notebook():
    code = '''evalution_results = []
for cv_split in range(1, 6):
    # Read in the train_{cv_split}, validation_{cv_split}, and test
    
    for feature_df in range(1, 20):
        # Read in the features file for this cv_split
        # Join it to the existing dataframes
    
    # Run the fit and predict
    
    # Compute the evaluation result (single number metric)
    
    # append to evalution_results
    
# Check the evaluation results of all 5 results in evalution_results
    
    
'''
    return create_notebook(filename='3.1_model.ipynb', code=code)
   



