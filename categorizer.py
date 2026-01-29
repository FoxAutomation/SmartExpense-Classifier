#!/usr/bin/env python3
"""
Job Expense Categorizer
Automatically categorizes business expenses to specific jobs
"""

import csv
import json
from datetime import datetime
from collections import defaultdict

def load_rules(rules_file='rules.json'):
    """Load job categorization rules from JSON file"""
    with open(rules_file, 'r') as f:
        return json.load(f)

def parse_date(date_str):
    """Parse date string to datetime object"""
    return datetime.strptime(date_str, '%Y-%m-%d')

def matches_job(transaction, job):
    """Check if a transaction matches a job's rules"""
    date = parse_date(transaction['Date'])
    start = parse_date(job['date_start'])
    end = parse_date(job['date_end'])
    
    # Check date range
    if not (start <= date <= end):
        return False
    
    # Check vendor patterns
    vendor_lower = transaction['Vendor'].lower()
    for pattern in job['vendor_patterns']:
        if pattern.lower() in vendor_lower:
            return True
    
    # Check description patterns
    desc_lower = transaction['Description'].lower()
    for pattern in job['description_patterns']:
        if pattern.lower() in desc_lower:
            return True
    
    return False

def categorize_transactions(csv_file, rules_file='rules.json'):
    """Read transactions and categorize them by job"""
    rules = load_rules(rules_file)
    categorized = defaultdict(list)
    
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        transactions = list(reader)
    
    for transaction in transactions:
        matched = False
        
        # Try to match with each job
        for job in rules['jobs']:
            if matches_job(transaction, job):
                categorized[job['name']].append(transaction)
                matched = True
                break  # First match wins
        
        if not matched:
            categorized['Uncategorized'].append(transaction)
    
    return categorized

def generate_report(categorized):
    """Generate text report of categorized expenses"""
    report = []
    report.append("=" * 60)
    report.append("JOB EXPENSE CATEGORIZATION REPORT")
    report.append("=" * 60)
    report.append("")
    
    grand_total = 0
    
    for job_name in sorted(categorized.keys()):
        transactions = categorized[job_name]
        job_total = sum(float(t['Amount']) for t in transactions)
        grand_total += job_total
        
        report.append(f"📁 {job_name.upper()}")
        report.append("-" * 60)
        
        for t in transactions:
            report.append(f"  {t['Date']}  {t['Vendor']:20s}  ${float(t['Amount']):>8.2f}  {t['Description']}")
        
        report.append(f"\n  SUBTOTAL: ${job_total:,.2f}")
        report.append("")
    
    report.append("=" * 60)
    report.append(f"GRAND TOTAL: ${grand_total:,.2f}")
    report.append("=" * 60)
    
    return "\n".join(report)

def export_to_csv(categorized, output_prefix='categorized'):
    """Export each job category to separate CSV files"""
    for job_name, transactions in categorized.items():
        filename = f"{output_prefix}_{job_name.replace(' ', '_')}.csv"
        
        with open(filename, 'w', newline='') as f:
            if transactions:
                writer = csv.DictWriter(f, fieldnames=transactions[0].keys())
                writer.writeheader()
                writer.writerows(transactions)
        
        print(f"✓ Exported {len(transactions)} transactions to {filename}")

def main():
    """Main execution"""
    print("🔍 Job Expense Categorizer\n")
    
    # Categorize transactions
    print("📊 Reading transactions...")
    categorized = categorize_transactions('sample_transactions.csv')
    
    # Generate and display report
    print("\n" + generate_report(categorized))
    
    # Export to CSV files
    print("\n📄 Exporting categorized files...")
    export_to_csv(categorized)
    
    print("\n✅ Categorization complete!")

if __name__ == "__main__":
    main()
