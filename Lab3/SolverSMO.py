class SolverSMO:
    def __init__(self, smo_type, lambda_, t_obsl, m, n):
        self.smo_type = smo_type
        self.Lambda = lambda_
        self.T_obsl = t_obsl
        self.m = m
        self.n = n

        if self.smo_type == 1:
            self.mu = 1 / self.T_obsl
            self.t_prostoya = 1 / self.Lambda
            self.p_obsl = self.mu / (self.mu + self.Lambda)
            self.p_otkaza = self.Lambda / (self.Lambda + self.mu)
            self.A = self.Lambda * self.p_obsl
            self.N_obsl = self.Lambda * self.p_obsl
            self.N_neobsl = self.Lambda * self.p_otkaza
            self.N_obsl_div_N_neobsl = self.N_obsl / self.N_neobsl
        elif self.smo_type == 2:
            self.mu = 1 / self.T_obsl
            self.p = self.Lambda / self.mu
            if self.p != 1:
                self.p0 = (1 - self.p) / (1 - self.p ** (self.m + 2))
            else:
                self.p0 = 1 / (self.m + 2)
            self.p_otkaza = self.p ** (self.m + 1) * self.p0
            self.p_obsl = 1 - self.p_otkaza
            self.Q = 1 - self.p_otkaza
            self.A = self.Lambda * self.Q
            if self.p != 1:
                self.L_och = self.p ** 2 * (1 - self.p ** self.m * (self.m - self.m * self.p + 1)) / (1 - self.p) ** 2
            else:
                self.L_och = self.m * (self.m + 1) / (2 * (self.m + 2))
            self.T_och = self.L_och / self.Lambda
            self.L_smo = 1 + self.L_och
            if self.p != 1:
                self.T_smo = self.L_smo / self.Lambda
            else:
                self.T_smo = (self.m + 1) / (2 * self.mu)
        elif self.smo_type == 3:
            self.mu = 1 / self.T_obsl
            self.p = self.Lambda / self.mu
            if self.p >= 1:
                return
            self.L_och = self.p ** 2 / (1 - self.p)
            self.T_och = self.L_och / self.Lambda
            self.L_smo = self.p / (1 - self.p)
            self.T_smo = self.L_smo / self.Lambda
        elif self.smo_type == 4:
            self.mu = 1 / self.T_obsl
            self.p = self.Lambda / self.mu
            self.p0 = SolverSMO.compute_series(self.n, self.p) ** (-1)
            self.p_otkaza = self.p0 * self.p ** self.n / SolverSMO.factorial(self.n)
            self.p_obsl = self.Lambda / (self.Lambda + self.mu)
            self.Q = self.p_obsl
            self.A = self.Lambda * self.Q
            self.k = self.A / self.mu
        elif self.smo_type == 5:
            self.mu = 1 / self.T_obsl
            self.p = self.Lambda / self.mu
            if self.p != self.n:
                self.p0 = (SolverSMO.compute_series(self.n, self.p) + self.p ** (self.n + 1) /
                           (SolverSMO.factorial(self.n) * (self.n - self.p)) * (1 - (self.p / self.n) ** self.m)) ** (
                              -1)
            else:
                self.p0 = (SolverSMO.compute_series(self.n, self.p) + self.m * self.p ** (self.n + 1) /
                           (SolverSMO.factorial(self.n) * self.n)) ** (-1)
            self.p_otkaza = self.p ** (self.n + self.m) * self.p0 / (self.n ** self.m * SolverSMO.factorial(self.n))
            if self.p != self.n:
                self.L_och = (self.p ** (self.n + 1) / (self.n * SolverSMO.factorial(self.n)) *
                              (1 - (self.p / self.n) ** self.m * (self.m + 1 - self.m * self.p / self.n)) /
                              (1 - self.p / self.n) ** 2)
            else:
                self.L_och = (self.p ** (self.n + 1) / (self.n * SolverSMO.factorial(self.n)) *
                              (self.m * (self.m + 1)) / 2 * self.p0)
            self.T_och = self.L_och / self.Lambda
            self.T_smo = self.T_och + (1 - self.p_otkaza) / self.mu
            self.k = self.p * (1 - self.p_otkaza)
            self.kz = self.k / self.n
        elif self.smo_type == 6:
            self.mu = 1 / self.T_obsl
            self.p = self.Lambda / self.mu
            if self.p >= self.n:
                return
            self.p0 = (SolverSMO.compute_series(self.n, self.p) + self.p ** (self.n + 1) / (
                        SolverSMO.factorial(self.n) *
                        (self.n - self.p))) ** (-1)
            self.p_och = self.p ** (self.n + 1) / (SolverSMO.factorial(self.n) * (self.n - self.p)) * self.p0
            self.L_och = self.n / (self.n - self.p) * self.p_och
            self.T_och = self.L_och / self.Lambda
            self.k = self.p
            self.L_smo = self.L_och + self.k
            self.T_smo = self.T_och + self.T_obsl
            self.kz = self.k / self.n

    @staticmethod
    def factorial(n):
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    @staticmethod
    def compute_series(n, p):
        result = 0
        for k in range(0, n + 1):
            result += p ** k / SolverSMO.factorial(k)
        return result

    def __str__(self):
        result = "Характеристики СМО:\n"
        if self.smo_type == 1:
            result += f"Интенсивность потока (lambda): {self.Lambda}\n"
            result += f"Время обслуживания (T_obsl): {self.T_obsl}\n"
            result += f"Интенсивность обслуживания (mu): {self.mu}\n"
            result += f"Время простоя (t_prostoya): {self.t_prostoya}\n"
            result += f"Вероятность обслуживания (p_obsl): {self.p_obsl}\n"
            result += f"Вероятность отказа (p_otkaza): {self.p_otkaza}\n"
            result += f"Абсолютная пропускная способность (A): {self.A}\n"
            result += f"Число обслуженных заявок (N_obsl): {self.N_obsl}\n"
            result += f"Число необслуженных заявок (N_neobsl): {self.N_neobsl}\n"
            result += f"Отношение числа обслуженных к необслуженным: {self.N_obsl_div_N_neobsl}\n"
        elif self.smo_type == 2:
            result += f"Число мест в очереди (m): {self.m}\n"
            result += f"Интенсивность потока (lambda): {self.Lambda}\n"
            result += f"Время обслуживания (T_obsl): {self.T_obsl}\n"
            result += f"Интенсивность обслуживания (mu): {self.mu}\n"
            result += f"Интенсивность нагрузки (p): {self.p}\n"
            result += f"Начальная интенсивность нагрузки (p0): {self.p0}\n"
            result += f"Вероятность отказа (p_otkaza): {self.p_otkaza}\n"
            result += f"Вероятность обслуживания (p_obsl): {self.p_obsl}\n"
            result += f"Относительная пропускная способность (Q): {self.Q}\n"
            result += f"Абсолютная пропускная способность (A): {self.A}\n"
            result += f"Средняя длина очереди (L_och): {self.L_och}\n"
            result += f"Среднее время ожидания в очереди (T_och): {self.T_och}\n"
            result += f"Среднее число заявок в СМО (L_smo): {self.L_smo}\n"
            result += f"Среднее время нахождения заявки в СМО (T_smo): {self.T_smo}\n"
        elif self.smo_type == 3:
            result += f"Интенсивность потока (lambda): {self.Lambda}\n"
            result += f"Время обслуживания (T_obsl): {self.T_obsl}\n"
            result += f"Интенсивность обслуживания (mu): {self.mu}\n"
            result += f"Интенсивность нагрузки (p): {self.p}\n"
            if self.p >= 1:
                result += "Стационарное состояние невозможно\n"
                return result
            result += f"Средняя длина очереди (L_och): {self.L_och}\n"
            result += f"Среднее время ожидания в очереди (T_och): {self.T_och}\n"
            result += f"Среднее число заявок в СМО (L_smo): {self.L_smo}\n"
            result += f"Среднее время нахождения заявки в СМО (T_smo): {self.T_smo}\n"
        elif self.smo_type == 4:
            result += f"Количество каналов (n): {self.n}\n"
            result += f"Интенсивность потока (lambda): {self.Lambda}\n"
            result += f"Время обслуживания (T_obsl): {self.T_obsl}\n"
            result += f"Интенсивность нагрузки (p): {self.p}\n"
            result += f"Начальная интенсивность нагрузки (p0): {self.p0}\n"
            result += f"Вероятность отказа (p_otkaza): {self.p_otkaza}\n"
            result += f"Вероятность обслуживания (p_obsl): {self.p_obsl}\n"
            result += f"Относительная пропускная способность (Q): {self.Q}\n"
            result += f"Абсолютная пропускная способность (A): {self.A}\n"
            result += f"Среднее число занятых каналов (k): {self.k}\n"
        elif self.smo_type == 5:
            result += f"Количество каналов (n): {self.n}\n"
            result += f"Число мест в очереди (m): {self.m}\n"
            result += f"Интенсивность потока (lambda): {self.Lambda}\n"
            result += f"Время обслуживания (T_obsl): {self.T_obsl}\n"
            result += f"Интенсивность обслуживания (mu): {self.mu}\n"
            result += f"Интенсивность нагрузки (p): {self.p}\n"
            result += f"Начальная интенсивность нагрузки (p0): {self.p0}\n"
            result += f"Вероятность отказа (p_otkaza): {self.p_otkaza}\n"
            result += f"Средняя длина очереди (L_och): {self.L_och}\n"
            result += f"Среднее время ожидания в очереди (T_och): {self.T_och}\n"
            result += f"Среднее время нахождения заявки в СМО (T_smo): {self.T_smo}\n"
            result += f"Среднее число занятых каналов (k): {self.k}\n"
            result += f"Коэффициент занятых каналов (kz): {self.kz}\n"
        elif self.smo_type == 6:
            result += f"Количество каналов (n): {self.n}\n"
            result += f"Интенсивность потока (lambda): {self.Lambda}\n"
            result += f"Время обслуживания (T_obsl): {self.T_obsl}\n"
            result += f"Интенсивность обслуживания (mu): {self.mu}\n"
            result += f"Интенсивность нагрузки (p): {self.p}\n"
            if self.p >= self.n:
                result += "Стационарное состояние невозможно\n"
                return result
            result += f"Начальная интенсивность нагрузки (p0): {self.p0}\n"
            result += f"Вероятность образования очереди (p_och): {self.p_och}\n"
            result += f"Средняя длина очереди (L_och): {self.L_och}\n"
            result += f"Среднее время ожидания в очереди (T_och): {self.T_och}\n"
            result += f"Среднее число занятых каналов (k): {self.k}\n"
            result += f"Коэффициент занятых каналов (kz): {self.kz}\n"
            result += f"Среднее число заявок в СМО (L_smo): {self.L_smo}\n"
            result += f"Среднее время нахождения заявки в СМО (T_smo): {self.T_smo}\n"

        return result
