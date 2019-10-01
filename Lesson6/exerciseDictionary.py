visits = {"Los Angeles":2016, "San Diego":2016, "San Francisco":2016, "Toronto":2018}

def year(city):
    '''
    input: A string. The city.
    output: A year. The corresponding value for that key.
    '''
    return visits[city]

# Loop among the places
for city in visits:
    print("City:",end=' ')
    print(city, end='. ')
    print("Year of visit:", end=' ')
    print(year(city))
