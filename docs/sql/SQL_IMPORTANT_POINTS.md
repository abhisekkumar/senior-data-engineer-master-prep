# Sql Important Points

> Publication note: reformatted from private study notes. Employer-specific personal details and confidential context have been removed or generalized.

## Row_Number:
Assigns a unique number to every row.

## Rank:
Assigns the same rank to ties and skips subsequent ranks.

## Dense_Rank:
Assigns the same rank to ties but does not skip subsequent ranks.

Need previous order: LAG()

Need Latest Order: ROW_NUMBER()

Latest Row: ROW_NUMBER()

Previous row                  : LAG()
Next row                      : LEAD()
Difference from prior event   :    LAG()
## Lead()

Running total       : SUM() OVER()
Cumulative metric   : SUM() OVER()

Top N per group     : ROW_NUMBER()
Second highest      : RANK()
Third highest       : DENSE_RANK()
