from parser import Parser
import argparse


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument("input_file", help="Path to input file")
    args = argparser.parse_args()

    path = args.input_file
    parser = Parser(path)

    text = parser.read()

    print("=== RAW INPUT START ===")
    print(text)
    print("=== RAW INPUT END ===")


if __name__ == "__main__":
    main()
