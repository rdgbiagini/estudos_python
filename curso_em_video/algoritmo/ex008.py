""" Desenvolva um programa que leia uma distância em metros e mostre os valores relativos em outras medidas. 
Ex:  Digite uma distância em metros: 185.72 A distância de 85.7m corresponde a: 0.18572Km 1.8572Hm 18.572Dam 1857.2dm 18572.0cm 185720.0mm  """

m = int(input('medida em m: '))

km = m / 1000
hm = m / 100
dm = m * 10
cm = m * 100
mm = m * 1000

print(f'''A medida em m digitada foi {m}.
Ela corresponde a {km}km;
Ou {hm}hm;
Ou {dm}dm;
Ou {cm}cm;
Ou {mm}mm.''')