# JsonToCsv
convert Json to Csv format
#used

python JsonToCsv.py Jsonfilepath

while print all list in two level object with key:value format.

simple
{
  "a": [
    {
      "b": "c"
    },
    {
      "b": "d"
    },
    {
      "e": "c"
    }
  ]
}

TO:

b	e
c	NULL
d	NULL
NULL	c
