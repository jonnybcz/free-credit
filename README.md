FREE-CREDIT
===========

Selenium testy pro služby

- Slevomat
- Rohlik
- Damejidlo

Požadavky: **Python3.5**, **chromedriver** pod aliasem chromedriver
 
Konfigurace:
************ 

v souboru **user.conf** zadej emailové adresy a hesla ke službám.

```python
[rohlik]
user=myemailaddress@domain.cz
password=password_for_rohlik
log=logs/rohlik.log

[slevomat]
user=myemailaddress@domain.cz
password=password_for_slevomat
log=logs/slevomat.log

[damejidlo]
user=myemailaddress@domain.cz
password=password_for_dajmejidlo
log=logs/damejidlo.log
```
 
Spouštěj:
*********

```bash
python3.5 damejidlo.py
python3.5 rohlik.py
python3.5 slevomat.py
```