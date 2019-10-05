'''
Caleb's API for the Salvage Log Form Response
'''

log_response = {
    'free removal': 'Free Removal',
    'small keepsake': 'Free Small Keepsake',
    'large keepsake':'Free Large Keepsake (Bowl or Hollow Form/Vessel)',
    'lucrative log':'We would like to discuss purchasing your log',
    'transport for fee':'We can offer our log transport service, but we cannot offer it as a free service due to the size & species of the log'
}

if (condition):
    return JsonResponse({
        'response': log_response[condition]
    })