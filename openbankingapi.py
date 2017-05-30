import requests

BANK_LIST_URL = 'https://developer.openbanking.org.uk/open-data/participant-store/participant_store.json'


class OpenBankingApi:
    def __init__(self, timeout=5):
        self.timeout = timeout

    def get_bank_api_data(self, endpoint, bank):
        if bank.get('supportedAPIs', {}).get(endpoint):
            url = '{0}/{1}/{2}'.format(
                bank['baseUrl'],
                bank['supportedAPIs'][endpoint][0],
                endpoint
            )

            response = requests.get(url, timeout=self.timeout)

            return response.json()

    def banks(self):
        response = requests.get(BANK_LIST_URL, timeout=self.timeout)

        return response.json().get('data', [])

    def unsecured_sme_loans(self, bank):
        return self.get_bank_api_data('unsecured-sme-loans', bank)

    def business_current_accounts(self, bank):
        return self.get_bank_api_data('business-current-accounts', bank)

    def commercial_credit_cards(self, bank):
        return self.get_bank_api_data('commercial-credit-cards', bank)
