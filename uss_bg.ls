/PROG  USS_BG
/ATTR
OWNER		= MNEDITOR;
COMMENT		= "";
PROG_SIZE	= 460;
CREATE		= DATE 20-04-08  TIME 02:11:58;
MODIFIED	= DATE 20-04-08  TIME 04:56:58;
FILE_NAME	= ;
VERSION		= 0;
LINE_COUNT	= 11;
MEMORY_SIZE	= 788;
PROTECT		= READ_WRITE;
TCD:  STACK_SIZE	= 0,
      TASK_PRIORITY	= 50,
      TIME_SLICE	= 0,
      BUSY_LAMP_OFF	= 0,
      ABORT_REQUEST	= 0,
      PAUSE_REQUEST	= 0;
DEFAULT_GROUP	= 1,*,*,*,*;
CONTROL_CODE	= 00000000 00000000;
/MN
   1:  R[14]=GI[R[6]]    ;
   2:  IF ((R[14]<=R[3]),R[15]=(1)) ;
   3:  IF ((R[14]>R[3]),R[15]=(0)) ;
   4:  IF ((R[14]>R[12]),R[16]=(1)) ;
   5:  IF ((R[14]<=R[12]),R[16]=(0)) ;
   6:  IF ((R[15]=1) AND (R[16]=1)),R[13]=(1) ;
   7:  IF ((R[15]=0) AND (R[16]=1)),R[13]=(0) ;
   8:  IF ((R[15]=1) AND (R[16]=0)),R[13]=(0) ;
   9:  IF ((R[15]=0) AND (R[16]=0)),R[13]=(0) ;
  10:   ;
  11:   ;
/POS
/END
