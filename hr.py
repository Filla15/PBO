class SistemPenggajian:
    def calculate_payroll(self, employees):
        print('Penghitungan Penggajian')
        print('=======================')
        for employee in employees:
            print(f'Penggajian untuuk: {employee.id}-{employee.name}')
            print(f'- Check Jumlahnya: {employee.calculate_payroll()}')
            print('')

class pegawai:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class GajiPegawai(pegawai):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary
    
class PegawaiJam(pegawai):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate
    
class KomisiPegawai(GajiPegawai):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission