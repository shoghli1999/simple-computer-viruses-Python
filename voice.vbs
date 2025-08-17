do
StrText=("ha ha ha")
set objvoice= CreateObject("SAPI.SpVoice")
objvoice.Rate=-3
objvoice.Speak StrText
loop