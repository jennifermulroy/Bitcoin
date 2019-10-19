from enum import Enum
class transactions_type(Enum):
    Transfers_Volume_Sum=1, #transfers_volume_sum 
    Transfers_Volume_Mean=2, #transfers_volume_mean
    Transfers_Volume_Median=3, #transfers_volume_median
    Transfers_Volume_Adjusted_Sum=4, #transfers_volume_adjusted_sum
    Transfers_Volume_Adjusted_Mean=5,  #transfers_volume_adjusted_mean
    Transfers_Volume_Adjusted_Median=6 #transfers_volume_adjusted_median