import test
import program

if __name__ == "__main__":
    for filename in 'abcdef':
        test.readAndTestOne(filename + '.txt')
    # test.readAndTestOne('a.txt')