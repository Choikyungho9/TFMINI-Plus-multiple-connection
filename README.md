저는 https://github.com/budryerson/TFMini-Plus_python 이 분의 코드를 가지고와서 
프로젝트를 진행했습니다. 

라즈베리파이 4B 모델 / 데비안 OS


원작자의 코드가 너무 잘 되어있어서 응용하기에 쉬울 것이라 생각됩니다. 

이 프로젝트는 아래와 같습니다. 

![image](https://user-images.githubusercontent.com/20491139/115367424-271fe200-a201-11eb-8347-d884f74bf1c7.png)

5개의 TFMINI를 구동하기 위해서 

Serial0 를 UART0~4 로 바꿨습니다. 
자세한 내용은 https://inha-kyungho9.tistory.com/4 를 참조하시길 바랍니다. 

5개를 연결한 TFMINI 프로젝트의 결과는 다음과 같습니다. 

![image](https://user-images.githubusercontent.com/20491139/115368067-b3caa000-a201-11eb-8c6b-4882b3964b0d.png)


사용 방법: tests 폴더 내에 tfmp_test.py 를 실행하면 됩니다.
