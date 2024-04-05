/*
 * helpers.c
 *
 *  Created on: Mar 19, 2024
 *      Author: claire
 */
#include <stdio.h>
#include <string.h>
#include "ov7670.h"
#include "main.h"
#include "helpers.h"
#include "liquidcrystal_i2c.h"


extern DCMI_HandleTypeDef hdcmi;
extern DMA_HandleTypeDef hdma_dcmi;

extern I2C_HandleTypeDef hi2c1;
extern I2C_HandleTypeDef hi2c2;

extern TIM_HandleTypeDef htim1;
extern TIM_HandleTypeDef htim2;

extern UART_HandleTypeDef huart3;
extern DMA_HandleTypeDef hdma_usart3_tx;
extern DMA_HandleTypeDef hdma_usart3_rx;
extern uint16_t snapshot_buff[IMG_ROWS*IMG_COLS];
extern uint8_t tx_buff[sizeof(PREAMBLE)+NUM_BYTES];
extern uint8_t dma_flag;

void rotateServo(char num){
	switch (num){
	case '1':
		HAL_GPIO_WritePin(GPIOD,  GPIO_PIN_7, GPIO_PIN_SET);
		htim2.Instance->CCR2=260; //180
		HAL_Delay(5000);
		htim2.Instance->CCR2=75; //90
		HAL_Delay(2000);
		HAL_GPIO_WritePin(GPIOD,  GPIO_PIN_7, GPIO_PIN_RESET);
		break;
	case '2':
		HAL_GPIO_WritePin(GPIOD,  GPIO_PIN_6, GPIO_PIN_SET);

		htim2.Instance->CCR2=260; //180
		HAL_Delay(5000);
		htim2.Instance->CCR2=75; //90
		HAL_Delay(2000);

		HAL_GPIO_WritePin(GPIOD,  GPIO_PIN_6, GPIO_PIN_RESET);
		break;

	case '3':
		HAL_GPIO_TogglePin(LD2_GPIO_Port, LD2_Pin);
		HAL_GPIO_WritePin(GPIOD,  GPIO_PIN_5, GPIO_PIN_SET);

		htim2.Instance->CCR2=750; //75% duty cycle = 2.0ms = CCW Rotation?
		HAL_Delay(1000);

		htim2.Instance->CCR2=0; //PAUSE
		HAL_Delay(2000);

		htim2.Instance->CCR2=100; //25% duty cycle = 0.5ms = CW Rotation?
		HAL_Delay(1000);

		HAL_GPIO_WritePin(GPIOD,  GPIO_PIN_5, GPIO_PIN_RESET);
		break;


	case '4':
		HAL_GPIO_WritePin(GPIOD,  GPIO_PIN_4, GPIO_PIN_SET);

		htim2.Instance->CCR2=750; //75% duty cycle = 1.5ms
		HAL_Delay(1000);

		htim2.Instance->CCR2=0; //PAUSE
		HAL_Delay(10000);

		htim2.Instance->CCR2=100; //25% duty cycle = 0.5ms
		HAL_Delay(1000);

		HAL_GPIO_WritePin(GPIOD,  GPIO_PIN_4, GPIO_PIN_RESET);
		break;
	}
}

void printCategory(char num){
	HD44780_Clear();
	HD44780_Backlight();
	HD44780_SetCursor(0,0);
	switch(num){
	case '1':
		HD44780_PrintStr("GARBAGE");
		break;
	case '2':
		HD44780_PrintStr("CONTAINERS");
		break;
	case '3':
		HD44780_PrintStr("PAPER");
		break;
	case '4':
		HD44780_PrintStr("COFFEE CUPS");
		break;
	}
}

void printIdle(void){
	HD44780_Clear();
	HD44780_Backlight();
	HD44780_SetCursor(0,0);
	HD44780_PrintStr("IDLE...");
}

void printPredicting(void){
	HD44780_Clear();
	HD44780_Backlight();
	HD44780_SetCursor(0,0);
	HD44780_PrintStr("PREDICTING...");
}

void LCDReset(void){
	HD44780_Clear();
	HD44780_NoBacklight();
}

HAL_StatusTypeDef print_msg(char * msg) {
  return HAL_UART_Transmit_DMA(&huart3, (uint8_t *)msg, strlen(msg));
}

void print_buf(uint8_t ai_flag) {
	if (ai_flag==0){
		for(int i=0; i<sizeof(PREAMBLE);i++){
			tx_buff[i] = PREAMBLE[i];
		}
	}
	else{
		for(int i=0; i<sizeof(AI_PREAMBLE);i++){
			tx_buff[i] = AI_PREAMBLE[i];
		}
	}
	for(int i=0; i<(IMG_ROWS*IMG_COLS); i+=2){
		uint8_t Y0= max(min(snapshot_buff[i]>>8, 230), 16);
		uint8_t U = max(min(snapshot_buff[i]&0xFF, 240), 16);
		uint8_t Y1 = max(min(snapshot_buff[i+1]>>8, 230), 16);
		uint8_t V = max(min(snapshot_buff[i+1]&0xFF, 240), 16);

		uint32_t R1 = min(R(Y0, V), 255);
		uint32_t G1 = min(G(Y0, U, V), 255);
		uint32_t B1 = min(B(Y0, U), 255);
		uint32_t R2 = min(R(Y1,V), 255);
		uint32_t G2 = min(G(Y1, U, V), 255);
		uint32_t B2 = min(B(Y1, U), 255);

		tx_buff[(3*i)+sizeof(PREAMBLE)] =  G1; //R?
		tx_buff[(3*i)+1+sizeof(PREAMBLE)] = B1; //G?
		tx_buff[(3*i)+2+sizeof(PREAMBLE)] = R1; //B?

		tx_buff[(3*i)+3+sizeof(PREAMBLE)] = G2; //R?
		tx_buff[(3*i)+4+sizeof(PREAMBLE)] = B2; //G?
		tx_buff[(3*i)+5+sizeof(PREAMBLE)] = R2; //B?
	}
	HAL_UART_Transmit_DMA(&huart3, tx_buff, sizeof(tx_buff));
	while (HAL_UART_GetState(&huart3)!=HAL_UART_STATE_READY){
		HAL_Delay(15);
	}
	HAL_DCMI_Resume(&hdcmi);
}
