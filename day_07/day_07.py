sample = "sample_input.txt"
real = "real_input.txt"

from dataclasses import dataclass, field

MAX_SIZE = 30000000

@dataclass()
class File():
    name: str
    size: int

@dataclass()
class Directory():
    name: str
    parrent: File
    size: int = 0
    files: list[File] = field(default_factory=list)
    dirs: list[File] = field(default_factory=list)


class FileSystem():
    def __init__(self):
        self.root = Directory("root", None)
        self.current_directory = self.root

    def cd(self, where: str):
        if where == "/":
            self.current_directory = self.root
        elif where == "..":
            self.current_directory = self.current_directory.parrent
        else:
            for dir in self.current_directory.dirs:
                if where == dir.name:
                    self.current_directory = dir
                    break

            else:
                print(f"Directory {where} does not exist!")

    def ls(self, files: list[tuple]):
        for file in files:
            name = file[1]
            try:
                size = int(file[0])
                self.current_directory.files.append(File(name, size))
                self.current_directory.size += size

                current_parrent = self.current_directory.parrent
                while current_parrent != None:
                    current_parrent.size += size
                    current_parrent = current_parrent.parrent

            except:
                self.current_directory.dirs.append(Directory(name, self.current_directory))




class CommandParser:
    def __init__(self, filename):
        self.system = FileSystem()
        self.size_to_delete = 0
        self.dirs_to_delete_list = []
        with open(filename, 'r') as file:
            self.commands = file.readlines()

        current_line = 0
        commands_len = len(self.commands)

        while current_line < commands_len:
            args = self.commands[current_line].split()

            if args[0] == "$":

                if args[1] == "cd":
                    self.system.cd(args[2])
                    current_line += 1

                elif args[1] == "ls":
                    ls_args = []
                    current_line += 1
                    while (current_line < commands_len) and (self.commands[current_line].split()[0] != "$"):
                        ls_args.append(tuple(self.commands[current_line].split()))
                        current_line += 1

                    self.system.ls(ls_args)


    def dirs_to_delete(self, current_root):
        for dir in current_root.dirs:
            if dir.size >= self.get_missing_space():
                self.dirs_to_delete_list.append((dir.name, dir.size))

            self.dirs_to_delete(dir)

    def get_missing_space(self):
        TOTAL_CAPACITY = 70000000
        REQUIRED_SPACE = 30000000

        current_free_space = TOTAL_CAPACITY - self.system.root.size
        missing_free_space = REQUIRED_SPACE - current_free_space
        return missing_free_space


    def get_size_to_delete(self):
        to_del = list(set(self.dirs_to_delete_list))
        to_del.sort(key=lambda a: a[1])
        print(to_del[0], to_del[-1])


c = CommandParser(real)
c.dirs_to_delete(c.system.root)
c.get_size_to_delete()



