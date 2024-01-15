def main():
    print("==========================================")
    print(":Escribe EOF y dale al enter para guardar:")
    print("================== EDIT ==================")
    with open("./C-drive/" + args[1], "w") as f:
        while True:
            inp = input()
            if inp == "EOF":
                break
            f.write(inp + "\n")
main()