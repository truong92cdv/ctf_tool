
undefined8 main(void)

{
  byte bVar1;
  int iVar2;
  size_t length;
  size_t sVar3;
  size_t sVar4;
  int c;
  int j;
  int i;
  int t;
  int k;
  
  i = 0;
  c = 0;
  while (c < 5) {
    j = 0;
    while (j < 5) {
      if (i == 9) {
        j = j + -1;
      }
      else {
        *(int *)(&something + ((long)c * 6 + (long)j) * 4) = i + 0x41;
      }
      i = i + 1;
      j = j + 1;
    }
    c = c + 1;
  }
  printf("PASSWORD:");
  gets(&PASSWORD);
  length = strlen(&PASSWORD);
  if (length == 0xe) {
    iVar2 = FUN_0010083a(&PASSWORD);
    if (iVar2 != 0) {
      t = 0;
      c = 0;
      while( true ) {
        sVar3 = strlen(&PASSWORD);
        if (sVar3 <= (ulong)(long)c) break;
        i = 0;
        while (i < 5) {
          j = 0;
          while (j < 5) {
            if (*(int *)(&something + ((long)i * 6 + (long)j) * 4) ==
                (int)(char)(&PASSWORD)[(long)c]) {
              (&ENCODED)[(long)t] = (char)i + 'A';
              (&ENCODED)[(long)(t + 1)] = (char)j + '1';
              t = t + 2;
            }
            j = j + 1;
          }
          i = i + 1;
        }
        c = c + 1;
      }
      c = 0;
      while( true ) {
        sVar3 = strlen(&ENCODED);
        if (sVar3 <= (ulong)(long)c) break;
        bVar1 = (byte)(c >> 0x37);
        (&V)[(long)c] = (&ENCODED)[(long)c] ^ ((char)c + (bVar1 >> 6) & 3) - (bVar1 >> 6);
        c = c + 1;
      }
      iVar2 = strcmp(s_B0C2A2C6A3A7C5_6B5F0A4G2B5A2_00302020,&V);
      if (iVar2 != 0) {
        printf("ACCESS DENIED");
                    /* WARNING: Subroutine does not return */
        exit(0);
      }
      k = 0;
      puts("[+]GOOD JOB ! u can submit with this :");
      c = 3;
      while( true ) {
        sVar3 = strlen(ALPHABET);
        if (sVar3 - 5 <= (ulong)(long)c) break;
        k = k + (int)ALPHABET[(long)c];
        (&FINAL)[(long)(c + -3)] = ALPHABET[(long)c];
        c = c + 1;
      }
      c = 0;
      while( true ) {
        sVar3 = strlen(&FINAL);
        if (sVar3 <= (ulong)(long)c) break;
        (&FINAL)[(long)c] = (&FINAL)[(long)c] ^ (char)c + (char)(c / 7) * -7;
        c = c + 1;
      }
      sVar3 = strlen(&PASSWORD);
      sVar4 = strlen(&FINAL);
      (&FINAL)[sVar4] = *(undefined *)(sVar3 + 0x30209f);
      strcpy(&DAT_00302221,&FINAL);
      FINAL = PASSWORD;
      (&FINAL)[(long)((k + -0x28) % 5)] = 0x5f;
      (&FINAL)[(long)((k + -0x28) % 0xd)] = 0x5f;
      sprintf(&FLAG,"%d_%s_HAHAHA",(ulong)(k - 0x28),&FINAL);
      printf("%s",&FLAG);
      return 0;
    }
  }
  printf("ACCESS DENIED");
                    /* WARNING: Subroutine does not return */
  exit(0);
}

