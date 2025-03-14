from semantic_kernel.functions import kernel_function

class userInitPlugin:
    userInfo = {
        id: {
            "location": "",
            "legal_first_name": "",
            "legal_last_name": "",
            "date_of_birth": "",
            "medical_background": {
                "appleAllgergy": False,
                "diabetes": False
            },
            "residing_country": "USA"
        }
    }
    listOfUsers = []
    
    @kernel_function(
        name="get_user_info",
        description='Request the user the userInfo: make sure it is asked in 4 phases - phase 1: first name and last name, phase 2: date of birth, phase 3: medical background, phase 4: residing country, location',)
    def userInit(location: str, legal_first_name: str, legal_last_name: str, date_of_birth: str, appleAllgergy: bool, diabetes: bool, residing_country: str):
        # future store in database but currenty just store in dictionary
        return {
            "location": location,
            "legal_first_name": legal_first_name,
            "legal_last_name": legal_last_name,
            "date_of_birth": date_of_birth,
            "medical_background": {
                "appleAllgergy": appleAllgergy,
                "diabetes": diabetes
            },
            "residing_country": residing_country
    }