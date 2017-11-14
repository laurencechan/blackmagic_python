# coding=utf-8

covalent_radius = {"C": 77, "H": 32, "O": 73, "N": 75}


class PolyStructAnalysis():
    def __init__(self):
        # self.struct1 = strct1
        # self.struct2 = struct2
        self.dt_dict = {}
        pass

    def str_int(self, c):
        c[2] = c[2][:-1]
        return [float(i) for i in c]

    def atom_distance(self, c1, c2):
        import math
        c1 = self.str_int(c1)
        c2 = self.str_int(c2)
        return math.sqrt(((c1[0] - c2[0]) ** 2) + ((c1[1] - c2[1]) ** 2) + ((c1[2] - c2[2]) ** 2))

    def key_distance(self, a1, a2):
        return ((covalent_radius[a1] + covalent_radius[a2]) / 100) * 1.2

    def data_container(self, dt_key, dt_value):
        for i in range(32):
            if self.dt_dict.has_key(dt_key + "-" + str(i) or dt_key[::-1] + "-" + str(i)):
                continue
            self.dt_dict[dt_key + "-" + str(i)] = dt_value
            break

    def handle_struct(self, struct):
        with open(struct, "r") as f:
            all_atom = f.readlines()
            k = 0
            for i in range(2, len(all_atom) - 1):
                for j in range(i + 1, len(all_atom)):
                    a = all_atom[i].split(" ")
                    b = all_atom[j].split(" ")
                    atom_dis = self.atom_distance(a[1:], b[1:])
                    key_dis = self.key_distance(a[0], b[0])
                    # if atom_dis < key_dis:
                    if a[0] < b[0]:
                        self.data_container(a[0] + "-" + b[0], atom_dis)
                    else:
                        self.data_container(b[0] + "-" + a[0], atom_dis)
            a = self.dt_dict
            return {k: a[k] for k in sorted(a)}


if __name__ == '__main__':
    tt = PolyStructAnalysis()
    ss = PolyStructAnalysis()
    print tt.handle_struct("aaa.xyz")
    print ss.handle_struct("bbb.xyz")
    pass
