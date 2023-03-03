# %%
# Mount google drive
from google.colab import drive
drive.mount('/content/drive')

# %%
# Read CSV files using pandas
dataset = pd.read_csv('file path')

# %%
# read text file
with open("file_path", "r") as file1:
    FileContent = file1.read()
    print(FileContent)

# %%
# read json file
with open("file_path", "r") as fin:
    for json_line in fin:
      json_dict = json.loads(json_line.strip())


