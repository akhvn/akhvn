#!/usr/bin/env python3

# ��� ������� ����������� ���������, ������� ��������� ��������,
# ������� ������, � ������� ����� ��������� ������, � ������
# ����� ������� (--->) ������ ��������� ������

# aAc   ---> a!A!c
# aZc   ---> a!Z!c
# aZZc  ---> a!Z!!Z!c
# aBaCa ---> a!B!a!C!a
REGEXP_1 = r'([A-Z])'   # ���������� ���������
REGEXP_1_REPL = r'!\1!' # ��������� ��� ������ ������

# abc    ---> abc
# abbc   ---> abc
# azzzc  ---> azc
# arrrrc ---> arc
# xxxxxx ---> x
REGEXP_2 = r'(\w)\1+'  # \1 remembers last template, e.g.: r(\w{4}\1+) in azzzzzzzzzc will bring \w{4} = zzzz, \1 = zzzz
REGEXP_2_REPL = r'\1'

# this is text         ---> this is text
# this is is text      ---> this *is* text
# this is is is text   ---> this *is* text
# this is text text    ---> this is *text*
# this is is text text ---> this *is* *text*
REGEXP_3 = r'\b(is|text)(\s\1)+'
REGEXP_3_REPL = r'*\1*'

# one two three ---> two one three
# dog cat wolf  ---> cat dog wolf
# goose car rat ---> goose rat car
REGEXP_4 = r'(\b\w{3}\b)\s(\b\w{3}\b)'
REGEXP_4_REPL = r'\2 \1'

# cat dog                     ---> cat dog
# cat dog cat                 ---> cat dog cat
# dog cat dog cat cat         ---> dog dog
# dog cat dog rat rat cat cat ---> dog dog rat rat
REGEXP_5 = r'\s(\b\w+\b)(.*)\s\1\s\1'
REGEXP_5_REPL = r'\2'