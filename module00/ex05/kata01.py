if __name__ == "__main__":
    languges = {
        'Python': 'Guido van Rossum',
        'Ruby': 'Yukihiro Matsumoto',
        'PHP': 'Rasmus Lerdorf',
    }

    for key, val in languges.items():
        print("{} was created by {}".format(key, val))