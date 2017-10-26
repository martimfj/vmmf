# Modulação e Demodulação BPSK
## Chat
### O que é BPSK?
BPSK (deslocamento de fase binário) é um tipo de modulação digital em que a fase da portadora varia entre 0 e 1 e permanece constante entre os intervalos, sem alterar a amplitude e a frequência. Fazendo isso, ela consegue identificar os símbolos através da mudança da fase, normalmente um seno de estado 0 ou 180°.

### Funcionamento Geral do Projeto
Utilizamos quatro arquivos, dois em python (links) e dois do GNURadio, sendo um de cada tipo representante ou do transmissor da mensagem, ou do receptor. No transmissor, a interface permite que se escreva uma mensagem, como em um chat comum, que será então modulada, e enviada via o socket que foi configurado no arquivo, para que então o receptor estabeleça uma comunicação com o ele e receba os dados via socket, demodulando e exibindo na interface desenvolvida.

### Frequencia de transmissão utilizada e banda que o sinal ocupa
A frequencia utilizada foi de 2200 Hz, pois através de testes empíricos determinamos que era um valor adequado para ambos os computadores. O sinal ocupa uma banda de...

## GNURadio (Gráficos com explicação)
### Transmissor
Sinal não codificado no tempo

![ncodificadot](img/ncodt.png)

Sinal não codificado em frequência

![ncodificadof](img/ncodf.png)

Sinal codificado no tempo

![codificadot](img/codt.png)

Sinal codificado em frequência

![codificadof](img/codf.png)

Sinal modulado no tempo

![moduladot](img/modt.png)

Sinal modulado em frequência

![moduladof](img/modf.png)

Diagrama de constelação

![constelacao](img/const.png)

Sobre o gráfico resultante

...

### Receptor
- Exibir o sinal de áudio recebido no tempo e em frequência
- Exibir o sinal de áudio demodulado no tempo e em frequência
- Exibir o diagrama de constelação.

#### Itens extras
- Fazer uma transmissão fullduplex (permitir os dois computadores enviar mensagens simultaneamente)
- Implementar uma transmissão com mais de um símbolo (QPSK)
- Implementar algum tipo de correção de erro na mensagem enviada (CRC, ACK/NACK/ Paridade...)

#### Validação
Em sala de aula, abrir as duas aplicações em computadores distintos e transmitir uma frase entre eles via o pipeline desenvolvido anteriormente.
