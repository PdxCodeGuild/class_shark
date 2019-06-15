import again

class Avg_Num():

    l_Nums = []


    def add_To(self, usr_num):
        self.l_Nums.append(usr_num)

    def check(self, is_num):
        if is_num == 'done':
            return False
        elif int(is_num):
            return True
        else:
            print('incorrect input')
            main()
            return False

    def total(self):
        total = 0
        for num in self.l_Nums:
            total += num
        return total / len(self.l_Nums)

    def clear(self):
        self.l_Nums = []
        print(self.l_Nums)

def main():
    while True:
        new_Avg.clear()
        while True:
            usr_int = input('Please enter an int, or \'done\':')
            if new_Avg.check(usr_int):
                new_Avg.add_To(int(usr_int))
            else:
                print(f'Your average for your numbers is {new_Avg.total()}')
                break
        if again.again("Would you like to go again?"):
            break


new_Avg = Avg_Num()
print(f'Welcome to Average Numbers!')
main()
