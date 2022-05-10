# That a simple Python console RSS-reader.
Use flag -h to get start.

Positional arguments:
  source         RSS URL

Optional arguments:
  -h, --help     show this help message and exit
  --version      Print version info
  --json         Print result as JSON in stdout
  --verbose      Outputs verbose status messages
  --to-html      Convert news to .html
  --to-pdf       Convert news to .pdf
  --date DATE    Find cached news on this date
  --limit LIMIT  Limit news topics if this parameter provided

JSON-object:
{
    "Feed": Source of news,
    "pub_**n**" (from **1** to **n**): {
        "Title": Title of news,
        "Text": News text (optional),
        "Link": General link,
        "Date": Publication date,
        "Inline picture": Picture link (optional)
    }
}

You can use --json, --to-html and --to-pdf together!

Script itself will install the necessary modules and create the directories it needs: cached news/[Source], conversions/[html, pdf] 
