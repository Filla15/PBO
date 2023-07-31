class Performansi:
    def track(self, employees, hours):
        print('Tracking Employee Productivity')
        print('==============================')
        for Employee in employees:
            Employee.work(hours)
        print('')