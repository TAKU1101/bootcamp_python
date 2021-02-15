import pprint


class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if not hasattr(self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1
    
    def transfer(self, amount):
        self.value += amount

    def get_name(self):
        return self.__dict__['name']

    def get_value(self):
        return self.__dict__['value']

    def get_id(self):
        return self.__dict__['id']

    def print_data(self):
        print(self.__dict__)


class Bank(object):
    """The bank"""
    def __init__(self):
        self.account = []

    def add(self, account):
        self.account.append(account)

    def get_account_by_name(self, account):
        for data in self.account:
            if isinstance(account, str) and data.get_name() == account:
                return data
            elif isinstance(account, int) and data.get_id() == account:
                return data
        return None

    def transfer(self, origin, dest, amount):
        """
            @origin:  int(id) or str(name) of the first account
            @dest:    int(id) or str(name) of the destination account
            @amount:  float(amount) amount to transfer
            @return         True if success, False if an error occured
        """
        origin_data = self.get_account_by_name(origin)
        if origin_data is None:
            return False
        dest_data = self.get_account_by_name(dest)
        if dest_data is None:
            return False
        if (dest_data.get_value() - amount < 0):
            return False
        origin_data.transfer(amount)
        dest_data.transfer(amount * -1)
        return True

    def fix_account(self, account):
        """
            fix the corrupted account
            @account: int(id) or str(name) of the account
            @return         True if success, False if an error occured
        """
        data = self.get_account_by_name(account)
        if data is None:
            return False

    def print_account(self):
        for data in self.account:
            data.print_data()
