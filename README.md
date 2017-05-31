OpenBanking API wrapper
----------------------
A simple wrapper for the the UK open banking APIs.

https://www.openbanking.org.uk

Currently implemented a simple wrapper around retrieving a list of banks and business related data.

Currently only tested on Python 3.4

Install
------

```
pip install openbankingapi
```

Example
-----

```
from openbankingapi import OpenBankingApi

api = OpenBankingApi(timeout=5)

banks = api.banks() # retrieves the list of participating banks

sme_loans = api.unsecured_sme_loans(banks[0])

current_accounts = api.business_current_accounts(banks[0])

credit_cards = api.commercial_credit_cards(banks[0])
```
