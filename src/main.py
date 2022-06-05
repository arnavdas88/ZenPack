from ZenPack import Manager

if __name__ == "__main__":
    pass

manager = Manager("./pack/")

for name, pack in manager.stack.items():
    print(name, pack)
    pack.routine()