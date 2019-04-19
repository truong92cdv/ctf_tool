// ------------------- main() ----------------------
void __cdecl __noreturn main()
{
  int choice; // eax
  char buf; // [esp+8h] [ebp-10h]
  unsigned int canary; // [esp+Ch] [ebp-Ch]

  canary = __readgsdword(0x14u);
  setvbuf(stdout, 0, 2, 0);
  setvbuf(stdin, 0, 2, 0);
  while ( 1 )
  {
    while ( 1 )
    {
      show_menu();
      read(0, &buf, 4u);
      choice = atoi(&buf);
      if ( choice != 2 )
        break;
      delete_note();
    }
    if ( choice > 2 )
    {
      if ( choice == 3 )
      {
        print_note();
      }
      else
      {
        if ( choice == 4 )
          exit(0);
LABEL_13:
        puts("Invalid choice");
      }
    }
    else
    {
      if ( choice != 1 )
        goto LABEL_13;
      create_note();
    }
  }
}


// ------------------- create_note() ----------------------
unsigned int create_note()
{
  note *Note; // ebx
  signed int i; // [esp+Ch] [ebp-1Ch]
  int size; // [esp+10h] [ebp-18h]
  char buf; // [esp+14h] [ebp-14h]
  unsigned int canary; // [esp+1Ch] [ebp-Ch]

  canary = __readgsdword(0x14u);
  if ( note_count <= 5 )
  {
    for ( i = 0; i <= 4; ++i )
    {
      if ( !NOTES[i] )
      {
        NOTES[i] = (note *)malloc(8u);
        if ( !NOTES[i] )
        {
          puts("Alloca Error");
          exit(-1);
        }
        NOTES[i]->pprint = pprint_note;
        printf("Note size :");
        read(0, &buf, 8u);
        size = atoi(&buf);
        Note = NOTES[i];
        Note->content = (char *)malloc(size);
        if ( !NOTES[i]->content )
        {
          puts("Alloca Error");
          exit(-1);
        }
        printf("Content :");
        read(0, NOTES[i]->content, size);
        puts("Success !");
        ++note_count;
        return __readgsdword(0x14u) ^ canary;
      }
    }
  }
  else
  {
    puts("Full");
  }
  return __readgsdword(0x14u) ^ canary;
}


// ------------------- print_note() ----------------------
unsigned int print_note()
{
  int index; // [esp+4h] [ebp-14h]
  char buf; // [esp+8h] [ebp-10h]
  unsigned int canary; // [esp+Ch] [ebp-Ch]

  canary = __readgsdword(0x14u);
  printf("Index :");
  read(0, &buf, 4u);
  index = atoi(&buf);
  if ( index < 0 || index >= note_count )
  {
    puts("Out of bound!");
    _exit(0);
  }
  if ( NOTES[index] )
    ((void (__cdecl *)(note *))NOTES[index]->pprint)(NOTES[index]);
  return __readgsdword(0x14u) ^ canary;
}


// ------------------- delete_note() ----------------------
unsigned int delete_note()
{
  int index; // [esp+4h] [ebp-14h]
  char buf; // [esp+8h] [ebp-10h]
  unsigned int canary; // [esp+Ch] [ebp-Ch]

  canary = __readgsdword(0x14u);
  printf("Index :");
  read(0, &buf, 4u);
  index = atoi(&buf);
  if ( index < 0 || index >= note_count )
  {
    puts("Out of bound!");
    _exit(0);
  }
  if ( NOTES[index] )
  {
    free(NOTES[index]->content);
    free(NOTES[index]);
    puts("Success");
  }
  return __readgsdword(0x14u) ^ canary;
}


// ------------------- struct note ------------------------
struct __attribute__((aligned(4))) note
{
  void *pprint;
  char *content;
};


// ------------------ pprint_note() ----------------------
int __cdecl pprint_note(note *a1)
{
  return puts(a1->content);
}