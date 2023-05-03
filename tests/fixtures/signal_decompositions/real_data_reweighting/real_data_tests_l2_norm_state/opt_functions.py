from sklearn.metrics import mean_absolute_error as mae
from solardatatools import DataHandler
    
def run_weight_scan(w, df, mae_list_s1, mae_list_s2, best_c1, l2_decomp_s1, l2_decomp_s2):    

        dh2 = DataHandler(df, convert_to_ts=True)
        dh2.l2norm = False 
        dh2.run_pipeline(power_col=dh2.keys[0][-1], fix_shifts=True, verbose=False, c1=best_c1, c2=w, solver="MOSEK")

        mae_list_s1.append(mae(dh2.time_shift_analysis.s1, l2_decomp_s1))
        mae_list_s2.append(mae(dh2.time_shift_analysis.s2, l2_decomp_s2))
        
        return mae_list_s1, mae_list_s2
        
