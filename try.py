import pickle

with open('data.pickle', 'rb') as f:
    data_dict = pickle.load(f)

print(data_dict.keys())
