import argparse

def main():
    parser = argparse.ArgumentParser(
                    prog='ConsoleDino',
                    description='The mini dinosaur escaped from Chrome to console!',
                    epilog='--dino-dino-dino-dino-dino-dino--')
    parser.add_argument("-c", "--compiler", type=str, default="gcc")
    # TODO
    args = parser.parse_args()
    # TODO

if __name__ == "__main__":
    main()