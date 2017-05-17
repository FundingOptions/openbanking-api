OpenBanking API wrapper
----------------------
A simple wrapper for the the UK open banking APIs.

https://www.openbanking.org.uk

Example
-----

```
from openbanking import OpenBankingApi

api = OpenBankingApi(timeout=5)

participants = api.participants()

sme_loans = api.unsecured_sme_loans(participants)

current_accounts = api.business_current_accounts(participants)

credit_cards = api.commercial_credit_cards(participants)
```
