# Pseudocode for PCR Commission Rates
commBase = commOT = commOF = commTZ = 0.0
baseSalary = 48_000
revTarget = 50_000
revGenerated = 57_499

baseComm = baseSalary * .2
targetQtrComm = baseComm / 4
pcr = baseComm / revTarget
actualToTargetPercent = revGenerated / revTarget

if actualToTargetPercent > 1.25:
    commBase = revTarget * pcr
    commOT = ((revTarget*1.15)-revTarget)*(pcr*1.2)
    commOF = ((revTarget*1.25)-(revTarget*1.15))*(pcr*1.5)
    commTZ = ((revGenerated)-(revTarget*1.25))*(pcr*2.0)
elif 1.25 > actualToTargetPercent > 1.15:
    commBase = revTarget * pcr
    commOT = ((revTarget*1.15)-revTarget)*(pcr*1.2)
    commOF = ((revGenerated)-(revTarget*1.15))*(pcr*1.5)
elif 1.15 > actualToTargetPercent > 1.0:
    commBase = revTarget * pcr
    commOT = ((revGenerated)-revTarget)*(pcr*1.2)
else:
    commBase = revGenerated*pcr

print("Original Commission: ", round(commBase, 2))
print("100-115% Commission", round(commOT,2))
print("115-125% Commission", round(commOF,2))
print("125%+ Commission", round(commTZ,2))
print("Total Comission:", round(commBase+commOF+commOT+commTZ,2))
