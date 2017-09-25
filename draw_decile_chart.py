def draw_decile_chart(df, bin_var, target, bins=10):
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    from math import ceil
    
    df_temp = df.copy()
    chart_df = df_temp.loc[:, list(set([bin_var] + target))]
    chart_df_sorted = chart_df.sort_values(bin_var)
    
    bin_col = []
    bin_size = ceil(len(chart_df_sorted) / bins)
    element_counter = 0
    bin_num = bins
    
    for i in range(len(chart_df_sorted)):
        bin_col.append(bin_num)
        element_counter += 1
        
        if element_counter == bin_size:
            bin_num -= 1
            element_counter = 0
    
    bin_col_name = bin_var + '_bin'
    chart_with_bin_df = chart_df_sorted.copy()
    chart_with_bin_df[bin_col_name] = bin_col

    bin_index = chart_with_bin_df.groupby(bin_col_name).mean().index
    grouped_by_age_bin = chart_with_bin_df.groupby(bin_col_name)
    display(grouped_by_age_bin.mean())
    
    for x in target:
        plt.plot(bin_index, grouped_by_age_bin.mean()[x], linestyle='-')