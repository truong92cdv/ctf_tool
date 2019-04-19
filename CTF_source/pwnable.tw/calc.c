// ---------------------------------------- function main() ------------------------
int __cdecl main(int argc, const char **argv, const char **envp)
{
  ssignal(14, timeout);
  alarm(60);
  puts("=== Welcome to SECPROG calculator ===");
  fflush(stdout);
  calc();
  return puts("Merry Christmas!");
}


// ---------------------------------------- function calc() ------------------------
unsigned int calc()
{
  int count; // [esp+18h] [ebp-5A0h]
  int numbers[100]; // [esp+1Ch] [ebp-59Ch]
  char s; // [esp+1ACh] [ebp-40Ch]
  unsigned int v4; // [esp+5ACh] [ebp-Ch]

  v4 = __readgsdword(0x14u);
  while ( 1 )
  {
    bzero(&s, 0x400u);
    if ( !get_expr((int)&s, 1024) )
      break;
    init_pool(&count);
    if ( parse_expr((int)&s, &count) )
    {
      printf((const char *)&unk_80BF804, numbers[count - 1]);
      fflush(stdout);
    }
  }
  return __readgsdword(0x14u) ^ v4;
}


// ---------------------------------------- function get_expr() ------------------------
int __cdecl get_expr(int s, int length)
{
  int v2; // eax
  char c; // [esp+1Bh] [ebp-Dh]
  int i; // [esp+1Ch] [ebp-Ch]
  int savedregs; // [esp+28h] [ebp+0h]

  i = 0;
  while ( i < length && read((int)&savedregs, 0, (int)&c, 1) != -1 && c != 10 )
  {
    if ( c == '+' || c == '-' || c == '*' || c == '/' || c == '%' || c > '/' && c <= '9' )
    {
      v2 = i++;
      *(_BYTE *)(s + v2) = c;
    }
  }
  *(_BYTE *)(i + s) = 0;
  return i;
}


// ---------------------------------------- function init_pool() ------------------------
_DWORD *__cdecl init_pool(_DWORD *count)
{
  _DWORD *result; // eax
  signed int i; // [esp+Ch] [ebp-4h]

  result = count;
  *count = 0;
  for ( i = 0; i <= 99; ++i )
  {
    result = count;
    count[i + 1] = 0;
  }
  return result;
}


// ---------------------------------------- function parse_expr() ------------------------
signed int __cdecl parse_expr(int expr, _DWORD *count)
{
  unsigned int v2; // ST2C_4
  int v4; // eax
  _BYTE *v5; // [esp+20h] [ebp-88h]
  int i; // [esp+24h] [ebp-84h]
  int j; // [esp+28h] [ebp-80h]
  char *s1; // [esp+30h] [ebp-78h]
  int v9; // [esp+34h] [ebp-74h]
  char s[100]; // [esp+38h] [ebp-70h]
  unsigned int v11; // [esp+9Ch] [ebp-Ch]

  v11 = __readgsdword(0x14u);
  v5 = (_BYTE *)expr;
  j = 0;
  bzero(s, 0x64u);
  for ( i = 0; ; ++i )
  {
    if ( (unsigned int)(*(char *)(i + expr) - '0') > 9 )
    {
      v2 = i + expr - (_DWORD)v5;
      s1 = (char *)malloc(v2 + 1);
      memcpy(s1, v5, v2);
      s1[v2] = 0;
      if ( !strcmp(s1, "0") )
      {
        puts("prevent division by zero");
        fflush(stdout);	
        return 0;
      }
      v9 = atoi(s1);
      if ( v9 > 0 )
      {
        v4 = (*count)++;
        count[v4 + 1] = v9;
      }
      if ( *(_BYTE *)(i + expr) && (unsigned int)(*(char *)(i + 1 + expr) - '0') > 9 )
      {
        puts("expression error!");
        fflush(stdout);
        return 0;
      }
      v5 = (_BYTE *)(i + 1 + expr);
      if ( s[j] )
      {
        switch ( *(char *)(i + expr) )
        {
          case '%':
          case '*':
          case '/':
            if ( s[j] != '+' && s[j] != '-' )
            {
              eval(count, s[j]);
              s[j] = *(_BYTE *)(i + expr);
            }
            else
            {
              s[++j] = *(_BYTE *)(i + expr);
            }
            break;
          case '+':
          case '-':
            eval(count, s[j]);
            s[j] = *(_BYTE *)(i + expr);
            break;
          default:
            eval(count, s[j--]);
            break;
        }
      }
      else
      {
        s[j] = *(_BYTE *)(i + expr);
      }
      if ( !*(_BYTE *)(i + expr) )
        break;
    }
  }
  while ( j >= 0 )
    eval(count, s[j--]);
  return 1;
}


// ---------------------------------------- function eval() ------------------------
_DWORD *__cdecl eval(_DWORD *count, char operation)
{
  _DWORD *result; // eax

  if ( operation == '+' )
  {
    count[*count - 1] += count[*count];
  }
  else if ( operation > '+' )
  {
    if ( operation == '-' )
    {
      count[*count - 1] -= count[*count];
    }
    else if ( operation == '/' )
    {
      count[*count - 1] /= count[*count];
    }
  }
  else if ( operation == '*' )
  {
    count[*count - 1] *= count[*count];
  }
  result = count;
  --*count;
  return result;
}