class Solution:
    """
    @param: n: a positive integer
    @return: n x 3 matrix
    """

    def consistentHashing(self, n):
        if n == 1:
            return [[0, 359, n]]
        elif n == 2:
            return [[0, 179, 1], [180, 359, 2]]
        elif n == 3:
            return [[0, 89, 1], [90, 179, 3], [180, 359, 2]]
        elif n == 4:
            return [[0, 89, 1], [90, 179, 3], [180, 269, 2], [270, 359, 4]]
        else:
            machines = [[0, 89, 1], [90, 179, 3], [180, 269, 2], [270, 359, 4]]
            for i in range(4, n):
                machines = self.scaleToMachines(machines)
        return machines

    def scaleToMachines(self, machines):
        size = len(machines)
        machines.sort(key=lambda x: (x[0] - x[1], x[2]))

        machine = machines[0]
        machines = machines[1:]

        mid = (machine[0] + machine[1]) // 2
        new_machine1 = [machine[0], mid, machine[2]]
        new_machine2 = [mid + 1, machine[1], size + 1]

        machines.append(new_machine1)
        machines.append(new_machine2)
        return machines
