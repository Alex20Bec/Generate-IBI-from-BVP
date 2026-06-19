import pandas as pd
import numpy as np
from scipy.signal import find_peaks

CSV_FILE = "/ANALOG_READY_DATA_SET_9.csv"
FS = 256

df = pd.read_csv(CSV_FILE , decimal=",")

bvp = df["BVP"].to_numpy(dtype=float)


peaks, _ = find_peaks(bvp, distance=int(0.4 * FS))


ibi_ms = np.diff(peaks) / FS * 1000


pd.DataFrame({"IBI_ms": ibi_ms}).to_csv("IBI_trial09.csv", index=False)

print("ΤΕΛΟΣ – IBI δημιουργήθηκαν")
