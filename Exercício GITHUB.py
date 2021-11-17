"""
Faça um programa que percorre uma lista com o seguinte formato: [['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha', [5, 7]],
['Italia', 'Espanha', [7,8]]]. Essa lista indica o número de faltas que cada time fez em cada jogo. Na lista acima, no jogo entre Brasil e Itália, 
o Brasil fez 10 faltas e a Itália fez 9. O programa deve imprimir na tela:

(a) o total de faltas do campeonato

(b) o time que fez mais faltas

(c) o time que fez menos faltas
"""

jogos = [['Brasil', 'Italia', [10, 9]],
        ['Brasil', 'Espanha', [5, 7]],
        ['Italia', 'Espanha', [7,8]]]
faltas = []
times = []
faltastotal = 0

for jogo in jogos:
    for i in range(2):
        faltastotal += jogo[2][i]
        if jogo[i] not in times:
            times.append(jogo[i])
            faltas.append(jogo[2][i])
        else:
            index = times.index(jogo[i])
            faltas[index] += jogo [2][i]

maisfaltas = times [0]
menosfaltas = times [0]
for (time, falta) in zip(times[1:], faltas[1:]):
    if falta > faltas[times.index(maisfaltas)]:
        maisfaltas = time
    elif falta < faltas [times.index(menosfaltas)]:
        menosfaltas = time
print ("O numero total de faltas no campeonato foi %d." % faltastotal)
print ("O time que mais fez faltas foi: %s." % maisfaltas)
print ("O time que menos praticou faltas foi: %s." % menosfaltas)