# Apiary Permalink Generator

Generates permalinks for existing apiary blueprint. Permalinks are generated from existing services in format your-service-name

## Getting Started

Download ApiaryPermalinkGen.py and run

```
python ApiaryPermalinkGen.py -i "your-file-with-apiary-blueprint"
```

It will generate new file called apiaryWithPermaLinks.txt in the same dir where the python file is. Generated file will contain blueprint with permalinks. Every permalink will be inserted after service name in format of `<a name="your-service-name">`

## How to use permalinks
if generated link is foo permalink is following
```
http://docs.{yourSubdomain}.apiary.io/#foo
```

## Options
- `-c` Clears previous permaliks. Use this option if you already have permalinks in your blueprint
- `-o` Output file. Allows to specify output file to write blueprint.

## Examples
Generate  with permaliks:
```
python ApiaryPermalinkGen.py -i "your-file-with-apiary-blueprint"
```
Clean previous permalinks and generate:
```
python ApiaryPermalinkGen.py -i -c "your-file-with-apiary-blueprint"
```
Clean previous permalinks specify output file and generate:
```
python ApiaryPermalinkGen.py -i "your-file-with-apiary-blueprint" -o "your-output-file.txt" -c
```


### Prerequisites

You need Python 3.3 or later to run Apiary Permalink Generator.  You can have multiple Python
versions (2.x and 3.x) installed on the same system without problems.

In Ubuntu, Mint and Debian you can install Python 3 like this:

    $ sudo apt-get install python3 python3-pip

For other Linux flavors, OS X and Windows, packages are available at

  http://www.python.org/getit/

## Author
* Mikk Laos

## License

This project is licensed under the MIT License. This product comes with no warranty.
