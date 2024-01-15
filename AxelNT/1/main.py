import os
def shell():
    while True:
        inp = input("C:\> ")
        if inp == "":
            continue
        args = inp.split()
        path = f"./C-drive/commands/{args[0]}.py"
        if not os.path.exists(path):
            print("Comando Desconocido.")
        with open(path, "r") as f:
            content = f.read()
        exec(content, {"args": args})
if __name__ == "__main__":
    shell()