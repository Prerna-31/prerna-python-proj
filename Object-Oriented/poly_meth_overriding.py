class identity_bef_mrg:
    gb_var = 10
    def __init__(iden, name):
        iden.name = name

    def show_id(iden):
        full_nm = iden.name + ' Singh'
        print('Before marriage , My identity is {}'.format(full_nm.upper()))

class identity_aft_mrg(identity_bef_mrg):
    def __init__(iden, name):
        super().__init__(name)
       ## iden.name = name

    def show_id(iden):            ##Method overridden
        super().show_id()
        full_nm = iden.name + ' Manjrekar'
        print('After marriage , My identity will be {}'.format(full_nm.upper()))


nm = input('Enter your first name: ')
o_id = identity_aft_mrg(nm)
o_id.show_id()