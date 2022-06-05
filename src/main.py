from ZenPack import Manager

if __name__ == "__main__":
    pass

manager = Manager("/Users/andrew/Desktop/Projects/ZensorPack/pack/")

for name, pack in manager.stack.items():
    print(name, pack)