"""WCAG 2.x contrast check for the Holiday Lair palette (build helper)."""
def lum(h):
    h=h.lstrip('#'); r,g,b=[int(h[i:i+2],16)/255 for i in (0,2,4)]
    f=lambda c: c/12.92 if c<=0.03928 else ((c+0.055)/1.055)**2.4
    return 0.2126*f(r)+0.7152*f(g)+0.0722*f(b)
def ratio(a,b):
    la,lb=sorted([lum(a),lum(b)],reverse=True); return (la+0.05)/(lb+0.05)
pairs=[("primary text on card","#F4F0E4","#103D2B"),("secondary text on card","#E9E6DC","#103D2B"),
 ("muted label on card","#C9D3C6","#103D2B"),("muted label on tile gradient (light end)","#C9D3C6","#1F5336"),
 ("tile name on tile gradient (light end)","#F4F0E4","#1F5336"),("gold icon on card","#D3A855","#103D2B"),
 ("dark text on active gold (light end)","#1B140A","#C99A3E"),("dark text on active gold (dark end)","#1B140A","#A8761F"),
 ("status strip value","#18221B","#FFFDF7"),("status strip caption","#4F5A51","#FFFDF7"),
 ("header subtitle on header","#C9D3C6","#031D12"),("page text on page bg","#F4F0E4","#0A321F"),
 ("old bug: #141414 label on card","#141414","#103D2B")]
for n,a,b in pairs: print(f"{ratio(a,b):5.2f}:1  {'PASS' if ratio(a,b)>=4.5 else 'FAIL'}  {n} ({a} on {b})")
