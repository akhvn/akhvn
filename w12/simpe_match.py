#!/usr/bin/env python3

# ��� ������� ����������� ���������, ������� ��������� ��������,
# ������� ������, ��������������� ����� ��������� (��� �������� ������ +),
# � ����� ������, �� ��������������� ����� ��������� (�������� ������ -)

# + a
# + ab
# - b
# - ba
REGEXP_1 = r'a'

# + aab
# + abb
# + acb
# - ab
# - aabc
REGEXP_2 = r'\b\w{3}$'

# + sofia.mp3
# + sofia.mp4
# - sofia.mp7
# - sofia.mp34
REGEXP_3 = r'sofia\.mp[3-4]$'

# + taverna
# + versus
# + vera
# + zveri
# - zver
REGEXP_4 = r'(?!zver$)'

# - a
# - aa
# + aaa
# - aaaa
# - b
# - bb
# + bbb
# - bbbb
# - ccc
REGEXP_5 = r'[ab]{3}$'

# - Ok
# - OkOk
# + OkOkOk
# - OkOkOkOk
# - ab
# - abab
# + ababab
# - abababab
REGEXP_6 = r'\b(\w{2}){3}$'

# - aaa
# - aaa aaa
# + aaa Aaa aaa
# + aaa aaa Aaa
# + Aaa aaa aaa
# - A
# - aaa A aaa
REGEXP_7 = r'.* \w{3} '

# + abc
# + abc03
# + a-b-c-3
# + a.b.c.0
# - Aabc
# - abc1
# - #abc
REGEXP_8 = r'a[^1]*$'