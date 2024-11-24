---
tags:
  - comp
---
1. In large spreadsheets, at least one incorrect bottom-line value is very likely to be present.
2. Errors are extremely difficult to detect and correct
3. spreadsheet developers and corporations are highly overconfident in the accuracy of their spreadsheets.

# Steps to Avoid Errors
To avoid errors, assumptions, input, output, and calculations should all be separated. Other techniques include:
1. When aggregating a row or column of numbers (e.g. average, sum), include a blank cell at the end of the list in the aggregate.
2. Calculate a value using two different methods, and check for equality
3. Check data entry using hash (checksum) totals, COUNT, MIN/MAX, validation, and sorting.
4. Test extreme values to see if you get the expected results.
5. Design the layout of the printed page with the reader in mind.
6. Watch out for rounding errors and arithmetic errors.
7. Use short codes for data entry.


# Communications Area
Shows the content of the **active cell**. This is normally very far away from the cell itself (the point of interest), meaning that it will take longer for the user to navigate to it (Fitt's Law) and that the user is less likely to see/check it.

Cells have **two modes**, normal data entry, and formulas. If you are entering a formula, clicking on another cell creates a [[#References|relative reference]] to that cell, where as in data entry mode, it simply selects it as the new **active cell**. 

Cells can be formatted to change the way the data is represented (e.g. date, phone number, integer, decimal, etc).

# References
- Relative (`C1`)
- Absolute (`$C$1`)
- Mixed (`$C1` or `C$1`)
- Ranges (`A1:A5` or `A1:B1`)

# Check Sums
A small-sized block of data derived from another block of digital data for the purpose of detecting errors

For barcodes, see [this resource](https://www.csunplugged.org/static/resources/en/barcode-checksum-poster/Barcode%20Checksum%20Poster%20(13%20digits%20-%20a4).pdf).

# Hash Total
The summation of numbers having no practical meaning as a control precaution.