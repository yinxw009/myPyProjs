t = range(250)
Time1 = 20
Time2 = 250
SSECp_start = 3050
SSECP_end = 3500

def SSECp_linear(T1, T2, Sp_start, Sp_end):
	if t < T1:
		return 