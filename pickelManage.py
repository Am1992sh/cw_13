import pickle


def load():
    try:
        with open("user.pkl", "x") as l:
            return {}
    except FileExistsError:
        with open("user.pkl", "rb") as l:
            return pickle.load(l)


def save(data):
    with open("user.pkl", "wb") as w:
        pickle.dump(data, w)
