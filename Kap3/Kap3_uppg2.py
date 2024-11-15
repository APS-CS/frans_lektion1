with open("log.txt", "r") as listfile:
            content = listfile.readlines()
            error_text = "Failed login attempt"
            for line in content:
                    if error_text in line:
                        print(line.strip())
                        