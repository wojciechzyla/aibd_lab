## Content
All files are divided into four main folders. 

Original_Data folder contains original data file earthquake_data.csv and subfolder Metadata with Metadata_Guide.txt. Last one contains information about original data file.

Documents folder contains Data_Appendix.txt with information about preprocessed data files. You can also find images in png format with bar charts presenting answers frequency from preprocessed data files.

Command_Files folder contains two jupyter notebooks. First one, preprocessing.ipynb, is used to preprocess data from earthquake_data.csv while construct_data_appendix.ipynb is used to create files in Documents folder.

Analysis_Data folder contains files which are the result of preprocessing.ipynb and are later used by construct_data_appendix.ipynb.

## Replicating the study
In this study I used Python3, Pandas and Matplotlib. Python code was written inside jupyter notebooks. 

To replicate the results, one must copy empty Analysis_Data folder, Command_Files folder with its content, Original_Data folder only with earthquake_data.csv and empty Documents folder. All those folders should be on the same level in directory. Command_Files folder should be set as working directory.

First file to execute is preprocessing.ipynb. It uses earthquake_data.csv from Original_Data folder and creates cleaned_data.csv and sub_table.csv in Analysis_Data folder. Then construct_data_appendix.ipynb should be executed. It uses earthquake_data.csv, cleaned_data.csv and sub_table.csv and then creates Data_Appendix.txt, cleaned_data_freq.png and sub_table_freq.png.