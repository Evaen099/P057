import os, sys
try:
    __import__("okk_enc").main()
except Exception as e:
    exit(str(e))
