class chuoi:
    def __init__(self):
        self.a=""

    def get_str(self):
        self.a=input('Nhap chuoi: ')

    def print_str(self):
        print(self.a.upper())
if __name__=="__main__":
    chuoi=chuoi()
    chuoi.get_str()
    chuoi.print_str()
