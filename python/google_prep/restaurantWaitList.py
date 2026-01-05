class RestauratnList:
    def __init__(self):
        #use queue:
        self.waitlist = []
        


    def join_waitlist(self,party_name, party_size):
        for name,size in self.waitlist:
            if name == party_name:
                print(f"Party name already in the waitingin list")
                return 
            self.waitlist.append((party_name,party_size))
            print(f"added party '{party_name}' of size {party_size} on the waitlist")


    def leave_waitList(self,party_name):
        for entry in self.waitlist:
            if entry[0] == party_name:
                self.join_waitlist.remove(entry)
                print(f"{party_name} already removed on the waitting list")
        print(f"can not find {party_name} on the waiting list")

    def serve_customer(self,table_size):
        for party_name,party_size in self.waitlist:
            if party_size == table_size:
                self.waitlist.remove(entry)
                print(f"{party_name} alreay served ")
        print(f"can not find the party {party_name}")



    def show_waitlist(self):
        "display the current waitlist status"
        if not self.waitlist:
            print("the waitlis tis empty")
        else:
            print("current waitting list:")
            for name,size in self.waitlist:
                print(f"-party {name} of size {size}")


        