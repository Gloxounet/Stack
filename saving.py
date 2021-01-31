import pickle

save_file = "save.pkl"

def save(obj) :
    with open(save_file, "wb") as f:
        pickle.dump(obj, f)

def get_save() :
    with open(save_file, "rb") as f:
        return pickle.load(f)
        