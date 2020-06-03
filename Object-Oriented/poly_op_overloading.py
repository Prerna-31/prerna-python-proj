class student:
    def __init__(self,m_phy,m_chem,m_math):
        self.m_phy = m_phy
        self.m_chem = m_chem
        self.m_math = m_math

    def display_marks(self):
        print('Physics:   ',self.m_phy)
        print('Chemistry: ',self.m_chem)
        print('Maths:     ', self.m_math)

    def __gt__(self, other):
        st1_marks_tot = self.m_phy + self.m_chem + self.m_math
        st2_marks_tot = other.m_phy + other.m_chem + other.m_math

        if st1_marks_tot > st2_marks_tot:
            return True
        else:
            return False

    def __add__(self, other):
        m_phy_tot = self.m_phy + other.m_phy
        m_chem_tot = self.m_chem + other.m_chem
        m_math_tot = self.m_math + other.m_math
        st_m_tot = student(m_phy_tot,m_chem_tot,m_math_tot)

        return st_m_tot

    def __truediv__(self, tot_st):
        m_phy_avg = self.m_phy / tot_st
        m_chem_avg = self.m_chem / tot_st
        m_math_avg = self.m_math / tot_st

        st_m_avg = student(m_phy_avg, m_chem_avg, m_math_avg)

        return st_m_avg

    def __str__(self):
        return '{} {} {}'.format(self.m_phy,self.m_chem,self.m_math)

#print('Enter student marks: ')
#m_phy = int(input('Physics:    '))
#m_chem = int(input('Chemistry: '))
#m_math = int(input('Maths:     '))
#st1 = student(m_phy,m_chem,m_math)
st1 = student(72,81,94)
print('Marks scored by student 1: ')
st1.display_marks()
print()
print('Marks scored by student 2: ')
st2 = student(67,98,99)
st2.display_marks()

if st1 > st2:
    print('Student 1 scored maximum in school.')
else:
    print('Student 2 scored maximum in school.')

print()

print('Sum of the marks scored by 2 students in physics, chemistry, maths: ')
##st_tot  = student((st1.m_phy + st2.m_phy),(st1.m_chem + st2.m_chem),(st1.m_math + st2.m_math))
##st_tot.display_marks()
st_tot = st1 + st2
st_tot.display_marks()
print()
print('Average marks scored by students in physics, chemistry, maths: ')
st_avg = st_tot/2
print(st_avg)
#st_avg = (st1 + st2)/2  ## this also works
#st_avg.display_marks()

