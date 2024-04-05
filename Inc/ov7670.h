#ifndef __OV7670_H
#define __OV7670_H

#include "main.h"

#define ADDR_OV7670 ((uint16_t)0x42)

 #define OV7670_REG_NUM 125

// Image settings
#define IMG_ROWS 120
#define IMG_COLS 160
#define NUM_BYTES 3*IMG_ROWS*IMG_COLS


#define PREAMBLE "\r\n!START!\r\n"
#define AI_PREAMBLE "\r\n!AIIII!\r\n"

#define  R(Y,V) Y + 1.402*(V- 128)
#define G(Y,U,V) Y - 0.3455*(U - 128) -0.71414*(V - 128)
#define B(Y, U) Y + 1.772*(U- 128)
#define max(a, b) ((a) > (b) ? (a) : (b))
#define min(a, b) ((a) < (b) ? (a) : (b))

HAL_StatusTypeDef ov7670_write(uint8_t reg,uint8_t val);
uint8_t ov7670_init(void);
void ov7670_capture(uint16_t *buff);

// size registers
#define REG_SCALING_XSC             0x70
#define REG_SCALING_YSC             0x71
#define REG_SCALING_DCWCTR          0x72
#define REG_SCALING_PCLK_DIV        0x73
#define REG_SCALING_PCLK_DELAY      0xa2

#define REG_HSTART                  ( 0x17 )        // Horiz start high bits
#define REG_HSTOP                   ( 0x18 )        // Horiz stop high bits
#define REG_VSTART                  ( 0x19 )        // Vert start high bits
#define REG_VSTOP                   ( 0x1a )        // Vert stop high bits

#define REG_COM14                   ( 0x3e )        // Control 14
#define REG_COM3                    ( 0x0c )        // Control 3
#define REG_HREF                    ( 0x32 )        // HREF pieces
#define REG_VREF                    ( 0x03 )

// QQVGA setting
#define COM7_QQVGA                  0x00
#define HSTART_QQVGA                0x16
#define HSTOP_QQVGA                 0x04
#define HREF_QQVGA                  0xa4
#define VSTART_QQVGA                0x02
#define VSTOP_QQVGA                 0x7a
#define VREF_QQVGA                  0x0a
#define COM3_QQVGA                  0x04
#define COM14_QQVGA                 0x1a
#define SCALING_XSC_QQVGA           0x3a
#define SCALING_YSC_QQVGA           0x35
#define SCALING_DCWCTR_QQVGA        0x22
#define SCALING_PCLK_DIV_QQVGA      0xf2
#define SCALING_PCLK_DELAY_QQVGA    0x02


#define SCALING_XSC (0x70)
#define SCALING_YSC (0x71)

#define SCALING_DCWCTR (0x72)
#define SCALING_PCLK_DIV (0x73)

#define SCALING_PCLK_DELAY (0xA2)




#endif
