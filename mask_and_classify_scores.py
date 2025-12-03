import numpy as np

def mask_and_classify_scores(arr):
    
    if not isinstance(arr, np.ndarray) or arr.ndim != 2:
        return None
    
    if arr.shape[0] != arr.shape[1] or arr.shape[0] < 4:
        return None
    
    cleaned = arr.copy()
    cleaned[cleaned < 0] = 0        
    cleaned[cleaned > 100] = 100
    
    levels = np.zeros(cleaned.shape, dtype=int)
    
    levels[cleaned >= 70] = 2
    levels[(cleaned >= 40) & (cleaned < 70)] = 1
    
    rows = arr.shape[0]
    row_pass_counts = np.zeros(rows, dtype=int)
    
    for i in range(rows):
        current_row = cleaned[i, :] 
        pass_count = 0             
        
        for score in current_row:
            if score >= 50:
                pass_count += 1
        
        row_pass_counts[i] = pass_count
    
    return (cleaned, levels, row_pass_counts)