import requests

PARTICIPANT_LIST_URL = 'https://developer.openbanking.org.uk/open-data/participant-store/participant_store.json'


class OpenBankingApi:
    def __init__(self, timeout=5):
        self.timeout = timeout

    def get_api_data(self, endpoint, participants):
        data = {}
        for participant in participants:
            if participant.get('supportedAPIs', {}).get(endpoint):
                url = '{0}/{1}/{2}'.format(
                    participant['baseUrl'],
                    participant['supportedAPIs'][endpoint][0],
                    endpoint
                )

                response = requests.get(url, timeout=self.timeout)

                data.setdefault(participant['name'], []).append(response.json())
        return data

    def participants(self):
        response = requests.get(PARTICIPANT_LIST_URL, timeout=self.timeout)

        return response.json().get('data', [])

    def unsecured_sme_loans(self, participants):
        return self.get_api_data('unsecured-sme-loans', participants)

    def business_current_accounts(self, participants):
        return self.get_api_data('business-current-accounts', participants)

    def commercial_credit_cards(self, participants):
        return self.get_api_data('commercial-credit-cards', participants)
