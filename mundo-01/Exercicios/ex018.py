from math import sin, cos, tan, radians
angulo = float((input('Digite o ângulo: ')))

print('O ângulo digitado foi: {:.0f}° \nSeno: {:.2f} \nCosseno:{:.2f} \nTangente: {:.2f}'.format(angulo, sin(radians(angulo)), cos(radians(angulo)), tan(radians(angulo))))
