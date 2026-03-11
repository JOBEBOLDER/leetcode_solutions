'''
第二轮: 亚洲女生，很chill，地里有的 餐厅排队。设计一个waitlist的structure，满足三种功能，
join waitlist, leave waitlist, serve customers with certain size. 
这题可能每个面试官都会有一些不一样，
serve customer这个部分我只需要检查有没有party size和table size完全一样的party就行了。
 join 和 leave可能要考虑一下有没有重复加waitlist或者重复leave的可能  ✅

 因为它用 list 做底层：
	•	查找/删除都是 O(n)（需要遍历）
'''



class RestaurantWaitlist:
    def __init__(self):
        self.waitlist = []
        #里面存的是很多个 (party_name, party_size) 的 tuple：
        #("Smith", 4)
        #("Johnson", 2)

    def join_waitlist(self, party_name, party_size):
        """
        Add a party (name and size) to the waitlist if not already present.
        """
        for name, size in self.waitlist:
            if name == party_name:
                print(f"Party with name '{party_name}' is already on the waitlist.")
                return
        self.waitlist.append((party_name, party_size))
        print(f"Added party '{party_name}' of size {party_size} to the waitlist.")

    def leave_waitlist(self, party_name):
        """
        Remove a party by name from the waitlist if it exists.
        """
        for entry in self.waitlist:
            if entry[0] == party_name:
                self.waitlist.remove(entry)
                print(f"Removed party '{party_name}' from the waitlist.")
                return
        print(f"Party with name '{party_name}' is not on the waitlist.")

    def serve_customer(self, table_size):
        """
        Serve a party from the waitlist that matches the table size exactly.
        """
        for entry in self.waitlist:
            party_name, party_size = entry
            if party_size == table_size:
                self.waitlist.remove(entry)
                print(f"Served party '{party_name}' of size {party_size}.")
                return
        print(f"No party of size {table_size} is currently waiting.")

    def show_waitlist(self):
        """
        Display the current waitlist for debugging or monitoring purposes.
        """
        if not self.waitlist:
            print("The waitlist is currently empty.")
        else:
            print("Current waitlist:")
            for name, size in self.waitlist:
                print(f"  - Party '{name}' of size {size}")

# Example Usage
if __name__ == "__main__":
    waitlist = RestaurantWaitlist()
    waitlist.join_waitlist("Smith", 4)
    waitlist.join_waitlist("Johnson", 2)
    waitlist.join_waitlist("Smith", 4)  # Duplicate join attempt
    waitlist.serve_customer(4)  # Serve a party of size 4
    waitlist.serve_customer(6)  # No matching party
    waitlist.leave_waitlist("Johnson")  # Leave waitlist
    waitlist.leave_waitlist("Brown")  # Nonexistent party
    waitlist.show_waitlist()