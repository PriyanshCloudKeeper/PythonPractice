def error_codes(series):
    match series:
        case 100:
            return 'Informational Responses'
        case 200:
            return 'Succes Responses'
        case 300:
            return 'Redirection Responses'
        case 400:
            return 'Client Errors'
        case 500:
            return 'Server Errors'
        
response_series= int(input("Enter the the error series:\n100 200 300 400 500\n"))
print(error_codes(response_series))