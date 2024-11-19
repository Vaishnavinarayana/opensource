input_data = input().strip()
vignesh, charan = input_data.split()
if vignesh == charan:
    print("NULL")
elif(vignesh == 'R' and charan == 's') or (vignesh == 'P' and charan == 'R') or (vignesh == 'S' and charan == 'P'):
    print("Vignesh")
else:
    print("Charan")
