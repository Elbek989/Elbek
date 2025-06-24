import re
from random import randint

class TTJ:
    def init(self, nomi, telefon, manzil):
        if not re.match(r"^\+998\d{9}$", telefon):
            raise ValueError("Telefon raqami +998 bilan boshlanib, 9 xonali bo'lishi kerak.")
        self.nomi = nomi
        self.telefon = telefon
        self.manzil = manzil
        self.xonalar = []

    def qosh_xona(self, xona):
        self.xonalar.append(xona)

    def repr(self):
        return f"TTJ: {self.nomi}, Telefon: {self.telefon}, Manzil: {self.manzil}"

class Xona:
    def init(self, raqam, holat, sigim, qavat, ttj):
        self._raqam = raqam
        self.holat = holat
        self.sigim = sigim
        self.qavat = qavat
        self.ttj = ttj
        ttj.qosh_xona(self)

    @property
    def raqam(self):
        return self._raqam

    @property
    def holat(self):
        return self._holat

    @holat.setter
    def holat(self, qiymat):
        if qiymat in ["bo'sh", "aktiv"]:
            self._holat = qiymat
        else:
            raise ValueError("Noto'g'ri holat kiritildi. 'bo'sh' yoki 'aktiv' bo'lishi kerak.")

    @property
    def sigim(self):
        return self._sigim

    @sigim.setter
    def sigim(self, qiymat):
        if qiymat > 0:
            self._sigim = qiymat
        else:
            raise ValueError("Sig'im 0 dan katta bo'lishi kerak.")

    @property
    def qavat(self):
        return self._qavat

    @qavat.setter
    def qavat(self, qiymat):
        if 1 <= qiymat <= 5:
            self._qavat = qiymat
        else:
            raise ValueError("Qavat 1 va 5 oralig'ida bo'lishi kerak.")

    def repr(self):
        return f"Xona {self.raqam} | Holat: {self.holat} | Sig'im: {self.sigim} | Qavat: {self.qavat}"

def yarat_xonalar(ttj):
    for raqam in range(1, 201):
        holat = "bo'sh" if randint(0, 9) == 0 else "aktiv"
        sigim = randint(2, 4)
        qavat = randint(1, 5)
        Xona(raqam, holat, sigim, qavat, ttj)

if name == "main":
    try:
        ttj = TTJ("TTJ-1", "+998901234567", "Toshkent, Mirzo Ulug'bek tumani")
        yarat_xonalar(ttj)

        print(ttj)
        print(f"Jami xonalar: {len(ttj.xonalar)}\n")
        print("Birinchi 5 xona:")
        for xona in ttj.xonalar[:5]:
            print(xona)

    except Exception as e:
        print(f"Xatolik: {e}")