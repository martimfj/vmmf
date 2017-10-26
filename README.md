# Modulação e Demodulação BPSK
## Chat
- O projeto (Explicar o funcionamento geral do projeto)
    1) O que é
    2) Arquitetura (camadas)
    3) Melhorias
- Modulação BPSK (Explicar a modulação BPSK)
- Frequência de transmissão utilizada e a banda que o sinal ocupa.

## GNURadio (Gráficos com explicação)
### Transmissor
- Exibir o gráfico no tempo e em frequência do sinal não codificado
- Exibir o gráfico no tempo e em frequência do sinal codificado (após o constellation modulator)
- Exibir o gráfico no tempo e em frequência do sinal modulado e explicar o gráfico resultante
- Exibir o diagrama de constelação.

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