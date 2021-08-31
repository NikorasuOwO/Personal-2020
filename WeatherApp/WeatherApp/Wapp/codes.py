from datapackage import Package


def main ():
    pass
  
if __name__ == '__main__':
    main()

def country_codes():
    package = Package('https://datahub.io/core/country-list/datapackage.json')

    for resource in package.resources:
        if resource.descriptor['datahub']['type'] == 'derived/csv':
            return resource.read()
