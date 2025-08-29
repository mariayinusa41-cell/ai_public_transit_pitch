"""
Prototype analysis for an AI‑powered public transit concept.

This script demonstrates how average commute times can be reduced through an
AI‑driven, pod‑based transit system.  It reads a synthetic dataset of
commuter origin–destination pairs, calculates the current average commute
time, applies a 30 percent reduction to simulate the proposed system and
generates a bar chart comparing the current and projected averages.

Usage:
    python analysis.py

Place your transit data in `data/sample_transit_data.csv` with columns
`origin`, `destination`, `current_commute_time_min` and `commuters_per_day`.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

def main() -> None:
    data_path = os.path.join('data', 'sample_transit_data.csv')
    if not os.path.exists(data_path):
        raise FileNotFoundError(
            f"Sample data not found at {data_path}. Please create the CSV file as described in the README."
        )
    df = pd.read_csv(data_path)

    # Weighted average commute time
    total_commute_time = (df['current_commute_time_min'] * df['commuters_per_day']).sum()
    total_commuters = df['commuters_per_day'].sum()
    avg_commute_time = total_commute_time / total_commuters

    # Apply a 30 percent reduction
    df['projected_commute_time_min'] = df['current_commute_time_min'] * 0.7
    total_new_time = (df['projected_commute_time_min'] * df['commuters_per_day']).sum()
    avg_commute_time_new = total_new_time / total_commuters

    # Print results
    print(f"Current average commute time: {avg_commute_time:.2f} minutes")
    print(f"Projected average commute time (30% reduction): {avg_commute_time_new:.2f} minutes")
    reduction = avg_commute_time - avg_commute_time_new
    print(f"Average time saved per commuter: {reduction:.2f} minutes")

    # Plot comparison
    os.makedirs('results', exist_ok=True)
    plt.figure()
    plt.bar(['Current', 'Projected'], [avg_commute_time, avg_commute_time_new])
    plt.title('Average Commute Time Before and After AI‑Powered Transit')
    plt.ylabel('Minutes')
    plt.savefig(os.path.join('results', 'commute_time_comparison.png'))
    plt.close()


if __name__ == '__main__':
    main()
