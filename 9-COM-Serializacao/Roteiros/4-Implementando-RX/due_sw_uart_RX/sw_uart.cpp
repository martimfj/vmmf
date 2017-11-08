#include "sw_uart.h"
#pragma GCC optimize ("-O3")

void sw_uart_setup(due_sw_uart *uart, int rx, int tx, int stopbits, int databits, int paritybit) {
	uart->pin_tx     = tx;
	uart->pin_rx     = rx;
	uart->stopbits   = stopbits;
	uart->paritybit  = paritybit;
  uart->databits   = databits;
  pinMode(rx, INPUT);
  pinMode(tx, OUTPUT);
  digitalWrite(tx, HIGH);
}

void sw_uart_write_data(due_sw_uart *uart, char* bufferData, int writeN) {
  for(int i = 0; i < writeN; i++) {
    sw_uart_write_byte(uart, bufferData[i]);
  }
}

void sw_uart_write_string(due_sw_uart *uart, char* stringData) {
  sw_uart_write_data(uart, stringData, strlen(stringData));
}

int calc_even_parity(char data) {
  int sum = 0;
  for(int bit = 0; bit <= 7; bit++){
    sum += data >> bit & 0x01;   
  }
  
  int parity_check = sum % 2;
  
  if (parity_check == 0){
    return 1; 
  } else {
    return 0;
  }
}

// recebimento de dados da serial
int sw_uart_receive_byte(due_sw_uart *uart, char* data) {

  // variavel para recebimento de dados
  char nchar  = 0;
  
  // variavel para calculo da paridade
  char parity, rx_parity;
  
  // aguarda start bit
  boolean checkstartbit = false;

  // Confirma start BIT
  while(digitalRead(uart->pin_rx)){}
    _sw_uart_wait_half_T(uart);
    
    // checa se bit ainda é 0
    if(digitalRead(uart->pin_rx) == 0){
       checkstartbit == true;
    }
    else{
      return(SW_UART_ERROR_FRAMING);
    }
   
_sw_uart_wait_T(uart);

  // recebe dados
  for(int i = 0; i <= 7; i++) {
    nchar = nchar|(digitalRead(uart->pin_rx) << i);
    _sw_uart_wait_T(uart);
  }
  // recebe paridade
    rx_parity = digitalRead(uart->pin_rx);
    _sw_uart_wait_T(uart);
  
  // recebe stop bit 
  int stopbit = digitalRead(uart->pin_rx);
  
  // checa paridade
  parity = calc_even_parity(nchar);
  
  if(parity != rx_parity) {
    return SW_UART_ERROR_PARITY;
  }
  
  *data = nchar;
  return SW_UART_SUCCESS;
}

void sw_uart_write_byte(due_sw_uart *uart, char data) {
 
}

// MCK 21MHz
// 1093 para baudrate 9600/2
void _sw_uart_wait_half_T(due_sw_uart *uart) {
  for(int i = 0; i < 1093; i++)
    asm("NOP");
}

void _sw_uart_wait_T(due_sw_uart *uart) {
  _sw_uart_wait_half_T(uart);
  _sw_uart_wait_half_T(uart);
}

