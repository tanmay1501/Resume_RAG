from datasets import load_dataset




def load_dataset():
    
    ds = load_dataset("cnamuangtoun/resume-job-description-fit")

#save the train dataset to a file as a csv
    ds["train"].to_csv("resume-job-description-fit-train.csv")
    return "dataset loaded and saved to resume-job-description-fit-train.csv"


