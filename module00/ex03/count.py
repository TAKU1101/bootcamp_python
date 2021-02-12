from re import findall

def text_analyzer(*args):
    """Count the number of letters, and the number of uppercase,
lowercase, punctuation, and spaces.
Prompts for input if there is no argument.

Parameters
----------
args:
    target string

Return
------
None"""
    try:
        argc = len(args)
        if argc == 0:
            print(">> ", end="")
            txt = input()
        elif argc == 1:
            txt = args[0]
        else:
            raise
        print("The text contains {} characters:".format(len(txt)))
        print("- {} upper letters".format(len(findall("[A-Z]", txt))))
        print("- {} lower letters".format(len(findall("[a-z]", txt))))
        print("- {} punctuation marks".format(len(findall("[.,'-]", txt))))
        print("- {} spaces".format(len(findall(" ", txt))))
    except:
        print("ERROR")

if __name__ == '__main__':
    text_analyzer("""The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!""")

    print("")

    text_analyzer("""Python is an interpreted, high-level, 
general-purpose programming language. Created by Guido van 
Rossum and first released in 1991, Python's design philosophy 
emphasizes code readability with its notable use of significant 
whitespace.""")

    print("")

    text_analyzer("""Python 2.0, released 2000, introduced 
features like List comprehensions and a garbage collection 
system capable of collecting reference cycles.""")

    print("")

    text_analyzer("python", "2.0")

    print(text_analyzer.__doc__)
