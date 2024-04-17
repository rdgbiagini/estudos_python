""" Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação. """

from time import sleep

popA = int(input('DIGITE POPULAÇÃO DO PAÍS A: '))
popB  = int(input('DIGITE POPULAÇÃO DO PAÍS B: '))

crescA = float(input('INFORME TAXA DE CRESCIMENTO DO PAÍS A: ')) 
crescB = float(input('INFORME TAXA DE CRESCIMENTO DO PAÍS A: '))

ano = 0

while popA <= popB:
    popA = int(popA + (popA * crescA))
    popB = int(popB + (popB * crescB))
    print(f'Após {ano} ano(s) A tem {popA} habitantes e B tem {popB} habitantes, portanto A ainda não passou.')
    ano += 1
    sleep(0.1)

print(f'Após {ano} anos a população de A ({popA}) ultrapassa ou iguala a população de B ({popB}). ')