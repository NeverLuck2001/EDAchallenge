/* ==================================================================================/* 
/*  Author: GWX Technology
/*  Attribution: Plain Text
/*  Birthday: Tue Oct 10 15:36:16 CST 2023
/*  Organization: GWX Technology
/*  Copyright: GWX Technology ©2023 GWX Technology Inc. All rights reserved.
/* ----------------------------------------------------------------------------------/* 
/*  Description:
/*  All the data in the file was generated by GWX Technology. This information was
/*  prepared only for EDA tools training. GWX Technology does not guarantee the
/*  accuracy or completeness of the information contained herein. GWX Technology
/*  shall not be liable for any loss or damage of any kind arising from the use of
/*  this document or the information contained herein.
/* ----------------------------------------------------------------------------------/* 
/*  Version: 0.9.0.0 Alpha
/* ==================================================================================/* 


/*   --------------------------------------------------------------   */
/*                       Template Revision : 3.6.3                    */
/*   --------------------------------------------------------------   */

MemoryTemplate ( ram128x32_2p2r2w ) {
   CellName:      ram128x32_2p2r2w;
   MemoryType:    SRAM;
   LogicalPorts:  2RW;
   NumberofWords:  128;
   NumberofBits :  32;
   Algorithm:  SMarch ;
   BitGrouping : 1;
   OperationSet: Sync;
   MinHold:  0.381;
   ShadowRead: Off;
   WriteOutOfRange: Off;
   AddressCounter {
     Function (Address) {
       LogicalAddressMaP {
         ColumnAddress [1:0] :
         Address [1:0] ;
         RowAddress [4:0] :
         Address [6:2] ;
       }
     }
     Function (Rowaddress) {
       CountRange [0:31];
     }
     Function (Columnaddress) {
       CountRange [0:3];
     }
   }
Port (  QA[31:0] )
             {   
               Direction: OUTPUT;
               LogicalPort: A;
               Function: data;

             }
Port (  QB[31:0] )
             {   
               Direction: OUTPUT;
               LogicalPort: B;
               Function: data;

             }
Port (  ADRA[6:0] )
             {   
               Direction: INPUT;
               LogicalPort: A;
               Function: Address;

             }
Port (  DA[31:0] )
             {   
               Direction: INPUT;
               LogicalPort: A;
               Function: data;

             }
Port (  WEA )
             {   
               Direction: INPUT;
               LogicalPort: A;
               Function: WriteEnable;
               Polarity: ActiveHigh;

             }
Port (  MEA )
             {   
               Direction: INPUT;
               LogicalPort: A;
               Function: Select;
               Polarity: ActiveHigh;

             }
Port (  CLKA )
             {   
               Direction: INPUT;
               LogicalPort: A;
               Function: Clock;
               Polarity: ActiveHigh;

             }
Port (  TEST1A )
             {   
               Direction: INPUT;
               LogicalPort: A;
               Function: LogicLow;

             }
Port (  RMEA )
             {   
               Direction: INPUT;
               LogicalPort: A;
               Function: LogicLow;

             }
Port (  RMA[3:0] )
             {   
               Direction: INPUT;
               LogicalPort: A;
               Function: none;

             }
Port (  ADRB[6:0] )
             {   
               Direction: INPUT;
               LogicalPort: B;
               Function: Address;

             }
Port (  DB[31:0] )
             {   
               Direction: INPUT;
               LogicalPort: B;
               Function: data;

             }
Port (  WEB )
             {   
               Direction: INPUT;
               LogicalPort: B;
               Function: WriteEnable;
               Polarity: ActiveHigh;

             }
Port (  MEB )
             {   
               Direction: INPUT;
               LogicalPort: B;
               Function: Select;
               Polarity: ActiveHigh;

             }
Port (  CLKB )
             {   
               Direction: INPUT;
               LogicalPort: B;
               Function: Clock;
               Polarity: ActiveHigh;

             }
Port (  TEST1B )
             {   
               Direction: INPUT;
               LogicalPort: B;
               Function: LogicLow;

             }
Port (  RMEB )
             {   
               Direction: INPUT;
               LogicalPort: B;
               Function: LogicLow;

             }
Port (  RMB[3:0] )
             {   
               Direction: INPUT;
               LogicalPort: B;
               Function: none;

             }
}