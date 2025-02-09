#import the  the data_loader.py file
import data_loader
from langchain.document_loaders import TextLoader
#if statement for if dataset is already loaded
if data_loader.load_dataset() == "dataset loaded and saved to resume-job-description-fit-train.csv":
    print("Dataset already loaded")
else:
    data_loader.load_dataset()


loader = TextLoader("data/test_data.txt")  # Load a document
documents = loader.load()

