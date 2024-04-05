/*
 * helpers.h
 *
 *  Created on: Mar 19, 2024
 *      Author: claire
 */

#ifndef INC_HELPERS_H_
#define INC_HELPERS_H_

void rotateServo(char num);
void printCategory(char num);
void LCDReset(void);
void print_buf(uint8_t ai_flag);
void printPredicting(void);
void printIdle(void);
HAL_StatusTypeDef print_msg(char * msg);


#endif /* INC_HELPERS_H_ */
