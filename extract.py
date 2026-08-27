from pypdf import PdfReader
path = r"C:\Users\lei yiming\Desktop\语音策略.pdf"
try:
    r = PdfReader(path)
    print("PAGES:", len(r.pages))
    for i, p in enumerate(r.pages):
        print(f"\n===== PAGE {i+1} =====")
        print(p.extract_text() or "(no text)")
except Exception as e:
    print("ERR", e)
