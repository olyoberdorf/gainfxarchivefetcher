# GainFXArchiveFetcher

This is a simple python  utility for batch downloading GainFX's historical data
archive.  You can specify the desired years and currency pairs and it will build
a folder with all the zipped csv files for you.

## Dependencies

Python 2.7 and the requests api

## Useage

Copy the `gainfxarchivefetcher.ini.example` file to `gainfxarchivefetcher.ini`
and edit to suit your setup.  Then you just run `gainfxarchivefetcher.py` from
the same directory as the ini file.

## Notes

I have found the GainFX csv files, the ones inside the zips, prior to 2009-06-01 to be corrupt.  I haven't checked all files or all pairs, but it seems to be a systemic problem.

## TODO

 * Eror handling (for now errors on the http request are assumed to be 404s)
 * Automatically stop requests in the future (i.e. December of this year if it's February)
