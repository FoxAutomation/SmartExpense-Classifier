# Job Expense Categorizer

**Automated expense classification system for contractors and businesses managing multiple projects.**

## Problem

Contractors and businesses juggling multiple simultaneous projects waste hours manually categorizing each expense. The result:
- **Time drain** — Hours of tedious data entry
- **Billing errors** — Expenses charged to wrong jobs
- **Inaccurate profitability tracking** — No clear view of job costs
- **Tax reporting headaches** — Disorganized expense records

This tool automates expense categorization in seconds, eliminating manual work and ensuring accurate job costing.

## How It Works

1. **Define job rules** — Set date ranges, vendor patterns, and keywords in `rules.json`
2. **Import transactions** — Load any bank/credit card CSV export
3. **Run categorization** — Pattern-matching algorithm assigns each expense to the correct job
4. **Get organized output** — Professional summary report + separate CSV files per category

## Key Features

| Feature | Description |
|---------|-------------|
| **Pattern Matching** | Vendor names, description keywords, flexible text search |
| **Date-Based Rules** | Assign expenses by project timeline |
| **Priority Matching** | First matching rule wins — handles overlapping projects |
| **CSV Export** | Separate CSV file per category for accounting software |
| **Uncategorized Flag** | Items requiring manual review are isolated |

## Tech Stack

- **Python 3** — Standard library only (no dependencies)
- **CSV Processing** — Native Python csv module
- **JSON Configuration** — Human-readable rule definitions
- **Datetime Parsing** — Standard library datetime

## Business Value

- **Save hours per week** — Categorization done in seconds
- **Accurate job costing** — Know exactly what each project costs
- **Clean data for accounting** — Export-ready CSVs
- **Scalable** — Add unlimited jobs via simple JSON config

## Quick Start

```bash
# Run the categorizer
python categorizer.py
```

## Configuration Example

```json
{
  "jobs": [
    {
      "name": "Kitchen Remodel",
      "date_start": "2026-01-05",
      "date_end": "2026-01-15",
      "vendor_patterns": ["home depot", "lowe's"],
      "description_patterns": ["lumber", "paint"]
    }
  ]
}
```

---

*Built for contractors, freelancers, and small businesses who need accurate expense tracking without the manual work.*
