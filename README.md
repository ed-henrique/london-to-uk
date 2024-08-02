# London to UK

Report on spending volumes for London-based customers versus those based in the
rest of the United Kingdom.

## 1. Understanding (Describing the problem)

- Which UK cities are currently underserved?
- Are the customers primarily London-based?

## 2. Starting at the End (Describing a Minimum Viable Answer)

### Which UK cities are currently underserved?

This requires us to calculate total customer spend by city and find cities with
the lowest customer spend.

### Are the customers primarily London-based?

This can be answerer from the output of the first answer.

## 3. Identify (Check for sources of data)

### Data Dictionary

| Column      | Definition                                                   |
| :---------- | :----------------------------------------------------------- |
| company_id  | A unique identifier for each customer company in the dataset |
| address     | A single field to store the customers’ address               |
| total_spend | The total amount this customer has spent to date (in GBP)    |

### Describing solution

It's possible to gather customers' cities from `address`, and customers' total
spent in `total_spend`. The `address` is not properly formatted, so it must be
transformed before use.

## 4. Obtain (Get data)

**[Data](https://github.com/davidasboth/solve-any-data-analysis-problem/blob/main/chapter-2/data/addresses.csv)**

If using UNIX:

```bash
curl -o data.csv https://github.com/davidasboth/solve-any-data-analysis-problem/blob/main/chapter-2/data/addresses.csv
```

## 5. Do (Hands-on)

Check [this](./main.py).

## Source

Most of this step-by-step framework to solve data analysis problems came from
[Solve Any Data Analysis Problem](https://www.manning.com/books/solve-any-data-analysis-problem).
