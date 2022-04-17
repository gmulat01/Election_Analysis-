counties = ["Arapahoue", "Denver", "Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties")

else: 
    print("El Paso is not the list of counties")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties")
else:
    print("Arapahoe or El Paso is not in the list of counties")

if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Araphoe is in the list of counties")
else: 
        print("Arapahoe is in the list of counties and El Paso is not in the list of counties")

        import datetime
        now = datetime.datetime.now()
        print("The time right now is ", now)

        import datetime as dt

        now = dt.datetime.now()
        print("The time right now is ", now)