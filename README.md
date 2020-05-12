# Parsing-Chemsep-database
python program to parse and xml document

# Scrapping Local Files using Beautiful Soup
Beautiful Soup- a python package is used here for parsing this XML document. It creates a parse tree for parsed pages that can be used to extract data from HTML, which is useful for web scraping. 

## About Chemsep Database
This is an XML document and contains the information about 431 chemical compounds.
This python code is written to fetch all the comppund names and their properties mainly CAS Number, Molecular Weight, Smiles.
Every compound in the database has all the above mentioned properties except Smiles.
So before fetching Smiles value for a compound we need to check whether the compound we search for has "Smiles" tag in it or not.
If the tag is not found, then the code returns "-" else the Smiles value.

Similar check needs to be perfomed to extract Melting point,Normal Boiling points etc for the compounds. 

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Please make sure to update tests as appropriate
