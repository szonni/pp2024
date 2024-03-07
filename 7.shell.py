import os

def main():
    while True:
        command = input("$ ")
        if command.lower() == "exit":
            break
        else:
            try:
                args = command.split()
                # Output Redirection ( > )
                if ">" in args:
                    index = args.index(">")
                    cmd = args[:index]
                    filename = args[index + 1]
                    with open(filename, "w") as out_file:
                        os.system(" ".join(cmd) + " > " + filename)
                # Input redirection ( < )
                elif "<" in args:
                    index = args.index("<")
                    cmd = args[:index]
                    filename = args[index + 1]
                    with open(filename, "r") as in_file:
                        os.system(" ".join(cmd) + " < " + filename)
                else:
                    os.system(command)
            except Exception as e:
                print("Errror: ", e)


if __name__ == "__main__":
    main()