class Evaluator:
    def zip_evaluate(coefs, words):
        if len(coefs) == len(words):
            s_num = 0
            for coef, word in zip(coefs, words):
                s_num += coef * len(word)
            return s_num
        else:
            return -1

    def enumerate_evaluate(coefs, words):
        if len(coefs) == len(words):
            s_num = 0
            for i, word in enumerate(coefs, words):
                s_num += coefs[i] * len(word)
            return s_num
        else:
            return -1
